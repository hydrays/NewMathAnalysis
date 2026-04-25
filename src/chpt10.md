# 多元函数的微分

> [!tip]
>
> 多元函数的微分是一元函数微分的推广, 它的一个非常重要的应用是求多元函数的极值. 例如 (P115例6) 有一块宽为 24cm 的方形铁板, 把它两边折起来做成一个断面为等腰梯形的水槽, 问怎样的折法才能使得截面面积最大? 设折出来的梯形底边长度为 $x$, 斜边的角度为 $\theta$, 则截面积可写成
>
> $$
> S(x, \theta) = 24 x \sin\theta - 2x^2 \sin\theta + x^2 \sin\theta \cos\theta
> $$
>
> 这是一个关于 $x, \theta$ 的二元函数, 如何求它的最大值呢? 我们可以带着这个问题开始本章的学习.

## 多元函数的连续性

> [!tip]
>
> 在一元微积分中, 连续函数是我们的主要研究对象, 在多元微积分中同样也是这样. 下面我们先介绍一些准备知识作为铺垫, 然后给出多元函数极限和连续的定义.
>

### 区域

> [!tip]
>
> 在一元函数中, 我们经常使用**区间**的概念, 如开区间 $(a, b)$, 闭区间 $[a, b]$. **区域**是区间在高维空间中的推广. 下面我们以 $\mathbb{R}^2$ 为例进行介绍, 但所有的概念都可以推广到 $\mathbb{R}^n$ 中.
>

> [!important: 邻域]
>
> 设 $P_0(x, y)$ 是 $\mathbb{R}^2$ 中的一点, 给定 $\delta > 0$, $\mathbb{R}^2$ 中所有与点 $P_0$ 距离小于 $\delta$ 的点构成一个集合, 称为点 $P_0$ 的 **$\delta$-邻域**, 记作 $U(P_0, \delta)$, 即
> $$
>   U(P_0, \delta) = \{ (x, y)| \sqrt{(x-x_0)^2+ (y-y_0)^2} < \delta\}.
> $$
>
> $P_0$ 与其自己的距离为0, 所以根据上述定义, $P_0\in U(P_0, \delta)$. 但有时候我们希望排除掉 $P_0$ 这一点, 在集合 $U(P_0, \delta)$ 中把 $P_0$ 去掉, 由此得到的集合称为 $P_0$ 的 **$\delta$-去心邻域**, 记作 $\overset{\circ}{U}(P_0, \delta)$, 即
> $$
>  \overset{\circ}{U}(P_0, \delta) = \{ (x, y)| 0 < \sqrt{(x-x_0)^2+ (y-y_0)^2} < \delta\}.
> $$
>
> 有时候我们不关心 $\delta$ 的具体取值 (比如接下来的问题中), 往往简单用 $U(P_0)$ 和 $\overset{\circ}{U}(P_0)$ 分别表示 $P_0$ 的**邻域**和**去心邻域**.
>

> [!important: 内点]
>
> 任意给定一个 $\mathbb{R}^2$ 中的集合 $D$, 任意一点 $P$ 与 $D$ 的关系必符合以下三种关系中的一种:
>
> 1. **内点**: 存在点 $P$ 的某个邻域 $U(P)$, 使得 $U(P) \subset D$.
> 2. **外点**: 存在点 $P$ 的某个邻域 $U(P)$, 使得 $U(P) \cap D = \emptyset$.
> 3. **边界点**: 点 $P$ 的任一邻域内既有属于 $D$ 的点, 又有不属于 $D$ 的点.
>
> 集合 $D$ 的全体**边界点**所构成的集合称为 $D$ 的**边界**, 记作 $\partial D$.
>

::: {. exercise id="chpt10-ex-015"}
:::

> [!important: 开集与闭集]
>
> **开集**: 集合中的所有点都是其内点
> **闭集**: 集合的边界属于该集合, $\partial D \subseteq D$
>

::: {. exercise id="chpt10-ex-016"}
:::

> [!important: 连通集]
>
> 顾名思义, 如果集合 $D$ 中的任意两点都可以用折线连接起来, 且该折线上的点都属于 $D$, 则称 $D$ 为**连通集**.

> [!important: 区域]
>
> **连通开集**称为**区域**(或**开区域**); 开区域连同它的边界一起所构成的集合称为**闭区域**.
>

> [!important: 例子]
>
> 集合 $\{(x,y) \mid 1 < x^2 + y^2 < 2\}$ 是开区域, 而集合 $\{(x,y) \mid 1 \leq x^2 + y^2 \leq 2\}$ 是闭区域.

> [!important: 有界集与无界集]
>
> **有界集** : 对于平面点集 $E$, 如果存在正数 $r$, 使得$E \subset U(O, r)$, 其中 $O$ 为坐标原点, 则称 $E$ 为有界集,
> **无界集** : 如果一个集合不是有界集, 则称其为无界集,

### 多元函数的极限

> [!tip]
>
> 下面我们以含有两个自变量的函数, 即二元函数为例引入多元函数及其极限的概念. 相关概念可以很容易推广到含有三个或更多自变量的多元函数中去.

> [!important: 二元函数的定义]
>
>设 $D$ 是 $\mathbb{R}^2$ 中的非空子集, 称映射 $f: D \to \mathbb{R}$ 为定义在 $D$ 上的**二元函数**, 记为
>$$
>z = f(x, y), \quad (x, y) \in D
>$$
>
>其中 $D$ 称为函数的**定义域** , $x$ 和 $y$ 称为**自变量**.

>[!important]
>
> **二元函数的极限**
>
> 设 $f(x,y)$ 为定义在 $D$ 上的二元函数, $P_0(x_0, y_0)$ 是 $D$ 的聚点, 如果存在常数 $A$, 对于任意给定的正数 $\varepsilon$, 总存在正数 $\delta$, 使得当 $(x,y) \in U(P_0, \delta)$ 时, 有 $ |f(x, y) - A| < \varepsilon $, 则称 $A$ 为函数 $f(x,y)$ 当 $(x,y)$ 趋于 $(x_0, y_0)$ 时的极限, 记作
> $$
> \displaystyle\lim_{(x,y) \to (x_0, y_0)} f(x,y) = A.
> $$
>

> [!warning]
>
> 注意从 $(x, y)$ 趋于 $(x_0, y_0)$ 有无数条路径, 极限存在要求**任意一条路径都成立**, 不能仅仅验证从 $x$-轴趋近和从$y$-轴趋近就断言极限存在.

::: {. exercise id="chpt10-ex-001"}
:::

::: {. exercise id="chpt10-ex-002"}
:::

::: {. exercise id="chpt10-ex-003"}
:::

### 多元函数的连续性

> [!tip]
>
> 下面我们仍然以二元函数为例引入多元函数连续的概念. 相关概念可以很容易推广到含有三个或更多自变量的多元函数中去.
>

