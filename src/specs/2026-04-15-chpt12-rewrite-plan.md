# Chapter 12 Full Authorial Rewrite — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `src/chpt12.md` (曲线积分和曲面积分) from scratch as a polished textbook chapter — physics-motivated, structurally clean, with full Green's theorem proof and a unified FTC payoff.

**Architecture:** Seven sections (§12.1–§12.7). Complete 2D theory first (§12.1–§12.4), then 3D extension (§12.5–§12.6), then unified perspective (§12.7). Physics-first narrative: every major concept opens with a physical problem, then derives the math.

**Tech Stack:** Markdown + KaTeX math, VLOOK callout syntax (`[!tip]`, `[!important]`, `[!note]`, `[!extension]`), exercise references (`::: {.exercise id="chptN-ex-NNN"} :::`), build via `python3 build/build.py` from `NewMathAnalysis/`.

**Spec:** `src/specs/2026-04-15-chpt12-rewrite-design.md`

---

## Callout Type Reference

| Type | Usage |
|---|---|
| `[!tip]` | Opening physical problems, motivating questions |
| `[!important]` | Definitions, theorems, key criteria |
| `[!note]` | Connections, remarks, side observations |
| `[!extension]` | Full proofs and proof sketches |

Callout syntax:
```markdown
> [!important]
>
> **定义（向量场）** ...
```

Callout with custom title:
```markdown
> [!important: 格林公式]
>
> ...
```

Exercise reference syntax (must be at column 0, not inside a callout):
```markdown
::: {.exercise id="chpt12-ex-001"}
:::
```

Image syntax: `![alt text](media/img/filename.png#200pt)`

Three.js block (preserve exactly — already working):
```html
<div style="display:flex;gap:10px;margin:1.2em 0 0.2em;">
<div id="vf3d-helix" style="flex:1;height:400px;min-width:0;position:relative;background:#04080f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
<div id="vf3d-dipole" style="flex:1;height:400px;min-width:0;position:relative;background:#06030f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
</div>
<script type="module" src="threejs/chapter12-vectorfield.js?v=20260414b"></script>
```

---

## Files

- **Rewrite:** `src/chpt12.md` — the only file changed
- **Build output (verify only):** `docs/chapter12.html` — rebuilt by `python3 build/build.py`

---

## Task 0: Backup and scaffold

**Files:**
- Create: `src/chpt12.md.bak` (copy of current)
- Rewrite: `src/chpt12.md` (skeleton only)

- [ ] **Step 1: Back up the current file**

```bash
cp src/chpt12.md src/chpt12.md.bak
```

- [ ] **Step 2: Write the skeleton** — replace `src/chpt12.md` with section headings only, no content yet. This locks in the heading structure before writing prose.

```markdown
# 第十二章 曲线积分和曲面积分

> [!tip]
>
> 本章综合运用多元函数微积分，解决物理中的核心问题：力沿路径做的功、流体穿过曲面的通量，以及将它们联系起来的三大积分定理（格林、高斯、斯托克斯）。每一个定理都是微积分基本定理在更高维度的推广。

## 12.1 场与向量场

## 12.2 第一类曲线积分

## 12.3 第二类曲线积分

## 12.4 格林公式与保守场

### 12.4.1 格林公式

### 12.4.2 保守场与曲线积分基本定理

## 12.5 曲面积分

## 12.6 高斯公式与斯托克斯公式

### 12.6.1 高斯公式

### 12.6.2 斯托克斯公式

## 12.7 统一视角：广义牛顿-莱布尼茨公式
```

- [ ] **Step 3: Build and verify skeleton renders**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

Expected: `→ docs/chapter12.html` with no errors.

- [ ] **Step 4: Commit skeleton**

```bash
git add src/chpt12.md src/chpt12.md.bak
git commit -m "refactor(chpt12): begin full rewrite — skeleton structure"
```

---

## Task 1: §12.1 场与向量场

**Files:**
- Modify: `src/chpt12.md` — fill in `## 12.1 场与向量场`

**Content required:**
- Opening: 2–3 sentences on physical fields (temperature, wind, gravity) to motivate the abstraction
- Definition block for scalar field and vector field
- Component form for 2D and 3D vector fields
- Four 2D figure examples
- Three.js 3D interactive note + HTML block
- Closing sentence setting up the chapter

- [ ] **Step 1: Write §12.1**

Replace `## 12.1 场与向量场` with the following (write in full):

