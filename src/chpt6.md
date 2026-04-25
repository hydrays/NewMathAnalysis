# 积分的应用

## 几何应用: 求体积与弧长

### 微元法思想

> [!tip]
>
> 微元法是积分学中解决几何与物理问题的核心思想, 它将复杂的整体问题分解为无穷多个简单的局部问题.
>
> **基本思路**:
>
> 1. **分割**: 将所求的整体量对应的区域分割成许多微小部分
> 2. **近似**: 在每个微小部分上, 用简单的几何量近似代替复杂的实际量
> 3. **求和取极限**: 将所有微小部分的近似值相加, 然后通过取极限得到精确值
>

> [!important: 微元法数学表述]
>
> 如果要求整体量 $Q$, 先找出微元 $dQ = f(x)dx$, 然后通过积分得到
> $$
> Q = \int_a^b dQ = \int_a^b f(x)dx
> $$

::: {.exercise id="chpt6-ex-017"}
:::


### 体积的计算

::: {.exercise id="chpt6-ex-001"}
:::



::: {.exercise id="chpt6-ex-002"}
:::

> [!important]
>
> 曲线 $y = f(x)$ 绕 $x$ 轴旋转一周形成的旋转体体积:
> $$
> V = \int_a^b \pi [f(x)]^2 dx
> $$
>
> **推导**: 在 $x$ 处垂直于 $x$ 轴的截面是半径为 $f(x)$ 的圆盘, 面积 $A(x) = \pi [f(x)]^2$

::: {.exercise id="chpt6-ex-003"}
:::


> [!important]
>
> 曲线 $y = f(x)$ 绕 $y$ 轴旋转一周形成的旋转体体积:
> $$
> V = \int_a^b 2\pi x f(x) dx
> $$
>
> **推导**: 在 $x$ 处厚度为 $dx$ 的柱壳体积微元 $dV = 2\pi x \cdot f(x) \cdot dx$
>

::: {.exercise id="chpt6-ex-004"}
:::


### 曲线弧长