> [!important: 二元函数连续性]
>
> 设 $f(x, y)$ 为定义在 $D$ 上的二元函数, $P_0 (x_0, y_0)$ 为 $D$ 的聚点, 且 $P_0 \in D$, 如果 $ \displaystyle\lim_{(x,y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$, 则称函数 $f(x, y)$ 在点 $P_0 (x_0, y_0)$ 连续, 进一步, 如果函数 $f(x, y)$ 在 $D$ 内**每一点都连续**, 则称函数 $f(x, y)$ 为 $D$ 上的**连续函数**.
>
> **间断点**
> 设函数 $f(x,y)$ 的定义域为 $D$, $P_0(x_0, y_0)$ 是 $D$ 的聚点, 如果函数 $f(x,y)$ 在点 $P_0(x_0, y_0)$ **不连续**, 那么称 $P_0(x_0, y_0)$ 为函数 $f(x,y)$ 的**间断点**,

> [!important: 连续函数的性质]
>
> 与**闭区间**上一元连续函数的性质相类似, 在**有界闭区域**上连续的多元函数具有如下性质:
>
> - **性质1: 最大值与最小值**
> 有界闭区域 $D$ 上的多元连续函数必定在 $D$ 上有界, 且能取到它的最大值和最小值,
>
> - **性质2: 介值定理**
> 有界闭区域 $D$ 上的多元连续函数能取到介于最大值和最小值之间的任何值,
>

## 偏导数

> [!tip]
>
> 固定其它变量, 看一个变量变化对函数值的影响.


> [!important: 偏导数]
>
> 设函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 的某一邻域内有定义, 固定 $y=y_0$ 让 $x$ 在 $x_0$ 附近变化, 若极限
> $$
> \displaystyle\lim_{\Delta x \to 0} \displaystyle\frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x} \tag{2-1} 
> $$
> 存在, 则称此极限为函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处对 $x$ 的**偏导数**, 记作:
> $$
> \left. \displaystyle\frac{\partial z}{\partial x} \right|_{x=x_0}, \quad \left. \displaystyle\frac{\partial f}{\partial x} \right|_{x=x_0}, \quad z_x \bigg|_{x=x_0} \text{ 或 } f_x(x_0, y_0)
> $$
>
> 类似地, 函数 $z=f(x,y)$ 对 $y$ 的偏导数为:
> $$
> \displaystyle\lim_{\Delta y \to 0} \displaystyle\frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y} 
> $$
> 记作:
> $$
> \displaystyle\left. \displaystyle\frac{\partial z}{\partial y} \right|_{y=y_0}, \quad \left. \displaystyle\frac{\partial f}{\partial y} \right|_{y=y_0}, \quad z_y \bigg|_{y=y_0} \text{ 或 } f_y(x_0, y_0)
> $$
>

> [!warning: 偏导函数]
>
> 若 $z=f(x,y)$ 在区域 $D$ 内每一点 $(x,y)$ 处对 $x$ 的偏导数存在, 则由此构成的函数称为**偏导函数**, 记作:
>$$
>\displaystyle\frac{\partial z}{\partial x}, \quad \displaystyle\frac{\partial f}{\partial x}, \quad z_x \text{ 或 } f_x(x, y)
>$$
> 对 $y$ 的偏导函数记为:
> $$
> \displaystyle\frac{\partial z}{\partial y}, \quad \displaystyle\frac{\partial f}{\partial y}, \quad z_y \text{ 或 } f_y(x, y)
> $$

::: {. exercise id="chpt10-ex-004"}
:::


>[!important]
>
>==高阶偏导数==
>
> 对偏导函数再求偏导数称为**二阶偏导数**, 以此类推还有三阶偏导数和更高阶的偏导数.
>

> [!warning: 二阶偏导数的四种形式]
>
>1. 对 $x$ 的二阶偏导:
>$$ \displaystyle\displaystyle\frac{\partial}{\partial x} \left( \displaystyle\frac{\partial z}{\partial x} \right) = \displaystyle\frac{\partial^2 z}{\partial x^2} = f_{xx}(x, y) $$
>
>2. 先对 $x$ 后对 $y$ 的混合偏导:
>$$ \displaystyle\frac{\partial}{\partial y} \left( \displaystyle\frac{\partial z}{\partial x} \right) = \displaystyle\frac{\partial^2 z}{\partial x \partial y} = f_{xy}(x, y) $$
>
>3. 先对 $y$ 后对 $x$ 的混合偏导:
>$$ \displaystyle\frac{\partial}{\partial x} \left( \displaystyle\frac{\partial z}{\partial y} \right) = \displaystyle\frac{\partial^2 z}{\partial y \partial x} = f_{yx}(x, y) $$
>
>4. 对 $y$ 的二阶偏导:
>$$ \displaystyle\frac{\partial}{\partial y} \left( \displaystyle\frac{\partial z}{\partial y} \right) = \displaystyle\frac{\partial^2 z}{\partial y^2} = f_{yy}(x, y) $$

::: {. exercise id="chpt10-ex-017"}
:::

>[!important]
>
>==二阶混合偏导数定理==
>
> 如果函数 $z = f(x, y)$ 的二阶混合偏导数 $ \displaystyle\frac{\partial^2 z}{\partial y \partial x} \quad \text{和} \quad \displaystyle\frac{\partial^2 z}{\partial x \partial y} $ 在区域 $D$ 内连续, 那么在该区域内必有:
> $$
> \displaystyle\frac{\partial^2 z}{\partial y \partial x} = \displaystyle\frac{\partial^2 z}{\partial x \partial y}
> $$
>
> 即: **二阶混合偏导数在连续条件下与求导次序无关**,

::: {. exercise id="chpt10-ex-005"}
:::

::: {. exercise id="chpt10-ex-006"}
:::

## 全微分

> [!tip]
>
> 在学习全微分的知识之前, 我们来回顾一下**一元函数微分**, 对于函数 $y=f(x)$, 其增量可表示为
>
> $$
> df = f'(x)dx
> $$
>
> 接下来我们要把上述关系推广到多元函数, 从而将函数值的变化与自变量的变化联系起来.
>

> [!important: 全微分公式]
>
> $$
> dz = \displaystyle\frac{\partial z}{\partial x}dx + \displaystyle\frac{\partial z}{\partial y}dy 
> $$
>

> [!warning: 全微分的几何理解]

