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

> [!tip: 引入问题：边界环量与内部旋转]
>
> 流体在平面区域 $D$ 内流动，速度场为 $\mathbf{F}=(P,Q)$。沿 $D$ 的边界 $C$（逆时针方向）一圈的环量 $\displaystyle\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ 是否能用 $D$ 内部每一点的"局部旋转"信息来计算？

为刻画向量场在一点的旋转倾向，引入**旋度**：

> [!important: 定义：二维旋度]
>
> 设 $\mathbf{F}=(P,Q)$ 在区域 $D$ 上有连续偏导数，称
>
> $$\operatorname{curl}\mathbf{F} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$
>
> 为 $\mathbf{F}$ 的**旋度**（二维）。$\operatorname{curl}\mathbf{F}>0$ 表示该点邻域内流体逆时针旋转，$<0$ 表示顺时针旋转，$=0$ 表示无旋。

格林公式将区域内所有点的旋度"积累"起来，得到边界上的环量：

> [!important: 格林公式]
>
> 设 $D$ 为平面上由分段光滑曲线围成的有界闭区域，$P(x,y)$ 和 $Q(x,y)$ 在 $D$ 上有一阶连续偏导数，$C = \partial D^+$ 表示 $D$ 的正向（逆时针）边界，则
>
> $$\oint_{C} P\,\mathrm{d}x + Q\,\mathrm{d}y = \iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}A.$$

> [!extension: 证明]
>
> 只需分别证明：
>
> $$\oint_C P\,\mathrm{d}x = -\iint_D P_y\,\mathrm{d}A, \qquad \oint_C Q\,\mathrm{d}y = \iint_D Q_x\,\mathrm{d}A. \tag{$*$}$$
>
> 两式对称，只证第一式。
>
> **第一步：竖直简单区域。** 设 $D$：$a\leq x\leq b$，$f_1(x)\leq y\leq f_2(x)$，正向边界由底弧 $C_1$（$y=f_1$，从左到右）、顶弧 $C_3$（$y=f_2$，从右到左）及两侧竖直边（若有）组成。在竖直边上 $\mathrm{d}x=0$，故其贡献为零。
>
> $$\oint_C P\,\mathrm{d}x = \int_a^b P(x,f_1(x))\,\mathrm{d}x - \int_a^b P(x,f_2(x))\,\mathrm{d}x = -\int_a^b\bigl[P(x,f_2(x))-P(x,f_1(x))\bigr]\mathrm{d}x.$$
>
> 另一方面，由单变量 FTC 对 $y$ 积分：
>
> $$-\iint_D P_y\,\mathrm{d}A = -\int_a^b\int_{f_1(x)}^{f_2(x)}\frac{\partial P}{\partial y}\,\mathrm{d}y\,\mathrm{d}x = -\int_a^b\bigl[P(x,f_2(x))-P(x,f_1(x))\bigr]\mathrm{d}x.$$
>
> 两式相等，第一式对竖直简单区域得证。
>
> **第二步：一般区域。** 将 $D$ 用一条竖直线段分成两个竖直简单子区域 $D_1, D_2$，对每个子区域应用第一步。内部公共边界的贡献方向相反而相消：$\int_\ell P\,\mathrm{d}x + \int_{-\ell} P\,\mathrm{d}x = 0$。两部分相加即得 $D$ 上的结论。对 $(*)$ 的第二式类似处理，两式相加即得格林公式。$\blacksquare$

> [!note: 应用：用边界曲线计算面积]
>
> 取 $P=-y,\,Q=x$，则 $Q_x-P_y=1+1=2$，格林公式给出
>
> $$A = \iint_D\mathrm{d}A = \frac{1}{2}\oint_C x\,\mathrm{d}y - y\,\mathrm{d}x.$$
>
> 这是仅用边界曲线参数方程就能计算区域面积的公式。

::: {.exercise id="chpt12-ex-010"}
:::