```markdown
## 12.1 场与向量场

自然界中许多物理量随空间位置变化：温度在房间各处不同，风速在每个地点有大小和方向，引力场在不同位置指向不同的方向。数学上，我们用**场**来描述这类"空间中每个点都对应一个量"的结构。

> [!important: 定义：标量场与向量场]
>
> 设 $D \subset \mathbb{R}^n$ 为一区域。
>
> - **标量场（scalar field）**：$D$ 上的实值函数 $f: D \to \mathbb{R}$，每个点对应一个数。例：温度场、密度场、电势场。
> - **向量场（vector field）**：$D$ 上的向量值函数 $\mathbf{F}: D \to \mathbb{R}^n$，每个点对应一个向量。例：引力场、流速场、电场。

向量场的**分量形式**：

$$
\mathbf{F}(x,y) = P(x,y)\,\hat{\mathbf{i}} + Q(x,y)\,\hat{\mathbf{j}} \qquad \text{（二维）}
$$

$$
\mathbf{F}(x,y,z) = P(x,y,z)\,\hat{\mathbf{i}} + Q(x,y,z)\,\hat{\mathbf{j}} + R(x,y,z)\,\hat{\mathbf{k}} \qquad \text{（三维）}
$$

其中 $P, Q, R$ 是普通的多元函数，分别表示向量在 $x, y, z$ 方向的分量。

> [!important: 几个二维向量场的例子]
>
> ==例 1==　$\mathbf{F}(x,y) = 2\hat{\mathbf{i}} + 3\hat{\mathbf{j}}$　— 均匀场，每处方向和大小相同。
>
> ![均匀向量场](media/img/fig2-4-1.png#200pt)
>
> ==例 2==　$\mathbf{F}(x,y) = x\hat{\mathbf{i}}$　— 水平分量随 $x$ 增大，无竖直分量。
>
> ![水平向量场](media/img/fig2-4-3.png#200pt)
>
> ==例 3==　$\mathbf{F}(x,y) = x\hat{\mathbf{i}} + y\hat{\mathbf{j}}$　— 从原点向外辐射的源场。
>
> ![辐射向量场](media/img/fig2-4-2.png#200pt)
>
> ==例 4==　$\mathbf{F}(x,y) = y\hat{\mathbf{i}} + x\hat{\mathbf{j}}$　— 场线呈双曲线形。
>
> ![双曲向量场](media/img/fig2-4-4.png#200pt)

> [!note]
>
> **三维向量场**的结构更为丰富。下面是两个典型例子，可拖动旋转查看：左图为螺旋场 $\mathbf{F}=(-z,\tfrac{1}{2},x)$，右图为磁偶极子场。

<div style="display:flex;gap:10px;margin:1.2em 0 0.2em;">
<div id="vf3d-helix" style="flex:1;height:400px;min-width:0;position:relative;background:#04080f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
<div id="vf3d-dipole" style="flex:1;height:400px;min-width:0;position:relative;background:#06030f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
</div>
<script type="module" src="threejs/chapter12-vectorfield.js?v=20260414b"></script>

本章的核心问题是：**如何在向量场中进行积分？**
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

Expected: `→ docs/chapter12.html`, no errors.

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.1 场与向量场"
```

---

## Task 2: §12.2 第一类曲线积分

**Files:**
- Modify: `src/chpt12.md` — fill in `## 12.2 第一类曲线积分`

**Content required:**
- Opening physical problem: mass of a wire with non-uniform density
- Riemann sum → definition of $\int_L f\,\mathrm{d}s$
- Parametric reduction theorem (derive $\mathrm{d}s = \sqrt{x'^2+y'^2}\,\mathrm{d}t$)
- Note that result is orientation-independent
- One worked example
- Exercises ex-001, ex-002

- [ ] **Step 1: Write §12.2**

Replace `## 12.2 第一类曲线积分` with:

```markdown
## 12.2 第一类曲线积分

> [!tip: 引入问题：不均匀细线的质量]
>
> 一段细线弯曲成平面曲线 $L$ 的形状，其线密度（单位长度的质量）在不同位置不同，记为 $\rho(x,y)$。如何计算这段细线的总质量？
>
> 将 $L$ 分成 $N$ 小段，第 $i$ 段的弧长为 $\Delta s_i$，取该段上任一点 $(x_i, y_i)$，则该段质量约为 $\rho(x_i, y_i)\,\Delta s_i$。对所有小段求和并令 $N\to\infty$，即得细线总质量：
>
> $$M = \lim_{N\to\infty}\sum_{i=1}^{N}\rho(x_i,y_i)\,\Delta s_i.$$

这个极限就是**第一类曲线积分**（或**弧长曲线积分**）的定义。

> [!important: 定义：第一类曲线积分]
>
> 设 $f(x,y)$ 在曲线 $L$ 上连续，将 $L$ 划分为 $N$ 段弧，第 $i$ 段弧长为 $\Delta s_i$，取该段上任一点 $(x_i,y_i)$。若极限
>
> $$\int_L f(x,y)\,\mathrm{d}s \;=\; \lim_{N\to\infty}\sum_{i=1}^{N}f(x_i,y_i)\,\Delta s_i$$
>
> 存在且与划分方式及取点无关，则称此极限为 $f$ 沿 $L$ 的**第一类曲线积分**，$\mathrm{d}s$ 称为**弧长微元**。

**计算方法（参数化化简）**：若 $L$ 由参数方程 $x=x(t),\,y=y(t),\,t\in[t_0,t_1]$ 给出，$x'(t),y'(t)$ 在 $[t_0,t_1]$ 上连续且 $x'^2+y'^2\neq 0$，则弧长微元为

$$\mathrm{d}s = \sqrt{[x'(t)]^2+[y'(t)]^2}\,\mathrm{d}t,$$

从而

$$\int_L f(x,y)\,\mathrm{d}s = \int_{t_0}^{t_1}f\bigl(x(t),y(t)\bigr)\sqrt{[x'(t)]^2+[y'(t)]^2}\,\mathrm{d}t.$$

> [!note]
>
> 第一类曲线积分有两个重要性质：
> 1. **与方向无关**：将 $L$ 反向，$\mathrm{d}s$ 始终为正，积分值不变。
> 2. **对加法可加**：$\int_{L_1+L_2}f\,\mathrm{d}s = \int_{L_1}f\,\mathrm{d}s + \int_{L_2}f\,\mathrm{d}s$。

> [!tip: 例题]
>
> 计算 $\displaystyle\int_L(x^2+y^2)\,\mathrm{d}s$，其中 $L$ 为圆 $x=\cos t,\,y=\sin t,\,t\in[0,2\pi]$。
>
> **解**：$\mathrm{d}s = \sqrt{\sin^2 t+\cos^2 t}\,\mathrm{d}t = \mathrm{d}t$，且在 $L$ 上 $x^2+y^2=1$，故
>
> $$\int_L(x^2+y^2)\,\mathrm{d}s = \int_0^{2\pi}1\cdot\mathrm{d}t = 2\pi.$$

::: {.exercise id="chpt12-ex-001"}
:::

::: {.exercise id="chpt12-ex-002"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.2 第一类曲线积分"
```

