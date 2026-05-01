# 偏微分方程

> [!tip: 章引言]
>
> 第七章的常微分方程 (ODE) 描述只依赖**一个自变量** (如时间 $t$) 的未知函数. 但现实中很多对象同时随时间和空间变化 —— 房间里的温度 $u(x,y,z,t)$, 水波 $u(x,t)$, 电磁场, 甚至现代 AI 中的扩散模型. 包含未知**多元函数及其偏导数**的方程称为**偏微分方程 (PDE)**.
>
> 本章以最具代表性的方程 ——**拉普拉斯方程 $\Delta u = 0$** 为主线: 它的物理来源 (热传导稳态)、解析解法 (分离变量、傅里叶变换)、数值解法 (有限差分), 以及它在 AI 图像处理里的"另一面身份".

## 14.1 偏微分方程的概念与经典模型

> [!important: 模型 — 热传导方程]
>
> 设 $u(x, y, z, t)$ 表示空间点 $(x, y, z)$ 在时刻 $t$ 的温度. 由傅里叶热传导定律与能量守恒, 温度随时间的变化率正比于该点的**二阶空间偏导之和**:
> $$
> \frac{\partial u}{\partial t} = \alpha\left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right),
> $$
> 其中常数 $\alpha > 0$ 称为**热导率**, 决定了热量在介质中传播的快慢.
>
> 等式右端的算子在数学上有专用记号 —— **拉普拉斯算子**:
> $$
> \Delta u := \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}.
> $$
> 故热传导方程可简写为 $\displaystyle \frac{\partial u}{\partial t} = \alpha \Delta u$.
>
> > <div id="chpt14-heat" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt14-heat.js?v=1"></script>
>
> 上图是一维热传导方程 $u_t = u_{xx}$ 在 $[0, \pi]$ 上、两端固定为零的演化过程. 初始分布 (浅蓝虚线) 取四个正弦模式的混合: $u(x, 0) = 0.6\sin x + 0.5 \sin 3x - 0.4 \sin 7x + 0.3 \sin 11x$, 故弯弯曲曲. 解析解 $u(x, t) = \sum b_n \sin(nx) e^{-n^2 t}$ 显示**第 $n$ 个频率以速率 $n^2$ 衰减** —— $n = 11$ 项的衰减是 $n = 1$ 项的 121 倍! 拖动滑块 $t$, 高频成分先消失, 曲线先变光滑, 再整体衰减为零稳态. 这就是热传导方程"平滑作用"的几何画面.

> [!tip: 从热传导走向拉普拉斯方程]
>
> 若房间的边界保持恒定温度分布, 经过足够长时间后房间内的温度趋于**稳态** —— 温度不再随时间变化, $\partial u/\partial t = 0$. 此时热传导方程退化为一个纯空间方程
> $$
> \Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} = 0,
> $$
> 这就是著名的**拉普拉斯方程**. 满足它的函数称为**调和函数 (harmonic function)**.

> [!note: 例 — 两个调和函数]
>
> 1. **二维对数函数**: $u(x, y) = \ln\sqrt{x^2 + y^2}$ 满足 $u_{xx} + u_{yy} = 0$ (在原点外). 直接求两次偏导即可验证, 这是后面"圆对称解"的关键基函数.
> 2. **三维 Newton 势 / 静电势**: $\displaystyle u(x, y, z) = \frac{1}{\sqrt{x^2 + y^2 + z^2}}$ 在原点外满足 $\Delta u = 0$. 引力与库仑力的势函数全是这一形式, 其物理重要性源于"调和"性.

## 14.2 拉普拉斯方程的解析解法

> [!tip: 解析方法的核心思想 —— 降维]
>
> PDE 比 ODE 难得多. 数学家们发明了很多精妙的技巧, 共同的核心是**"降维"** —— 把多元偏微分方程化归为一元常微分方程. 本节给出两种经典工具: **分离变量法** (圆形区域, 配合极坐标) 与**傅里叶变换法** (无界区域, 把 $\partial/\partial x$ 变成代数乘法).

### 14.2.1 拉普拉斯算子在极坐标下的形式

