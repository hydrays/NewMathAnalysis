# Chapter 11 Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite §11 (多元函数的积分) as an application-driven, callout-only chapter where every prose chunk is a typed callout, every figure sits inside its supporting callout, and every theorem proof folds behind a reveal button.

**Architecture:** Three phases. **Phase A** ships the new fold-callout mechanism (Pandoc `Div` filter + delegated JS toggle + CSS) — a self-contained reusable feature. **Phase B** authors the 5 new Three.js scenes one by one, each independent. **Phase C** writes the new prose section by section, weaving in the existing + new figures and using the fold mechanism for proofs. **Phase D** updates `WORKFLOW.md` and cleans up.

**Tech Stack:** Pandoc + Lua filter, vanilla JS (delegated event handler), vanilla CSS, Three.js 0.160 (self-hosted), Python build pipeline.

**Spec:** `specs/2026-04-24-chpt11-rewrite-design.md`.

**Repo context:**

- Working directory: `NewMathAnalysis/`. Source-of-truth assets are in `build/assets/`, `media/threejs/`, `src/`. `docs/` is generated and gitignored.
- The user runs tasks inline (no per-task commits). Final commit happens at the end of each phase or at the user's call.
- Build = `python3 build/build.py`; serve = `cd docs && python3 -m http.server 8080 --bind 127.0.0.1`.

---

## Phase A — Fold callout mechanism

Adds `::: {.fold label="…"} ⟨body⟩ :::` syntax that the author can drop inside any callout. Renders as a labelled button + an initially-hidden body that toggles on click.

### Task A1: Lua filter handler for `.fold` divs

**Files:**
- Modify: `NewMathAnalysis/build/filters.lua`
- Create: `NewMathAnalysis/build/test_fixtures/fold.md`

**Context:** Pandoc's parsed AST already lifts `::: {.fold label="证明"} … :::` to a `pandoc.Div` with class `fold` and an attribute `label="证明"`. Verified during brainstorming. We need the filter to wrap that div's content in the toggle markup.

- [ ] **Step 1: Write the test fixture**

Create `build/test_fixtures/fold.md`:

```markdown
---
title: Fold fixture
---

# Fixture

> [!important: 定理 — Fubini]
>
> 设 $f$ 在矩形 $D$ 上连续, 则 $\iint_D f\,dA = \int_a^b\!\int_c^d f \,dy\,dx$.
>
> ::: {.fold label="证明"}
> 证明的第一步.
>
> 证明的第二步.
> :::

> [!note: 例 1 — 没有 fold]
>
> 普通例题, 不含 fold 块.
```

- [ ] **Step 2: Add the `Div` handler**

Edit `build/filters.lua`. After the `BlockQuote` function (current line ~72) and before the `Image` function, add:

```lua
-- ::: {.fold label="..."} ⟨body⟩ ::: ───────────────────────────────────────
-- Wrap a fenced div with class "fold" into a toggle button + hidden body.
-- The author writes this inside a callout to defer "the work" (proof,
-- derivation, alternate solution) behind a click.
function Div(el)
  if not el.classes:includes("fold") then return nil end

  local label = el.attributes["label"] or "展开"

  local btn_html = string.format(
    '<button class="callout-fold-btn" type="button" '
    .. 'aria-expanded="false">&#9654; %s</button>',
    label)

  local open_html  = '<div class="callout-fold-body" hidden>'
  local close_html = '</div>'

  local out = {
    pandoc.RawBlock("html",
      '<div class="callout-fold" data-label="' .. label .. '">'),
    pandoc.RawBlock("html", btn_html),
    pandoc.RawBlock("html", open_html),
  }
  for _, child in ipairs(el.content) do
    table.insert(out, child)
  end
  table.insert(out, pandoc.RawBlock("html", close_html))
  table.insert(out, pandoc.RawBlock("html", '</div>'))

  return out
end
```

- [ ] **Step 3: Build the fixture and grep**

Run from `NewMathAnalysis/`:

```bash
pandoc build/test_fixtures/fold.md \
  --lua-filter build/filters.lua \
  --from markdown-mark+raw_html+smart+tex_math_dollars \
  --to html \
  -o /tmp/fold.html
```

Verify:

```bash
grep -c 'class="callout-fold"' /tmp/fold.html
# Expected: 1

grep -c 'class="callout-fold-btn"' /tmp/fold.html
# Expected: 1

grep -o '&#9654; 证明' /tmp/fold.html | wc -l
# Expected: 1

grep -c 'class="callout-fold-body" hidden' /tmp/fold.html
# Expected: 1

# The 证明的第一步 / 第二步 paragraphs must be inside .callout-fold-body
awk '/callout-fold-body/{f=1} f; /<\/div>/&&f{exit}' /tmp/fold.html | grep '证明的第一步\|证明的第二步' | wc -l
# Expected: 2

# The 没有 fold example must NOT contain a callout-fold:
awk '/callout-note/{f=1} f' /tmp/fold.html | grep -c 'callout-fold'
# Expected: 0
```

If anything diverges, re-read the handler and reconcile.

### Task A2: CSS for the fold widget

