# 第十二章 曲线积分和曲面积分

> [!tip]
>
> 本章综合运用多元函数微积分，解决物理中的核心问题：力沿路径做的功、流体穿过曲面的通量，以及将它们联系起来的三大积分定理（格林、高斯、斯托克斯）。每一个定理都是微积分基本定理在更高维度的推广。

## 12.1 场与向量场

自然界中许多物理量随空间位置变化：温度在房间各处不同，风速在每个地点有大小和方向，引力场在不同位置指向不同的方向。数学上，我们用**场**来描述这类"空间中每个点都对应一个量"的结构。

> [!important: 定义：标量场与向量场]
>
> 设 $D \subset \mathbb{R}^n$ 为一区域。
>
> - **标量场（scalar field）**：$D$ 上的实值函数 $f: D \to \mathbb{R}$，每个点对应一个数。例：温度场、密度场、电势场。
> - **向量场（vector field）**：$D$ 上的向量值函数 $\mathbf{F}: D \to \mathbb{R}^n$，每个点对应一个向量。例：引力场、流速场、电（力）场。

向量场的**分量形式**：

$$
\mathbf{F}(x,y) = P(x,y)\,\hat{\mathbf{i}} + Q(x,y)\,\hat{\mathbf{j}} \qquad \text{（二维）}
$$

$$
\mathbf{F}(x,y,z) = P(x,y,z)\,\hat{\mathbf{i}} + Q(x,y,z)\,\hat{\mathbf{j}} + R(x,y,z)\,\hat{\mathbf{k}} \qquad \text{（三维）}
$$

其中 $P, Q, R$ 是普通的多元函数，分别表示向量在 $x, y, z$ 方向的分量。

> [!note: 几个二维向量场的例子]
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

## 12.2 第一类曲线积分

> [!tip: 引入问题：不均匀细线的质量]
>
> 一段细线弯曲成平面曲线 $L$ 的形状，其线密度（单位长度的质量）在不同位置不同，记为 $\rho(x,y)$。如何计算这段细线的总质量？
>
> 将 $L$ 分成 $N$ 小段，第 $i$ 段的弧长为 $\Delta s_i$，取该段上任一点 $(x_i, y_i)$，则该段质量约为 $\rho(x_i, y_i)\,\Delta s_i$。对所有小段求和并令 $N\to\infty$，即得细线总质量：
>
> $$M = \lim_{\lambda\to 0}\sum_{i=1}^{N}\rho(x_i,y_i)\,\Delta s_i,$$
>
> 其中 $\lambda = \max_i \Delta s_i$ 为最大小段弧长。

这个极限就是**第一类曲线积分**（或**弧长曲线积分**）的定义。

> [!important: 定义：第一类曲线积分]
>
> 设 $f(x,y)$ 在曲线 $L$ 上连续。将 $L$ 划分为 $N$ 段弧，第 $i$ 段弧长为 $\Delta s_i$，在该段上取任一点 $(x_i,y_i)$，令 $\lambda = \max_i \Delta s_i$。若极限
>
> $$\lim_{\lambda\to 0}\sum_{i=1}^{N}f(x_i,y_i)\,\Delta s_i$$
>
> 存在且与划分方式及取点无关，则称该极限为 $f$ 沿 $L$ 的**第一类曲线积分**，记作
>
> $$\int_L f(x,y)\,\mathrm{d}s = \lim_{\lambda\to 0}\sum_{i=1}^{N}f(x_i,y_i)\,\Delta s_i,$$
>
> $\mathrm{d}s$ 称为**弧长微元**。

**计算方法（参数化化简）**：若 $L$ 由参数方程 $x=x(t),\,y=y(t),\,t\in[t_0,t_1]$ 给出，$t_0 < t_1$，$x'(t),y'(t)$ 在 $[t_0,t_1]$ 上连续，且对所有 $t\in[t_0,t_1]$ 均有 $[x'(t)]^2+[y'(t)]^2\neq 0$，则弧长微元为

$$\mathrm{d}s = \sqrt{[x'(t)]^2+[y'(t)]^2}\,\mathrm{d}t,$$

从而

$$\int_L f(x,y)\,\mathrm{d}s = \int_{t_0}^{t_1}f\bigl(x(t),y(t)\bigr)\sqrt{[x'(t)]^2+[y'(t)]^2}\,\mathrm{d}t.$$

