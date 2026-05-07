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

def test_figures_default_to_problem():
    src = """\
---
id: chpt0-ex-001
chapter: 0
tags: []
difficulty: easy
figures:
  - foo.png
---

## Problem

P body.

## Solution 1

### Hint
H.

### Answer
A body.
"""
    ex = parse_exercise_file(src)
    assert ex["figures"][0]["file"] == "foo.png"
    assert ex["figures"][0]["where"] == "problem"
    assert ex["figures"][0]["width"] == 400
    html = render_exercise_html(ex)
    # image goes into problem box, not the (hidden) answer panel
    pre_ctrl = html.split("ex-controls")[0]
    assert "foo.png" in pre_ctrl
    post_ctrl = html.split("ex-controls")[1]
    assert "foo.png" not in post_ctrl


def test_figures_routed_to_answer():
    src = """\
---
id: chpt0-ex-002
chapter: 0
tags: []
difficulty: easy
figures:
  - { file: only-in-problem.png, where: problem, alt: P, width: 320 }
  - { file: only-in-answer-2.png, where: "answer:2", alt: A2 }
---

## Problem

P.

## Solution 1

### Hint
H1.

### Answer
A1.

## Solution 2

### Hint
H2.

### Answer
A2.
"""
    ex = parse_exercise_file(src)
    html = render_exercise_html(ex)
    pre_ctrl, _, post_ctrl = html.partition("ex-controls")
    assert "only-in-problem.png" in pre_ctrl
    assert "only-in-problem.png" not in post_ctrl
    assert "width=320" in pre_ctrl or "320w" in pre_ctrl
    # answer:2 lands in the second answer panel only
    ans2_block = post_ctrl.split("ex-ans-panel")[2]  # index 0=before first split, 1=first panel, 2=second
    assert "only-in-answer-2.png" in ans2_block
    ans1_block = post_ctrl.split("ex-ans-panel")[1]
    assert "only-in-answer-2.png" not in ans1_block


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