**Files:**
- Modify: `NewMathAnalysis/build/assets/app.css`

- [ ] **Step 1: Add styles**

Append the following block to `build/assets/app.css` immediately after the `.callout-video-btn` rules (find them via the comment at line ~341 — the rules ending in `.callout-video-btn.is-active`):

```css
/* Foldable content inside a callout — proof of a theorem, derivation
   detail, alternate solution. Visually echoes the "答案" reveal of an
   exercise: emerald left bar, near-black text, white background. */
.callout-fold {
  margin: 0.8em 0 0.2em;
}

.callout-fold-btn {
  display: inline-flex;
  align-items: center;
  padding: 3px 12px;
  background: transparent;
  border: 1px solid currentColor;
  border-radius: 4px;
  color: inherit;
  font: inherit;
  font-size: 0.88em;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.callout-fold-btn:hover {
  background: rgba(0, 0, 0, 0.06);
}
.callout-fold-btn[aria-expanded="true"] {
  background: rgba(0, 0, 0, 0.10);
  border-width: 2px;
  padding: 2px 11px;  /* keep the same outer size as the closed state */
}

.callout-fold-body {
  margin-top: 0.6em;
  padding: 10px 14px;
  background: #fff;
  color: #111;
  border-left: 3px solid #10b981;   /* emerald — same as ex-ans-panel */
  border-radius: 0 4px 4px 0;
  font-size: 0.95em;
}
.callout-fold-body > *:first-child { margin-top: 0; }
.callout-fold-body > *:last-child  { margin-bottom: 0; }
```

- [ ] **Step 2: Rebuild + sanity check**

```bash
python3 build/build.py
grep -c 'callout-fold' docs/assets/app.css
# Expected: ≥ 5  (multiple selectors for the widget)
```

### Task A3: JS toggle handler

**Files:**
- Modify: `NewMathAnalysis/build/assets/app.js`

**Context:** The file already has a delegated click handler near the bottom (~line 401, the exercise `.ex-action-btn` block). We add a parallel handler for `.callout-fold-btn`. Per the spec it lives in the same delegated `document.addEventListener("click", …)` style we used for `.callout-video-btn`.

- [ ] **Step 1: Add the handler**

Find the existing line near app.js ~line 387 that opens the click handler block for video buttons:

```javascript
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".callout-video-btn");
    if (!btn) return;
    e.preventDefault();
    if (activeVideoOwner === btn) {
      closeVideoPanel();
    } else {
      openVideoPanelFor(btn);
    }
  });
```

Immediately after the closing `});` of that block, insert:

```javascript

  // ── Fold toggle inside callouts ─────────────────────────────
  // Author writes ::: {.fold label="证明"} ⟨body⟩ :::
  // Filter renders a button + a hidden body. Click toggles.

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".callout-fold-btn");
    if (!btn) return;
    e.preventDefault();

    var wrap = btn.closest(".callout-fold");
    if (!wrap) return;
    var body = wrap.querySelector(".callout-fold-body");
    if (!body) return;

    var nowOpen = body.hasAttribute("hidden");
    if (nowOpen) {
      body.removeAttribute("hidden");
      btn.setAttribute("aria-expanded", "true");
    } else {
      body.setAttribute("hidden", "");
      btn.setAttribute("aria-expanded", "false");
    }

    // Swap the leading arrow glyph (▶ ↔ ▼) without disturbing the label.
    var label = wrap.getAttribute("data-label") || "展开";
    btn.innerHTML = (nowOpen ? "&#9660; " : "&#9654; ") + label;

    // KaTeX may need to render any math that just became visible.
    if (nowOpen && typeof renderMathInElement === "function") {
      renderMathInElement(body, {
        delimiters: [
          { left: "$$", right: "$$", display: true  },
          { left: "$",  right: "$",  display: false }
        ]
      });
    }
  });
```

- [ ] **Step 2: Verify rebuild syncs the new file**

```bash
python3 build/build.py
grep -c 'callout-fold-btn' docs/assets/app.js
# Expected: ≥ 1
```

- [ ] **Step 3: End-to-end smoke test**

