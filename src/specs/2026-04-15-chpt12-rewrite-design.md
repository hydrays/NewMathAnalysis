# Chapter 12 Rewrite — Design Spec

**Date:** 2026-04-15  
**File:** `src/chpt12.md`  
**Scope:** Full authorial rewrite — current file treated as raw lecture notes to draw from; prose, structure, and pedagogy written from scratch.

---

## Pedagogical Decisions

| Dimension | Decision |
|---|---|
| Narrative thread | Physics motivation first; FTC-generalization payoff at the end |
| Proof depth | Full proof for Green's theorem; proof sketches for Gauss and Stokes |
| 2D vs 3D | Complete the 2D story first (§12.1–12.4), then explicitly extend to 3D (§12.5–12.6) |
| Notation | Unified throughout: $\mathbf{F}$ for vector fields, $\hat{\mathbf{i}},\hat{\mathbf{j}},\hat{\mathbf{k}}$ for unit vectors, $\mathrm{d}$ for differentials |

---

## Section-by-Section Spec

### 12.1 场与向量场

**Length:** ~1 page  
**Role:** Orientation — no heavy math, establishes vocabulary and visual intuition.

**Content:**
- Open with physical examples: temperature (scalar), wind velocity (vector), gravitational force (vector)
- Definition: a **scalar field** is a function $f: \mathbb{R}^n \to \mathbb{R}$; a **vector field** is $\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^n$
- Component form: $\mathbf{F}(x,y) = P(x,y)\hat{\mathbf{i}} + Q(x,y)\hat{\mathbf{j}}$ (2D); $\mathbf{F}(x,y,z) = P\hat{\mathbf{i}} + Q\hat{\mathbf{j}} + R\hat{\mathbf{k}}$ (3D)
- Keep all four 2D vector field figures (fig2-4-1 through fig2-4-4) with brief descriptions of what each one "looks like" physically
- Keep both Three.js 3D interactive panels
- Closing sentence: "本章的核心问题是：如何在向量场中进行积分？"

**Callout types to use:** `[!important]` for definitions; `[!note]` for the 3D figures.

---

### 12.2 第一类曲线积分：标量场沿曲线的积分

**Length:** ~2 pages  
**Role:** Introduce line integrals through the simplest physical picture; establish the parametric reduction technique.

**Content:**
- **Opening problem (callout-tip):** A wire bent into curve $L$, linear density $\rho(x,y)$. Total mass?
- Riemann sum: partition $L$ into arcs $\Delta s_i$, total mass $\approx \sum \rho(x_i, y_i)\Delta s_i$, take limit → $\int_L \rho\,\mathrm{d}s$
- **Definition (callout-important):** $\int_L f(x,y)\,\mathrm{d}s$ for $f$ continuous on $L$
- Reduction theorem: if $L$ is parametrized by $x=x(t)$, $y=y(t)$, $t\in[t_0,t_1]$, then $\mathrm{d}s = \sqrt{x'(t)^2+y'(t)^2}\,\mathrm{d}t$, so
  $$\int_L f(x,y)\,\mathrm{d}s = \int_{t_0}^{t_1} f(x(t),y(t))\sqrt{x'(t)^2+y'(t)^2}\,\mathrm{d}t$$
- Note: result is independent of parametrization and of orientation (because $\mathrm{d}s > 0$ always)
- One worked example: mass of a wire along $y=x^2$ from $(0,0)$ to $(1,1)$ with $\rho=1$

**Fix from current draft:** The definition block incorrectly uses $\mathrm{d}x$ instead of $\mathrm{d}s$. Fixed here.

**Exercises:** ex-001, ex-002

---

### 12.3 第二类曲线积分：向量场沿曲线做的功

**Length:** ~3 pages  
**Role:** The more physically important type of line integral; introduces orientation and the connection between the two types.

**Content:**
- **Opening problem (callout-tip):** Particle moves along $L$ under force field $\mathbf{F}(x,y)$. How much work is done?
- Physical argument: work = force · displacement, so $W \approx \sum \mathbf{F}(x_i,y_i)\cdot\Delta\mathbf{r}_i$ → $W = \int_L \mathbf{F}\cdot\mathrm{d}\mathbf{r}$
- Expand: $\mathrm{d}\mathbf{r} = \mathrm{d}x\,\hat{\mathbf{i}} + \mathrm{d}y\,\hat{\mathbf{j}}$, so $W = \int_L P\,\mathrm{d}x + Q\,\mathrm{d}y$
- **Definition (callout-important)**
- **Key difference from type I:** orientation matters — reversing $L$ negates the integral. State clearly with brief physical justification (walking against the force does negative work).
- Reduction to parameter integral: substitute $\mathrm{d}x = x'(t)\,\mathrm{d}t$, $\mathrm{d}y = y'(t)\,\mathrm{d}t$
- **Relationship between the two types (callout-note):** Since $\mathrm{d}\mathbf{r} = \boldsymbol{\tau}\,\mathrm{d}s$ where $\boldsymbol{\tau}$ is the unit tangent vector, we have $W = \int_L \mathbf{F}\cdot\boldsymbol{\tau}\,\mathrm{d}s$. This is type I with integrand $\mathbf{F}\cdot\boldsymbol{\tau}$.

