# 多元函数的积分

> [!tip]
>
> 在单变量积分中, 我们通过定积分研究了一个变量在区间上的累积问题, 例如曲线下的面积, 物体的位移等. 然而, 现实世界中的许多问题涉及多个变量的相互作用, 例如: 三维空间中不均匀物体的质量 (质量密度随位置变化), 平面区域上的温度分布平均值等. 这些问题要求我们将积分的概念从一维推广到高维空间. 重积分 (Multiple Integrals) 正是解决这类问题的核心工具. 本章将系统学习二重积分 (Double Integrals) 与三重积分 (Triple Integrals) 的定义, 计算方法及其应用.

## 二重积分

> [!tip]
>
> 跟单变量积分一样, 二重积分的本质仍然是“分割-近似-求和”的极限过程.


### 二重积分的概念

> [!tip]
>
> 我们要计算曲线 $y = f(x)$ 在区间 $[a, b]$ 下的面积, 可以通过以下步骤实现:
> 将区间 $[a, b]$ 等分为 $N$ 个子区间, 每个子区间的宽度为 $\displaystyle\Delta x = \frac{b-a}{N}$. 通过分割得到 $N$ 个窄矩形 (小柱体), 每个矩形的左端点或右端点记为 $x_i$ (例如 $x_i = a + i\Delta x$). 每个窄矩形的面积可近似为底边长度 $\Delta x$ 乘以高度 $f(x_i)$, 即第 $i$ 个矩形的面积为 $\Delta x \cdot f(x_i)$. 将所有窄矩形的面积相加, 得到总面积 $S_N$ 的近似值:
> $$
> \displaystyle S_N = \sum_{i=1}^N \Delta x \cdot f(x_i)
> $$
> 当 $N \to \infty$ (即子区间宽度 $\Delta x \to 0$) 时, 近似值 $S_N$ 趋近于精确面积 $S$:
> $$
> \displaystyle S = \lim_{N \to \infty} S_N = \lim_{\Delta x \to 0} S_N
> $$
> 最终, 面积 $S$ 可表示为定积分:
> $$
> S = \int_{a}^{b} f(x) \, \mathrm{d}x
> $$


> [!important: 多变量积分]
>
<div id="chpt11-double-integral" style="width:100%; height:440px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
<script type="module" src="threejs/chpt11-double-integral.js?v=1"></script>
>
> 如图所示, 对于定义在平面区域 $D$ 上的函数 $z = f(x,y)$, 若要计算其对应的体积或物理量 (如质量, 电荷量等), 其思想是单变量积分在二维空间的自然推广. 首先将积分区域 $D$ 分割为 $N$ 个面积微元 $\Delta A$, 每个微元可近似视为一个小矩形区域, 并选取其代表点 $(x_i, y_i)$ (例如取中心点或顶点坐标). 每个微元的体积可近似为底面积 $\Delta A$ 乘以高度 $f(x_i, y_i)$, 即 $\Delta A \cdot f(x_i, y_i)$. 将所有微元的贡献叠加, 得到近似总体积:
> $$
> \displaystyle V_N = \sum_{i=1}^N \Delta A \cdot f(x_i, y_i)
> $$
> 当分割无限细化 (即 $N \to \infty$, 且每个微元面积 $\Delta A \to 0$) 时, 近似值趋于精确值:
> $$
> \displaystyle V = \lim_{N \to \infty} V_N = \lim_{\Delta A \to 0}V_N
> $$
> 这一极限过程即为二重积分的定义, 可表示为:
> $$
> V = \iint_{D} f(x,y) \, \mathrm{d}A
> $$
> 其中 $D$ 是积分区域, $f(x,y)$ 为被积函数, $\mathrm{d}A$ 为面积元 (直角坐标系中通常写作 $\mathrm{d}x\mathrm{d}y$).
>
> **如何计算?**
> [图略, 待补充]
> $$
> \displaystyle M=\sum_{i=1}^N \rho (x_i,y_i)\mathrm{d}A_i=\iint_D \rho(x,y)\mathrm{d}A
> $$

