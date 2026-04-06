#!/usr/bin/env python3
"""
build.py — Build NewMathAnalysis chapters from source to HTML.

Pipeline (single step):
  src/chptN.md  →  inject head.yaml + section numbering  →  Pandoc  →  docs/chapterN.html

Usage:
  python3 build/build.py                 # build all chapters
  python3 build/build.py src/chpt1.md   # build one chapter

Output goes to docs/  (relative to NewMathAnalysis/).
Assets (CSS/JS) are copied to docs/assets/ on first run or when changed.
"""

import re
import sys
import json
import shutil
import hashlib
import subprocess
import tempfile
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────

ROOT       = Path(__file__).resolve().parent.parent   # NewMathAnalysis/
BUILD_DIR  = Path(__file__).resolve().parent          # NewMathAnalysis/build/
DOCS_DIR   = ROOT / "docs"
ASSETS_SRC = BUILD_DIR / "assets"
ASSETS_DST = DOCS_DIR / "assets"
THREEJS_SRC = ROOT / "media" / "threejs"
THREEJS_DST = DOCS_DIR / "threejs"
PLOTLY_SRC = ROOT / "media" / "plotly"
PLOTLY_DST = DOCS_DIR / "plotly"
TEMPLATE   = BUILD_DIR / "template.html"
LUA_FILTER = BUILD_DIR / "vlook.lua"

# Source CSS from the VLOOK repo (sibling of NewMathAnalysis/)
VLOOK_CSS_SRC = ROOT.parent / "VLOOK" / "released" / "themes" / "vlook-thinking.css"
VLOOK_CSS_DST = ASSETS_DST / "vlook-thinking.css"

# Chapter source directory
SRC_DIR  = ROOT / "src"
HEAD_YAML = SRC_DIR / "head.yaml"

# ── Helpers ──────────────────────────────────────────────────────────────────

def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()

def copy_if_changed(src: Path, dst: Path):
    if not dst.exists() or file_hash(src) != file_hash(dst):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  Copied: {dst.relative_to(ROOT)}")

def copy_tree_if_changed(src_dir: Path, dst_dir: Path):
    if not src_dir.exists():
        return
    for src in src_dir.rglob("*"):
        if src.is_file():
            copy_if_changed(src, dst_dir / src.relative_to(src_dir))

def sync_assets():
    """Copy assets, theme CSS, and external media helpers into docs/."""
    ASSETS_DST.mkdir(parents=True, exist_ok=True)
    for src in ASSETS_SRC.iterdir():
        copy_if_changed(src, ASSETS_DST / src.name)
    if VLOOK_CSS_SRC.exists():
        copy_if_changed(VLOOK_CSS_SRC, VLOOK_CSS_DST)
    else:
        print(f"  Warning: {VLOOK_CSS_SRC} not found — skipping theme CSS")
    copy_tree_if_changed(THREEJS_SRC, THREEJS_DST)
    copy_tree_if_changed(PLOTLY_SRC, PLOTLY_DST)

# ── Source pre-processing (formerly post_process.py) ─────────────────────────

def load_head_yaml() -> str:
    if HEAD_YAML.exists():
        return HEAD_YAML.read_text(encoding="utf-8").rstrip() + "\n\n"
    return ""

def add_numbering(content: str, chapter_num: str) -> str:
    sec = sub = subsub = 0
    out = []
    for line in content.split("\n"):
        if line.startswith("# "):
            sec = sub = subsub = 0
            out.append(f"# 第{chapter_num}章 {line[2:].strip()}")
        elif line.startswith("## "):
            sec += 1; sub = subsub = 0
            out.append(f"## {chapter_num}.{sec} {line[3:].strip()}")
        elif line.startswith("### "):
            sub += 1; subsub = 0
            out.append(f"### {chapter_num}.{sec}.{sub} {line[4:].strip()}")
        elif line.startswith("#### "):
            subsub += 1
            out.append(f"#### {chapter_num}.{sec}.{sub}.{subsub} {line[5:].strip()}")
        else:
            out.append(line)
    return "\n".join(out)

# ── Markdown pre-processing ──────────────────────────────────────────────────