---

## Task 3: §12.3 第二类曲线积分

**Files:**
- Modify: `src/chpt12.md` — fill in `## 12.3 第二类曲线积分`

**Content required:**
- Opening physical problem: work done by a force field along a path
- Riemann sum → definition of $\int_L \mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_L P\,\mathrm{d}x+Q\,\mathrm{d}y$
- Orientation matters (state + brief physical justification)
- Parametric reduction
- Connection to type I: $W = \int_L \mathbf{F}\cdot\boldsymbol{\tau}\,\mathrm{d}s$
- Exercises ex-003, ex-004, ex-005, ex-006, ex-007, ex-008

- [ ] **Step 1: Write §12.3**

Replace `## 12.3 第二类曲线积分` with:

```markdown
## 12.3 第二类曲线积分

> [!tip: 引入问题：力沿路径做的功]
>
> 质点在向量场 $\mathbf{F}(x,y) = P(x,y)\hat{\mathbf{i}}+Q(x,y)\hat{\mathbf{j}}$ 的作用下沿曲线 $L$ 运动。如何计算场对质点所做的总功？
>
> 将路径分为 $N$ 小段，第 $i$ 段的位移向量为 $\Delta\mathbf{r}_i = (\Delta x_i, \Delta y_i)$，该段上的力约为 $\mathbf{F}(x_i,y_i)$。做功约为 $\mathbf{F}(x_i,y_i)\cdot\Delta\mathbf{r}_i = P_i\Delta x_i + Q_i\Delta y_i$。对所有小段求和并取极限：
>
> $$W = \lim_{N\to\infty}\sum_{i=1}^{N}\mathbf{F}(x_i,y_i)\cdot\Delta\mathbf{r}_i.$$

> [!important: 定义：第二类曲线积分]
>
> 设向量场 $\mathbf{F}(x,y)=P(x,y)\hat{\mathbf{i}}+Q(x,y)\hat{\mathbf{j}}$ 在有向曲线 $L$ 上连续，则 $\mathbf{F}$ 沿 $L$ 的**第二类曲线积分**（**向量场曲线积分**）定义为
>
> $$\int_L \mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_L P(x,y)\,\mathrm{d}x + Q(x,y)\,\mathrm{d}y.$$
>
> 其中 $\mathrm{d}\mathbf{r} = \mathrm{d}x\,\hat{\mathbf{i}}+\mathrm{d}y\,\hat{\mathbf{j}}$ 为**有向弧元**。

> [!important: 方向性]
>
> 第二类曲线积分与曲线的**方向**有关：若 $-L$ 表示 $L$ 的反向，则
>
> $$\int_{-L}\mathbf{F}\cdot\mathrm{d}\mathbf{r} = -\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r}.$$
>
> 物理直觉：逆着力的方向运动，场做负功。

**计算方法（参数化化简）**：若 $L$：$x=x(t),\,y=y(t),\,t$ 从 $t_1$ 到 $t_2$，则 $\mathrm{d}x=x'(t)\,\mathrm{d}t,\,\mathrm{d}y=y'(t)\,\mathrm{d}t$，故

$$\int_L P\,\mathrm{d}x+Q\,\mathrm{d}y = \int_{t_1}^{t_2}\bigl[P(x(t),y(t))\,x'(t)+Q(x(t),y(t))\,y'(t)\bigr]\mathrm{d}t.$$

注意：$t_1$ 到 $t_2$ 的方向决定了曲线的方向。

> [!note: 两类曲线积分的联系]
>
> 设 $\boldsymbol{\tau} = \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}s}$ 为 $L$ 的单位切向量，则 $\mathrm{d}\mathbf{r} = \boldsymbol{\tau}\,\mathrm{d}s$，从而
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_L\mathbf{F}\cdot\boldsymbol{\tau}\,\mathrm{d}s.$$
>
> 即第二类曲线积分是以 $\mathbf{F}\cdot\boldsymbol{\tau}$（场沿切向的分量）为被积函数的第一类积分。两类积分本质上是同一件事。

> [!tip: 例题]
>
> 计算 $\displaystyle\int_L y\,\mathrm{d}x - x\,\mathrm{d}y$，其中 $L$ 为从 $(1,0)$ 到 $(-1,0)$ 的上半圆 $x=\cos t,\,y=\sin t,\,t\in[0,\pi]$。
>
> **解**：$\mathrm{d}x=-\sin t\,\mathrm{d}t,\,\mathrm{d}y=\cos t\,\mathrm{d}t$，故
>
> $$\int_L y\,\mathrm{d}x-x\,\mathrm{d}y = \int_0^{\pi}\bigl(\sin t\cdot(-\sin t)-\cos t\cdot\cos t\bigr)\mathrm{d}t = \int_0^{\pi}(-1)\,\mathrm{d}t = -\pi.$$

::: {.exercise id="chpt12-ex-003"}
:::

::: {.exercise id="chpt12-ex-004"}
:::

::: {.exercise id="chpt12-ex-005"}
:::

::: {.exercise id="chpt12-ex-006"}
:::

::: {.exercise id="chpt12-ex-007"}
:::

::: {.exercise id="chpt12-ex-008"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.3 第二类曲线积分"
```