::: {.exercise id="chpt12-ex-011"}
:::

::: {.exercise id="chpt12-ex-012"}
:::

::: {.exercise id="chpt12-ex-013"}
:::

### 12.4.2 保守场与曲线积分基本定理

> [!tip: 引入问题：做功何时与路径无关？]
>
> 对于同一起点 $A$、终点 $B$，力场 $\mathbf{F}$ 沿不同路径所做的功是否相同？引力场是**保守的**——无论绕多远，做功只取决于位移；摩擦力是**非保守的**——路径越长，克服摩擦做的负功越大。决定这一区别的关键是什么？

> [!important: 定义：保守场与势函数]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}$ 在区域 $D$ 上连续。若存在可微函数 $f(x,y)$，使得
>
> $$\mathbf{F} = \nabla f = \frac{\partial f}{\partial x}\hat{\mathbf{i}}+\frac{\partial f}{\partial y}\hat{\mathbf{j}},$$
>
> 则称 $\mathbf{F}$ 为 $D$ 上的**保守场**（conservative field，亦称**梯度场**），$f$ 称为 $\mathbf{F}$ 的**势函数**（potential function）。

> [!important: 曲线积分基本定理]
>
> 若 $\mathbf{F}=\nabla f$ 在包含有向曲线 $L$ 的区域上连续可微，$L$ 从点 $A$ 到点 $B$，则
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = f(B) - f(A).$$
>
> **证明**：设 $L$：$\mathbf{r}(t)=(x(t),y(t))$，$t\in[t_0,t_1]$，$\mathbf{r}(t_0)=A$，$\mathbf{r}(t_1)=B$，则
>
> $$\int_L\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_{t_0}^{t_1}\!\!\left(\frac{\partial f}{\partial x}x'(t)+\frac{\partial f}{\partial y}y'(t)\right)\mathrm{d}t = \int_{t_0}^{t_1}\frac{\mathrm{d}}{\mathrm{d}t}f(x(t),y(t))\,\mathrm{d}t = f(B)-f(A). \quad\blacksquare$$

这是一元微积分基本定理 $\int_a^b f'(x)\,\mathrm{d}x=f(b)-f(a)$ 的直接推广：**"对梯度的曲线积分只取决于边界"**。

> [!important: 保守场的等价条件]
>
> 在**单连通区域** $D$（无"洞"的区域）上，以下四个条件等价：
>
> 1. $\mathbf{F}$ 是保守场（存在势函数 $f$）；
> 2. 曲线积分与路径无关：对 $D$ 中任意 $A,B$，积分值与连接 $A,B$ 的路径无关；
> 3. 对 $D$ 内任意封闭曲线 $C$，$\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}=0$；
> 4. $\operatorname{curl}\mathbf{F} = \dfrac{\partial Q}{\partial x}-\dfrac{\partial P}{\partial y} = 0$。
>
> **条件 4 的必要性**：若 $f$ 存在，则 $P=f_x,\,Q=f_y$，由混合偏导连续性得 $P_y=f_{xy}=f_{yx}=Q_x$，即 $\operatorname{curl}\mathbf{F}=0$。
>
> **注**：条件 4 的充分性依赖单连通性。在非单连通区域（如去掉原点的平面 $\mathbb{R}^2\setminus\{(0,0)\}$）中，$\operatorname{curl}\mathbf{F}=0$ 不能保证 $\mathbf{F}$ 是保守场（经典反例：$\mathbf{F}=\dfrac{(-y,\,x)}{x^2+y^2}$）。

**求势函数的方法**：已知 $\mathbf{F}=(P,Q)$ 满足 $\operatorname{curl}\mathbf{F}=0$，求 $f(x,y)$。

对 $x$ 积分：$f(x,y)=\displaystyle\int P(x,y)\,\mathrm{d}x + g(y)$，其中 $g(y)$ 为待定函数。再由 $f_y=Q$ 确定 $g'(y)$，积分得 $g(y)$。