<div id="grad3d" style="width:100%; max-width:780px; height:450px; position: relative; margin:1.5em auto; background: #0B6E4F; border-radius:8px; overflow: hidden; box-shadow:0 10px 30px rgba(6,18,10,0.28);"></div>
<script type="module" src="threejs/chapter10-scene.js?v=20260330i"></script>
<div id="grad3d_local" style="width:100%; max-width:780px; height:430px; position: relative; margin:1.0em auto 1.5em auto; background: #0B6E4F; border-radius:8px; overflow: hidden; box-shadow:0 10px 30px rgba(6,18,10,0.28);"></div>
<script type="module" src="threejs/chapter10-local-scene.js?v=20260331c"></script>
<div id="grad2d" style="width:100%; max-width:780px; height:440px; position: relative; margin:1.5em auto; background: #0d1a2e; border-radius:8px; overflow: hidden; box-shadow:0 10px 30px rgba(6,18,10,0.28);"></div>
<script type="module" src="threejs/chapter10-gradient2d.js?v=20260331a"></script>
<div style="display: flex; gap:8px; width:100%; max-width:960px; margin:1.5em auto;">
<div id="cplx-2d" style="flex:1; height:440px; position: relative; background: #0d1a2e; border-radius:8px; overflow: hidden; box-shadow:0 10px 30px rgba(0,0,0,0.4);"></div>
<div id="cplx-3d" style="flex:1.4; height:440px; position: relative; background: #0b1020; border-radius:8px; overflow: hidden; box-shadow:0 10px 30px rgba(0,0,0,0.4);"></div>
</div>
<script type="module" src="threejs/chapter10-complex.js?v=20260331a"></script>

::: {. exercise id="chpt10-ex-007"}
:::

::: {. exercise id="chpt10-ex-008"}
:::

::: {. exercise id="chpt10-ex-009"}
:::

### 链式法则

> [!tip]
>
> 全微分公式能够表示因变量 $z$ 对自变量 $x, y$ 的依赖关系. 如果我们把全微分公式稍微变形, 就能非常自然地推导出多元微积分中极其重要的**链式法则 (Chain Rule)**. 无论是物理学中寻找随时间变化的变化率, 还是在不同坐标系 (如直角坐标与极坐标) 之间进行变量替换, 链式法则都不可或缺.
>

> [!important: 一元函数与多元函数复合的情形]
>
> 设 $z = f(u, v)$, 而 $u = u(t)$, $v = v(t)$.
> 则复合函数 $z$ 对 $t$ 的全导数公式为:
> $$
> \frac{dz}{dt} = \frac{\partial z}{\partial u}\frac{du}{dt} + \frac{\partial z}{\partial v}\frac{dv}{dt}
> $$
>
> **多元函数与多元函数复合的情形**
>
> 更一般地, 如果中间变量本身又是多个变量的函数, 例如 $u = u(x,y)$, $v = v(x,y)$.
> 则复合函数分别对 $x$ 和 $y$ 的偏导数法则为:
> $$
> \frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}
> $$
> $$
> \frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y}
> $$
>

::: {. exercise id="chpt10-ex-018"}
:::

### 全微分形式不变性

> [!tip]
>
> 微分符号的奇妙之处在于, 无论 $u, v$ 是作为**最终自变量**, 还是作为进一步依赖其他变量的**中间变量**, 全微分的表达式 $dz = \frac{\partial z}{\partial u}du + \frac{\partial z}{\partial v}dv$ 始终保持形式上的一致. 这个深刻的性质被称为**全微分形式不变性**. 它能帮我们绕开繁琐的链式法则, 直接通过代数代入来求导!
>

::: {. exercise id="chpt10-ex-019"}
:::

### 隐函数求导

> [!tip]
>
> 在实际问题中, 变量之间的关系常常以隐式方程 $F(x,y)=0$ 或 $F(x,y,z)=0$ 的形式给出, 直接解出因变量 (即求反函数) 往往非常繁琐甚至不可能. 利用全微分的性质, 我们可以极其优雅地绕过这一困难, 直接求出隐函数的导数. 因为方程恒为零, 对其取全微分也必为零.
>

> [!important: 一元隐函数的求导公式]
>
> 设方程 $F(x,y) = 0$ 确定了隐函数 $y = f(x)$.
> 对方程两端取全微分得:
> $dF = F_x dx + F_y dy = 0$
> 只要 $F_y \neq 0$, 直接移项即可得到一阶导数:
> $$
> \frac{dy}{dx} = -\frac{F_x}{F_y}
> $$
>
> **二元隐函数的求导公式**
>
> 若方程 $F(x,y,z) = 0$ 确定了二元隐函数 $z = f(x,y)$.
> 当需要计算偏导数 $\frac{\partial z}{\partial x}$ 时, 意味着 $y$ 为常数 (即 $dy = 0$), 全微分退化为 $F_x dx + F_z dz = 0$:
> $$
> \frac{\partial z}{\partial x} = -\frac{F_x}{F_z} \quad (F_z \neq 0)
> $$
> 同理可得:
> $$
> \frac{\partial z}{\partial y} = -\frac{F_y}{F_z} \quad (F_z \neq 0)
> $$
> 这个自带负号的公式, 正是全微分移项产生的自然结果.
>

::: {. exercise id="chpt10-ex-020"}
:::

## 梯度与方向导数

### 梯度

>[!important]
>
>==梯度的定义==
>设二元函数$f(x,y) $ 在区域$D$ 内具有一阶连续偏导数, 则对于任意点 $ P_0(x_0,y_0) \in D $, 其梯度定义为:
>$$\text{grad}\, f(x_0,y_0) = \nabla f(x_0,y_0) = f_x(x_0,y_0)\,\mathbf{i} + f_y(x_0,y_0)\,\mathbf{j}$$
>其中微分算子$  \nabla = \dfrac{\partial}{\partial x}\mathbf{i} + \dfrac{\partial}{\partial y}\mathbf{j} ,$

> [!warning: 梯度方向是函数值增长最快的方向]

::: {. exercise id="chpt10-ex-010"}
:::

::: {. exercise id="chpt10-ex-011"}
:::

::: {. exercise id="chpt10-ex-012"}
:::

> [!important: 三元函数的梯度定义与性质]
>
>设三元函数 $f(x,y,z)$ 在空间区域 $G$ 内具有一阶连续偏导数, 则对于点 $P_0(x_0, y_0, z_0) \in G$, 其梯度为:
>
> $$\text{grad}\, f(x_0,y_0,z_0) = \nabla f(x_0,y_0,z_0) = f_x\,\mathbf{i} + f_y\,\mathbf{j} + f_z\,\mathbf{k}$$
> 其中三维Nabla算子:
> $$ \nabla = \dfrac{\partial}{\partial x}\mathbf{i} + \dfrac{\partial}{\partial y}\mathbf{j} + \dfrac{\partial}{\partial z}\mathbf{k} $$
>

::: {. exercise id="chpt10-ex-021"}
:::


### 方向导数