### 二重积分的计算

> [!tip: 例1 与 例2 的几何意义]
>
> 下面两图对应本节的 **例1** 与 **例2**, 两者的被积函数都是抛物面 $z = 1 - x^2 - y^2$, 唯一区别在于积分区域 $D$:
>
> - **左图 (例1)** $D = [0,1]\times[0,1]$ 是单位正方形. 抛物面在 $x^2+y^2 < 1$ 处取正值 (<span style="color: #15803d">绿色</span>), 在靠近角点 $(1,1)$ 的区域取负值 (<span style="color: #b91c1c">红色</span>). 因此 $\displaystyle\iint_D (1-x^2-y^2)\,dA = \tfrac{1}{3}$ 代表的是**带符号的体积**: 绿色部分算作正贡献, 红色部分算作负贡献, 两者相抵后的净值.
> - **右图 (例2)** $D$ 是第一象限的单位圆盘 $\{x^2+y^2\le 1, x,y\ge 0\}$, 恰好是抛物面保持非负的最大区域. 此时 $\displaystyle\iint_D (1-x^2-y^2)\,dA = \tfrac{\pi}{8}$ 就是**纯粹的体积**: 以四分之一圆盘为底, 以抛物面为顶盖所围成的立体的体积.
>
> 对比两图可以看到: 相同的被积函数配合不同的积分区域, 几何意义会从“抵消后的净体积”变为“完整的立体体积”——这正是选择合适的 $D$ (以及合适的坐标系) 在重积分计算中的关键作用.

<div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.2em 0;">
 <div id="chpt11-example1" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
 <div id="chpt11-example2" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
</div>
<script type="module" src="threejs/chpt11-example1.js?v=1"></script>
<script type="module" src="threejs/chpt11-example2.js?v=1"></script>

::: {.exercise id="chpt11-ex-001"}
:::

::: {.exercise id="chpt11-ex-002"}
:::

::: {.exercise id="chpt11-ex-003"}
:::

::: {.exercise id="chpt11-ex-004"}
:::

::: {.exercise id="chpt11-ex-012"}
:::

## 多变量积分的换元法

> [!important: 变量替换与雅可比行列式]
>
> 考虑坐标变换 $\begin{cases} u = u(x,y) \\ v = v(x,y) \end{cases}$, 其全微分形式可表示为:
> $$
> \begin{cases} 
> \mathrm{d}u = \frac{\partial u}{\partial x}\mathrm{d}x + \frac{\partial u}{\partial y}\mathrm{d}y \\ 
> \mathrm{d}v = \frac{\partial v}{\partial x}\mathrm{d}x + \frac{\partial v}{\partial y}\mathrm{d}y 
> \end{cases}
> $$
> 该微分系统可写成矩阵形式:
> $$
> \begin{bmatrix}
> \mathrm{d}u \\
> \mathrm{d}v
> \end{bmatrix} = 
> \begin{bmatrix}
> \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
> \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
> \end{bmatrix}
> \begin{bmatrix}
> \mathrm{d}x \\
> \mathrm{d}y
> \end{bmatrix}
> $$
> [图略, 待补充]
> $$
> \mathrm{d}u\mathrm{d}v = \left|\frac{\partial (u,v)}{\partial (x,y)}\right|\mathrm{d}x\mathrm{d}y =
> \left|\begin{vmatrix}
> \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y}\\
> \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
> \end{vmatrix}\right|\mathrm{d}x\mathrm{d}y = \left|\frac{\partial u}{\partial x}\frac{\partial v}{\partial y}-\frac{\partial u}{\partial y}\frac{\partial v}{\partial x}\right|\mathrm{d}x\mathrm{d}y
> $$

<div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.2em 0;">
 <div id="chpt11-jacobian-uv" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
 <div id="chpt11-jacobian-xy" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
</div>
<script type="module" src="threejs/chpt11-jacobian.js?v=1"></script>

