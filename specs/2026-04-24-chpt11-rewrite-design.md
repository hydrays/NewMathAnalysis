# Chapter 11 Rewrite — Design

Date: 2026-04-24
Scope: `NewMathAnalysis/src/chpt11.md` (full rewrite), plus a small new
`fold` callout feature touching `build/filters.lua`, `build/assets/app.js`,
`build/assets/app.css`, and `WORKFLOW.md`.

## Goal

Rewrite §11 ("多元函数的积分") as an application-driven, callout-only
chapter where every prose chunk lives in a typed callout, every figure
sits inside the callout it supports, and every theorem proof / multi-step
derivation is folded behind a reveal button so the visible block stays on
the focused statement.

The current chpt11.md is the only source. No outside textbook.

## Design principle (load-bearing)

> **Each callout shows only its focused statement by default. Anything
> that's "the work behind it" — proof, derivation, alternate solution —
> lives inside the same callout and reveals on click.**

Readers see structure first, depth on demand. This mirrors how the
existing exercise system handles 答案 / 提示. We extend the same idea to
theorems with proofs and to long worked derivations. The principle is
documented in `WORKFLOW.md` so future chapters can follow the pattern.

## Outline (Z — application-driven)

```
§11.0 章引言 (single tip callout)
§11.1 物理动机: 不均匀薄片的质量
       Riemann 分割动机 → 数值实验 → 极限
§11.2 把动机变成定义: 二重积分
       形式定义 + 几何意义 (带符号体积 vs. 纯体积) + 性质
§11.3 通过累次积分求解 (Fubini)
       矩形区域 / X-型 / Y-型 / 换序
§11.4 坐标变换
       Jacobian 直觉 → 极坐标 → 一般公式 → 何时换坐标
§11.5 推广到三维: 三重积分
       动机 → 定义 → 累次积分 → 柱面坐标 → 球面坐标
§11.6 更多应用
       质心 / 转动惯量 (拓展, 不要求) / 平行轴定理 (拓展) /
       体积、表面积速查
```

§11.6's subsections are independent — students may pick what they need.

## Callout role → type mapping

| Role | Type | Header convention |
|---|---|---|
| 动机 / 直觉 | `tip` 提示 | `[!tip: 动机 — ...]` |
| 定义 | `important` 重要 | `[!important: 定义 — ...]` |
| 定理 (with foldable proof) | `important` 重要 | `[!important: 定理 — ...]` |
| 例题 | `note` 注 | `[!note: 例 N — ...]` (auto-numbered globally) |
| 易错 / 提醒 | `caution` 注意 | `[!caution: 易错 — ...]` |
| 不要求 / 拓展 | `extension` 拓展 | `[!extension: 拓展 — ...]` |
| 历史 / 文化 | `warning` 警告 | `[!warning: 历史 — ...]` (used sparingly) |

### Authoring rules

- **One callout = one idea.** Derivations beyond ~8 equations split into a
  `note` chain or fold into the parent callout.
- **No plain markdown prose between callouts.** Section headings (`##`,
  `###`) and exercise cites (`::: {.exercise id="..."} :::`) are the only
  loose markdown.
- **Figures live inside the callout that explains them**, using the
  `> ` prefix so Pandoc keeps them inside the blockquote (verified: works
  with current `filters.lua` + `build.py` lazy-load rewrite).
- **例 N counter is global to the chapter** for easy cross-reference.

## Fold mechanism (new feature)

### Author syntax

```markdown
> [!important: 定理 — Fubini]
>
> 设 $f$ 在矩形 $D = [a,b]\times[c,d]$ 上连续, 则
> $$ \iint_D f \, dA = \int_a^b\!\left(\int_c^d f(x,y)\,dy\right)dx. $$
>
> ::: {.fold label="证明"}
> ⟨multi-paragraph proof⟩
> :::
```

