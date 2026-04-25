# NewMathAnalysis — Build Workflow

## Directory Structure

```
NewMathAnalysis/
├── src/                       ← raw chapter sources (edit here)
│   ├── chpt0.md – chpt14.md
│   ├── mid_exam.md
│   ├── head.yaml              ← frontmatter injected into every chapter
│   └── exercises/
│       └── chptN-ex-NNN.md    ← one file per exercise (see §Exercises)
├── build/                     ← build pipeline
│   ├── build.py               ← src/ → docs/ via Pandoc
│   ├── template.html          ← HTML page template
│   ├── filters.lua            ← Pandoc Lua filter (callouts, image sizing)
│   ├── exercise.py            ← exercise parser + renderer
│   ├── publish.sh             ← build + push docs/ → hydrays.github.io
│   └── assets/                ← source of truth for app.css / app.js / fonts
├── docs/                      ← HTML output (generated, gitignored)
│   ├── index.html
│   ├── chapter0.html – chapter14.html
│   ├── assets/                ← rsynced from build/assets/
│   ├── threejs/               ← rsynced from media/threejs/
│   └── exercises/index.json   ← exercise index (built)
├── media/
│   ├── img/                   ← images referenced from chapters
│   └── threejs/               ← Three.js interactive figure scripts (source of truth)
├── code/                      ← Python teaching examples
└── Support/                   ← supplementary material
```

## Build

```bash
# All chapters
python3 build/build.py

# One chapter
python3 build/build.py src/chpt1.md
```

`build.py` reads `src/chptN.md`, injects `src/head.yaml` frontmatter, adds
hierarchical section numbering (`1.1`, `1.1.1`, …), runs Pandoc with
`build/filters.lua`, and writes the final HTML to `docs/`.

`docs/` is generated output — do not edit it directly, and it is gitignored
in this repo. (The copy in `hydrays.github.io` is the published one.)

## Serving Locally

```bash
cd /home/hydra/Code/books/NewMathAnalysis/docs
python3 -m http.server 8080 --bind 127.0.0.1         # localhost only
python3 -m http.server 8080 --bind 100.74.177.128    # over Tailscale
```

Open `http://127.0.0.1:8080/` (or the Tailscale IP).

## Publishing

```bash
bash build/publish.sh                # commit message = "publish: update"
bash build/publish.sh "my message"
```

Builds, then rsyncs `docs/` into the sibling `hydrays.github.io/` checkout
and pushes. The target path is controlled by `$HYDRAYS_IO` (default:
`~/Code/books/hydrays.github.io`).

## Markdown Authoring

### Callout blocks

Use the `[!type: title]` header form. A blank `>` line separates the header
from the body.

```markdown
> [!tip: 映射与函数]
>
> 函数是一种特殊的映射: 从数集 $A$ 到数集 $B$ 的映射 $f: A \to B$ 称为函数.
```

- Types: `note` 注 · `tip` 提示 · `important` 重要 · `warning` 警告 · `caution` 注意 · `extension` 扩展
- Title-only: `> [!tip: 标题]` — header shows "标题".
- Type-only: `> [!tip]` followed by inline text on the next line — header shows "提示: …".

### Video on a callout (opt-in, per callout)

Append `| video: URL` to the title of any `[!type: ...]` callout. Clicking the
`▶ 观看视频` button in the banner opens the video panel between the banner and
the body.

```markdown
> [!tip: 映射与函数 | video: https://player.bilibili.com/player.html?bvid=BV1jEDcBoE8F&autoplay=0]
>
> Callout body…
```

Titleless form: `> [!tip: | video: URL]` — header falls back to the default
label (提示 etc.). Omit `| video:` for no button.

Do **not** embed `<iframe>` directly inside callouts any more; use the
`| video:` syntax so the iframe lazy-loads only when clicked.

### Inline emphasis

```markdown
极限是一个[动中取静]{.key}的过程.   ← blue bold (key term)
这[不是]{.hl}真正意义上的极限.      ← yellow highlight
==重要文字==                         ← yellow mark (==text==)
```

### Image sizing