*图: 线性变换 $\varphi(u,v) = (1.2u + 0.6v,\; 0.4u + 1.3v)$ 把 $(u,v)$-平面的单位正方形网格映射为 $(x,y)$-平面的平行四边形网格. 每个小格的面积都被放大为原来的 $|J| = 1.32$ 倍. 两个彩色向量是像 $\partial\varphi/\partial u$, $\partial\varphi/\partial v$, 它们正是所得平行四边形的两条边.*

> [!important: 雅可比行列式与坐标变换的深层关系]
>
> 在坐标变换 $(x,y) \leftrightarrow (u,v)$ 中, 雅可比行列式不仅描述面积元的缩放比例, 更揭示了双向变换的对称性. 由基本关系:
> $$
> \mathrm{d}u\mathrm{d}v=\left|J\right|\mathrm{d}x\mathrm{d}y=\left|\frac{\partial (u,v)}{\partial (x,y)}\right|\mathrm{d}x\mathrm{d}y
> $$
> 通过反函数定理, 可得逆变换关系:
> $$
> \mathrm{d}x\mathrm{d}y=\left|\frac{\partial (x,y)}{\partial (u,v)}\right|\mathrm{d}u\mathrm{d}v
> $$
> 这建立了双向变换的精确对应: 雅可比行列式互为倒数, 即:
> $$
> \left| \frac{\partial (x,y)}{\partial (u,v)} \right| = \left| \frac{\partial (u,v)}{\partial (x,y)} \right|^{-1}
> $$
> **经典示例: 极坐标变换**
> 对极坐标变换 $\begin{cases} x = \rho \cos\theta \\ y = \rho \sin\theta \end{cases}$, 其雅可比矩阵为:
> $$
> J(\rho ,\theta)=\frac{\partial (x,y)}{\partial (\rho ,\theta)}=
> \begin{vmatrix}
> \frac{\partial x}{\partial \rho } & \frac{\partial x}{\partial \theta}\\
> \frac{\partial y}{\partial \rho } & \frac{\partial y}{\partial \theta}
> \end{vmatrix}=
> \begin{vmatrix}
> \cos\theta & -\rho \sin\theta\\
> \sin\theta & \rho \cos\theta
> \end{vmatrix} = \rho
> $$
> 因此面积元变换为:
> $$
> \mathrm{d}x\mathrm{d}y = \left|\rho\right| \mathrm{d}\rho\mathrm{d}\theta = \rho \mathrm{d}\rho\mathrm{d}\theta
> $$
> **矩阵互逆性的几何诠释**
> 变换矩阵的互逆性直接体现在坐标系转换中:
> $$
> \begin{bmatrix}
> \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
> \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
> \end{bmatrix}
> \quad\text{与}\quad
> \begin{bmatrix}
> \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
> \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
> \end{bmatrix}
> $$
> 这两个雅可比矩阵的乘积为单位矩阵, 其行列式乘积为1. 例如当 $J_{uv} = 5$ 时, 逆变换的行列式为 $\displaystyle\frac{1}{5}$, 此时:
> $$
> \mathrm{d}x\mathrm{d}y = \frac{1}{5} \mathrm{d}u\mathrm{d}v
> $$
> 这种精确的倒数关系确保了积分在不同坐标系下计算结果的一致性, 是多重积分变量替换定理的核心数学基础.

<div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.2em 0;">
 <div id="chpt11-polar-rtheta" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
 <div id="chpt11-polar-xy" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
</div>
<script type="module" src="threejs/chpt11-polar-change.js?v=1"></script>

*图: 极坐标变换 $(r,\theta)\mapsto (r\cos\theta,\, r\sin\theta)$. 左侧 $(r,\theta)$-矩形 $[0,1]\times[0,\pi/2]$ 被等分为 $5\times 6$ 个同样大小的小矩形; 右侧映射为四分之一圆盘的极坐标网格. 每个"小矩形"的面积是 $dr\,d\theta$; 其像的面积约为 $r\,dr\,d\theta$, 因此靠近 $r=0$ 的格子变得很小, 靠近 $r=1$ 的格子最大——这正是雅可比行列式 $|J| = r$ 的几何含义.*