- The `::: {.fold label="..."} ... :::` block must sit inside a callout.
- `label` defaults to `"展开"` if omitted; common labels: `证明`, `推导`,
  `详细计算`, `更多细节`.

### Build behaviour

`filters.lua` adds a `Div` handler:

- If a `Div` has class `fold`, it is replaced by a `pandoc.RawBlock`
  containing:
  ```html
  <div class="callout-fold">
    <button class="callout-fold-btn" type="button">▶ 证明</button>
    <div class="callout-fold-body" hidden>
      <!-- inner content (re-walked by Pandoc as nested blocks) -->
    </div>
  </div>
  ```
- The button text uses the `label` attribute prefixed with `▶` when
  closed, swapped to `▼` when open.

### Front-end

- `app.js` delegated click handler matches `.callout-fold-btn`, toggles
  the sibling `.callout-fold-body` `hidden` attribute, swaps the arrow
  glyph, and adds/removes a `.is-open` class on the parent `.callout-fold`
  for styling.
- `app.css` styles `.callout-fold-body` with a thin top border and
  matching emerald left border, echoing the existing `.ex-ans-panel`
  treatment so 定理→证明 visually mirrors 例→答案.

## Figure plan

| § | Callout | Figure | Status |
|---|---|---|---|
| 11.1 | `tip: 动机 — 不均匀薄片的质量` | `chpt11-mass-plate.js` (NEW) — density-coloured plate, slider over N, shows Riemann sum vs. true integral | new |
| 11.2 | `important: 定义 — 二重积分` | `chpt11-double-integral.js` | reuse |
| 11.2 | `tip: 几何意义 — 带符号体积 vs. 纯体积` | `chpt11-example1.js` + `chpt11-example2.js` | reuse, paired |
| 11.3 | `tip: 直觉 — 切片求和` | `chpt11-iterated.js` (NEW) — 3-D solid, two slicing orders side-by-side, partial-integral curves | new |
| 11.3 | `note: 例 — 双向求积比较` | static SVG of an X-型/Y-型 region | new, lightweight |
| 11.4 | `important: 定义 — Jacobian` | `chpt11-jacobian.js` | reuse |
| 11.4 | `note: 例 — 极坐标网格的面积元` | `chpt11-polar-change.js` | reuse |
| 11.5 | `tip: 动机 — 不均匀立体` | `chpt11-mass-solid.js` (NEW) — density-coloured solid, slicing visualisation | new |
| 11.5 | `important: 坐标变换 — 柱面坐标` | `chpt11-cylindrical.js` (NEW) — cylindrical grid on a cylinder, one volume element highlighted | new |
| 11.5 | `important: 坐标变换 — 球面坐标` | `chpt11-spherical.js` (NEW) — spherical grid on a ball, one volume element highlighted | new |
| 11.5 | `note: 例 — 球的体积 / 类似立体` | `chpt11-example12.js` + `chpt11-example13.js` | reuse, paired |
| 11.6 | `note: 例 — 质心定位` | static SVG of plate with centroid star (P2) | optional |
| 11.6 | `extension: 拓展 — 转动惯量` | none | skip |

**Counts.** 6 reused, 5 new Three.js scenes, 1 small SVG, 1 optional SVG.

**Figure rule.** No long equations rendered inside the figure. Short
axis labels and one-symbol annotations (e.g., `f(x,y)`) only. Math stays
in the surrounding prose callout.

**Three.js scene constraints** (matching existing scenes):

- ES module under `media/threejs/`, no per-scene importmap (head
  importmap covers `three` and `three/addons/`).
- Imports only: `three`, `three/addons/controls/OrbitControls.js`,
  optionally `three/addons/renderers/CSS2DRenderer.js`,
  `three/addons/lines/Line2.js` (and its deps). All already self-hosted.
- Coordinate convention: math `(x, y, z)` → Three.js `(x, z, -y)`.
- Container `<div>` placed inside its callout via `> ` prefix.
- `<script type="module" src="threejs/...js">` directly under the div
  (build.py rewrites to `data-lazy-module` form).

