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
    """Copy assets, theme CSS, and external Three.js modules into docs/."""
    ASSETS_DST.mkdir(parents=True, exist_ok=True)
    for src in ASSETS_SRC.iterdir():
        copy_if_changed(src, ASSETS_DST / src.name)
    if VLOOK_CSS_SRC.exists():
        copy_if_changed(VLOOK_CSS_SRC, VLOOK_CSS_DST)
    else:
        print(f"  Warning: {VLOOK_CSS_SRC} not found — skipping theme CSS")
    copy_tree_if_changed(THREEJS_SRC, THREEJS_DST)

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

    targets = []
    if len(sys.argv) > 1:
        targets = [Path(a) for a in sys.argv[1:]]
    else:
        targets = find_chapters()

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