::: {.exercise id="chpt11-ex-013"}
:::

## 重积分的应用

> [!important: 质量]
>
> 对于分布在平面区域 $D$ 上的物体 (如薄片), 若其密度函数为 $\rho(x,y)$, 则总质量可通过二重积分计算:
> $$
> M = \iint_D \rho(x,y) \, \mathrm{d}\sigma
> $$
> 其中 $\mathrm{d}\sigma$ 表示面积元 (即直角坐标系中的 $\mathrm{d}x\mathrm{d}y$). 当密度均匀时 ($\rho$ 为常数), 总质量退化为密度与面积的乘积 $M = \rho \cdot A$, 其中 $\displaystyle A = \iint_D \mathrm{d}\sigma$ 为区域 $D$ 的面积.
>
> **质心**
>
> 质心是物体质量分布的加权平均位置. 对于离散质点系, 质心坐标 $(\bar{x}, \bar{y})$ 定义为:
> $$
> \displaystyle \bar{x} = \frac{\sum_{i=1}^n m_i x_i}{\sum_{i=1}^n m_i}, \quad \bar{y} = \frac{\sum_{i=1}^n m_i y_i}{\sum_{i=1}^n m_i}
> $$
> 将其推广到连续情形, 则质心坐标通过二重积分表达. 当密度函数为 $\mu(x,y)$ 时:
> $$
> \displaystyle \bar{x} = \frac{\iint_D x \mu(x,y) \, \mathrm{d}\sigma}{\iint_D \mu(x,y) \, \mathrm{d}\sigma}, \quad \bar{y} = \frac{\iint_D y \mu(x,y) \, \mathrm{d}\sigma}{\iint_D \mu(x,y) \, \mathrm{d}\sigma}
> $$

::: {.exercise id="chpt11-ex-005"}
:::

::: {.exercise id="chpt11-ex-006"}
:::


> [!warning: 转动惯量与质心的关系(不要求)]
>
> 对于平面区域 $D$ 上的质量分布, 若密度函数为 $\mu(x,y)$, 则系统对某点 $(x_0, y_0)$ 的转动惯量为:
> $$
> I(x_0, y_0) = \iint_D \mu(x,y) \left[ (x-x_0)^2 + (y-y_0)^2 \right] \mathrm{d}x\mathrm{d}y
> $$
> 此式可视为质量元 $\mu(x,y)\mathrm{d}x\mathrm{d}y$ 到参考点距离平方的加权积分. 特别地, 当参考点为原点时, 转动惯量简化为:
> $$
> I = \iint_D \mu(x,y) r^2(x,y) \mathrm{d}x\mathrm{d}y \quad (r^2 = x^2 + y^2)
> $$
>
> **质心的极值特性**:
> 质心具有重要物理性质: 它是使系统转动惯量取极小值的位置. 为证明这一点, 对 $I(x_0, y_0)$ 分别关于 $x_0, y_0$ 求偏导并令其为零:
> $$
> \frac{\partial I}{\partial x_0} = \iint_D 2\mu(x,y)(x_0 - x)\mathrm{d}x\mathrm{d}y = 0 \\
> \frac{\partial I}{\partial y_0} = \iint_D 2\mu(x,y)(y_0 - y)\mathrm{d}x\mathrm{d}y = 0
> $$
> 由此可得方程组:
> $$
> x_0 \iint_D \mu\mathrm{d}x\mathrm{d}y = \iint_D \mu x\mathrm{d}x\mathrm{d}y \\
> y_0 \iint_D \mu\mathrm{d}x\mathrm{d}y = \iint_D \mu y\mathrm{d}x\mathrm{d}y
> $$
> 最终解得质心坐标为:
> $$
> \displaystyle x_0 = \frac{\iint_D \mu x\mathrm{d}x\mathrm{d}y}{\iint_D \mu\mathrm{d}x\mathrm{d}y}, \quad 
> y_0 = \frac{\iint_D \mu y\mathrm{d}x\mathrm{d}y}{\iint_D \mu\mathrm{d}x\mathrm{d}y}
> $$
> 这与离散质点系的质心公式一致:
> $$
> \displaystyle \begin{cases}
> x_0 = \frac{\sum m_i x_i}{\sum m_i} & \text{（质量加权平均）} \\
> y_0 = \frac{\sum m_i y_i}{\sum m_i} & \text{（质量加权平均）}
> \end{cases}
> $$