## Exercises

`src/exercises/chpt11-ex-001.md` … `chpt11-ex-013.md` stay as-is. The
rewrite redistributes their `::: {.exercise id="..."} :::` cites across
the new outline so each lands in the section that matches its content. A
section without a relevant exercise carries no exercise cite; we don't
add filler.

## Length target

Roughly **480–520 lines** in `src/chpt11.md` — about 1.5× the current
~316. Growth is driven by:

- Filling the two `[图略, 待补充]` placeholders with real prose + figure.
- Promoting §11.5 三重积分 from stub to a full section.
- Adding 动机 callouts at the head of §11.1 and §11.5.
- Cylindrical / spherical coordinate sections (currently absent).

Anything significantly longer signals over-writing.

## File plan

- **Backup**: `cp src/chpt11.md src/chpt11.md.bak` before overwriting.
  Delete `chpt11.md.bak` after a clean build + visual review.
- **Replace** `src/chpt11.md` with the new content.
- **New scenes** under `media/threejs/`:
  - `chpt11-mass-plate.js`
  - `chpt11-iterated.js`
  - `chpt11-mass-solid.js`
  - `chpt11-cylindrical.js`
  - `chpt11-spherical.js`
- **Lightweight assets** under `media/img/`: one or two new SVGs (X-型/Y-型
  region; optionally centroid plate).
- **`build/filters.lua`**: add `Div` handler for class `fold`.
- **`build/assets/app.js`**: extend the existing delegated click handler
  for `.callout-fold-btn`.
- **`build/assets/app.css`**: styles for `.callout-fold`,
  `.callout-fold-btn`, `.callout-fold-body`.
- **`WORKFLOW.md`**: new "Foldable content (`::: {.fold} :::`)" section
  + the design principle stated up front under "Markdown Authoring".

## Test plan

After full rebuild:

- [ ] Every prose chunk in chpt11 sits in a callout (no plain `<p>`
      directly inside `#content`).
- [ ] Each figure container is a child of a `.callout-body`.
- [ ] All `> [!type: title]` callouts render with the right type colour.
- [ ] All 5 new Three.js scenes load on scroll and render a non-blank
      canvas in their callout.
- [ ] The two reused figure pairs (chpt11-example1+2, chpt11-example12+13)
      still render side-by-side.
- [ ] At least one `[!important: 定理 — ...]` callout exercises the fold
      mechanism: button visible, body hidden by default, click toggles.
- [ ] Console clean: no importmap warnings, no module resolution errors.
- [ ] Section TOC in the right sidebar lists §11.1 – §11.6 in order.
- [ ] All `::: {.exercise id="chpt11-ex-NNN"} :::` cites resolve (no
      missing-id warnings from `exercise.py`).

## Out of scope

- Re-authoring `src/exercises/chpt11-ex-*.md` content.
- Style changes to other chapters; they stay as-is. WORKFLOW.md documents
  the new pattern; future chapters can opt in.
- The §11.6 centroid SVG is P2 — only if writing budget allows.
- The §11.6 转动惯量 figure is dropped (formulas suffice for an extension
  callout).

## Risks

- **Three.js scene authoring time** is the largest cost. 5 new scenes at
  ~200–400 lines each is roughly 1500 lines of WebGL code. Mitigation: do
  scenes one section at a time; ship sections progressively.
- **Fold mechanism interactions with SPA nav** — `app.js` already handles
  delegated clicks across SPA swaps for exercises and video buttons. The
  fold handler follows the same pattern; should be uneventful.
- **Pandoc fenced div inside `> ` blockquote** is verified: the fenced
  `::: {.fold label="证明"}` block lifts cleanly to a
  `<div class="fold" data-label="证明">` with its content as proper
  child blocks, even when the whole thing is `> `-prefixed. The Lua
  filter's `Div` handler operates on the parsed structure, so no
  fall-back path is needed.