> [!note: 例题]
>
> 验证 $\mathbf{F}=(2xy+1,\,x^2-1)$ 是保守场，并求满足 $f(0,0)=0$ 的势函数 $f$。
>
> **解**：$P_y=2x=Q_x$，故 $\operatorname{curl}\mathbf{F}=0$，$\mathbf{F}$ 是保守场。
>
> 对 $x$ 积分：$f=\int(2xy+1)\,\mathrm{d}x+g(y)=x^2y+x+g(y)$。
>
> 由 $f_y=x^2+g'(y)=x^2-1$，得 $g'(y)=-1$，故 $g(y)=-y+c$。
>
> 代入 $f(0,0)=0$：$c=0$，从而 $f(x,y)=x^2y+x-y$。

::: {.exercise id="chpt12-ex-009"}
:::

## 12.5 曲面积分

至此，二维的积分理论已经完整：沿曲线积分（第一类、第二类）以及将区域内部与边界联系起来的格林公式。现在将同样的思路推广到三维空间：**曲面**取代曲线，**通量**取代做功。

> [!tip: 引入问题：流体穿过曲面的通量]
>
> 流体以速度场 $\mathbf{F}(x,y,z)=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 流动，空间中有一有向曲面 $S$。单位时间内穿过 $S$ 的流体体积（**通量**）是多少？
>
> 将 $S$ 分成 $N$ 个小面片，第 $i$ 片的面积为 $\Delta S_i$，外法向单位向量为 $\mathbf{n}_i$。穿过该小片的流量约为 $\mathbf{F}(x_i,y_i,z_i)\cdot\mathbf{n}_i\,\Delta S_i$。令各小片面积最大值 $\to 0$，取极限即得通量。

> [!important: 定义：曲面积分（通量型）]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 在有向曲面 $S$ 上连续，$\mathbf{n}$ 为 $S$ 的单位法向量，则 $\mathbf{F}$ 穿过 $S$ 的**通量**定义为
>
> $$\iint_S\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S}.$$

**计算方法**：设 $S$ 由 $z=g(x,y)$，$(x,y)\in D_{xy}$ 给出，取朝上法向量。曲面上的切向量为

$$\mathbf{v}_1=(1,\,0,\,g_x), \quad \mathbf{v}_2=(0,\,1,\,g_y),$$

法向量微元为

$$\mathbf{n}\,\mathrm{d}S = \mathbf{v}_1\times\mathbf{v}_2\,\mathrm{d}x\,\mathrm{d}y = (-g_x,\,-g_y,\,1)\,\mathrm{d}x\,\mathrm{d}y.$$

（朝下法向量取反号。）于是

$$\iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S} = \iint_{D_{xy}}\bigl(-P\,g_x - Q\,g_y + R\bigr)\,\mathrm{d}x\,\mathrm{d}y.$$

> [!note: 方向的选取]
>
> 曲面积分与曲面的**定向**有关，改变法向量方向则积分变号。对**封闭曲面**（如球面），通常约定外法向量为正方向；对**开曲面**，需事先指定法向量朝哪一侧。