---

## Task 4: §12.4.1 格林公式

**Files:**
- Modify: `src/chpt12.md` — fill in `### 12.4.1 格林公式`

**Content required:**
- Opening physical problem: circulation around a boundary and internal rotation
- Motivate curl $\mathbf{F} = Q_x - P_y$ as pointwise rotation rate
- State Green's theorem precisely (counterclockwise boundary, notation $\partial D^+$)
- Full proof in `[!extension]` block: (1) $Q=0$ special case on a vertically simple region, (2) additivity argument
- Application corollary: area formula $A = \frac{1}{2}\oint_C x\,\mathrm{d}y - y\,\mathrm{d}x$
- Exercises ex-010, ex-011, ex-012, ex-013

- [ ] **Step 1: Write §12.4.1**

Replace `### 12.4.1 格林公式` with:

```markdown
### 12.4.1 格林公式

> [!tip: 引入问题：边界上的环量与内部的旋转]
>
> 流体在平面区域 $D$ 内流动，速度场为 $\mathbf{F}=(P,Q)$。沿 $D$ 的边界 $C$（逆时针方向）一圈做功（即**环量**）$\displaystyle\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}$，是否能用 $D$ 内部各点的局部旋转信息来计算？

为此我们引入**旋度**（curl）刻画向量场在一点的局部旋转强度：

> [!important: 定义：二维旋度]
>
> 设 $\mathbf{F}=(P,Q)$ 在区域 $D$ 上有连续偏导数，称
>
> $$\operatorname{curl}\mathbf{F} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$
>
> 为 $\mathbf{F}$ 的**旋度**（二维）。$\operatorname{curl}\mathbf{F}>0$ 表示该点邻域内流体逆时针旋转，$<0$ 表示顺时针旋转。

格林公式告诉我们：将 $D$ 内所有点的旋度"积累"起来，恰好等于沿边界的环量。

> [!important: 格林公式]
>
> 设 $D$ 为平面上由分段光滑曲线 $C$ 围成的有界闭区域，$P(x,y)$ 和 $Q(x,y)$ 在 $D$ 上有一阶连续偏导数，$C = \partial D^+$ 表示 $D$ 的正向（逆时针）边界，则
>
> $$\oint_{C} P\,\mathrm{d}x + Q\,\mathrm{d}y = \iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}A.$$

> [!extension: 证明]
>
> 只需分别证明以下两个等式：
>
> $$\oint_C P\,\mathrm{d}x = -\iint_D\frac{\partial P}{\partial y}\,\mathrm{d}A, \qquad \oint_C Q\,\mathrm{d}y = \iint_D\frac{\partial Q}{\partial x}\,\mathrm{d}A. \tag{$*$}$$
>
> 两式对称，只证第一式。
>
> **第一步：竖直简单区域**。设 $D$ 为竖直简单区域：$a\leq x\leq b$，$f_1(x)\leq y\leq f_2(x)$，边界 $C$ 由四段组成：$C_1$（底，$y=f_1(x)$，从左到右）、$C_2$（右侧竖直边，若有）、$C_3$（顶，$y=f_2(x)$，从右到左）、$C_4$（左侧竖直边，若有）。在竖直段上 $\mathrm{d}x=0$，故 $\int_{C_2}P\,\mathrm{d}x = \int_{C_4}P\,\mathrm{d}x = 0$。
>
> 计算其余两段（注意方向）：
>
> $$\oint_C P\,\mathrm{d}x = \int_a^b P(x,f_1(x))\,\mathrm{d}x - \int_a^b P(x,f_2(x))\,\mathrm{d}x = -\int_a^b\bigl[P(x,f_2(x))-P(x,f_1(x))\bigr]\mathrm{d}x.$$
>
> 另一方面，由单变量 FTC：
>
> $$-\iint_D\frac{\partial P}{\partial y}\,\mathrm{d}A = -\int_a^b\int_{f_1(x)}^{f_2(x)}\frac{\partial P}{\partial y}\,\mathrm{d}y\,\mathrm{d}x = -\int_a^b\bigl[P(x,f_2(x))-P(x,f_1(x))\bigr]\mathrm{d}x.$$
>
> 两式相等，第一式得证（对竖直简单区域）。
>
> **第二步：一般区域**。将 $D$ 用一条竖直线段分成两个竖直简单子区域 $D_1, D_2$（如有必要可分更多）。对每个子区域应用第一步的结论，再利用内部公共边界的贡献方向相反而相消（$\int_\ell + \int_{-\ell} = 0$），相加即得 $D$ 上的结论。对 $(*)$ 的第二式类似处理，两式相加即得格林公式。$\blacksquare$

> [!note: 应用：面积公式]
>
> 取 $P=-y,\,Q=x$，则 $Q_x-P_y=1+1=2$，格林公式给出
>
> $$A = \iint_D\mathrm{d}A = \frac{1}{2}\oint_C x\,\mathrm{d}y - y\,\mathrm{d}x.$$
>
> 这是用边界曲线计算面积的公式，在计算机图形学中有实际应用。

::: {.exercise id="chpt12-ex-010"}
:::

::: {.exercise id="chpt12-ex-011"}
:::

::: {.exercise id="chpt12-ex-012"}
:::

::: {.exercise id="chpt12-ex-013"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.4.1 格林公式 with full proof"
```