> [!important: 定理 — 极坐标下的拉普拉斯算子]
>
> 二维直角坐标到极坐标 $x = r\cos\theta,\ y = r\sin\theta$ 的变换下, 二维拉普拉斯算子有如下形式 ($r > 0$):
> $$
> \boxed{\;\Delta u = \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}\;}
> $$
> 这一形式在所有"圆对称"或"圆盘内"的问题里都是首选 —— 角向变量 $\theta$ 自然以 $2\pi$ 为周期, 直接提示我们对其用傅里叶展开.
>
> ::: {.fold label="详细推导 (链式法则四步)"}
> **第一步: $r, \theta$ 对 $x, y$ 的偏导数.**
>
> 由 $r = \sqrt{x^2 + y^2}$ 和 $\theta = \arctan(y/x)$:
> $$
> r_x = \frac{x}{r} = \cos\theta, \qquad r_y = \frac{y}{r} = \sin\theta,
> $$
> $$
> \theta_x = -\frac{y}{x^2 + y^2} = -\frac{\sin\theta}{r}, \qquad \theta_y = \frac{x}{x^2 + y^2} = \frac{\cos\theta}{r}.
> $$
>
> **第二步: 一阶导数.**
>
> 由复合函数链式法则,
> $$
> u_x = u_r r_x + u_\theta \theta_x = \cos\theta\,u_r - \frac{\sin\theta}{r}u_\theta,
> $$
> $$
> u_y = u_r r_y + u_\theta \theta_y = \sin\theta\,u_r + \frac{\cos\theta}{r}u_\theta.
> $$
> 即微分算子本身可写为
> $$
> \frac{\partial}{\partial x} = \cos\theta\,\frac{\partial}{\partial r} - \frac{\sin\theta}{r}\frac{\partial}{\partial \theta}, \quad
> \frac{\partial}{\partial y} = \sin\theta\,\frac{\partial}{\partial r} + \frac{\cos\theta}{r}\frac{\partial}{\partial \theta}.
> $$
>
> **第三步: 二阶导数 $u_{xx}, u_{yy}$.**
>
> $u_{xx} = \dfrac{\partial}{\partial x}\!\left(\cos\theta\,u_r - \dfrac{\sin\theta}{r}u_\theta\right)$, 把 $\partial/\partial x$ 算子代入展开 (两部分逐项):
> $$
> u_{xx} = \cos^2\theta\, u_{rr} + \frac{\sin^2\theta}{r}u_r + \frac{\sin^2\theta}{r^2}u_{\theta\theta} - \frac{2\sin\theta\cos\theta}{r}u_{r\theta} + \frac{2\sin\theta\cos\theta}{r^2}u_\theta.
> $$
> 同理,
> $$
> u_{yy} = \sin^2\theta\, u_{rr} + \frac{\cos^2\theta}{r}u_r + \frac{\cos^2\theta}{r^2}u_{\theta\theta} + \frac{2\sin\theta\cos\theta}{r}u_{r\theta} - \frac{2\sin\theta\cos\theta}{r^2}u_\theta.
> $$
>
> **第四步: 相加.** 混合项 $\pm 2\sin\theta\cos\theta\,u_{r\theta}/r$ 与一阶角向项 $\pm 2\sin\theta\cos\theta\,u_\theta/r^2$ 恰好成对相消; 余下用 $\sin^2\theta + \cos^2\theta = 1$ 化简, 得
> $$
> \Delta u = u_{xx} + u_{yy} = u_{rr} + \frac{1}{r}u_r + \frac{1}{r^2}u_{\theta\theta}. \qquad \blacksquare
> $$
> :::