**Exercises:** ex-003, ex-004, ex-005, ex-006, ex-007, ex-008

---

### 12.4 格林公式与保守场

**Length:** ~5 pages (the heart of the chapter)

#### 12.4.1 格林公式

**Content:**
- **Opening problem (callout-tip):** Fluid circulates in region $D$. The circulation $\oint_C \mathbf{F}\cdot\mathrm{d}\mathbf{r}$ around the boundary — can we compute it from what's happening inside?
- Motivate $\operatorname{curl}\mathbf{F} = Q_x - P_y$ as the pointwise "rotation rate" of the field (without invoking the 3D curl yet)
- **Theorem (callout-important):** Green's theorem — state cleanly with orientation convention (counterclockwise boundary, $C = \partial D^+$):
  $$\oint_C P\,\mathrm{d}x + Q\,\mathrm{d}y = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathrm{d}A$$
- **Full proof** in a callout-extension block:
  1. Special case: $Q=0$, $D$ vertically simple. Reduce to single-variable FTC.
  2. Additivity: split $D$ into two vertically simple subregions; interior edges cancel.
  3. General case follows by decomposition.
- **Application (callout-note):** Area formula $A = \frac{1}{2}\oint_C x\,\mathrm{d}y - y\,\mathrm{d}x$ as a corollary

**Exercises:** ex-010, ex-011, ex-012, ex-013

#### 12.4.2 保守场与曲线积分基本定理

**Content:**
- **Opening question:** When is work path-independent? Physical examples: gravity (yes), friction (no).
- **Definition (callout-important):** $\mathbf{F}$ is **conservative** (保守场) if $\oint_C \mathbf{F}\cdot\mathrm{d}\mathbf{r} = 0$ for every closed curve $C$.
- **Fundamental Theorem of Line Integrals (callout-important):** If $\mathbf{F} = \nabla f$, then $\int_C \mathbf{F}\cdot\mathrm{d}\mathbf{r} = f(B) - f(A)$. Proof: substitute $\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \mathrm{d}f$ and apply FTC.
- **Criterion (callout-important):** On a simply connected domain, $\mathbf{F}$ is conservative $\Leftrightarrow$ $P_y = Q_x$. Derive necessity from mixed partials; note sufficiency follows from Green's theorem (state without proving).
- **Finding the potential $f$:** Integration method — integrate $P$ with respect to $x$, differentiate with respect to $y$, match $Q$.
- **Definition of curl in 2D (callout-note):** $\operatorname{curl}\mathbf{F} = Q_x - P_y$. Conservative $\Leftrightarrow$ $\operatorname{curl}\mathbf{F} = 0$.

**Exercises:** ex-009

---

### 12.5 曲面积分：向量场穿过曲面的通量

**Length:** ~3 pages  
**Role:** Bridge into 3D; the natural 3D analogue of the type II line integral.

**Content:**
- Bridge sentence opening the 3D half: "现在我们将相同的思路从曲线推广到曲面."
- **Opening problem (callout-tip):** Fluid flows with velocity field $\mathbf{F}(x,y,z)$. A surface $S$ lies in the fluid. How much fluid passes through $S$ per unit time?
- Physical argument: flux through a small patch $\Delta S_i$ with outward normal $\mathbf{n}_i$ is $\mathbf{F}\cdot\mathbf{n}_i\,\Delta S_i$; sum and take limit → $\iint_S \mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S$
- **Definition (callout-important)**
- **Reduction for $z = g(x,y)$:** Tangent vectors $\mathbf{v}_1 = (1,0,g_x)$, $\mathbf{v}_2 = (0,1,g_y)$; normal $\mathbf{n}\,\mathrm{d}S = \mathbf{v}_1\times\mathbf{v}_2\,\mathrm{d}x\,\mathrm{d}y = (-g_x,-g_y,1)\,\mathrm{d}x\,\mathrm{d}y$; reduces to a double integral over $D_{xy}$
- **Orientation (callout-note):** For a closed surface, "outward" is well-defined; for open surfaces, a choice must be made. Changing orientation negates the integral.
- One worked example: flux of $\mathbf{F} = x\hat{\mathbf{i}}+y\hat{\mathbf{j}}+z\hat{\mathbf{k}}$ through the upper hemisphere

**Exercises:** ex-014

---

### 12.6 高斯公式与斯托克斯公式

**Length:** ~4 pages

#### 12.6.1 高斯公式

**Content:**
- **Opening problem (callout-tip):** Sources and sinks inside a closed region $V$ — every unit of fluid created must eventually exit through $\partial V$. Total outward flux = total creation rate.
- **Definition (callout-note):** $\operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = P_x + Q_y + R_z$ — pointwise source strength.
- **Theorem (callout-important):** Gauss's theorem:
  $$\oiint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iiint_V \nabla\cdot\mathbf{F}\,\mathrm{d}V$$