> [!warning: 平行轴定理]
>
> 平行轴定理揭示了物体绕不同轴转动惯量之间的关系: **绕任意轴的转动惯量等于绕质心轴的转动惯量加上总质量与该轴到质心距离平方的乘积**. 其数学推导可通过二重积分展开:
>
> 设质心坐标为 $(x_c, y_c)$, 绕点 $(x_0, y_0)$ 的转动惯量为:
> $$
> \begin{aligned}
> I(x_0,y_0) &= \iint_D \mu \left[ (x-x_0)^2 + (y-y_0)^2 \right] \mathrm{d}x\mathrm{d}y \\
> &= \iint_D \mu \left[ (x-x_c + x_c - x_0)^2 + (y-y_c + y_c - y_0)^2 \right] \mathrm{d}x\mathrm{d}y 
> \end{aligned}
> $$
>
> 展开平方项并重组积分:
> $$
> \begin{aligned}
> &= \underbrace{\iint_D \mu \left[ (x-x_c)^2 + (y-y_c)^2 \right] \mathrm{d}x\mathrm{d}y}_{I_c \ (\text{绕质心的转动惯量})} \\
> &\quad + \underbrace{\iint_D \mu \left[ (x_c - x_0)^2 + (y_c - y_0)^2 \right] \mathrm{d}x\mathrm{d}y}_{M r^2 \ (\text{总质量} \times \text{距离平方})} \\
> &\quad + 2(x_c - x_0)\underbrace{\iint_D \mu (x - x_c) \mathrm{d}x\mathrm{d}y}_{0 \ (\text{质心定义})} \\
> &\quad + 2(y_c - y_0)\underbrace{\iint_D \mu (y - y_c) \mathrm{d}x\mathrm{d}y}_{0 \ (\text{质心定义})}
> \end{aligned}
> $$
>
> 关键消去项: 根据质心坐标的定义 $\displaystyle x_c = \frac{1}{M}\iint_D \mu x \mathrm{d}x\mathrm{d}y$, 交叉项中的积分 $\displaystyle\iint_D \mu(x - x_c)\mathrm{d}x\mathrm{d}y$ 和 $\displaystyle\iint_D \mu(y - y_c)\mathrm{d}x\mathrm{d}y$ 必然为零. 最终得到简洁形式:
> $$
> I(x_0, y_0) = I_c + M r^2
> $$
> 其中 $r = \sqrt{(x_c - x_0)^2 + (y_c - y_0)^2}$ 为两轴间距离, $\displaystyle M = \iint_D \mu \mathrm{d}x\mathrm{d}y$ 为总质量.





::: {.exercise id="chpt11-ex-007"}
:::

::: {.exercise id="chpt11-ex-008"}
:::



::: {.exercise id="chpt11-ex-009"}
:::


## 三重积分

::: {.exercise id="chpt11-ex-010"}
:::

::: {.exercise id="chpt11-ex-011"}
:::

<div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.2em 0;">
 <div id="chpt11-example12" style="flex:1 1 320px; min-width:300px; height:400px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
 <div id="chpt11-example13" style="flex:1 1 320px; min-width:300px; height:400px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
</div>
<script type="module" src="threejs/chpt11-example12.js?v=2"></script>
<script type="module" src="threejs/chpt11-example13.js?v=2"></script>