>[!important]
>
>==方向导数的定义==
>设函数 $f(x,y,z)$ 在点 $P_0(x_0,y_0,z_0)$ 的某邻域内有定义, $\mathbf{l}$ 为从 $P_0$ 出发的给定方向向量, $P(x,y,z)$ 为 $\mathbf{l}$ 上邻近 $P_0$ 的点, 若极限
>$$
> \displaystyle\lim_{\rho \to 0^+} \frac{f(P) - f(P_0)}{\rho} = \left. \frac{\partial f}{\partial l} \right|_{P_0}
>$$
>存在, 则称此极限为 $f$ 在 $P_0$ 点沿方向 $\mathbf{l}$ 的**方向导数**, 其中 $\rho = |PP_0|$.

>[!warning]
>==方向导数与梯度的关系==
>
> 方向导数等于梯度在该方向上的投影.

## 多元函数的极值

### 无约束极值问题

::: {. exercise id="chpt10-ex-013"}
:::

::: {. exercise id="chpt10-ex-014"}
:::

#### 无约束极值的判别法

> [!tip]
>
> 我们知道, 在一元函数中, 通过令一阶导数 $f'(x)=0$ 我们可以找到驻点, 然后通过二阶导数 $f''(x)$ 的符号可以判断该点是极大值还是极小值.
> 对于多元函数, 我们同样通过令所有一阶偏导数为零来寻找**临界点 (驻点)**. 但是, 多元函数的临界点除了极大值和极小值之外, 还有可能是**鞍点 (Saddle Point, 即在某些方向上是极大, 在另一些方向上是极小)**. 如何准确对临界点进行分类呢? 我们需要用到二阶导数判别法.

> [!important: 二元函数的极值充分条件]
>
> 设函数 $z = f(x,y)$ 在临界点 $(x_0, y_0)$ 的某邻域内连续, 且具有一阶及二阶连续偏导数, 且满足一阶必要条件: $f_x(x_0,y_0)=0, f_y(x_0,y_0)=0$.
>
> 我们计算该点处的三个二阶偏导数值, 并记为:
> * $A = f_{xx}(x_0,y_0)$
> * $B = f_{xy}(x_0,y_0)$
> * $C = f_{yy}(x_0,y_0)$
>
> 构造判别式 $\Delta = AC - B^2$. 则在 $(x_0, y_0)$ 处是否取得极值的判断准则如下:
>
> 1. **当 $\Delta = AC - B^2 > 0$ 时, 具有极值**. 具体而言:
> * 如果 **$A > 0$**, 则该点为 **极小值点** (Local Minimum);
> * 如果 **$A < 0$**, 则该点为 **极大值点** (Local Maximum).
> 2. **当 $\Delta = AC - B^2 < 0$ 时, 没有极值**. 该点是一个 **鞍点** (Saddle Point).
> 3. **当 $\Delta = AC - B^2 = 0$ 时, 无法判断** (退化情形). 该点可能有极值, 也可能没有极值, 需要借助其他方法或更高阶的导数来另作讨论.

<!-- ── 临界点分类交互图 ──────────────────────────────────────────────────── -->
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<div style="width:100%; max-width:960px; margin:1.5em auto; background: rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.10); border-radius:10px; padding:14px 18px 10px;"><div style="display: flex; align-items: center; gap:28px; flex-wrap: wrap; justify-content: center; margin-bottom:6px;"><div style="display: flex; align-items: center; gap:10px;"><span style="color: #d5dbe7; font-size:13px; font-family: sans-serif; white-space: nowrap;">λ₁ = <span id="critpt-l1-val" style="display: inline-block; width:38px; text-align: right;">1.0</span></span><input type="range" id="critpt-l1" min="-3" max="3" step="0.1" value="1" style="width:160px; accent-color: #5599ee;"></div><div style="display: flex; align-items: center; gap:10px;"><span style="color: #d5dbe7; font-size:13px; font-family: sans-serif; white-space: nowrap;">λ₂ = <span id="critpt-l2-val" style="display: inline-block; width:38px; text-align: right;">1.0</span></span><input type="range" id="critpt-l2" min="-3" max="3" step="0.1" value="1" style="width:160px; accent-color: #5599ee;"></div><div id="critpt-type-badge" style="padding:4px 16px; border-radius:20px; font-size:13px; font-family: sans-serif; font-weight:600; background: #1a3a1a; color: #66ee88; border:1px solid #3a6a3a; white-space: nowrap;">极小值点 (Local Min)</div></div><div style="font-size:11px; color: #7a8aa0; text-align: center; font-family: sans-serif; margin-bottom:10px;">f(x, y) = ½(λ₁x² + λ₂y²) — 拖动滑块改变 Hessian 特征值, 观察曲面形状变化</div><div style="display: flex; gap:12px;"><div style="flex:1; min-width:0;"><div style="text-align: center; font-size:11px; color: #8899bb; font-family: sans-serif; margin-bottom:4px;">Three. js</div><div id="critpt-3d" style="width:100%; height:380px; position: relative; background: #0d1120; border-radius:8px; overflow: hidden; box-shadow:0 6px 20px rgba(0,0,0,0.5);"></div></div><div style="flex:1; min-width:0;"><div style="text-align: center; font-size:11px; color: #8899bb; font-family: sans-serif; margin-bottom:4px;">Plotly</div><div id="critpt-plotly" style="width:100%; height:380px; background: #0d1120; border-radius:8px; overflow: hidden; box-shadow:0 6px 20px rgba(0,0,0,0.5);"></div></div></div></div>
<script type="module" src="threejs/chapter10-critpt.js?v=20260406a"></script>
<script>
(function () {
const N = 40, R = 2.3;
const xs = Array.from({length: N + 1}, (_, i) => -R + 2 * R * i / N);
const ys = Array.from({length: N + 1}, (_, j) => -R + 2 * R * j / N);
function makeSurface(l1, l2) {
  return [{x: xs, y: ys, z: ys.map(y => xs.map(x => 0.5 * (l1*x*x + l2*y*y))), type: 'surface',
    colorscale: [[0,'#2166ac'],[0.25,'#74add1'],[0.5,'#f7f7f7'],[0.75,'#f46d43'],[1,'#d73027']],
    showscale: false, opacity: 0.85}];
}
const plotlyLayout = {
  margin: {l:0, r:0, t:0, b:0}, paper_bgcolor: '#0d1120',
  scene: {bgcolor: '#0d1120',
    xaxis: {title:'x', color:'#8899bb', gridcolor:'#1e2a44', zerolinecolor:'#3a4a6a', titlefont:{size:11}},
    yaxis: {title:'y', color:'#8899bb', gridcolor:'#1e2a44', zerolinecolor:'#3a4a6a', titlefont:{size:11}},
    zaxis: {title:'z', color:'#8899bb', gridcolor:'#1e2a44', zerolinecolor:'#3a4a6a', titlefont:{size:11}},
    camera: {eye: {x:1.55, y:1.55, z:1.15}}, aspectratio: {x:1, y:1, z:0.85}},
  font: {color:'#8899bb', size:10}
};
let plotlyReady = false;
function initPlotly(l1, l2) {
  if (typeof Plotly === 'undefined') return;
  Plotly.newPlot('critpt-plotly', makeSurface(l1, l2), plotlyLayout, {responsive:true, displayModeBar:false});
  plotlyReady = true;
}
function updatePlotly(l1, l2) {
  if (typeof Plotly === 'undefined') return;
  if (!plotlyReady) { initPlotly(l1, l2); return; }
  Plotly.react('critpt-plotly', makeSurface(l1, l2), plotlyLayout);
}
function updateBadge(l1, l2) {
  const badge = document.getElementById('critpt-type-badge');
  if (!badge) return;
  const eps = 0.001;
  let text, bg, color, border;
  if (l1 > eps && l2 > eps)           { text='极小值点 (Local Min)'; bg='#0f2a18'; color='#55dd88'; border='#2a6a44'; }
  else if (l1 < -eps && l2 < -eps)    { text='极大值点 (Local Max)'; bg='#2a0f0f'; color='#ee5555'; border='#6a2a2a'; }
  else if (l1 * l2 < -eps * eps)      { text='鞍点 (Saddle Point)';  bg='#1a1a0a'; color='#ddcc44'; border='#5a5a1a'; }
  else                                  { text='退化情形 (Δ = 0)';    bg='#151520'; color='#9999cc'; border='#333355'; }
  badge.textContent = text;
  Object.assign(badge.style, {background:bg, color, borderColor:border});
}
function dispatch() {
  const l1 = parseFloat(document.getElementById('critpt-l1').value);
  const l2 = parseFloat(document.getElementById('critpt-l2').value);
  document.getElementById('critpt-l1-val').textContent = l1.toFixed(1);
  document.getElementById('critpt-l2-val').textContent = l2.toFixed(1);
  updateBadge(l1, l2);
  updatePlotly(l1, l2);
  window.dispatchEvent(new CustomEvent('critpt-update', {detail: {l1, l2}}));
}
document.getElementById('critpt-l1').addEventListener('input', dispatch);
document.getElementById('critpt-l2').addEventListener('input', dispatch);
if (typeof Plotly !== 'undefined') {
  initPlotly(1, 1);
} else {
  const s = document.querySelector('script[src*="plotly"]');
  if (s) s.addEventListener('load', () => initPlotly(1, 1));
}
updateBadge(1, 1);
})();
</script>
<!-- ── end 临界点分类交互图 ──────────────────────────────────────────────── -->