> [!important: 方法 1 — 极坐标下的分离变量法]
>
> 在圆盘内求解 $\Delta u = 0$ 时, 极坐标形式让边界条件 (圆周) 变得简单. 大胆设
> $$ u(r, \theta) = R(r)\, \Theta(\theta), $$
> 把它代入极坐标 Laplace 方程并整理, 等式两边一边只依赖 $r$、一边只依赖 $\theta$, 必都等于同一个常数 $\lambda$:
> $$
> \frac{r^2 R'' + r R'}{R} = -\frac{\Theta''}{\Theta} = \lambda.
> $$
> 一个 PDE 被"撕"成了两个 ODE. 其中关于 $\Theta$ 的方程 $\Theta'' + \lambda \Theta = 0$ 加上 "$\Theta$ 必须以 $2\pi$ 为周期" 的边界条件, 自然挑出 $\lambda = n^2$ 与正余弦解 $\cos(n\theta), \sin(n\theta)$. 最终所有分离解的叠加恰好就是 §13.4 学过的**傅里叶级数**.
>
> > <div id="chpt14-disk-harmonic" style="width:100%; height:520px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt14-disk-harmonic.js?v=1"></script>
>
> 上图把分离变量法的结论可视化: 在单位圆盘上指定一个边界函数 $f(\theta)$ (按钮可切换为**阶跃**, **余弦**, **三角脉冲**), 内部的调和延拓
> $$ u(r, \theta) = \frac{a_0}{2} + \sum_{n=1}^{N} r^n \bigl(a_n \cos n\theta + b_n \sin n\theta\bigr) $$
> 用 viridis 色谱画在圆盘中. 圆周上的薄环显示边界值 $f(\theta)$. 拖动 $N$, 看高频项如何对边界细节产生贡献. 注意三件事:
>
> - **中心值** $u(0, 0) = a_0/2$ 永远等于边界平均值 (调和函数的均值性质);
> - **越靠近中心 $u$ 越光滑** —— $r^n$ 因子把高频压低, 离边界越远越平缓;
> - 即使 $f$ 是阶跃 (不连续), 内部仍是处处光滑的调和函数, 边界附近会有 Gibbs-style 振荡.

> [!important: 方法 2 — 傅里叶变换法 (无界区域)]
>
> 当区域是无限大 (例如整个上半平面), 直接对 PDE 两边做**傅里叶变换** $\mathcal{F}$. 关键性质: 时空域的求导, 在频域里变成代数乘法,
> $$
> \mathcal{F}\!\left[\frac{\partial^2 u}{\partial x^2}\right] = (i\omega)^2\,U(\omega, y) = -\omega^2\, U(\omega, y).
> $$
> 对方程 $u_{xx} + u_{yy} = 0$ 关于 $x$ 取变换后,
> $$
> -\omega^2\, U(\omega, y) + \frac{d^2 U}{dy^2} = 0.
> $$
> 一个含两个变量的 PDE 瞬间变成关于 $y$ 的 ODE, 解为
> $$
> U(\omega, y) = A(\omega)\, e^{-|\omega| y} + B(\omega)\, e^{|\omega| y}.
> $$
> 配合"$y \to \infty$ 时解有界"等条件定 $A, B$, 再做一次逆变换即得原方程的解析解. **求导 → 代数乘法**, 这是现代 PDE 理论中最有力的降维武器.

## 14.3 偏微分方程的数值方法与 AI 视角

> [!tip: 为什么需要数值方法]
>
> 实际工程问题 (复杂形状的发动机散热、航天器流场、地震波传播…) 几乎不可能求出解析解 —— 边界条件太复杂、几何形状不规则. 这时只能借助计算机的**数值方法**给出近似解, 同时控制误差到可接受的范围.

> [!important: 数值方法 — 有限差分法 (FDM)]
>
> 第八章介绍过用**中心差商**近似二阶导数:
> $$ f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2}. $$
> 在二维网格 (步长 $h$) 上, 二阶偏导数离散化为
> $$
> u_{xx} \approx \frac{u(x+h, y) - 2u(x, y) + u(x-h, y)}{h^2}, \quad
> u_{yy} \approx \frac{u(x, y+h) - 2u(x, y) + u(x, y-h)}{h^2}.
> $$
> 相加并代入 $\Delta u = 0$, 一行代数整理后得到
> $$
> \boxed{\;u(x, y) \approx \frac{u(x+h, y) + u(x-h, y) + u(x, y+h) + u(x, y-h)}{4}.\;}
> $$
> **物理意义**: 在拉普拉斯方程的稳态下, 任意一点的温度 (势函数值) 恰好是其上下左右四个邻居的**平均值**. 计算机只需在网格上反复迭代这个等式 (Jacobi/Gauss–Seidel 等), 整个区域的解便逐渐收敛.
>
> > <div id="chpt14-jacobi" style="width:100%; height:520px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt14-jacobi.js?v=1"></script>
>
> 上图是 $60 \times 60$ 网格上的 Jacobi 迭代. 边界四条边给定温度模式 (顶部一段正弦弧, 左右两边线性渐变, 底部为零), 内部初始全设为 $0.5$ (色谱中段). 拖动滑块或点击**▶播放**可看到迭代如何把这种"中性的中间状态"逐渐压平成一张光滑的调和曲面. **每一步, 每个内部格点取上下左右四邻居的平均** —— 仅此一条规则, 计算机就把边界的影响一层层"渗透"到中心. 右下显示 $\|u^{(k)} - u^{(k-1)}\|_\infty$, 它指数衰减, 收敛率由网格的 Jacobi 谱半径决定.

> [!extension: 拓展 — 拉普拉斯算子与图像卷积核]
>
> 把上面的差分公式写成矩阵权重 (各乘以 $h^2$): 当前点系数 $-4$, 上下左右邻居各 $1$. 这正是计算机视觉 (CV) 中大名鼎鼎的**离散拉普拉斯卷积核**:
> $$
> \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}.
> $$
> 把图像看作二维函数 $I(x, y)$, 该卷积核在图像上滑动等价于近似计算 $\Delta I$:
>
> - 平缓区域: $\Delta I \approx 0$ (像素值接近邻居平均);
> - 颜色突变的边缘: $|\Delta I|$ 显著大于零.
>
> 因此, 这一来自偏微分方程的算子被直接搬到 AI 图像处理领域, 用于**边缘检测**与**特征提取**. 一个出生在物理学中的二阶微分算子, 同时是现代视觉算法的基本工具 —— 这正是数学跨越学科边界的力量.