Add a temporary fold to the top of `src/chpt11.md` (we'll remove it during Phase C):

```markdown
> [!important: 定理 — Fubini (smoke test)]
>
> ::: {.fold label="证明"}
> 这是 fold 测试. 我看到了就说明渲染正确.
> :::
```

Rebuild, serve, open `http://127.0.0.1:8080/chapter11.html`. Verify:

- Button labelled `▶ 证明` appears under the theorem statement.
- Body hidden by default (no "这是 fold 测试" text visible until click).
- Click → button becomes `▼ 证明`, body becomes visible.
- Click again → collapses.
- No console errors.

Remove the smoke-test callout from chpt11 once verified.

---

## Phase B — Author the 5 new Three.js scenes

Five scenes, one per task. Each is independent — different containers, different ids, no shared state. They all import `three` and `three/addons/controls/OrbitControls.js`; some also import `three/addons/renderers/CSS2DRenderer.js`.

**Pre-flight (do once before B1):**

- [ ] Confirm the addon list our self-host already covers what these scenes need:

```bash
grep -h "from ['\"]three" media/threejs/chpt11-double-integral.js media/threejs/chpt11-jacobian.js
# All addons referenced should also appear under build/assets/three-addons/.
```

- [ ] Skim `media/threejs/chpt11-double-integral.js` (existing, working) so the new scenes can copy its structure: container lookup, renderer setup, OrbitControls, axes / labels with CSS2DRenderer, animation loop, resize handler.

Each B-task below follows the same template:

1. Decide the scene's *visual goal* (one sentence).
2. Write the module under `media/threejs/`.
3. Place the container `<div>` + `<script type="module">` in the right callout in `src/chpt11.md`. (At this point chpt11.md is still the old version — that's fine. Phase C will rewrite the prose, but the figure containers can sit at the right anchor before then.)
4. Build, serve, scroll to figure, eyeball.

### Task B1: `chpt11-mass-plate.js` (§11.1 motivation)

**Goal:** A flat 2-D plate with colour-mapped non-uniform density $\rho(x,y)$, overlaid with an $N\times N$ Riemann grid. Below it: the running Riemann sum $\sum_i \rho(x_i,y_i)\Delta A$ versus the converged true integral. A range slider drives `N` from 4 to 64.

**Files:**
- Create: `media/threejs/chpt11-mass-plate.js`

- [ ] **Step 1: Pick density function and domain**

Use $\rho(x,y) = 0.6 + 0.5\sin(2x)\cos(1.5y)$ on $D = [0, \pi]\times[0, \pi]$. Range 0.1–1.1, smooth, has clear high/low regions for visual contrast.

- [ ] **Step 2: Sketch the scene structure**

```
Top half (canvas): orthographic top-down view of D
  - density-coloured filled mesh (PlaneGeometry with vertex colors)
  - grid overlay at current N (Line2 segments)
  - small dots at evaluation points (one per cell)
Bottom half (DOM, not Three.js): a status row with two numbers:
  - "Riemann 和 (N = X): ____"
  - "真实积分: ____"  (precomputed once, ~1.234)
Range slider (DOM input[type=range]): updates N → re-renders grid + dots, recomputes the Riemann sum.
```

- [ ] **Step 3: Write the module**

Write `media/threejs/chpt11-mass-plate.js`. Use the same skeleton as `chpt11-double-integral.js` (existing, ~250 lines): top-of-file convention comment, `import * as THREE from 'three'`, OrbitControls / CSS2DRenderer if needed, container lookup via `document.getElementById('chpt11-mass-plate')`, renderer + camera + lights, build the plane geometry with per-vertex colour from `density(x,y)`, draw grid lines via `Line2`. Hook the slider's `input` event to update grid + sum in place.

The exact code is too long to inline here. Write it iteratively: a) plain density-coloured plate, b) add grid, c) add dots, d) wire slider. After each sub-step, rebuild and reload.

- [ ] **Step 4: Wire it into chpt11**

Replace the first `[图略, 待补充]` placeholder in `src/chpt11.md` (currently around line 53) with:

```markdown
> <div id="chpt11-mass-plate" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> <script type="module" src="threejs/chpt11-mass-plate.js?v=1"></script>
```

(`> ` prefix so it stays inside the surrounding `[!important: 多变量积分]` callout.)

- [ ] **Step 5: Verify**

```bash
python3 build/build.py
```

Open `chapter11.html` in browser, scroll to the figure. Expect: the plate renders with density colours, grid is visible, slider works smoothly, no console errors.

### Task B2: `chpt11-iterated.js` (§11.3 累次积分 intuition)

**Goal:** A 3-D solid $\{(x,y,z): 0\le z\le f(x,y), (x,y)\in D\}$ shown twice side-by-side. Left: vertical slabs perpendicular to the $x$-axis (computing $\int_a^b A(x)\,dx$). Right: slabs perpendicular to $y$. A slider sweeps the slice plane through the solid; the cross-section is highlighted in colour and the partial integral $A(x_0)$ or $B(y_0)$ is displayed numerically.

**Files:**
- Create: `media/threejs/chpt11-iterated.js`

- [ ] **Step 1: Pick $f$ and $D$**

$f(x,y) = 0.6 + 0.4\sin(\pi x)\sin(\pi y)$ on $D = [0,1]\times[0,1]$. Smooth, surface above 0, easy cross-section curves.

- [ ] **Step 2: Layout**

The container is split horizontally via flexbox into two equal panels (echoes the existing `chpt11-example1` + `chpt11-example2` pair pattern). Each panel runs its own renderer. A single shared slider above (or below) drives both: left panel highlights the $x$-slab at the slider value; right panel the $y$-slab.

- [ ] **Step 3: Write the module**

Pattern: same renderer-per-container approach as `chpt11-jacobian.js` (existing, two scenes in one module). Compute $f$ on a grid; build a `BufferGeometry` for the solid (or use `ParametricGeometry`). For each slider value, place an opaque coloured quad at $x = x_0$ (left panel) and $y = y_0$ (right panel). Display partial integral as a `CSS2DObject` label.

- [ ] **Step 4: Wire and verify**