def preprocess(content: str) -> str:
    """
    Handle syntax Pandoc doesn't natively understand:
      _~Tag~_        → stripped (tag removed, text kept bare)
      [toc]          → removed (Pandoc --toc handles this)
    """
    # Remove [toc] / [TOC] directives (Pandoc generates TOC separately)
    content = re.sub(r"^\s*\[toc\]\s*$", "", content, flags=re.IGNORECASE | re.MULTILINE)

    # _~Tag~_ — strip entirely (no output)
    content = re.sub(r"_~[^~\n]+~_", "", content)

    return content

def _replace_outside_code(text: str, pattern: str, repl) -> str:
    """Apply regex replacement only outside fenced code blocks, inline code, and raw script/style blocks."""
    result = []
    in_fence = False
    fence_marker = ""
    in_raw_block = False
    raw_end_pat = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if in_raw_block:
            result.append(line)
            if raw_end_pat and re.search(raw_end_pat, line, flags=re.IGNORECASE):
                in_raw_block = False
                raw_end_pat = None
            continue
        if not in_fence:
            if re.match(r"^<script\b", stripped, flags=re.IGNORECASE):
                in_raw_block = True
                raw_end_pat = r"</script>"
                result.append(line)
                continue
            if re.match(r"^<style\b", stripped, flags=re.IGNORECASE):
                in_raw_block = True
                raw_end_pat = r"</style>"
                result.append(line)
                continue
            m = re.match(r"^(`{3,}|~{3,})", stripped)
            if m:
                in_fence = True
                fence_marker = m.group(1)[0]
                result.append(line)
                continue
            # Replace inline, but skip content inside backticks on this line
            result.append(_replace_outside_inline_code(line, pattern, repl))
        else:
            result.append(line)
            m = re.match(rf"^{re.escape(fence_marker[0])}{{3,}}", stripped)
            if m:
                in_fence = False
    return "".join(result)

def _replace_outside_inline_code(line: str, pattern: str, repl) -> str:
    """Apply replacement on a single line, skipping `code` spans."""
    parts = re.split(r"(`[^`]+`)", line)
    return "".join(
        p if p.startswith("`") else re.sub(pattern, repl, p)
        for p in parts
    )

# ── YAML front-matter ────────────────────────────────────────────────────────

def _fix_yaml_md_links(yaml_str: str) -> str:
    """Quote list items that are bare Markdown links [text](url) — invalid YAML."""
    def quote_item(m):
        indent, content = m.group(1), m.group(2)
        # already quoted
        if content.startswith('"') or content.startswith("'"):
            return m.group(0)
        # Use single quotes (the link titles use double quotes inside)
        return f"{indent}'{content}'"
    return re.sub(r'^(\s*-\s+)(\[.+)', quote_item, yaml_str, flags=re.MULTILINE)