- **Proof sketch (callout-extension):** Split $\mathbf{F}$ into three components; handle $R\hat{\mathbf{k}}$ component: integrate $R_z$ over $V$ in $z$ first (single-variable FTC) → surface integrals on top and bottom faces; the other components follow by symmetry.
- Physical interpretation: $\operatorname{div}\mathbf{F} > 0$ is a source, $< 0$ is a sink, $= 0$ is incompressible flow.

**Exercises:** ex-015, ex-016, ex-017, ex-018

#### 12.6.2 斯托克斯公式

**Content:**
- Introduce 3D line integrals briefly: $\int_C P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z$ — same definition as 2D, just one more component.
- **Definition of 3D curl (callout-important):**
  $$\operatorname{curl}\mathbf{F} = \nabla\times\mathbf{F} = \begin{vmatrix}\hat{\mathbf{i}}&\hat{\mathbf{j}}&\hat{\mathbf{k}}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix} = (R_y-Q_z)\hat{\mathbf{i}}+(P_z-R_x)\hat{\mathbf{j}}+(Q_x-P_y)\hat{\mathbf{k}}$$
- Note: $\operatorname{curl}\mathbf{F}$ is a vector in 3D; the 2D curl $Q_x-P_y$ is its $\hat{\mathbf{k}}$-component. This connects the two.
- **Theorem (callout-important):** Stokes's theorem — for oriented surface $S$ with boundary curve $\partial S$:
  $$\oint_{\partial S}\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \iint_S(\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S$$
- **Proof sketch (callout-extension):** Parametrize $S$ as $\mathbf{r}(u,v)$ over a region $R$ in the $uv$-plane; transform both sides using the chain rule; the result reduces to Green's theorem on $R$.
- **Conservative fields in 3D (callout-important):** $\mathbf{F} = \nabla f \Leftrightarrow \operatorname{curl}\mathbf{F} = \mathbf{0}$. The three scalar conditions $Q_x=P_y$, $R_y=Q_z$, $R_x=P_z$ follow from mixed partials.

**Exercises:** ex-019, ex-020, ex-021, ex-022

---

### 12.7 统一视角：广义牛顿-莱布尼茨公式

**Length:** ~1.5 pages  
**Role:** The payoff — reveal that all four theorems are one idea.

**Content:**
- Open by lining up the four theorems in a table:

  | 定理 | 对象 | 区域 $\Omega$ | 边界 $\partial\Omega$ | 公式 |
  |---|---|---|---|---|
  | 牛顿-莱布尼茨 | 函数 $f'$ | 区间 $[a,b]$ | 端点 $\{a,b\}$ | $\int_a^b f' = f(b)-f(a)$ |
  | 格林公式 | $\operatorname{curl}\mathbf{F}$ | 平面区域 $D$ | 曲线 $\partial D$ | $\iint_D \operatorname{curl}\mathbf{F}\,\mathrm{d}A = \oint_{\partial D}\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ |
  | 斯托克斯公式 | $\operatorname{curl}\mathbf{F}$ | 曲面 $S$ | 曲线 $\partial S$ | $\iint_S (\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S = \oint_{\partial S}\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ |
  | 高斯公式 | $\operatorname{div}\mathbf{F}$ | 空间区域 $V$ | 曲面 $\partial V$ | $\iiint_V \nabla\cdot\mathbf{F}\,\mathrm{d}V = \oiint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S$ |

- State the pattern in words: "对区域上某种'导数'的积分，等于对其边界上'原函数'的积分."
- Mention (one sentence, no development) that in the language of differential forms, all four are a single formula $\int_\Omega \mathrm{d}\omega = \int_{\partial\Omega}\omega$ — a horizon for further study (real analysis or differential geometry).
- Close with a short, authorial paragraph on the unity of calculus.

---

## Assets Retained From Current Chapter

- All four 2D vector field figures (`fig2-4-1` through `fig2-4-4`)
- Both Three.js interactive panels (`chapter12-vectorfield.js`)
- All 22 exercise references (`ex-001` through `ex-022`) — none dropped, placement adjusted

## Notation Standardized

| Item | Standard used throughout |
|---|---|
| Vector field | $\mathbf{F}$ (not $\vec{F}$) |
| Unit vectors | $\hat{\mathbf{i}},\hat{\mathbf{j}},\hat{\mathbf{k}}$ (not $\hat{i}$) |
| Curl (2D) | $\operatorname{curl}\mathbf{F} = Q_x - P_y$ |
| Curl (3D) | $\nabla\times\mathbf{F}$ |
| Divergence | $\nabla\cdot\mathbf{F}$ |
| Differentials | $\mathrm{d}x$, $\mathrm{d}s$, $\mathrm{d}S$, $\mathrm{d}V$ (upright) |

## What Is Removed

- All bare "图" placeholder text
- The `[!TIP]**有问题**` draft block
- The "(以下文字由AI生成)" paragraph
- The duplicate Green's theorem presentation (was stated twice in different styles)
- The disconnected "两类曲线积分之间的关系" sub-subsection (absorbed into §12.3)