---

## Task 5: §12.4.2 保守场与曲线积分基本定理

**Files:**
- Modify: `src/chpt12.md` — fill in `### 12.4.2 保守场与曲线积分基本定理`

**Content required:**
- Opening question: when is work path-independent?
- Definition of conservative field and potential function
- Fundamental Theorem of Line Integrals (statement + proof)
- Consequences: path independence ↔ closed loops zero
- Criterion $P_y = Q_x$ on simply connected domains (derive necessity; state sufficiency)
- Method for finding potential $f$
- 2D curl as the obstruction to being conservative
- Exercise ex-009

- [ ] **Step 1: Write §12.4.2**

Replace `### 12.4.2 保守场与曲线积分基本定理` with:

```markdown
### 12.4.2 保守场与曲线积分基本定理

> [!tip: 引入问题：功与路径无关的条件]
>
> 对于同一起点 $A$、终点 $B$，力场 $\mathbf{F}$ 沿不同路径做的功是否相同？引力场是**保守的**——无论怎么绕路，最终做功只取决于位移；而摩擦力是**非保守的**——路径越长，克服摩擦做的功越多。什么决定了这一区别？

> [!important: 定义：保守场与势函数]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}$ 在区域 $D$ 上连续。若存在可微函数 $f(x,y)$，使得
>
> $$\mathbf{F} = \nabla f = \frac{\partial f}{\partial x}\hat{\mathbf{i}}+\frac{\partial f}{\partial y}\hat{\mathbf{j}},$$
>
> 则称 $\mathbf{F}$ 为 $D$ 上的**保守场**（或**梯度场**），$f$ 称为 $\mathbf{F}$ 的**势函数**。

> [!important: 曲线积分基本定理]
>
> 若 $\mathbf{F}=\nabla f$ 在包含曲线 $L$ 的区域上连续，$L$ 从点 $A$ 到点 $B$，则
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = f(B) - f(A).$$
>
> **证明**：设 $L$：$x=x(t),\,y=y(t),\,t\in[t_0,t_1]$，则
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_{t_0}^{t_1}\left(\frac{\partial f}{\partial x}x'(t)+\frac{\partial f}{\partial y}y'(t)\right)\mathrm{d}t = \int_{t_0}^{t_1}\frac{\mathrm{d}}{\mathrm{d}t}f(x(t),y(t))\,\mathrm{d}t = f(B)-f(A). \quad\blacksquare$$

这与一元微积分基本定理 $\int_a^b f'(x)\,\mathrm{d}x = f(b)-f(a)$ 完全类比。

> [!important: 等价条件]
>
> 在**单连通区域** $D$（无"洞"的区域）上，以下四个条件等价：
>
> 1. $\mathbf{F}$ 是保守场（存在势函数 $f$）；
> 2. 曲线积分与路径无关：对 $D$ 中任意两点 $A,B$，$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ 的值与连接 $A,B$ 的路径 $L$ 无关；
> 3. 对 $D$ 内任意封闭曲线 $C$，$\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}=0$；
> 4. $\operatorname{curl}\mathbf{F} = \dfrac{\partial Q}{\partial x}-\dfrac{\partial P}{\partial y} = 0$。
>
> **条件 4 的必要性（推导）**：若 $f$ 存在，则 $P=f_x,\,Q=f_y$，由混合偏导连续性 $P_y = f_{xy} = f_{yx} = Q_x$，即 $Q_x-P_y=0$。
>
> **注**：在非单连通区域（有洞的区域，如 $\mathbb{R}^2\setminus\{(0,0)\}$），条件 4 成立不保证条件 1 成立（经典反例：$\mathbf{F}=\frac{(-y,x)}{x^2+y^2}$）。

**求势函数的方法**：已知 $\mathbf{F}=(P,Q)$ 满足 $P_y=Q_x$，求 $f$。

先对 $x$ 积分求 $f$：$f(x,y)=\int P(x,y)\,\mathrm{d}x + g(y)$，其中 $g(y)$ 为待定函数。再由 $f_y=Q$ 确定 $g'(y)$，积分得 $g(y)$。

> [!tip: 例题]
>
> 验证 $\mathbf{F}=(y,x)$ 是保守场，并求势函数 $f$（满足 $f(0,0)=0$）。
>
> **解**：$P=y,\,Q=x$，故 $P_y=1=Q_x$。$\checkmark$ 先积：$f=\int y\,\mathrm{d}x+g(y)=xy+g(y)$。再由 $f_y=x+g'(y)=x$，得 $g'(y)=0$，即 $g=c$。代入初值 $f(0,0)=0$ 得 $c=0$，故 $f(x,y)=xy$。

::: {.exercise id="chpt12-ex-009"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.4.2 保守场与曲线积分基本定理"
```

---

## Task 6: §12.5 曲面积分

**Files:**
- Modify: `src/chpt12.md` — fill in `## 12.5 曲面积分`

**Content required:**
- Bridge sentence opening the 3D half
- Opening physical problem: fluid flux through a surface
- Definition of flux integral $\iint_S\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S$
- Reduction for $z=g(x,y)$: tangent vectors, cross product, $\mathbf{n}\,\mathrm{d}S=(-g_x,-g_y,1)\,\mathrm{d}x\,\mathrm{d}y$
- Orientation (outward vs. inward normal)
- One worked example
- Exercise ex-014