<!-- ── Hessian特征方向可视化（旋转版）────────────────────────────────────── -->

> [!tip]
>
> **海森矩阵总是对称的** ($f_{xy}=f_{yx}$), 因此由**谱定理**, 其特征向量**必然互相垂直**——这是无法绕开的.
> 但当 $B = f_{xy} \neq 0$ 时, 这两个特征方向会相对坐标轴**旋转**, 形成非对角的 Hessian.
> 下图中 $\theta$ 滑块正是控制这一旋转角, 橙色/蓝色抛物线分别对应沿 $\mathbf{e}_1$, $\mathbf{e}_2$ 方向的曲率 (即 $\lambda_1$, $\lambda_2$), 原点处的直角符号说明两特征向量始终垂直.

<div id="critpt2-wrap" style="width:100%; max-width:800px; margin:1.2em auto; background: rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.10); border-radius:10px; padding:14px 18px 10px;"><div style="display: flex; align-items: center; gap:22px; flex-wrap: wrap; justify-content: center; margin-bottom:6px;"><div style="display: flex; align-items: center; gap:8px;"><span style="color: #ff9966; font-size:13px; font-family: sans-serif; white-space: nowrap;">λ₁ = <span id="critpt2-l1-val" style="display: inline-block; width:38px; text-align: right;">2.0</span></span><input type="range" id="critpt2-l1" min="-3" max="3" step="0.1" value="2" style="width:130px; accent-color: #ff7744;"></div><div style="display: flex; align-items: center; gap:8px;"><span style="color: #66ccff; font-size:13px; font-family: sans-serif; white-space: nowrap;">λ₂ = <span id="critpt2-l2-val" style="display: inline-block; width:38px; text-align: right;">-1.0</span></span><input type="range" id="critpt2-l2" min="-3" max="3" step="0.1" value="-1" style="width:130px; accent-color: #44aaff;"></div><div style="display: flex; align-items: center; gap:8px;"><span style="color: #d5dbe7; font-size:13px; font-family: sans-serif; white-space: nowrap;">θ = <span id="critpt2-theta-val" style="display: inline-block; width:34px; text-align: right;">35</span>°</span><input type="range" id="critpt2-theta" min="0" max="90" step="1" value="35" style="width:130px; accent-color: #aaccee;"></div><div id="critpt2-type-badge" style="padding:4px 14px; border-radius:20px; font-size:12px; font-family: sans-serif; font-weight:600; background: #1a1a0a; color: #ddcc44; border:1px solid #5a5a1a; white-space: nowrap;">鞍点 (Saddle)</div></div><div style="font-size:11px; color: #7a8aa0; text-align: center; font-family: sans-serif; margin-bottom:8px;">f = ½(λ₁(x cosθ + y sinθ)² + λ₂(−x sinθ + y cosθ)²) &nbsp; ·&nbsp; 特征向量始终互相垂直</div><div style="text-align: center; font-size:11px; color: #8899bb; font-family: sans-serif; margin-bottom:4px;">Three. js</div><div id="critpt2-3d" style="width:100%; height:460px; position: relative; background: #0a0e1a; border-radius:8px; overflow: hidden; box-shadow:0 6px 24px rgba(0,0,0,0.6);"></div></div>
<script type="module" src="threejs/chapter10-critpt2.js?v=20260406a"></script>
<script>
(function(){
function updateBadge2(l1,l2){
  const b=document.getElementById('critpt2-type-badge'); if(!b)return;
  const eps=0.001; let text,bg,color,border;
  if(l1>eps&&l2>eps)         {text='极小值点 (Local Min)';bg='#0f2a18';color='#55dd88';border='#2a6a44';}
  else if(l1<-eps&&l2<-eps)  {text='极大值点 (Local Max)';bg='#2a0f0f';color='#ee5555';border='#6a2a2a';}
  else if(l1*l2<-eps*eps)    {text='鞍点 (Saddle Point)'; bg='#1a1a0a';color='#ddcc44';border='#5a5a1a';}
  else                        {text='退化情形 (Δ = 0)';   bg='#151520';color='#9999cc';border='#333355';}
  b.textContent=text; Object.assign(b.style,{background:bg,color,borderColor:border});
}
function dispatch2(){
  const l1=parseFloat(document.getElementById('critpt2-l1').value);
  const l2=parseFloat(document.getElementById('critpt2-l2').value);
  const th=parseFloat(document.getElementById('critpt2-theta').value);
  document.getElementById('critpt2-l1-val').textContent=l1.toFixed(1);
  document.getElementById('critpt2-l2-val').textContent=l2.toFixed(1);
  document.getElementById('critpt2-theta-val').textContent=th.toFixed(0);
  updateBadge2(l1,l2);
  window.dispatchEvent(new CustomEvent('critpt2-update',{detail:{l1,l2,theta:th*Math.PI/180}}));
}
document.getElementById('critpt2-l1').addEventListener('input',dispatch2);
document.getElementById('critpt2-l2').addEventListener('input',dispatch2);
document.getElementById('critpt2-theta').addEventListener('input',dispatch2);
updateBadge2(2,-1);
})();
</script>
<!-- ── end Hessian特征方向可视化 ──────────────────────────────────────────── -->