Add a callout `[!tip: 直觉 — 切片求和]` to `src/chpt11.md` in §11.3 (after the §11.3 heading), and place the container + script inside it via `> ` prefix:

```markdown
> [!tip: 直觉 — 切片求和]
>
> 文字略, Phase C 写.
>
> <div id="chpt11-iterated" style="width:100%; height:420px; ...></div>
> <script type="module" src="threejs/chpt11-iterated.js?v=1"></script>
```

Build, serve, eyeball: both panels render, slider sweeps both slice planes synchronously, partial-integral labels update.

### Task B3: `chpt11-mass-solid.js` (§11.5 motivation)

**Goal:** A 3-D solid ($\{0\le z\le 1, x^2+y^2\le 1\}$ or similar simple shape), rendered with volumetric density colour applied via per-vertex sampling on the surface mesh, plus interior wireframe slices that reveal density variation. Slider varies the slicing plane $z = z_0$; the slab is shown as a coloured cross-section disk.

**Files:**
- Create: `media/threejs/chpt11-mass-solid.js`

- [ ] **Step 1: Density and shape**

$\rho(x,y,z) = 0.5 + 0.4 z + 0.3 (x^2 + y^2)$ on the unit cylinder $x^2+y^2\le 1$, $0\le z\le 1$.

- [ ] **Step 2: Approach**

Outer surface: cylinder side + top/bottom disks, vertex-coloured by density. Slice: a horizontal disk at $z = z_0$, density-coloured, opaque. Slider drives $z_0$.

- [ ] **Step 3: Write + wire + verify**

Place the figure inside a new `[!tip: 动机 — 不均匀立体]` callout in §11.5. Pattern follows B1.

### Task B4: `chpt11-cylindrical.js` (§11.5 柱面坐标)