> [!note: 例题]
>
> 计算 $\mathbf{F}=z\hat{\mathbf{k}}$ 穿过上半球面 $S:\,x^2+y^2+z^2=a^2,\,z\geq 0$（取朝上法向量）的通量。
>
> **解**：$z=g(x,y)=\sqrt{a^2-x^2-y^2}$，$P=Q=0,\,R=z$，$g_x=-x/z,\,g_y=-y/z$，故
>
> $$\iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S} = \iint_{x^2+y^2\leq a^2} z\,\mathrm{d}x\,\mathrm{d}y = \iint_{x^2+y^2\leq a^2}\sqrt{a^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y.$$
>
> 用极坐标 $x=r\cos\theta,\,y=r\sin\theta$：
>
> $$= \int_0^{2\pi}\int_0^a\sqrt{a^2-r^2}\cdot r\,\mathrm{d}r\,\mathrm{d}\theta = 2\pi\cdot\frac{a^3}{3} = \frac{2\pi a^3}{3}.$$

::: {.exercise id="chpt12-ex-014"}
:::

## 12.6 高斯公式与斯托克斯公式

### 12.6.1 高斯公式

> [!tip: 引入问题：源与通量的关系]
>
> 设空间区域 $V$ 内有流体流动，速度场为 $\mathbf{F}$。若 $V$ 内某处是流体的**源**（即流体在那里被持续"产生"），这些新产生的流体必然向外流出并最终穿越边界曲面 $\partial V$。那么，$V$ 内总的产生率与穿越边界的总通量之间有何定量关系？

> [!important: 定义：散度]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 有连续偏导数，称
>
> $$\operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$
>
> 为 $\mathbf{F}$ 的**散度**。$\operatorname{div}\mathbf{F}>0$ 表示该点是源，$<0$ 表示是汇，$=0$ 表示不可压缩（流体既不产生也不消失）。

> [!important: 高斯公式（散度定理）]
>
> 设 $V$ 为空间中由分片光滑封闭曲面 $\Sigma=\partial V$ 围成的有界区域，$\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 在 $V$ 上有一阶连续偏导数，$\mathbf{n}$ 为 $\Sigma$ 的外法向量，则
>
> $$\oiint_{\Sigma}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iiint_V\nabla\cdot\mathbf{F}\,\mathrm{d}V.$$

> [!extension: 证明思路]
>
> 分别证明（以 $R$ 分量为例）：
>
> $$\oiint_\Sigma R\,\mathrm{d}x\,\mathrm{d}y = \iiint_V \frac{\partial R}{\partial z}\,\mathrm{d}V.$$
>
> 设 $V$ 为"竖直简单"区域：投影到 $xy$ 平面得 $D_{xy}$，$z$ 介于底面 $z=z_1(x,y)$ 和顶面 $z=z_2(x,y)$ 之间。在顶面（朝外即朝上）$\mathrm{d}x\,\mathrm{d}y>0$；在底面（朝外即朝下）$\mathrm{d}x\,\mathrm{d}y<0$；在侧面 $\mathrm{d}x\,\mathrm{d}y=0$。故
>
> $$\oiint_\Sigma R\,\mathrm{d}x\,\mathrm{d}y = \iint_{D_{xy}}\bigl[R(x,y,z_2)-R(x,y,z_1)\bigr]\,\mathrm{d}x\,\mathrm{d}y.$$
>
> 另一方面，由单变量 FTC：
>
> $$\iiint_V R_z\,\mathrm{d}V = \iint_{D_{xy}}\int_{z_1}^{z_2}R_z\,\mathrm{d}z\,\mathrm{d}x\,\mathrm{d}y = \iint_{D_{xy}}\bigl[R(x,y,z_2)-R(x,y,z_1)\bigr]\,\mathrm{d}x\,\mathrm{d}y.$$
>
> 两式相等。$P$ 和 $Q$ 分量类似处理，三式相加即得高斯公式。$\blacksquare$

> [!note: 与格林公式的类比]
>
> 高斯公式是格林公式通量形式的三维版本：
>
> | 维度 | 公式 |
> |:---|:---|
> | 二维（格林通量形式）| $\oint_{\partial D}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}s = \iint_D\nabla\cdot\mathbf{F}\,\mathrm{d}A$ |
> | 三维（高斯）| $\oiint_{\partial V}\mathbf{F}\cdot\mathbf{n}\,\mathrm{d}S = \iiint_V\nabla\cdot\mathbf{F}\,\mathrm{d}V$ |
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

### 12.6.2 斯托克斯公式

三维空间中的曲线积分是二维情形的自然推广：

