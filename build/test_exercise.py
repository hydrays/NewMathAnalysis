import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from exercise import parse_exercise_file, render_exercise_html

SAMPLE = """\
---
id: chpt1-ex-001
chapter: 1
tags: [极限, epsilon-delta]
difficulty: medium
video:
---

## Problem

Show that $\\lim_{x \\to 2}(3x-1) = 5$.

## Solution 1

### Hint
Work backwards from $|f(x) - L| < \\varepsilon$.

### Answer
Let $\\varepsilon > 0$. Choose $\\delta = \\varepsilon / 3$.
"""

def test_parse_metadata():
    ex = parse_exercise_file(SAMPLE)
    assert ex["id"] == "chpt1-ex-001"
    assert ex["chapter"] == 1
    assert ex["tags"] == ["极限", "epsilon-delta"]
    assert ex["difficulty"] == "medium"
    assert ex["video"] is None

def test_parse_problem():
    ex = parse_exercise_file(SAMPLE)
    assert "3x-1" in ex["problem"]

def test_parse_solutions():
    ex = parse_exercise_file(SAMPLE)
    assert len(ex["solutions"]) == 1
    assert "varepsilon" in ex["solutions"][0]["hint"]
    assert "delta" in ex["solutions"][0]["answer"]

def test_render_contains_key_elements():
    ex = parse_exercise_file(SAMPLE)
    html = render_exercise_html(ex)
    assert 'class="exercise-block"' in html
    assert 'data-difficulty="medium"' in html
    assert "极限" in html
    assert "epsilon-delta" in html
    assert "ex-hint-btn" in html
    assert "ex-ans-btn" in html
    assert "提示" in html
    assert "答案" in html
    # single solution: no 解法一 label
    assert "解法一" not in html
    # no video button when video is None
    assert "视频" not in html

def test_render_video_button_appears():
    import copy
    ex = parse_exercise_file(SAMPLE)
    ex = dict(ex)
    ex["video"] = "https://example.com/video"
    html = render_exercise_html(ex)
    assert "视频" in html
    assert "https://example.com/video" in html

def test_render_multiple_solutions():
    sample2 = SAMPLE + """
## Solution 2

### Hint
Use linearity of limits.

### Answer
$\\lim(3x-1) = 3 \\cdot 2 - 1 = 5$.
"""
    ex = parse_exercise_file(sample2)
    assert len(ex["solutions"]) == 2
    html = render_exercise_html(ex)
    # multiple solutions: 解法一 label appears
    assert "解法一" in html
    # solution 2: toggle button present
    assert "解法二" in html
    assert 'class="ex-sol-toggle"' in html