**Goal:** A solid cylinder shown with its cylindrical-coordinate grid drawn on the side (a $\rho \times \theta \times z$ partition, but visually it's a $\theta \times z$ grid on the side surface, plus a circular grid on the top). One representative volume element $\Delta V = \rho\,\Delta\rho\,\Delta\theta\,\Delta z$ highlighted in solid colour with its dimensions labelled.

**Files:**
- Create: `media/threejs/chpt11-cylindrical.js`

- [ ] **Step 1: Define the grid**

Use $N_\rho = 4$, $N_\theta = 12$, $N_z = 5$ — enough to read clearly without clutter.

- [ ] **Step 2: Highlight one cell**

Pick the cell at index $(i_\rho, i_\theta, i_z) = (2, 2, 2)$ and render it as a small solid wedge. Add three short axis-labels (using `CSS2DObject`): $\rho\,\Delta\rho$, $\rho\,\Delta\theta$, $\Delta z$. Per the spec, **no equations** in figures — just these short labels.

- [ ] **Step 3: Write + wire + verify**

Place inside `[!important: 坐标变换 — 柱面坐标]` callout.

### Task B5: `chpt11-spherical.js` (§11.5 球面坐标)

**Goal:** A solid ball shown with its spherical-coordinate grid (latitude $\varphi$ + longitude $\theta$). One volume element $\Delta V = \rho^2\sin\varphi\,\Delta\rho\,\Delta\theta\,\Delta\varphi$ highlighted, dimensions labelled.

**Files:**
- Create: `media/threejs/chpt11-spherical.js`

- [ ] **Step 1: Grid**

$N_\rho = 3$, $N_\varphi = 8$, $N_\theta = 12$.

- [ ] **Step 2: Highlight one cell**

Same approach as B4. Cell labels: $\Delta\rho$, $\rho\sin\varphi\,\Delta\theta$, $\rho\,\Delta\varphi$.

- [ ] **Step 3: Write + wire + verify**

Place inside `[!important: 坐标变换 — 球面坐标]` callout.

### Task B6: Static SVG for §11.3 (X-型 / Y-型 region)

**Files:**
- Create: `media/img/chpt11-region-types.svg`

- [ ] **Step 1: Draw**

A single SVG with two side-by-side panels:
- Left: the same region $D$ shaded grey, with a vertical strip highlighted (X-型: $a\le x\le b$, $g_1(x)\le y\le g_2(x)$).
- Right: the same region with a horizontal strip highlighted (Y-型).

Keep it simple: lines + fill, no JS, no labels longer than one symbol.

- [ ] **Step 2: Reference it**

Inside `[!note: 例 — 双向求积比较]` callout in §11.3:

```markdown
> ![X-型 与 Y-型 区域](../media/img/chpt11-region-types.svg#600w)
```

Build, verify it shows up, sized ~600px wide.

---

## Phase C — Rewrite chpt11.md prose section by section

**Pre-flight:**

- [ ] **Backup the current file**

```bash
cp src/chpt11.md src/chpt11.md.bak
```

The rewrite happens *in place* in `src/chpt11.md`. The backup is a safety net while the chapter is half-rewritten. Delete it after Phase D verification.

**Authoring conventions (apply to every C task):**

- One callout per idea. Vary type per the role mapping in the spec.
- 例 N counter is global to the chapter; renumber as you go.
- All prose lives in callouts (no plain markdown body between section headings).
- Figures inside the callout that explains them, via `> ` prefix.
- Theorem proofs / multi-step derivations folded with `::: {.fold label="证明"} ... :::` (or `推导`, `详细计算`, etc.).
- Exercise cites (`::: {.exercise id="chpt11-ex-NNN"} :::`) sit at the end of the most relevant section, not nested inside a callout.

Each section below is one task. Steps within: write the prose; build; eyeball; iterate.

### Task C0: §11.0 章引言

**Files:**
- Modify: `src/chpt11.md` (top of file)

- [ ] **Step 1: Replace the current top tip callout**

Replace lines 1–11 (the `# 多元函数的积分` heading + the two top tip callouts) with a single, tighter chapter intro tip callout:

- One short paragraph stating *what* the chapter teaches and the *physical thread* (mass of a non-uniform plate / solid).
- One short paragraph naming the four moves ("分割 → 近似 → 求和 → 取极限") that recur in every section.

Keep it under ~120 Chinese characters total.

- [ ] **Step 2: Verify**

```bash
python3 build/build.py src/chpt11.md
```

Reload chapter 11. Top of page shows the new intro callout, no old "本章将系统学习…" prose.

### Task C1: §11.1 物理动机 — 不均匀薄片的质量

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline the callouts**

```
[!tip: 动机 — 不均匀薄片的质量]
  - 引入: 均匀薄片 M = ρ·A, 直接乘. 非均匀 ρ(x,y), 怎么办?
  - 分割: 把 D 划分为 N 个小片 ΔA_i; 每片几乎均匀, 用代表点 (x_i, y_i) 估计 ρ.
  - 求和: M ≈ Σ ρ(x_i, y_i) ΔA_i.
  - 取极限: N→∞, 得到精确 M.
  > 嵌入 chpt11-mass-plate 图: 看不同 N 下 Riemann 和如何收敛.

[!note: 数值实验 — 验证收敛]
  - 用图中的滑块取 N = 4, 16, 64, 观察 Riemann 和与真实积分的差距.
  - 列出数据: N=4, 16, 64 对应的近似值 + 误差.
  - 一句话总结: 极限存在 ⇒ 我们有了"质量"的精确定义.
```

- [ ] **Step 2: Write the prose**

Author the two callouts in the outlined order. Put the `chpt11-mass-plate` container (already placed in B1) inside the first callout via `> ` prefix.

- [ ] **Step 3: Build + eyeball**

```bash
python3 build/build.py src/chpt11.md
```

Section §11.1 reads top-to-bottom: motivation → figure → numerical experiment. No plain prose anywhere.

### Task C2: §11.2 把动机变成定义 — 二重积分

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline**

```
[!important: 定义 — 二重积分]
  - 假设 f(x,y) 在有界闭区域 D 上有界.
  - 划分 D = ⋃ ΔD_i, max diam(ΔD_i) → 0; 选取代表点 (ξ_i, η_i).
  - 若 lim Σ f(ξ_i, η_i) ΔA_i 存在且与划分/代表点选取无关, 称该极限为 f 在 D 上的二重积分:
    ∬_D f(x,y) dA.
  - dA 在直角坐标系中是 dx dy.
  > 嵌入 chpt11-double-integral (复用): Riemann 柱体收敛到曲面下体积.

[!tip: 几何意义 — 带符号体积 vs. 纯体积]
  > 嵌入 chpt11-example1 + chpt11-example2 配对图.
  - 短文字: 当 f ≥ 0, 二重积分给曲面下方的几何体积; 当 f 变号, 它给"带符号体积"——绿色为正, 红色为负, 净值是积分.

[!important: 性质 — 线性 / 区域可加性 / 单调性 / 平均值]
  - 4 条性质各一句, 用公式. 无证明.

[!extension: 拓展 — 可积性的充分条件]
  - 一句话: f 连续 ⇒ 可积; 仅在零测集上不连续也可积.
  - 不展开. 拓展类型, 表示"了解即可".
```

- [ ] **Step 2: Migrate existing prose**

The current chpt11.md has the definition derivation in the `[!important: 多变量积分]` callout (lines 33–56 of the old file, kept in `chpt11.md.bak`). Read it from the backup, lift the math content, rewrite tighter to match the role of `[!important: 定义]`.

- [ ] **Step 3: Embed reused figures**

`chpt11-double-integral` already inside its callout from the backup; reattach inside `[!important: 定义]` of the new prose.

`chpt11-example1` + `chpt11-example2` (currently outside any callout in the backup) move into the `[!tip: 几何意义]` callout via `> ` prefix wrapping the flex container.

- [ ] **Step 4: Build + eyeball**

### Task C3: §11.3 通过累次积分求解 (Fubini)

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline**

```
[!tip: 直觉 — 切片求和]
  > 嵌入 chpt11-iterated (B2 新): 两种切法并排.
  - 短文字: 把体积按 x 切片求和, 等价于先内层 ∫f dy 算每片的面积, 再外层 ∫(...) dx 求总体积. 反过来一样.

[!important: 定理 — Fubini (矩形区域)]
  - 设 f 在 D = [a,b]×[c,d] 上连续, 则 ∬_D f dA = ∫_a^b ∫_c^d f dy dx = ∫_c^d ∫_a^b f dx dy.
  ::: {.fold label="证明"}
    简短证明: f 一致连续 + Riemann 和分组求和 + 累次极限交换. 5–8 行.
  :::

[!important: 定理 — 一般区域上的累次积分 (X-型 / Y-型)]
  - X-型: D = {(x,y): a ≤ x ≤ b, g_1(x) ≤ y ≤ g_2(x)}, ∬_D f dA = ∫_a^b ∫_{g_1(x)}^{g_2(x)} f dy dx.
  - Y-型: 对偶定义.
  > 嵌入 chpt11-region-types.svg (B6).

[!note: 例 1 — 矩形区域上的二重积分]
  - 计算 ∬_{[0,1]×[0,2]} (x+y) dA. 选一个顺序, 算出.
  ::: {.fold label="详细计算"}
    完整三行计算.
  :::

[!note: 例 2 — X-型区域]
  - D 是 y = x 与 y = x^2 围成的区域. 算 ∬_D xy dA.
  ::: {.fold label="详细计算"}

[!tip: 何时换序? — 简化计算]
  - 一句话: 内积分若没有初等原函数 (如 e^{-y^2}), 换序常能救场.
  - 一个小例子: ∫_0^1 ∫_x^1 e^{y^2} dy dx → 换序 = ∫_0^1 ∫_0^y e^{y^2} dx dy = ...

[!caution: 易错 — 上下限的依赖关系]
  - 提醒: 内层积分变量的上下限可以依赖外层变量 (X-型那种); 外层不能依赖内层. 用错会无法消元.

::: {.exercise id="chpt11-ex-001"} :::
::: {.exercise id="chpt11-ex-002"} :::
::: {.exercise id="chpt11-ex-003"} :::
::: {.exercise id="chpt11-ex-004"} :::
::: {.exercise id="chpt11-ex-012"} :::
```

- [ ] **Step 2: Author**

Write each callout in order. Existing exercise cites (chpt11-ex-001..004, ex-012) move to the end of §11.3 — they fit here.

- [ ] **Step 3: Build + eyeball**

The two `[!important: 定理]` callouts each carry a `::: {.fold label="证明"}` — confirm both buttons appear, both bodies hidden by default, both toggle on click.

### Task C4: §11.4 坐标变换

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline**

```
[!tip: 直觉 — 面积元在变换下放缩多少?]
  - 线性变换 (u,v) → (x,y), 单位正方形 → 平行四边形. 面积放缩 = |det J|.
  > 嵌入 chpt11-jacobian (复用).

[!important: 定义 — Jacobian]
  - 给出 2-D Jacobian 矩阵和行列式公式.
  ::: {.fold label="为什么是这个公式"}
    全微分 + 矩阵形式 + 平行四边形面积 = |行列式|. 短推导.
  :::

[!important: 定理 — 二重积分换元公式]
  - 设 (u,v) → (x,y) 为 C^1 双射且 J ≠ 0, 则 ∬_D f(x,y) dx dy = ∬_{D'} f(x(u,v), y(u,v)) |J| du dv.
  ::: {.fold label="证明"}
    分割 D' → 用 J 估计每个像的面积 → 求和 → 极限. 6–10 行.
  :::

[!note: 例 — 极坐标作为重要特例]
  - x = r cosθ, y = r sinθ ⇒ J = r ⇒ dx dy = r dr dθ.
  > 嵌入 chpt11-polar-change (复用).

[!note: 例 — 用极坐标算 ∬_{x²+y²≤1} (1−x²−y²) dA]
  - 完整计算; 折叠详细步骤.
  ::: {.fold label="详细计算"}

[!tip: 何时换坐标?]
  - 圆形 / 扇形 / 环形 → 极坐标.
  - 椭圆 / 平行四边形 → 线性变换.
  - 双曲线区域 → uv = xy 之类.

[!caution: 易错 — Jacobian 的绝对值]
  - 要 |J|, 不是 J. 若 J<0 而漏了绝对值, 积分变号但面积应为正.

::: {.exercise id="chpt11-ex-013"} :::
```

- [ ] **Step 2: Author**

Reuse the existing detailed Jacobian content from chpt11.md.bak (the long `[!important: 雅可比行列式与坐标变换的深层关系]` callout, lines 134–182 in the backup) — much of it folds nicely into the `::: {.fold label="为什么是这个公式"}` body and the换元公式证明 fold.

- [ ] **Step 3: Build + eyeball**

### Task C5: §11.5 推广到三维 — 三重积分

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline**

```
[!tip: 动机 — 不均匀立体]
  > 嵌入 chpt11-mass-solid (B3 新).
  - 一句话: 把上一节的薄片换成立体, ρ(x,y,z), 总质量 = ∭_V ρ dV.

[!important: 定义 — 三重积分]
  - 平行 §11.2 的措辞: 划分 V = ⋃ ΔV_i, 取代表点, lim Σ f(ξ,η,ζ) ΔV_i.
  - 在直角系中, dV = dx dy dz.

[!important: 定理 — Fubini in 3-D (XY-投影 / Z-投影)]
  - XY-投影型: V = {(x,y,z): (x,y) ∈ D_{xy}, z_1(x,y) ≤ z ≤ z_2(x,y)}, ∭_V f dV = ∬_{D_{xy}} ∫_{z_1}^{z_2} f dz dA.
  - Z-投影型: 对偶.
  ::: {.fold label="证明"}
    类比二维; 4–6 行.
  :::

[!note: 例 — 直接累次积分]
  - 一个简单例子, 比如长方体 [0,1]³ 上的 xyz 积分.
  ::: {.fold label="详细计算"}

[!important: 坐标变换 — 柱面坐标]
  - x = ρ cosθ, y = ρ sinθ, z = z; |J| = ρ; dV = ρ dρ dθ dz.
  > 嵌入 chpt11-cylindrical (B4 新).

[!important: 坐标变换 — 球面坐标]
  - x = ρ sinφ cosθ, y = ρ sinφ sinθ, z = ρ cosφ; |J| = ρ²sinφ; dV = ρ²sinφ dρ dφ dθ.
  > 嵌入 chpt11-spherical (B5 新).
  ::: {.fold label="为什么是 ρ²sinφ"}
    几何分解: dρ × ρ dφ × ρ sinφ dθ. 4 行.
  :::

[!note: 例 — 球的体积, 算两遍 (球坐标 / 柱坐标)]
  > 嵌入 chpt11-example12 + chpt11-example13 (复用).
  - 球坐标: ρ²sinφ 直接积出 4πR³/3.
  - 柱坐标: ρ √(R²-ρ²) 积分, 结果一致 → 验证.
  ::: {.fold label="详细计算 (两种方式)"}

[!tip: 何时用哪种坐标?]
  - 圆柱状: 柱坐标.
  - 球状或锥状: 球坐标.
  - 方盒: 直角.
  - 一般原则: 让积分区域成为坐标网格的"自然"形状.

::: {.exercise id="chpt11-ex-010"} :::
::: {.exercise id="chpt11-ex-011"} :::
```

- [ ] **Step 2: Author**

The existing chpt11.md.bak has essentially nothing for §11.5 (just orphan figures + 2 exercises). This is the most-from-scratch section.

- [ ] **Step 3: Build + eyeball**

### Task C6: §11.6 更多应用

**Files:**
- Modify: `src/chpt11.md`

- [ ] **Step 1: Outline**

```
[!important: 应用 — 质心 (2-D / 3-D)]
  - 离散公式 → 连续推广; 二维 (x̄, ȳ); 三维 (x̄, ȳ, z̄).
  - 质量公式 M = ∬_D μ dA / ∭_V μ dV.

[!note: 例 — 求半圆盘的质心 (取 μ = 1)]
  - 利用对称性: x̄ = 0; 算 ȳ.
  ::: {.fold label="详细计算"}

[!extension: 拓展 — 转动惯量]
  - I(x_0, y_0) = ∬_D μ [(x-x_0)² + (y-y_0)²] dA.
  - 质心是使 I 取最小值的位置 (一句话).
  ::: {.fold label="为什么质心使 I 最小"}
    分别对 x_0, y_0 求偏导 = 0 → 解出. 6 行.
  :::

[!extension: 拓展 — 平行轴定理]
  - I(x_0, y_0) = I_c + M r² (r = 两轴间距).
  ::: {.fold label="证明"}
    展开 + 交叉项消去 (质心定义). 8 行.
  :::

[!tip: 速查 — 体积 / 表面积 / 流量]
  - 体积: V = ∭_V dV (f ≡ 1).
  - 曲面下方体积: V = ∬_D f dA (f ≥ 0).
  - 流量、引力等: 第 12 章.

::: {.exercise id="chpt11-ex-005"} :::
::: {.exercise id="chpt11-ex-006"} :::
::: {.exercise id="chpt11-ex-007"} :::
::: {.exercise id="chpt11-ex-008"} :::
::: {.exercise id="chpt11-ex-009"} :::
```

- [ ] **Step 2: Author**

Lift content from the existing 质量 / 转动惯量 / 平行轴定理 callouts in `chpt11.md.bak`. Most of the math survives; the wrapping changes (statement visible, derivation folded).

The §11.6 centroid SVG (P2) is *not* added in this task — skip.

- [ ] **Step 3: Build + eyeball**

### Task C7: Final-pass review

**Files:**
- Modify: `src/chpt11.md` (touch-ups)
- Delete: `src/chpt11.md.bak` (after this task passes)

- [ ] **Step 1: Run the spec test plan**

The spec's "Test plan" section lists 10 checks. Walk each:

```bash
# 1. Every prose chunk in chpt11 is a callout (no plain <p> direct under #content).
#    Quick proxy:
grep -c '<div id="content">' docs/chapter11.html  # 1
# Then visually confirm the only direct children of #content (besides headings) are .callout divs.

# 2. Each figure container is inside a .callout-body.
for id in chpt11-mass-plate chpt11-double-integral chpt11-example1 chpt11-example2 \
          chpt11-iterated chpt11-jacobian chpt11-polar-change chpt11-mass-solid \
          chpt11-cylindrical chpt11-spherical chpt11-example12 chpt11-example13; do
  awk -v id="id=\"$id\"" '
    /callout-body/{in_body=1}
    /<\/div>/&&in_body{in_body=0}
    in_body && index($0, id){print id " ✓ inside callout-body"; found=1}
    END{if(!found) print id " ✗ NOT inside callout-body"}
  ' docs/chapter11.html
done

# 3. Console clean — open browser, walk through every section, no errors/warnings.

# 4. Every fold button toggles. Click each one once.

# 5. Sidebar TOC lists §11.1 – §11.6 in order — visual.

# 6. All exercise cites resolve (no missing-id complaints from build):
python3 build/build.py src/chpt11.md 2>&1 | grep -i 'missing\|unknown.*exercise'
# Expected: empty
```

- [ ] **Step 2: Tighten**

Read top-to-bottom in browser. Tighten any callout that runs over half a screen. Promote any embedded "but actually…" caveat into a proper `[!caution]` callout if it's worth flagging.

- [ ] **Step 3: Delete the backup**

```bash
rm src/chpt11.md.bak
```

- [ ] **Step 4: Final commit (user-driven)**

User decides commit boundary; not scripted here.

---

## Phase D — WORKFLOW.md update

**Files:**
- Modify: `NewMathAnalysis/WORKFLOW.md`

### Task D1: Document the design principle

- [ ] **Step 1: Add a "Design principle" subsection at the top of "Markdown Authoring"**

Insert immediately after the existing "Markdown Authoring" heading line:

```markdown
### Design principle: focused statement visible, depth on demand

Each callout shows only its focused statement by default. Anything that's
"the work behind it" — proof, derivation, alternate solution — lives
inside the same callout and reveals on click via `::: {.fold label="证明"} ... :::`.

Readers see structure first, depth on demand. This mirrors the existing
exercise system (problem visible, 答案 / 提示 reveal). Apply the same
pattern when authoring theorems, derivations, and worked examples in any
chapter.
```

### Task D2: Document the fold syntax

- [ ] **Step 1: Add a "Foldable content" subsection**

Add a new subsection between "Video on a callout" and "Inline emphasis":

```markdown
### Foldable content (`::: {.fold label="..."} :::`)

Hide a multi-paragraph block (theorem proof, derivation, alternate solution)
behind a reveal button inside any callout:

​```markdown
> [!important: 定理 — Fubini]
>
> 设 $f$ 在矩形 $D$ 上连续, 则
> $$ \iint_D f \, dA = \int_a^b\!\int_c^d f \,dy\,dx. $$
>
> ::: {.fold label="证明"}
> 证明的多段内容…
> :::
​```

- `label` defaults to `"展开"` if omitted.
- The fold body is hidden until clicked; common labels: `证明`, `推导`, `详细计算`, `更多细节`.
- KaTeX renders math inside the body the first time it opens.
- The fold renders the same way regardless of the parent callout type.
```

### Task D3: Update the callout role mapping

- [ ] **Step 1: Add a "Recommended type per role" subsection**

After the existing "Available types" line in the callout section, add:

```markdown
**Recommended type per role:**

| Role | Type |
|---|---|
| 动机 / 直觉 | `tip` |
| 定义 / 定理 | `important` |
| 例题 | `note` |
| 易错 / 提醒 | `caution` |
| 不要求 / 拓展 | `extension` |
| 历史 / 文化 | `warning` |

Theorem proofs, derivations, and detailed example calculations live
inside a `::: {.fold label="..."} :::` block within the same callout.
```

---

## Self-review

**Spec coverage:**
- §11 outline (Z) → Phase C (one task per section, C0–C6).
- Callout role→type mapping → Phase D3 + applied throughout Phase C tasks.
- Fold mechanism → Phase A (A1 filter, A2 CSS, A3 JS).
- Figure plan (5 new + 1 SVG + 6 reused) → Phase B (B1–B5 scenes, B6 SVG; reuses placed in C tasks).
- Exercises redistributed, not re-authored → Phase C tasks each end with the exercise cites for that section.
- Length target ~480–520 lines → enforced by C7 step 2 ("tighten any callout that runs over half a screen").
- File plan (backup, replace, new scenes, etc.) → Phase C pre-flight + B/C tasks.
- Test plan → C7 step 1.
- WORKFLOW.md updates → Phase D.

**Placeholder scan:** No "TBD" or "implement later". Prose tasks (Phase C) intentionally don't pre-write the Chinese math content — that's the actual work the author does in the task — but each task gives a concrete callout outline so there's no ambiguity about *what* to write, only *how to phrase it*.

**Type / name consistency:**
- `.callout-fold`, `.callout-fold-btn`, `.callout-fold-body`, `data-label`, `aria-expanded` used consistently across A1/A2/A3.
- New scene module filenames consistent with existing pattern: `chpt11-<purpose>.js`.
- Callout title conventions match the spec's role mapping.

No gaps found.
