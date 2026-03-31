# NewMathAnalysis — Build Workflow

## Directory Structure

```
NewMathAnalysis/
├── src/                  ← raw chapter sources (edit here)
│   ├── chpt0.md – chpt14.md
│   ├── mid_exam.md
│   ├── head.yaml         ← YAML frontmatter injected into every chapter
│   └── post_process.py   ← step 1: adds numbering, writes to Chapters/
├── Chapters/             ← processed intermediate (do not edit directly)
│   └── chapter0.md – chapter14.md
├── build/                ← build pipeline
│   ├── build.py          ← step 2: Pandoc → HTML, writes to docs/
│   ├── template.html     ← HTML page template
│   ├── vlook.lua         ← Pandoc Lua filter (callouts, image sizing)
│   └── assets/
│       ├── app.css       ← layout + Thinking theme styling
│       └── app.js        ← sidebar, TOC, chapter nav
├── docs/                 ← HTML output (served by http.server)
│   ├── index.html
│   └── chapter0.html – chapter14.html
├── media/
│   └── img/              ← images referenced in chapters
├── code/                 ← Python teaching examples
└── Support1/             ← Jupyter notebook supplements
```

## Two-Step Build

### Step 1 — Post-process source

Run from the repo root:

```bash
# All chapters
python src/post_process.py

# One chapter
python src/post_process.py chpt1.md
```

This reads `src/chptN.md`, injects `head.yaml` frontmatter, adds hierarchical
section numbering (`1.1`, `1.1.1`, …), and writes `Chapters/chapterN.md`.

### Step 2 — Build HTML

```bash
# All chapters
python build/build.py

# One chapter
python build/build.py Chapters/chapter1.md
```

This runs Pandoc with the custom template and Lua filter, copies assets to
`docs/assets/`, and writes the final HTML to `docs/`.

## Serving Locally

The server is started from `NewMathAnalysis/` so that `../media/img/` paths
resolve correctly:

```bash
cd /home/hydra/Code/books/NewMathAnalysis
python3 -m http.server 8080 --bind 0.0.0.0
```

Access at: `http://100.74.177.128:8080/docs/`

## Markdown Authoring

### Callout blocks

```markdown
> [!important]
> Plain callout body.

> [!important] 自定义标题
> Callout with custom title → renders as "重要: 自定义标题".
```

Available types: `note` 注 · `tip` 提示 · `important` 重要 · `warning` 警告 · `caution` 注意 · `extension` 扩展

### Inline emphasis

```markdown
极限是一个[动中取静]{.key}的过程。   ← blue bold (key term)

这[不是]{.hl}真正意义上的极限。      ← yellow highlight

==重要文字==                           ← yellow mark (==text==)
```

### Image sizing

```markdown
![描述](../media/img/fig.png#400w)    ← 400px wide
![描述](../media/img/fig.png#200h)    ← 200px tall
![描述](../media/img/fig.png#300pt)   ← 300pt wide
```

## Interactive Figures (Three.js)

Inline 3-D interactive figures can be embedded directly in any chapter `.md`
file as a raw HTML block (blank lines before and after).  Pandoc passes them
through untouched because the build uses `--from markdown+raw_html`.

**CDN imports** — each figure loads Three.js via `<script type="module">` from
`cdn.jsdelivr.net`.  Students need internet access; no local install required.

**Coordinate convention** — all figures use the same mapping from Manim/math
axes to Three.js:

```
Manim (x, y, z)  →  Three.js (x, z, -y)
```

i.e. x stays right, math-z (up) becomes Three.js y, math-y (into screen)
becomes Three.js −z.

### Chapter 10 gradient figure  (`Chapters/chapter10.md`)

Located right after the opening tip callout, before §10.1.

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
2. Insert it into the `.md` file with blank lines above and below.
3. Rebuild: `python build/build.py Chapters/chapterN.md`

## Exporting to GitHub Pages

When ready, copy `docs/` output into `hydrays.github.io/Chapters/` and update
`hydrays.github.io/index.html` links accordingly.