```markdown
![描述](../media/img/fig.png#400w)    ← 400px wide
![描述](../media/img/fig.png#200h)    ← 200px tall
![描述](../media/img/fig.png#300pt)   ← 300pt wide
```

### Exercises

One file per exercise in `src/exercises/chptN-ex-NNN.md`, with YAML
frontmatter and fixed headings:

```markdown
---
id: chpt1-ex-003
difficulty: medium
tags: [limit, epsilon-delta]
---

## Problem
求 $\lim_{x\to 0} \frac{\sin x}{x}$.

## Solution 1
...

### Hint
考虑夹逼准则.

### Answer
$1$
```

Cite in the chapter body:

```markdown
::: {.exercise id="chpt1-ex-003"} :::
```

Behavior:
- Auto-numbered per chapter as 例1, 例2, … (resets per chapter).
- Difficulty dot: 🟢 easy · 🟡 medium · 🔴 hard.
- Problem visible; 提示 / 答案 reveal in a shared frame below.
- Multiple `## Solution N` sections render as 解法一, 解法二, …; solutions 2+ are hidden behind a toggle.
- `build/exercises/index.json` is generated automatically.

## Interactive Figures (Three.js)

Inline 3-D interactive figures live in `media/threejs/*.js` and are rsynced
to `docs/threejs/` on build. Embed in chapter markdown as a raw HTML block
(blank lines before and after; Pandoc passes it through because the build
uses `--from markdown+raw_html`):

```html
<div id="my-scene"></div>
<script type="module" src="threejs/my-scene.js"></script>
```

- The page template (`build/template.html`) already declares the
  `three` / `three/addons/` importmap once in `<head>`. Do **not** add a
  per-figure `<script type="importmap">` — duplicates trigger browser
  warnings.
- `build.py` rewrites `<script type="module" src="…">` to a deferred
  `<script data-lazy-module="…">` form, so figures only load when their
  container scrolls near the viewport.
- Inner container divs need `min-width: 0` to prevent flex auto-min-width
  blowout.
- Do **not** set `width: 100%; max-width: 960px` on flex containers — use
  default block width.

**Coordinate convention:** all figures map Manim/math axes to Three.js via

```
Manim (x, y, z)  →  Three.js (x, z, -y)
```

i.e. x stays right, math-z (up) becomes Three.js y, math-y (into screen)
becomes Three.js −z.

### Chapter 10 gradient figure  (`src/chpt10.md`)

Located right after the opening tip callout, before §多元函数的连续性.

**Surface:** `z = −0.3x² − 0.4y² + 1.6x + 2.8y − 2.7`
- `f(1,1) = 1`,  `∂f/∂x|(1,1) = 1`,  `∂f/∂y|(1,1) = 2`
- Concave (`f_xx = −0.6 < 0`, `f_yy = −0.8 < 0`)

**Phases** (◀/▶ buttons):

| # | 中文标签 | Content |
|---|---|---|
| 0 | 曲面与点 P | Gray transparent surface, axes, point P=(1,1,1) with dashed drop line |
| 1 | 偏导数 ∂z/∂x | Orange cutting plane y=1 (∥ xOz), intersection curve, white dashed tangent, tangent point (1+Δx, 1, 1+Δx) |
| 2 | 偏导数 ∂z/∂y | Purple cutting plane x=1 (∥ yOz), intersection curve, yellow dashed tangent, tangent point (1, 1+Δy, 1+2Δy) |
| 3 | 切平面 | Orange vector v1=(Δx,0,Δx), purple vector v2=(0,Δy,2Δy), gold tangent patch z=x+2y−2 |

**Manim source:** `code/gradient_surface.py` — same scene, renders as video.
Build with:
```bash
manim -pql code/gradient_surface.py GradientVisualization
```

### Adding a new figure

1. Write a self-contained `<div id="...">` + `<script type="module">` block.
2. Save the module to `media/threejs/<name>.js`.
3. Insert the HTML block into the relevant `src/chptN.md` with blank lines above and below.
4. Rebuild: `python3 build/build.py src/chptN.md`.