> [!important: 直角坐标系下的弧长]
>
> 曲线 $y = f(x)$ 在 $[a,b]$ 上的弧长:
> $$
> L = \int_a^b \sqrt{1 + [f'(x)]^2}  dx
> $$
>
> **推导**: 弧长微元 $ds = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx$

::: {.exercise id="chpt6-ex-005"}
:::

> [!important: 参数方程下的弧长]
>
> 曲线由参数方程 $x = x(t), y = y(t)$ ($\alpha \leq t \leq \beta$) 给出时, 弧长为:
> $$
> L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}  dt
> $$

::: {.exercise id="chpt6-ex-006"}
:::


> [!important: 极坐标下的弧长]
>
> 曲线由极坐标方程 $r = r(\theta)$ ($\alpha \leq \theta \leq \beta$) 给出时, 弧长为:
> $$
> L = \int_\alpha^\beta \sqrt{[r(\theta)]^2 + \left[\frac{dr}{d\theta}\right]^2}  d\theta
> $$
>
> **推导**: 利用直角坐标与极坐标的关系 $x = r\cos\theta, y = r\sin\theta$, 代入参数方程的弧长公式可得.

::: {.exercise id="chpt6-ex-007"}
:::

## 物理中的应用: 功与能量

>
> 在物理学中, 力沿路径做的功定义为力与位移的乘积. 当力是变力时, 需要用积分计算.
>

### 有限区域内的变力做功

::: {.exercise id="chpt6-ex-008"}
:::


::: {.exercise id="chpt6-ex-009"}
:::

### 无穷区域上的做功问题

::: {.exercise id="chpt6-ex-010"}
:::

> [!warning: 无界函数的积分]
>
> 当被积函数在积分区间内无界时, 也需要通过极限来定义积分.

::: {.exercise id="chpt6-ex-011"}
:::

## 概率中的应用

> [!tip]
>
> 积分学在概率论中扮演着核心角色, 特别是在处理连续型随机变量时. 本节将介绍如何用积分来描述和分析连续随机现象. 掌握积分在概率中的应用, 不仅是学习概率论的基础, 也是理解现代统计学, 金融工程等领域的必备工具.


> [!important: 概率密度函数]
>
> 对于连续型随机变量, 我们不能像离散情况那样谈论某个具体值的概率, 而是使用概率密度函数来描述概率分布.
>
> **定义**:
> 如果存在非负函数 $f(x)$, 使得对任意实数 $a \leq b$, 随机变量 $X$ 落在区间 $[a,b]$ 内的概率为
> $$
> P(a \leq X \leq b) = \int_a^b f(x)  dx
> $$
> 则称 $f(x)$ 为 $X$ 的概率密度函数.
>
> **性质**:
> 1. 非负性: $f(x) \geq 0$ 对所有 $x$ 成立
> 2. 归一性: $\displaystyle\int_{-\infty}^\infty f(x)  dx = 1$
>

::: {.exercise id="chpt6-ex-012"}
:::

> [!important: 均匀分布]
>
> 均匀分布描述了一个随机变量在某个区间内等可能取值的现象.
>
> **定义**:
> 如果随机变量 $X$ 在区间 $[a,b]$ 上有概率密度函数
> $$
> f(x) = \begin{cases}
> \frac{1}{b-a} & a \leq x \leq b \\
> 0 & \text{其他}
> \end{cases}
> $$
> 则称 $X$ 服从均匀分布, 记作 $X \sim U(a,b)$.
>

::: {.exercise id="chpt6-ex-013"}
:::


> [!important: 指数分布]
>
> 指数分布常用于描述等待时间, 寿命等随机现象.
>
> **定义**:
> 如果随机变量 $X$ 有概率密度函数
> $$
> f(x) = \begin{cases}
> \lambda e^{-\lambda x} & x \geq 0 \\
> 0 & x < 0
> \end{cases}
> $$
> 其中 $\lambda > 0$, 则称 $X$ 服从参数为 $\lambda$ 的指数分布.

::: {.exercise id="chpt6-ex-014"}
:::


> [!important: 正态分布]
>
> 正态分布 (高斯分布) 是概率论与统计学中最重要的分布, 它描述了自然界中大量随机现象的分布规律.
>
> **定义**:
> 如果随机变量 $X$ 有概率密度函数
> $$
> f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
> $$
> 则称 $X$ 服从正态分布, 记作 $X \sim N(\mu,\sigma^2)$.
>
> **参数意义**:
> - $\mu$: 均值, 决定分布的中心位置
> - $\sigma$: 标准差, 决定分布的分散程度
>
> **标准正态分布**:
> 当 $\mu = 0$, $\sigma = 1$ 时, 称为标准正态分布, 其概率密度函数为
> $$
> \varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
> $$
>
> **概率计算**:
> 对于 $X \sim N(\mu,\sigma^2)$, $P(a \leq X \leq b) = \displaystyle\int_a^b \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}  dx$
>
> 这个积分没有初等函数形式的原函数, 谜底留到第二册.


## 反常积分

> [!tip]
>
> 反常积分处理两类问题: 无穷区间上的积分和无界函数的积分.

> [!important: 无穷区间上的反常积分]
>
> **定义**:
> 1. $\displaystyle\int_a^\infty f(x)  dx = \lim_{b \to \infty} \int_a^b f(x)  dx$
> 2. $\displaystyle\int_{-\infty}^b f(x)  dx = \lim_{a \to -\infty} \int_a^b f(x)  dx$
> 3. $\displaystyle\int_{-\infty}^\infty f(x)  dx = \int_{-\infty}^c f(x)  dx + \int_c^\infty f(x)  dx$ ($c$ 为任意实数)
>
> **收敛判别**:
> 如果极限存在且有限, 则称反常积分收敛; 否则称发散.

::: {.exercise id="chpt6-ex-015"}
:::

> [!important: 无界函数的反常积分 (瑕积分)]
>
> 如果函数 $f(x)$ 在点 $c$ 的任意邻域内无界, 则称 $c$ 为瑕点.
>
> **定义**:
> 1. 若 $f(x)$ 在 $[a,b)$ 上连续, 且 $\lim_{x \to b^-} f(x) = \infty$, 则
> $$
>    \int_a^b f(x)  dx = \lim_{t \to b^-} \int_a^t f(x)  dx
>    $$
>
> 2. 若 $f(x)$ 在 $(a,b]$ 上连续, 且 $\lim_{x \to a^+} f(x) = \infty$, 则
> $$
>    \int_a^b f(x)  dx = \lim_{t \to a^+} \int_t^b f(x)  dx
>    $$
>
> 3. 若 $c \in (a,b)$ 是瑕点, 则
> $$
>    \int_a^b f(x)  dx = \int_a^c f(x)  dx + \int_c^b f(x)  dx
>    $$

::: {.exercise id="chpt6-ex-016"}
:::