def split_frontmatter(content: str):
    """Return (yaml_dict, body_str). yaml_dict is {} if no front-matter."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    yaml_str = _fix_yaml_md_links(content[3:end])
    body = content[end + 4:]
    try:
        import yaml
        meta = yaml.safe_load(yaml_str) or {}
    except Exception as e:
        print(f"  Warning: YAML parse error: {e}")
        meta = {}
    return meta, body

_DOC_LIB_RE = re.compile(r"\[([^\]]+)\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")

def parse_doc_lib(items) -> list:
    """Convert vlook-doc-lib list of markdown links to [{title, url}]."""
    if not items:
        return []
    result = []
    for item in items:
        m = _DOC_LIB_RE.match(str(item).strip())
        if m:
            url = m.group(2).split("?")[0]   # strip ?target=_self etc.
            result.append({"title": m.group(1), "url": url})
    return result

# ── Pandoc invocation ─────────────────────────────────────────────────────────

def check_pandoc():
    try:
        r = subprocess.run(["pandoc", "--version"], capture_output=True, text=True)
        first = r.stdout.splitlines()[0] if r.stdout else ""
        # Warn if version < 3
        m = re.search(r"pandoc (\d+)", first)
        if m and int(m.group(1)) < 3:
            print(f"  Warning: Pandoc {first.strip()} detected. v3.2+ recommended for best callout support.")
        return True
    except FileNotFoundError:
        return False

def build_chapter(md_path: Path):
    print(f"Building {md_path.name} ...")

    raw = md_path.read_text(encoding="utf-8")

    # If reading from src/chptN.md: inject head.yaml + section numbering
    m_num = re.search(r"chpt(\d+)\.md$", md_path.name)
    if m_num:
        head = load_head_yaml()
        raw = head + add_numbering(raw, m_num.group(1))

    content = raw
    meta, body = split_frontmatter(content)
    body = preprocess(body)

    doc_lib = parse_doc_lib(meta.get("vlook-doc-lib", []))
    chp_autonum = ""
    # Gather vlook-chp-autonum (may appear as a string)
    raw_autonum = meta.get("vlook-chp-autonum", "")
    if isinstance(raw_autonum, str):
        chp_autonum = raw_autonum.strip()

    # Determine output filename
    stem = md_path.stem
    # Normalize chpt* → chapter* names
    out_stem = re.sub(r"^chpt(\d+)$", r"chapter\1", stem)
    out_path = DOCS_DIR / f"{out_stem}.html"
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # Write preprocessed content to a temp file (keep YAML so Pandoc reads title etc.)
    import yaml as _yaml
    # Re-serialise only standard meta keys Pandoc understands
    pandoc_meta = {k: v for k, v in meta.items() if not k.startswith("vlook")}
    combined = f"---\n{_yaml.dump(pandoc_meta, allow_unicode=True)}---\n{body}"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md",
                                     encoding="utf-8", delete=False) as tmp:
        tmp.write(combined)
        tmp_path = Path(tmp.name)

    try:
        cmd = [
            "pandoc", str(tmp_path),
            "--output", str(out_path),
            "--template", str(TEMPLATE),
            "--standalone",
            "--katex",
            "--toc",
            "--toc-depth=4",
            "--lua-filter", str(LUA_FILTER),
            "--from", "markdown-mark+raw_html+smart+tex_math_dollars",
            "--variable", f"doc_lib_json={json.dumps(doc_lib)}",
            "--variable", f"chp_autonum={chp_autonum}",
            "--highlight-style", "pygments",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ERROR: pandoc failed:\n{result.stderr}")
        else:
            if result.stderr:
                print(f"  Pandoc warnings: {result.stderr.strip()}")
            print(f"  → {out_path.relative_to(ROOT)}")
    finally:
        tmp_path.unlink(missing_ok=True)

# ── Index page builder ───────────────────────────────────────────────────────

def build_index():
    """Generate docs/index.html from src/index.md."""
    src = SRC_DIR / "index.md"
    if not src.exists():
        print("  Skipping index: src/index.md not found")
        return

    lines = src.read_text(encoding="utf-8").splitlines()

    title = ""
    intro_link = None          # chapter 0 link before first ##
    sections = []              # list of (section_label, [(num, title, url), ...])
    current_section = None
    before_sections = True

    link_re = re.compile(r"^\[(\d+)\.\s+(.+?)\]\((.+?)\)$")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            before_sections = False
            current_section = (line[3:].strip(), [])
            sections.append(current_section)
        else:
            m = link_re.match(line)
            if m:
                num, chap_title, url = m.group(1), m.group(2), m.group(3)
                entry = (num, chap_title, url)
                if before_sections:
                    intro_link = entry
                elif current_section is not None:
                    current_section[1].append(entry)

    def card(num, chap_title, url, extra_class=""):
        cls = f"chapter-link{' ' + extra_class if extra_class else ''}"
        return (
            f'        <a href="{url}" class="{cls}">\n'
            f'            <div class="chapter-card">\n'
            f'                <div class="chapter-number">{num}</div>\n'
            f'                <div class="chapter-info"><h3>{chap_title}</h3></div>\n'
            f'            </div>\n'
            f'        </a>\n'
        )

    body_parts = []
    if intro_link:
        body_parts.append(card(*intro_link, extra_class="intro-link"))
    for label, entries in sections:
        body_parts.append(
            f'        <div class="section-divider" aria-hidden="true">'
            f'<span>{label}</span></div>\n'
        )
        for entry in entries:
            body_parts.append(card(*entry))

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; }}
        body {{ background-color: #f5f7fa; color: #333; line-height: 1.4; padding: 15px; max-width: 1400px; margin: 0 auto; }}
        .container {{ background-color: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); overflow: hidden; margin-bottom: 30px; }}
        .image-container {{ width: 100%; height: 300px; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
        .custom-image {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
        .image-overlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; justify-content: center; align-items: center; color: white; font-size: 32px; font-weight: 600; text-align: center; padding: 20px; }}
        .main-content {{ --content-rail-width: 80%; column-count: 2; column-gap: 20px; margin-top: 20px; }}
        .intro-link {{ display: block; }}
        .section-divider {{ display: flex; align-items: center; gap: 10px; width: var(--content-rail-width); margin: 0 auto 8px; break-inside: avoid; }}
        .section-divider::before, .section-divider::after {{ content: ""; flex: 1; height: 1px; background: #d7dee7; }}
        .section-divider span {{ color: #94a3b8; font-size: 13px; letter-spacing: 0.08em; white-space: nowrap; }}
        .chapter-card {{ background: white; border-radius: 12px; padding: 10px 14px; box-shadow: 0 3px 12px rgba(15,23,42,0.06); transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease; border: 1px solid #dbe4ee; min-height: 68px; display: flex; align-items: center; gap: 10px; height: 100%; }}
        .chapter-card:hover {{ transform: translateY(-4px); box-shadow: 0 10px 24px rgba(15,23,42,0.1); border-color: #aac7e6; }}
        .chapter-number {{ width: 40px; height: 40px; background: #2f7fbf; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 16px; }}
        .chapter-info {{ flex: 1 1 auto; }}
        .chapter-info h3 {{ font-size: 17px; margin: 0; color: #2c3e50; line-height: 1.2; }}
        .chapter-link {{ text-decoration: none; color: inherit; display: block; width: var(--content-rail-width); margin-bottom: 8px; margin-left: auto; margin-right: auto; break-inside: avoid; }}
        footer {{ text-align: center; padding: 20px; color: #7f8c8d; font-size: 14px; margin-top: 30px; }}
        @media (max-width: 768px) {{ .main-content {{ column-count: 1; --content-rail-width: 100%; }} .image-overlay {{ font-size: 28px; }} }}
        @media (max-width: 480px) {{ body {{ padding: 10px; }} .chapter-card {{ padding: 10px 12px; min-height: 66px; }} .chapter-number {{ width: 36px; height: 36px; font-size: 14px; }} .image-container {{ height: 200px; }} .image-overlay {{ font-size: 24px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="image-container">
            <img src="../media/img/cover.jpg" alt="{title}" class="custom-image">
            <div class="image-overlay"><h2 style="margin-top: 2em;">{title}</h2></div>
        </div>
    </div>
    <div class="main-content">
{"".join(body_parts)}    </div>
    <footer><p>首都师范大学交叉科学研究院 &copy; 2025</p></footer>
    <script>
        document.querySelector('.custom-image').addEventListener('error', function() {{
            this.style.display = 'none';
            var c = document.querySelector('.image-container');
            c.style.background = 'linear-gradient(135deg, #6a11cb 0%, #2575fc 100%)';
        }});
    </script>
</body>
</html>
"""

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    out = DOCS_DIR / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  → {out.relative_to(ROOT)}")