> [!note: 推广到空间曲线]
>
> 对空间曲线 $L$：$x=x(t),\,y=y(t),\,z=z(t),\,t\in[t_0,t_1]$，弧长微元为
>
> $$\mathrm{d}s = \sqrt{[x'(t)]^2+[y'(t)]^2+[z'(t)]^2}\,\mathrm{d}t,$$
>
> 积分公式形式相同：$\displaystyle\int_L f(x,y,z)\,\mathrm{d}s = \int_{t_0}^{t_1}f(x(t),y(t),z(t))\sqrt{[x'(t)]^2+[y'(t)]^2+[z'(t)]^2}\,\mathrm{d}t$。

> [!note: 基本性质]
>
> 第一类曲线积分有两个重要性质：
>
> 1. **与方向无关**：将 $L$ 反向，$\mathrm{d}s$ 始终为正，积分值不变。
> 2. **对路径可加**：$\int_{L_1+L_2}f\,\mathrm{d}s = \int_{L_1}f\,\mathrm{d}s + \int_{L_2}f\,\mathrm{d}s$。

> [!note: 例题]
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

## 12.3 第二类曲线积分

> [!tip: 引入问题：力沿路径做的功]
>
> 质点在向量场 $\mathbf{F}(x,y) = P(x,y)\hat{\mathbf{i}}+Q(x,y)\hat{\mathbf{j}}$ 的作用下沿有向曲线 $L$ 运动。如何计算场对质点所做的总功？
>
> 将路径分为 $N$ 小段，第 $i$ 段的位移向量为 $\Delta\mathbf{r}_i = (\Delta x_i, \Delta y_i)^T$，该段上的力约为 $\mathbf{F}(x_i,y_i)$。做功约为 $\mathbf{F}(x_i,y_i)\cdot\Delta\mathbf{r}_i = P_i\Delta x_i + Q_i\Delta y_i$。令 $\lambda = \max_i|\Delta\mathbf{r}_i|$ 并取极限：
>
> $$W = \lim_{\lambda\to 0}\sum_{i=1}^{N}\bigl(P(x_i,y_i)\Delta x_i + Q(x_i,y_i)\Delta y_i\bigr).$$

> [!important: 定义：第二类曲线积分]
>
> 设向量场 $\mathbf{F}(x,y)=P(x,y)\hat{\mathbf{i}}+Q(x,y)\hat{\mathbf{j}}$ 在有向曲线 $L$ 上连续。若上述极限存在且与划分及取点无关，则称该极限为 $\mathbf{F}$ 沿 $L$ 的**第二类曲线积分**（或**向量场曲线积分**），记作
>
> $$\int_L \mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_L P(x,y)\,\mathrm{d}x + Q(x,y)\,\mathrm{d}y,$$
>
> 其中 $\mathrm{d}\mathbf{r} = \mathrm{d}x\,\hat{\mathbf{i}}+\mathrm{d}y\,\hat{\mathbf{j}}$ 为**有向弧元**。

> [!important: 方向性]
>
> 第二类曲线积分与曲线的**方向**有关：若 $-L$ 表示 $L$ 的反向，则
>
> $$\int_{-L}\mathbf{F}\cdot\mathrm{d}\mathbf{r} = -\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r}.$$
>
> 物理直觉：逆着力的方向运动，场做负功。这与第一类积分不同（第一类积分的弧长 $\mathrm{d}s > 0$ 与方向无关）。

**计算方法（参数化化简）**：若 $L$：$x=x(t),\,y=y(t)$，$t$ 从 $t_1$ 到 $t_2$（$t_1$ 对应起点，$t_2$ 对应终点），则 $\mathrm{d}x=x'(t)\,\mathrm{d}t,\,\mathrm{d}y=y'(t)\,\mathrm{d}t$，故

$$\int_L P\,\mathrm{d}x+Q\,\mathrm{d}y = \int_{t_1}^{t_2}\bigl[P(x(t),y(t))\,x'(t)+Q(x(t),y(t))\,y'(t)\bigr]\mathrm{d}t.$$

注意：$t_1$ 到 $t_2$ 的积分方向与曲线的定向一致；若反向，则交换 $t_1, t_2$，积分变号。

> [!note: 两类曲线积分的联系]
>
> 设 $\boldsymbol{\tau}$ 为 $L$ 的单位切向量（与定向一致），则 $\mathrm{d}\mathbf{r} = \boldsymbol{\tau}\,\mathrm{d}s$，从而
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_L\mathbf{F}\cdot\boldsymbol{\tau}\,\mathrm{d}s.$$
>
> 即第二类曲线积分是以 $\mathbf{F}\cdot\boldsymbol{\tau}$（场沿切向的分量）为被积函数的第一类积分。两类积分本质上是同一件事：前者强调向量的分量，后者强调弧长方向。

> [!note: 例题]
>
> 计算 $\displaystyle\int_L y\,\mathrm{d}x - x\,\mathrm{d}y$，其中 $L$ 为从 $(1,0)$ 到 $(-1,0)$ 的上半圆 $x=\cos t,\,y=\sin t,\,t\in[0,\pi]$。
>
> **解**：$\mathrm{d}x=-\sin t\,\mathrm{d}t,\,\mathrm{d}y=\cos t\,\mathrm{d}t$，代入：
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

## 12.4 格林公式与保守场

### 12.4.1 格林公式

### 12.4.2 保守场与曲线积分基本定理

## 12.5 曲面积分

## 12.6 高斯公式与斯托克斯公式

### 12.6.1 高斯公式

### 12.6.2 斯托克斯公式

## 12.7 统一视角：广义牛顿-莱布尼茨公式