### 条件极值

> [!important]
>
> **条件极值** 是指函数 $f(x, y, \dots)$ 在满足约束条件 $g(x, y, \dots) = 0$ 的前提下取得的极大值或极小值.
> **拉格朗日乘数法 (Lagrange Multipliers)** 是用于求**带有约束条件的极值问题**的一种重要方法. 假设要求函数 $f(x, y)$ 在约束条件 $g(x, y) = 0$ 下的极值,
> **方法**
> 1. 构造拉格朗日函数
> $$ L(x, y, \lambda) = f(x, y) + \lambda g(x, y) $$
> 2. 求偏导并列方程组
> $$\displaystyle\frac{\partial L}{\partial x} = 0,\quad \displaystyle\frac{\partial L}{\partial y} = 0,\quad \displaystyle\frac{\partial L}{\partial \lambda} = 0 $$
> 3. 解这个方程组, 得到可疑点 (驻点);
> 4. 将这些点代入 $f(x, y)$, 比较函数值, 判断极值.

> [!tip: WHY: 为什么拉格朗日乘数法有效? ]
>
> 想象我们要最小化 (或最大化) 函数 $f(x,y)$, 但我们的活动范围被严格限制在约束曲线 $g(x,y) = c$ 上.
>
> 1. **等高线与相切**: 我们在平面上画出固定的约束曲线 $g(x,y) = c$, 然后再画出目标函数 $f(x,y)$ 的**等高线 (Level curves)**. 当我们改变 $f$ 的值时, 等高线会一圈圈扩大或缩小. 当 $f$ 的等高线刚好**触碰 (相切)**到约束曲线的那一瞬间, 我们就找到了这条线上的最小值或最大值!
> 2. **梯度的平行**: 在切点处, 两条曲线完全相切, 这意味着它们的法线是同一条. 我们之前学过, **函数的梯度向量 (Gradient) 总是垂直于它的等高线**. 既然在极值点两曲线相切, 那么 $f$ 的梯度 $\nabla f$ 必须与 $g$ 的梯度 $\nabla g$ 平行!
> 3. **方程的诞生**: 数学上, 我们用一个比例常数 $\lambda$ (拉格朗日乘子) 来表示两个向量的平行关系:
> $$ \nabla f = \lambda \nabla g $$
> 将其拆解为分量形式, 也就是 $f_x = \lambda g_x$ 和 $f_y = \lambda g_y$. 这正是拉格朗日函数 $L_x = 0$ 和 $L_y = 0$ 移项后所表达的核心本质!
>
> ! [拉格朗日乘数法几何直观](.. /media/img/Lagrange_multipliers_geometry. png#200pt)
> *(图注: 在极值点处, 蓝色的 $f$ 等高线与黄色的约束曲线相切, 此时两者的梯度向量 $\nabla f$ 与 $\nabla g$ 必然平行. )*

<!-- ── 拉格朗日乘数法：梯度平行交互可视化 ────────────────────────────────── -->
<div id="lagrange-wrap" style="width:100%; max-width:960px; margin:1.5em auto; background: rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.10); border-radius:10px; padding:14px 18px 10px;"><div style="font-size:12px; color: #7a8aa0; text-align: center; font-family: sans-serif; margin-bottom:10px;">移动鼠标, 观察 <span style="color: #ff2222; font-weight:600">∇f</span> (红色) 与 <span style="color: #22ee22; font-weight:600">∇g</span> (绿色) 的方向: <b style="color: #ccd8ee">仅在极值点处两梯度平行 (或反向) </b></div><div style="display: flex; gap:16px;"><div style="flex:1; min-width:0;"><div style="text-align: center; font-size:11px; color: #aabbff; font-family: sans-serif; font-weight:600; margin-bottom:4px;">例1: f = x²+y², 约束 g: xy = 4</div><div id="lagrange-ex1" style="width:100%; height:400px; position: relative; background: #0c1830; border-radius:8px; overflow: hidden; box-shadow:0 6px 24px rgba(0,0,0,0.6);"></div><div id="lagrange-info-1" style="margin-top:6px; text-align: center; font-size:12px; font-family: monospace; color: #7a8aa0; min-height:20px; padding:3px 8px; background: rgba(0,0,0,0.25); border-radius:5px;">将鼠标移入图形区域</div></div><div style="flex:1; min-width:0;"><div style="text-align: center; font-size:11px; color: #aabbff; font-family: sans-serif; font-weight:600; margin-bottom:4px;">例2: f = xy, 约束 g: x²+y² = 4</div><div id="lagrange-ex2" style="width:100%; height:400px; position: relative; background: #0c1830; border-radius:8px; overflow: hidden; box-shadow:0 6px 24px rgba(0,0,0,0.6);"></div><div id="lagrange-info-2" style="margin-top:6px; text-align: center; font-size:12px; font-family: monospace; color: #7a8aa0; min-height:20px; padding:3px 8px; background: rgba(0,0,0,0.25); border-radius:5px;">将鼠标移入图形区域</div></div></div></div>
<script type="module" src="threejs/chapter10-lagrange.js?v=20260410f"></script>
<!-- ── end 拉格朗日乘数法：梯度平行交互可视化 ──────────────────────────────── -->

> [!warning]
>
> 拉格朗日乘数法只会给你提供**临界点 (候选点)**. 方程本身**并不会**告诉你它是最大值还是最小值 (此时无法使用二阶导数判别法). 你必须将解出来的这些点统一代入原函数 $f(x,y)$ 中, 通过比较数值的大小, 或者结合实际几何背景, 来最终敲定谁是极小值, 谁是极大值.

::: {. exercise id="chpt10-ex-022"}
:::

### 人工智能中的优化问题

> [!tip: 引例: 如何让机器学会画一条“完美”的曲线? ]
>
> 想象我们在做一个科学实验. 我们观察到一个隐藏的真实物理规律 (比如一个正弦波 $y = \sin(2\pi x)$), 但我们在实验室里用仪器测出来的数据往往是不精确的.
>
> 假设我们采集到了 $N$ 个数据点 $(x_1, t_1), (x_2, t_2), \dots, (x_N, t_N)$. 由于测量误差 (随机噪声) 的存在, 这些点会在真实的 $\sin(2\pi x)$ 曲线上下随机波动.
>
> 现在, 我们要求计算机 (AI模型) 在**不知道真实规律是正弦函数**的前提下, 仅凭这 $N$ 个带噪声的散点, 去“猜”并画出一条能够最好地穿过这些点的曲线.
>
> 最自然的想法是, 我们用一个 **$M$ 阶多项式** 去拟合它:
> $$ y(x, \mathbf{w}) = w_0 + w_1 x + w_2 x^2 + \cdots + w_M x^M = \sum_{j=0}^M w_j x^j $$
> 这里的 $x$ 是输入, $w_0, w_1, \dots, w_M$ 是多项式的系数 (在人工智能中通常称为**权重参数**).
>
> **问题来了**: 对于给定的数据点, 我们到底该怎么确定这组参数 $\mathbf{w}$, 才能让这条多项式曲线“最完美”地贴合数据呢? 这就需要引入一种衡量误差的数学标准, 也就是接下来要讲的**最小二乘法**.

#### 数据拟合与最小二乘法

> [!important: 最小二乘法的核心思想 (Least Squares)]
>
> 在工程与科学计算中, 当我们面对一组实验数据时, 我们要找的并不是能**完美穿过**每一个点的曲线 (那往往会导致严重的“过拟合”), 而是寻找一条使得**整体误差最小**的曲线.
>
> 什么样的误差定义最好? 最通用且拥有极好数学性质的方法是: 测量每一个真实数据点 $t_i$ 与模型预测值 $y(x_i, \mathbf{w})$ 之间的偏差 (Deviation), 并将这些**偏差的平方和**作为总误差:
> $$ E(\mathbf{w}) = \frac{1}{2} \sum_{i=1}^N \left( y(x_i, \mathbf{w}) - t_i \right)^2 $$
> (注: 前面乘上 $\frac{1}{2}$ 是为了后续求导时刚好能和平方项的 $2$ 抵消, 方便计算, 不影响极值点的位置. )
>
> 这就是大名鼎鼎的**最小二乘法 (Method of Least Squares)**. 通过寻找使得误差函数 $E(\mathbf{w})$ 达到**极小值**的权重参数 $\mathbf{w}^*$, 我们就找到了“最佳拟合”曲线!

> [!extension: 从多元微积分看最小二乘法的求解]
>
> 结合我们在前几节学过的**多元函数极值**知识, 最小二乘法本质上就是一个**无约束的多元函数求极小值问题**!
>
> 为了直观, 我们退回最简单的线性拟合 (即用直线 $f(x) = ax + b$ 来拟合数据). 此时, 误差函数 $D$ 是关于参数 $a$ 和 $b$ 的二元函数:
> $$ D(a, b) = \sum_{i=1}^N \left( y_i - (ax_i + b) \right)^2 $$
>
> 如何求它的极小值点? 我们只需要让它对 $a$ 和对 $b$ 的**偏导数分别等于 0** 即可找到临界点 (驻点):
> $$ \frac{\partial D}{\partial a} = -2 \sum_{i=1}^N x_i (y_i - ax_i - b) = 0 $$
> $$ \frac{\partial D}{\partial b} = -2 \sum_{i=1}^N (y_i - ax_i - b) = 0 $$
>
> 将上述方程组展开并合并同类项, 你会发现它完全变成了一个关于 $a$ 和 $b$ 的**二元一次线性方程组**:
> $$ \begin{cases} \left(\sum x_i^2\right) a + \left(\sum x_i\right) b = \sum x_i y_i \\ \left(\sum x_i\right) a + n b = \sum y_i \end{cases} $$
> 只要数据点给定了, $\sum x_i$, $\sum y_i$, $\sum x_i^2$ 这些求和项就全是确定的常数数字. 利用矩阵或消元法瞬间就能解出最佳的 $a$ 和 $b$! 即使扩展到前面的 $M$ 阶多项式, 原理也是完全相同的 (偏导数等于0, 解线性方程组). 这正是最小二乘法如此被广泛使用且高效的数学底层逻辑.

#### 正则化与带约束极值问题

> [!extension: 带约束极值问题与人工智能中的正则化 (Regularization)]
>
> 在人工智能和机器学习中, 我们经常面临一个核心痛点: **过拟合 (Overfitting)**. 如果仅仅为了让模型在训练数据上误差 (Loss) 最小, 模型往往会变得异常复杂, 甚至把数据里的“随机噪声”也死记硬背下来, 导致在面对新数据时表现极差.
>
> 为了防止过拟合, AI 工程师们会给模型加上一道“紧箍咒”: 要求模型的参数 (权重 $w_1, w_2, \dots$) 不能太大. 这样一来, 一个纯粹的**无约束极小化问题**, 就顺理成章地变成了一个**带约束的极值问题**!
>
> **1. 从约束极值到拉格朗日函数**
> 假设我们的原本目标是最小化损失函数 $f(w_1, w_2)$. 现在加上一个参数大小的限制, 比如要求权重向量的长度不能超过某个常数: $g(w_1, w_2) = w_1^2 + w_2^2 \le C$ (这在几何上被限制在一个圆盘内).
> 根据本节学过的**拉格朗日乘数法**, 为了求解这个处于边界上的约束极值问题, 我们需要构造拉格朗日函数:
> $$ L(w_1, w_2, \lambda) = f(w_1, w_2) + \lambda (w_1^2 + w_2^2 - C) $$
>
> **2. 机器学习中的 L2 正则化 (权重衰减)**
> 在对权重 $w$ 求偏导时, 常数 $C$ 并不会产生影响. 因此, 在实际的深度学习代码 (如 PyTorch 或 TensorFlow) 中, 优化目标常常被直接写为以下形式:
> $$ \text{Loss}_{\text{total}} = \underbrace{\text{Loss}_{\text{data}}(w)}_{\text{原目标函数 } f} + \underbrace{\lambda (w_1^2 + w_2^2)}_{\text{拉格朗日约束项 } \lambda g} $$
> 这就是机器学习中赫赫有名的 **L2 正则化 (L2 Regularization)**, 在神经网络中也常被称为**权重衰减 (Weight Decay)**!
> 这里的 $\lambda$ 正是我们刚才在微积分中引入的**拉格朗日乘子**. 在 AI 中, 它被称为**惩罚系数** (或正则化系数). 它就像是一个调节器: $\lambda$ 越大, 表示我们对模型复杂度的惩罚越重, 强迫权重向零收缩.
>
> **3. 几何直观的重现**
> 如果没有约束, 损失函数 $f(w)$ 的极小值 (谷底) 可能在一个极远的高风险位置. 加上约束后, 我们的搜索范围被死死锁在了原点附近的圆形栅栏内 ($w_1^2 + w_2^2 \le C$). 损失函数的等高线一圈圈向外膨胀, 直到与这个圆**刚好相切**的那一点, 就是正则化后的最优权重. 此时, 损失函数的梯度与惩罚项的梯度再次满足了**平行**的拉格朗日核心条件!

## 多元函数的泰勒展开

> [!tip]
>
> 在一元微积分中, 泰勒展开 (Taylor Expansion) 为我们提供了一种用多项式来局部逼近复杂函数的强大工具. 在多元微积分中, 这一思想同样适用. 特别是当我们想要了解一个多元函数 (例如三维空间中的曲面) 在某一点附近的弯曲形状时, 多元函数的泰勒展开是不可或缺的.
> 更重要的是, 在人工智能中, 寻找损失函数的极小值往往依赖于多元泰勒展开提供的局部几何信息.

### 多元函数的泰勒展开公式

> [!important: 二元函数的泰勒公式]
>
> 设二元函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某一邻域内连续且有直到 $(n+1)$ 阶的连续偏导数. 为了方便, 我们记自变量的增量为 $h = x - x_0$, $k = y - y_0$.
> 则函数在该点附近的二阶泰勒展开式为:
> $$
> \begin{aligned}
> f(x, y) \approx f(x_0, y_0) &+ \underbrace{\left( h \frac{\partial f}{\partial x} + k \frac{\partial f}{\partial y} \right)}_{\text{一阶项 (线性逼近)}} \\
> &+ \underbrace{\frac{1}{2!} \left( h^2 \frac{\partial^2 f}{\partial x^2} + 2hk \frac{\partial^2 f}{\partial x \partial y} + k^2 \frac{\partial^2 f}{\partial y^2} \right)}_{\text{二阶项 (二次逼近)}}
> \end{aligned}
> $$
>
> 如果回顾前面的知识, 你会发现: **一阶项其实就是全微分 $df$ (几何上对应切平面), 而二阶项则描述了曲面偏离切平面的弯曲程度. **

> [!warning: 向量与矩阵形式 (极其重要! )]
>
> 当变量数量增多时, 写出一大堆偏导数是非常繁琐的. 在机器学习中, 我们通常将自变量写成向量 $\mathbf{x}$, 并将泰勒展开改写为极其优雅的**矩阵形式**.
> 设 $\mathbf{x} = (x, y)^T$, 增量 $\Delta \mathbf{x} = \mathbf{x} - \mathbf{x}_0 = (h, k)^T$.
>
> 1. **一阶导数向量**被称为**梯度 (Gradient)**: $\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)^T$
> 2. **二阶导数矩阵**被称为**海森矩阵 (Hessian Matrix)**: $\mathbf{H} = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix}$
>
> 于是, 多元函数的二阶泰勒展开可以紧凑地写为:
> $$
> f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T \Delta \mathbf{x} + \frac{1}{2} \Delta \mathbf{x}^T \mathbf{H} \Delta \mathbf{x}
> $$
> 这正是现代优化算法 (如牛顿法) 推导的起点!