- [ ] **Step 1: Write §12.5**

Replace `## 12.5 曲面积分` with:

```markdown
## 12.5 曲面积分

至此，我们已完整建立了二维的积分理论：沿曲线的两类积分，以及将边界与区域内部联系起来的格林公式。现在我们将相同的思路推广到三维空间：**曲面**取代曲线，**通量**取代做功。

> [!tip: 引入问题：流体穿过曲面的通量]
>
> 流体以速度场 $\mathbf{F}(x,y,z)$ 流动。空间中有一曲面 $S$。单位时间内有多少流体穿过 $S$？
>
> 将 $S$ 分成 $N$ 个小面片，第 $i$ 片的面积为 $\Delta S_i$，外法向单位向量为 $\mathbf{n}_i$。穿过这一小片的流量约为（流速分量 $\times$ 面积）$\mathbf{F}(x_i,y_i,z_i)\cdot\mathbf{n}_i\,\Delta S_i$，对所有小片求和并取极限即得**通量**：
>
> $$\text{Flux} = \lim_{N\to\infty}\sum_{i=1}^{N}\mathbf{F}(x_i,y_i,z_i)\cdot\mathbf{n}_i\,\Delta S_i.$$

> [!important: 定义：曲面积分（通量型）]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 在有向曲面 $S$ 上连续，$\mathbf{n}$ 为 $S$ 的单位外法向量，则 $\mathbf{F}$ 穿过 $S$ 的**通量**（曲面积分）定义为
>
> $$\iint_S\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S}.$$

**计算方法（化为二重积分）**：设 $S$ 由 $z=g(x,y)$ 给出，$(x,y)\in D_{xy}$。曲面上的切向量为 $\mathbf{v}_1=(1,0,g_x)$ 和 $\mathbf{v}_2=(0,1,g_y)$，法向量

$$\mathbf{n}\,\mathrm{d}S = \mathbf{v}_1\times\mathbf{v}_2\,\mathrm{d}x\,\mathrm{d}y = (-g_x,-g_y,1)\,\mathrm{d}x\,\mathrm{d}y.$$

（此为朝上的法向量；若需朝下，取反号。）于是

$$\iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S} = \iint_{D_{xy}}\bigl[-P\,g_x - Q\,g_y + R\bigr]\,\mathrm{d}x\,\mathrm{d}y.$$

> [!note: 方向的选取]
>
> 曲面积分与曲面的**定向**有关，改变法向量方向（即翻转曲面的"正面"），积分变号。对**封闭曲面**（如球面、椭球面），通常约定外法向量为正方向；对**开曲面**（如一片抛物面），需事先指定法向量朝哪一侧。

> [!tip: 例题]
>
> 计算 $\mathbf{F}=z\hat{\mathbf{k}}$ 穿过上半球面 $S:\,x^2+y^2+z^2=a^2,\,z\geq 0$（取朝上法向量）的通量。
>
> **解**：$z=g(x,y)=\sqrt{a^2-x^2-y^2}$，$g_x=-\frac{x}{z},\,g_y=-\frac{y}{z}$，$P=Q=0,\,R=z$，故
>
> $$\iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S} = \iint_{D_{xy}} z\,\mathrm{d}x\,\mathrm{d}y = \iint_{x^2+y^2\leq a^2}\sqrt{a^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y = \frac{2\pi a^3}{3}.$$
>
> （最后一步用极坐标计算。）

::: {.exercise id="chpt12-ex-014"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.5 曲面积分"
```

---

## Task 7: §12.6.1 高斯公式

**Files:**
- Modify: `src/chpt12.md` — fill in `### 12.6.1 高斯公式`

**Content required:**
- Opening physical problem: sources/sinks inside a closed region
- Definition of divergence $\nabla\cdot\mathbf{F} = P_x+Q_y+R_z$
- Statement of Gauss's theorem
- Proof sketch in `[!extension]` block
- Physical interpretation of divergence
- Exercises ex-015, ex-016, ex-017, ex-018

- [ ] **Step 1: Write §12.6.1**

Replace `### 12.6.1 高斯公式` with:

```markdown
### 12.6.1 高斯公式

> [!tip: 引入问题：源泉与通量]
>
> 设空间区域 $V$ 内有流体流动，速度场为 $\mathbf{F}$。若区域内某处是流体的**源**（即流体在那里被持续"创造"），这些新产生的流体必然向外流出，最终穿越边界曲面 $\partial V$。那么，区域内总的"产生率"与穿越边界的总通量之间有何关系？

为量化每一点的"产生率"，引入**散度**：

> [!important: 定义：散度]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 有连续偏导数，称
>
> $$\operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$
>
> 为 $\mathbf{F}$ 的**散度**。$\operatorname{div}\mathbf{F}>0$ 表示该点是源，$<0$ 表示是汇，$=0$ 表示不可压缩（流体既不创造也不消失）。

> [!important: 高斯公式（散度定理）]
>
> 设 $V$ 为空间中由分片光滑封闭曲面 $\Sigma=\partial V$ 围成的有界区域，$\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 在 $V$ 上有一阶连续偏导数，$\mathbf{n}$ 为 $\Sigma$ 的外法向量，则
>
> $$\oiint_{\Sigma}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iiint_V\nabla\cdot\mathbf{F}\,\mathrm{d}V.$$

> [!extension: 证明思路]
>
> 分别证明 $\oiint_\Sigma R\,\mathrm{d}x\,\mathrm{d}y = \iiint_V R_z\,\mathrm{d}V$（另两式对称）。
>
> 设 $V$："竖直简单"：$a\leq x,\,b\leq y$，$z$ 介于底面 $z=z_1(x,y)$ 和顶面 $z=z_2(x,y)$ 之间。在顶面取朝外（朝上）的法向量，$\mathrm{d}x\,\mathrm{d}y>0$；在底面取朝外（朝下）的法向量，$\mathrm{d}x\,\mathrm{d}y<0$；在侧面 $\mathrm{d}x\,\mathrm{d}y=0$。故
>
> $$\oiint_\Sigma R\,\mathrm{d}x\,\mathrm{d}y = \iint_{D_{xy}}\bigl[R(x,y,z_2)-R(x,y,z_1)\bigr]\mathrm{d}x\,\mathrm{d}y.$$
>
> 另一方面，由单变量 FTC 对 $z$ 积分：
>
> $$\iiint_V R_z\,\mathrm{d}V = \iint_{D_{xy}}\int_{z_1}^{z_2}R_z\,\mathrm{d}z\,\mathrm{d}x\,\mathrm{d}y = \iint_{D_{xy}}\bigl[R(x,y,z_2)-R(x,y,z_1)\bigr]\mathrm{d}x\,\mathrm{d}y.$$
>
> 两式相等。对一般区域用与格林公式类似的分拆与拼合论证。$\blacksquare$

> [!note: 物理意义]
>
> 高斯公式是格林公式"通量形式"的三维版本：
>
> - 格林（通量形式）：$\oint_C\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}s = \iint_D\nabla\cdot\mathbf{F}\,\mathrm{d}A$
> - 高斯：$\oiint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iiint_V\nabla\cdot\mathbf{F}\,\mathrm{d}V$
>
> 两者都说：**区域边界上的总通量 $=$ 区域内部散度的积分**。

::: {.exercise id="chpt12-ex-015"}
:::

::: {.exercise id="chpt12-ex-016"}
:::

::: {.exercise id="chpt12-ex-017"}
:::

::: {.exercise id="chpt12-ex-018"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.6.1 高斯公式"
```

---

## Task 8: §12.6.2 斯托克斯公式

**Files:**
- Modify: `src/chpt12.md` — fill in `### 12.6.2 斯托克斯公式`

**Content required:**
- 3D line integrals (brief: $\int_C P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z$)
- Definition of 3D curl via determinant
- Connection: 2D curl is the $\hat{\mathbf{k}}$-component of 3D curl
- Statement of Stokes's theorem
- Proof sketch: reduce to Green's theorem on a parametrized surface
- Conservative fields in 3D: $\operatorname{curl}\mathbf{F}=\mathbf{0} \Leftrightarrow \mathbf{F}=\nabla f$
- Exercises ex-019, ex-020, ex-021, ex-022

- [ ] **Step 1: Write §12.6.2**

Replace `### 12.6.2 斯托克斯公式` with:

```markdown
### 12.6.2 斯托克斯公式

三维空间中的曲线积分与二维情形完全类似：

$$\int_C\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_C P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z,$$

其中 $\mathrm{d}\mathbf{r}=(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$，计算方法与二维完全相同（参数化后代入）。

> [!tip: 引入问题：三维中的环量与旋转]
>
> 三维向量场 $\mathbf{F}$ 沿封闭曲线 $C$ 的环量 $\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}$，是否等于 $C$ 所围曲面 $S$ 上"旋转强度"的积分？这是格林公式在三维的推广。

为此需要三维旋度：

> [!important: 定义：三维旋度]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 有连续偏导数，定义 $\mathbf{F}$ 的**旋度**为
>
> $$\operatorname{curl}\mathbf{F} = \nabla\times\mathbf{F} = \begin{vmatrix}\hat{\mathbf{i}}&\hat{\mathbf{j}}&\hat{\mathbf{k}}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix} = (R_y-Q_z)\hat{\mathbf{i}}+(P_z-R_x)\hat{\mathbf{j}}+(Q_x-P_y)\hat{\mathbf{k}}.$$

> [!note]
>
> 对于平面向量场 $\mathbf{F}=(P,Q,0)$，旋度为 $(0,0,Q_x-P_y)$，其 $\hat{\mathbf{k}}$-分量恰好是二维旋度 $Q_x-P_y$。三维旋度是二维旋度的自然推广。

> [!important: 斯托克斯公式]
>
> 设 $S$ 为分片光滑的有向曲面，其边界 $\partial S$ 为分段光滑的封闭曲线（方向由右手法则与 $S$ 的法向量确定），$\mathbf{F}$ 在含 $S$ 的区域上有连续偏导数，则
>
> $$\oint_{\partial S}\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \iint_S(\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S.$$

> [!extension: 证明思路]
>
> 将 $S$ 用参数方程 $\mathbf{r}(u,v) = (x(u,v), y(u,v), z(u,v))$，$(u,v)\in R$ 参数化。将积分 $\oint_{\partial S} P\,\mathrm{d}x$ 用链式法则写成 $\oint_{\partial R}(P\,x_u\,\mathrm{d}u + P\,x_v\,\mathrm{d}v)$，再对 $R$ 应用格林公式，展开后与右边 $\iint_S(\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S$ 的参数化表达式比较。逐项对 $P, Q, R$ 做此处理后相加，即得斯托克斯公式。$\blacksquare$

> [!important: 三维保守场判定]
>
> 在单连通空间区域 $D$ 上，以下条件等价：
>
> 1. $\mathbf{F}=\nabla f$（存在势函数）；
> 2. $\operatorname{curl}\mathbf{F}=\mathbf{0}$，即 $R_y=Q_z,\;P_z=R_x,\;Q_x=P_y$；
> 3. 对 $D$ 内任意封闭曲线 $C$，$\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}=0$。
>
> 势函数求法与二维相同：依次对 $x,y,z$ 积分，逐步确定待定函数。

::: {.exercise id="chpt12-ex-021"}
:::

::: {.exercise id="chpt12-ex-022"}
:::

::: {.exercise id="chpt12-ex-019"}
:::

::: {.exercise id="chpt12-ex-020"}
:::
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Commit**

```bash
git add src/chpt12.md
git commit -m "feat(chpt12): write §12.6.2 斯托克斯公式"
```

---

## Task 9: §12.7 统一视角

**Files:**
- Modify: `src/chpt12.md` — fill in `## 12.7 统一视角：广义牛顿-莱布尼茨公式`