$$\int_C\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \int_C P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z,$$

其中 $\mathrm{d}\mathbf{r}=(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$，计算方法与二维相同（参数化代入）。

> [!tip: 引入问题：三维中的环量与旋转]
>
> 三维向量场 $\mathbf{F}$ 沿封闭曲线 $C$ 的环量 $\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}$ 与 $C$ 所围曲面 $S$ 上的"旋转强度"有何关系？这是格林公式在三维的推广：格林公式中的平面区域推广为任意曲面。

> [!important: 定义：三维旋度]
>
> 设 $\mathbf{F}=P\hat{\mathbf{i}}+Q\hat{\mathbf{j}}+R\hat{\mathbf{k}}$ 有连续偏导数，定义 $\mathbf{F}$ 的**旋度**（三维）为
>
> $$\operatorname{curl}\mathbf{F} = \nabla\times\mathbf{F} = \begin{vmatrix}\hat{\mathbf{i}}&\hat{\mathbf{j}}&\hat{\mathbf{k}}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix} = (R_y-Q_z)\hat{\mathbf{i}}+(P_z-R_x)\hat{\mathbf{j}}+(Q_x-P_y)\hat{\mathbf{k}}.$$

> [!note: 二维旋度是三维旋度的分量]
>
> 对平面向量场 $\mathbf{F}=(P,Q,0)$，三维旋度为 $(0,\,0,\,Q_x-P_y)$，其 $\hat{\mathbf{k}}$-分量恰是二维旋度 $Q_x-P_y$。三维旋度是二维旋度的自然推广。

> [!important: 斯托克斯公式]
>
> 设 $S$ 为分片光滑的有向曲面，其边界 $\partial S$ 为分段光滑的有向封闭曲线（方向由右手法则与 $S$ 的法向量相符），$\mathbf{F}$ 在含 $S$ 的区域上有连续偏导数，则
>
> $$\oint_{\partial S}\mathbf{F}\cdot\mathrm{d}\mathbf{r} = \iint_S(\nabla\times\mathbf{F})\cdot\mathbf{n}\,\mathrm{d}S.$$

> [!extension: 证明思路]
>
> 将 $S$ 用参数方程 $\mathbf{r}(u,v)=(x(u,v),y(u,v),z(u,v))$，$(u,v)\in R$ 参数化。用链式法则将 $\oint_{\partial S} P\,\mathrm{d}x$ 转化为参数域 $R$ 的边界上的积分 $\oint_{\partial R}(\cdots)\,\mathrm{d}u+(\cdots)\,\mathrm{d}v$，再对 $R$ 应用格林公式展开，所得表达式恰与右端 $\iint_S (R_y-Q_z,P_z-R_x,Q_x-P_y)\cdot\mathbf{n}\,\mathrm{d}S$ 中的对应项相等。对 $P,Q,R$ 三项逐一处理后相加，即得斯托克斯公式。$\blacksquare$

> [!important: 三维保守场的判定]
>
> 在单连通空间区域 $D$ 上，以下条件等价：
>
> 1. $\mathbf{F}=\nabla f$（存在势函数）；
> 2. $\operatorname{curl}\mathbf{F}=\mathbf{0}$，即 $R_y=Q_z,\;P_z=R_x,\;Q_x=P_y$；
> 3. 对 $D$ 内任意封闭曲线 $C$，$\oint_C\mathbf{F}\cdot\mathrm{d}\mathbf{r}=0$。
>
> 势函数的求法与二维相同：依次对 $x,y,z$ 积分，逐步确定待定函数。

::: {.exercise id="chpt12-ex-021"}
:::

::: {.exercise id="chpt12-ex-022"}
:::

::: {.exercise id="chpt12-ex-019"}
:::

::: {.exercise id="chpt12-ex-020"}
:::

## 12.7 统一视角：广义牛顿-莱布尼茨公式