### 多元函数泰勒展开的应用

> [!tip]
>
> 泰勒展开之所以重要, 是因为它能把复杂的非线性函数在局部"降维打击"成简单的多项式. 以下是它在数学理论与人工智能中的两个核心应用.

> [!important: 应用一: 证明极值的充分条件 (第二阶导数测试)]
>
> 在前面的章节中, 我们给出了判断多元函数极值的结论: 在驻点处 (即一阶偏导数 $f_x=0, f_y=0$), 若 $AC - B^2 > 0$ 且 $A > 0$, 则有极小值. 这个结论是怎么来的?
>
> **MIT 18.02 课程视角: **
> 我们可以用泰勒展开轻松证明它. 在驻点 $(x_0, y_0)$ 处, 梯度为零, 因此一阶项消失了. 函数值的变化量 $\Delta f = f(x, y) - f(x_0, y_0)$ 完全由**二阶项**主导:
> $$
> \Delta f \approx \frac{1}{2} \left( f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2 \right) = \frac{1}{2} \left( A h^2 + 2B hk + C k^2 \right)
> $$
> 这是一个关于 $h$ 和 $k$ 的二次型. 通过初等代数的配方, 我们可以将其改写为:
> $$
> \Delta f \approx \frac{1}{2A} \left[ (Ah + Bk)^2 + (AC - B^2)k^2 \right]
> $$
> 显然, 当 $AC - B^2 > 0$ 且 $A > 0$ 时, 无论 $h, k$ 取何值 (不全为零), 中括号内的值永远为正, 这意味着 $\Delta f > 0$ 恒成立. 因此函数值在这一点比周围都小, 这正是一个**局部极小值**!

