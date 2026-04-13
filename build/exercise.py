"""
exercise.py — Exercise library parser and HTML renderer for NewMathAnalysis.

Public API:
  parse_exercise_file(text: str) -> dict
  render_exercise_html(ex: dict) -> str
  inject_exercises(content: str, exercises_dir: Path) -> str
  build_exercise_index(exercises_dir: Path, out_path: Path) -> None
"""

import re
import sys
import json
import html
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# ── Parser ────────────────────────────────────────────────────────────────────

def _split_frontmatter(text: str):
    """Return (meta_dict, body_str)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---\n", 3)
    if end == -1:
        # Try \n--- at end of string
        if text.find("\n---", 3) == len(text) - 4:
            end = len(text) - 4
        else:
            return {}, text
    yaml_str = text[3:end]
    body = text[end + 5:]  # skip \n---\n (5 chars)
    if yaml is None:
        raise ImportError("PyYAML is required: pip install pyyaml")
    result = yaml.safe_load(yaml_str)
    meta = result if isinstance(result, dict) else {}
    return meta, body


def _parse_sections(body: str) -> dict:
    """
    Split body into:
      problem: str
      solutions: list of {hint: str, answer: str}
    """
    parts = re.split(r"^## ", body, flags=re.MULTILINE)
    problem = ""
    solutions = []

    for part in parts:
        part = part.strip()
        if not part:
            continue
        first_line, _, rest = part.partition("\n")
        heading = first_line.strip().lower()

        if heading == "problem":
            problem = rest.strip()
        elif re.match(r"solution\s*\d*", heading):
            hint, answer = _parse_solution_body(rest)
            solutions.append({"hint": hint, "answer": answer})

    return {"problem": problem, "solutions": solutions}


def _parse_solution_body(text: str) -> tuple:
    """Return (hint_str, answer_str) from a solution body."""
    hint = ""
    answer = ""
    parts = re.split(r"^### ", text, flags=re.MULTILINE)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        first_line, _, rest = part.partition("\n")
        heading = first_line.strip().lower()
        if heading == "hint":
            hint = rest.strip()
        elif heading == "answer":
            answer = rest.strip()
    return hint, answer


def parse_exercise_file(text: str) -> dict:
    """
    Parse an exercise .md file (as a string) and return a dict:
      id, chapter, tags, difficulty, video, problem, solutions
    """
    meta, body = _split_frontmatter(text)
    sections = _parse_sections(body)

    return {
        "id":         str(meta.get("id", "")),
        "chapter":    meta.get("chapter", 0),
        "tags":       meta.get("tags") or [],
        "difficulty": str(meta.get("difficulty", "medium")),
        "video":      meta.get("video") or None,
        "problem":    sections["problem"],
        "solutions":  sections["solutions"],
    }


# ── HTML renderer ─────────────────────────────────────────────────────────────

_DIFFICULTY_DOT = {
    "easy":   ("difficulty-easy",   "🟢"),
    "medium": ("difficulty-medium", "🟡"),
    "hard":   ("difficulty-hard",   "🔴"),
}

_SOLUTION_LABELS = [
    "解法一", "解法二", "解法三", "解法四", "解法五",
    "解法六", "解法七", "解法八", "解法九", "解法十",
]


def _tag_pill(tag: str) -> str:
    return f'<span class="ex-tag">{html.escape(tag)}</span>'


def _solution_panel(sol: dict, idx: int, ex_id: str) -> str:
    label = _SOLUTION_LABELS[idx] if idx < len(_SOLUTION_LABELS) else f"解法{idx+1}"
    panel_id  = f"{ex_id}-sol-{idx}"
    hint_id   = f"{ex_id}-hint-{idx}"
    answer_id = f"{ex_id}-ans-{idx}"

    hint_block = ""
    if sol["hint"]:
        hint_block = (
            f'<button class="ex-reveal-btn" data-target="{hint_id}">显示提示</button>\n'
            f'<div class="ex-collapsible" id="{hint_id}" hidden>{sol["hint"]}</div>\n'
        )

    answer_block = (
        f'<button class="ex-reveal-btn" data-target="{answer_id}">显示答案</button>\n'
        f'<div class="ex-collapsible" id="{answer_id}" hidden>{sol["answer"]}</div>\n'
    )

    return (
        f'<button class="ex-solution-toggle" data-target="{panel_id}">{label} ▼</button>\n'
        f'<div class="ex-solution-panel" id="{panel_id}" hidden>\n'
        f'{hint_block}'
        f'{answer_block}'
        f'</div>\n'
    )


def render_exercise_html(ex: dict) -> str:
    ex_id = ex["id"]
    diff_class, diff_dot = _DIFFICULTY_DOT.get(
        ex["difficulty"], ("difficulty-medium", "🟡")
    )

    tags_html = "".join(_tag_pill(t) for t in ex["tags"])

    video_btn = ""
    if ex.get("video"):
        video_btn = (
            f'<a class="ex-video-btn" href="{ex["video"]}" '
            f'target="_blank" rel="noopener">📹 视频</a>\n'
        )

    solutions_html = "".join(
        _solution_panel(sol, i, ex_id)
        for i, sol in enumerate(ex["solutions"])
    )

    return (
        f'<div class="exercise-block" id="{ex_id}" data-difficulty="{ex["difficulty"]}">\n'
        f'  <div class="ex-header">\n'
        f'    <span class="ex-label">练习</span>\n'
        f'    <span class="ex-dot {diff_class}">{diff_dot}</span>\n'
        f'    <span class="ex-tags">{tags_html}</span>\n'
        f'  </div>\n'
        f'  <div class="ex-problem">{ex["problem"]}</div>\n'
        f'  <div class="ex-controls">\n'
        f'{solutions_html}'
        f'{video_btn}'
        f'  </div>\n'
        f'</div>\n'
    )


# ── Build-time injection ──────────────────────────────────────────────────────

_EX_DIV_RE = re.compile(
    r'^:::[ \t]*\{\.exercise[ \t]+id="([^"]+)"[ \t]*\}[ \t]*\n:::[ \t]*$',
    re.MULTILINE,
)


def _load_exercise(ex_id: str, exercises_dir: Path) -> dict:
    """Find and parse the exercise file for ex_id."""
    matches = sorted(exercises_dir.rglob(f"{ex_id}.md"))
    if len(matches) > 1:
        raise ValueError(f"Exercise id '{ex_id}' is ambiguous: {matches}")
    if not matches:
        raise FileNotFoundError(f"Exercise '{ex_id}' not found in {exercises_dir}")
    return parse_exercise_file(matches[0].read_text(encoding="utf-8"))


def inject_exercises(content: str, exercises_dir: Path) -> str:
    """
    Replace all ::: {.exercise id="..."} ::: blocks in content with
    raw HTML exercise blocks. Missing exercises emit a warning comment.
    """
    def replace(m):
        ex_id = m.group(1)
        try:
            ex = _load_exercise(ex_id, exercises_dir)
            html = render_exercise_html(ex)
            return f"\n{html}\n"
        except FileNotFoundError as e:
            print(f"  Warning: {e}", file=sys.stderr)
            return f'<!-- exercise not found: {ex_id} -->\n'

    return _EX_DIV_RE.sub(replace, content)


# ── Index builder ─────────────────────────────────────────────────────────────

def build_exercise_index(exercises_dir: Path, out_path: Path) -> None:
    """
    Scan all exercise .md files and write out_path/index.json.
    """
    if not exercises_dir.exists():
        return

    index = []
    for md_file in sorted(exercises_dir.rglob("*.md")):
        try:
            ex = parse_exercise_file(md_file.read_text(encoding="utf-8"))
            index.append({
                "id":         ex["id"],
                "chapter":    ex["chapter"],
                "tags":       ex["tags"],
                "difficulty": ex["difficulty"],
                "video":      ex["video"],
                "source":     str(md_file.relative_to(exercises_dir)),
            })
        except Exception as e:
            print(f"  Warning: could not index {md_file.name}: {e}")

    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  → docs/exercises/index.json ({len(index)} exercises)")