**Content required:**
- Summary table of four theorems
- State the unifying pattern in words
- One-sentence mention of differential forms (horizon, not developed)
- Closing authorial paragraph

- [ ] **Step 1: Write §12.7**

Replace `## 12.7 统一视角：广义牛顿-莱布尼茨公式` with:

```markdown
## 12.7 统一视角：广义牛顿-莱布尼茨公式

本章的四个核心定理并非彼此独立的结论——它们是同一件事在不同维度的面貌。

> [!important: 四个定理的统一形式]
>
> | 定理 | 区域 $\Omega$ | 边界 $\partial\Omega$ | 公式 |
> |:---|:---|:---|:---|
> | 牛顿-莱布尼茨 | 区间 $[a,b]$ | 端点 $\{a,b\}$ | $\displaystyle\int_a^b f'(x)\,\mathrm{d}x = f(b)-f(a)$ |
> | 格林公式 | 平面区域 $D$ | 有向曲线 $\partial D$ | $\displaystyle\iint_D\operatorname{curl}\mathbf{F}\,\mathrm{d}A = \oint_{\partial D}\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ |
> | 斯托克斯公式 | 曲面 $S$ | 有向曲线 $\partial S$ | $\displaystyle\iint_S(\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S = \oint_{\partial S}\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ |
> | 高斯公式 | 空间区域 $V$ | 封闭曲面 $\partial V$ | $\displaystyle\iiint_V\nabla\cdot\mathbf{F}\,\mathrm{d}V = \oiint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S$ |
>
> **规律**：对区域上某种"导数"的积分，等于对其边界上"原函数"的积分。

> [!note: 微分形式语言]
>
> 在**微分形式**的语言中，上述四个公式统一为一个公式：
>
> $$\int_\Omega \mathrm{d}\omega = \int_{\partial\Omega}\omega,$$
>
> 其中 $\omega$ 是微分形式，$\mathrm{d}$ 是外微分算子。这是实变函数论和微分几何的核心定理，感兴趣的读者可在后续课程中深入探索。

回顾本章的旅程：我们从**场**出发，建立了**沿曲线积分**和**穿越曲面积分**的概念，发现了将区域与边界联系起来的三大定理。每一个定理的背后，都是牛顿和莱布尼茨三百年前的那个洞见——**积分与微分互为逆运算**——在更广阔的空间中回响。

格林公式告诉我们，平面上一个区域内所有点的旋转强度可以"抵消"为边界上的一圈循环。高斯公式告诉我们，一个封闭容器内所有的源与汇，最终都体现为穿越容器壁的净流量。斯托克斯公式告诉我们，曲面上所有的旋转，都会在曲面边界的环绕中留下印记。

这不仅仅是计算技巧——这是关于微积分之统一性最深刻的一句话。
```

- [ ] **Step 2: Build and verify**

```bash
python3 build/build.py 2>&1 | grep -E "chapter12|Error|error"
```

- [ ] **Step 3: Final full build check**

```bash
python3 build/build.py 2>&1 | tail -5
```

Expected: `Done. 15/15 succeeded.`

- [ ] **Step 4: Remove backup file**

```bash
rm src/chpt12.md.bak
git add src/chpt12.md.bak src/chpt12.md
git commit -m "feat(chpt12): complete full authorial rewrite

Seven-section structure: fields → type-I → type-II → Green (full proof)
+ conservative fields → surface integrals → Gauss (sketch) + Stokes
(sketch) → unified FTC perspective. Physics-first narrative throughout,
all 22 exercises retained, notation standardized."
```

---

## Self-Review Checklist

- [x] **Spec coverage:** All 7 sections from spec covered in Tasks 1–9. All 22 exercises present (ex-001–022). Notation table from spec applied throughout ($\mathbf{F}$, $\hat{\mathbf{i}}$, $\mathrm{d}s$ etc.). Three.js block preserved verbatim in Task 1.
- [x] **No placeholders:** All content written out in full. No "TBD", "TODO", or "similar to above."
- [x] **Consistency:** `\operatorname{curl}` used in Tasks 4, 5, 7, 8. `\nabla\cdot` used in Tasks 7, 8. `\nabla\times` used in Task 8. Exercise IDs are zero-padded (ex-001 not ex-1). Callout types consistent with reference table.
- [x] **Build command:** `python3 build/build.py` run from `NewMathAnalysis/` directory in every task.