> [!caution: 应用二: 神经网络训练中的局部二次近似 (Bishop 教材经典内容)]
>
> 在人工智能 (特别是深度学习) 中, 我们需要训练神经网络, 本质上就是寻找一组庞大的权重参数 $\mathbf{w}$, 使得误差函数 $E(\mathbf{w})$ 达到极小值.
>
> 根据 Bishop 的《Pattern Recognition and Machine Learning (PRML)》一书, 我们很难直接找到解析解, 而是必须在权重空间中进行迭代漫游: $\mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} + \Delta \mathbf{w}$.
>
> 为了决定往哪个方向走最好, 我们会利用泰勒展开对误差函数进行**局部二次近似 (Local quadratic approximation)**:
> $$
> E(\mathbf{w}) \simeq E(\mathbf{\hat{w}}) + (\mathbf{w}-\mathbf{\hat{w}})^T \mathbf{b} + \frac{1}{2} (\mathbf{w}-\mathbf{\hat{w}})^T \mathbf{H} (\mathbf{w}-\mathbf{\hat{w}})
> $$
> 其中 $\mathbf{b}$ 是误差梯度的向量, $\mathbf{H}$ 是海森矩阵.
>
> * 如果我们只看**一阶项 (梯度)**, 我们将得到**梯度下降法 (Gradient Descent)**, 指导我们沿着最陡峭的下坡方向前进.
> * 如果我们同时考虑**二阶项 (海森矩阵)**, 我们将得到**牛顿法 (Newton's Method)**. 海森矩阵包含了误差曲面的曲率信息 (比如这是一个尖锐的峡谷还是一个平缓的盆地), 它能告诉算法在不同方向上应该迈出多大的步子, 从而极大地加速神经网络的收敛过程!