# ── Main ─────────────────────────────────────────────────────────────────────

def find_chapters() -> list:
    """Return chpt*.md source files from src/."""
    return sorted(SRC_DIR.glob("chpt*.md"))

def main():
    if not check_pandoc():
        print("Error: pandoc not found. Install with:")
        print("  sudo apt install pandoc")
        print("Or for v3.x: download .deb from https://github.com/jgm/pandoc/releases")
        sys.exit(1)

    print("Syncing assets ...")
    sync_assets()

    print("Building index ...")
    build_index()

    targets = []
    if len(sys.argv) > 1:
        targets = [Path(a) for a in sys.argv[1:]]
    else:
        targets = find_chapters()

    # index.md is handled by build_index(); skip it from Pandoc targets
    targets = [t for t in targets if t.name != "index.md"]

    if not targets:
        print("No .md files found.")
        sys.exit(0)

    print(f"\nBuilding {len(targets)} chapter(s) ...\n")
    errors = 0
    for md in targets:
        try:
            build_chapter(md)
        except Exception as e:
            print(f"  FAILED {md.name}: {e}")
            errors += 1

    print(f"\nDone. {len(targets) - errors}/{len(targets)} succeeded.")
    if errors:
        sys.exit(1)

if __name__ == "__main__":
    main()
