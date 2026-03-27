# 偏微分方程

> [!tip]
> 在第七章中，我们学习了常微分方程（ODE），它描述的是**只依赖于一个自变量**（如时间 $t$）的未知函数的变化规律。然而，现实世界要复杂得多：房间里的温度不仅随时间变化，还在空间的不同位置有所不同；水波的传播、电磁场的振荡、甚至是现代 AI 中的“扩散模型（Diffusion Models）”，都依赖于多个自变量（如时间 $t$ 和空间坐标 $x, y, z$）。
> 
> 包含未知多元函数及其**偏导数**的方程，被称为**偏微分方程 (Partial Differential Equation, PDE)**。本章我们将以最著名的偏微分方程——拉普拉斯方程为例，探索它的物理背景、解析求法以及数值解法。

## 偏微分方程的概念与经典模型

> [!important]
> ==热传导方程 (The Heat Equation)==
> 
> 偏微分方程的建立往往源于物理规律。MIT 的微积分课程中给出了一个经典的例子：**热传导方程**。
> 假设我们要研究一个房间内的温度分布。设 $u(x, y, z, t)$ 表示空间点 $(x, y, z)$ 在时间 $t$ 的温度。物理学告诉我们，热量总是从高温区流向低温区。根据傅里叶热传导定律和能量守恒，温度随时间的变化率，与该点在空间上的“二阶偏导数之和”成正比：
> $$ \frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right) $$
> 其中常数 $\alpha > 0$ 称为热导率（Heat conductivity），它决定了热量在这个介质中传播有多快。等式右边的算子在数学上非常重要，我们用一个专用的符号——**拉普拉斯算子 (Laplacian)** $\Delta$ 来表示它：
> $$ \Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} $$
> 所以热传导方程可以简写为：$\displaystyle \frac{\partial u}{\partial t} = \alpha \Delta u$。

> [!note]
> ==从热传导走向拉普拉斯方程==
> 
> 想象一下，如果房间的墙壁一直保持恒定的温度分布，经过足够长的时间后，房间内的温度分布会趋于一个稳定状态（稳态）。
> 既然是稳态，意味着温度不再随时间变化，即 $\displaystyle \frac{\partial u}{\partial t} = 0$。此时，热传导方程就退化为了一个纯空间的偏微分方程：
> $$
> \begin{align*}
> \Delta u
> &= \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \\
> &= 0
> \end{align*}
> $$
> 这个极其优美的方程就是著名的**拉普拉斯方程 (Laplace's Equation)**。满足拉普拉斯方程的函数被称为**调和函数 (Harmonic functions)**。
> 
> **实例：** 
> 我们可以验证某些特殊函数是拉普拉斯方程的解：
> 1. 二维空间中的对数函数 $z = \ln\sqrt{x^2 + y^2}$ 满足 $\displaystyle \frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 0$。
> 2. 三维空间中的引力势/静电势函数 $\displaystyle u = \frac{1}{\sqrt{x^2+y^2+z^2}}$ 满足 $\Delta u = 0$。

## 拉普拉斯方程的解析解法

> [!tip]
> 求解偏微分方程比常微分方程难得多。数学家们发明了许多精妙的技巧，其中最核心的思想就是**“降维”**——将多元偏微分方程转化为一元常微分方程。这里我们介绍两种经典方法：分离变量法与傅里叶变换法。

### 拉普拉斯算子在极坐标下的形式

> [!important]
> ==推导目标==
> 
> 在二维情形中，我们从直角坐标变换到极坐标：
> $$
> x = r \cos\theta, \qquad y = r \sin\theta.
> $$
> 设 $u = u(x,y)$，在极坐标下仍记作 $u = u(r,\theta)$。我们的目标是把
> $$
> \Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}
> $$
> 改写为
> $$
> \Delta u = \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}.
> $$
> 注意：以下推导默认 $r>0$，即先不讨论原点处的奇异性。

> [!tip]
> ==第一步：求 $r,\theta$ 对 $x,y$ 的偏导数==
> 
> 由
> $$
> r=\sqrt{x^2+y^2}, \qquad \theta = \arctan\frac{y}{x},
> $$
> 可得
> $$
> \begin{align*}
> \frac{\partial r}{\partial x}
> &= \frac{x}{\sqrt{x^2+y^2}} \\
> &= \frac{x}{r} \\
> &= \cos\theta, \\
> \frac{\partial r}{\partial y}
> &= \frac{y}{\sqrt{x^2+y^2}} \\
> &= \frac{y}{r} \\
> &= \sin\theta.
> \end{align*}
> $$
> 对 $\theta = \arctan(y/x)$ 使用链式法则：
> $$
> \frac{\partial \theta}{\partial x}
> = \frac{1}{1+(y/x)^2}\left(-\frac{y}{x^2}\right)
> = -\frac{y}{x^2+y^2}
> = -\frac{\sin\theta}{r},
> $$
> $$
> \frac{\partial \theta}{\partial y}
> = \frac{1}{1+(y/x)^2}\frac{1}{x}
> = \frac{x}{x^2+y^2}
> = \frac{\cos\theta}{r}.
> $$
> 因此，
> $$
> r_x = \cos\theta,\qquad r_y=\sin\theta,\qquad
> \theta_x = -\frac{\sin\theta}{r},\qquad
> \theta_y = \frac{\cos\theta}{r}.
> $$

> [!tip]
> ==第二步：先把一阶导数写成极坐标形式==
> 
> 由多元复合函数求导法则，
> $$
> u_x = u_r r_x + u_\theta \theta_x,
> \qquad
> u_y = u_r r_y + u_\theta \theta_y.
> $$
> 代入上一步结果，得到
> $$
> u_x = u_r\cos\theta - \frac{1}{r}u_\theta \sin\theta,
> $$
> $$
> u_y = u_r\sin\theta + \frac{1}{r}u_\theta \cos\theta.
> $$
> 因而微分算子本身也可以写为
> $$
> \frac{\partial}{\partial x}
> =
> \cos\theta \frac{\partial}{\partial r}
> - \frac{\sin\theta}{r}\frac{\partial}{\partial \theta},
> \qquad
> \frac{\partial}{\partial y}
> =
> \sin\theta \frac{\partial}{\partial r}
> + \frac{\cos\theta}{r}\frac{\partial}{\partial \theta}.
> $$

> [!tip]
> ==第三步：计算 $u_{xx}$ 与 $u_{yy}$==
> 
> 先看 $u_{xx}$：
> $$
> u_{xx}
> =
> \left(
> \cos\theta \frac{\partial}{\partial r}
> - \frac{\sin\theta}{r}\frac{\partial}{\partial \theta}
> \right)
> \left(
> u_r\cos\theta - \frac{1}{r}u_\theta \sin\theta
> \right).
> $$
> 展开时分两部分处理。
> 
> 第一部分：
> $$
> \cos\theta \frac{\partial}{\partial r}
> \left(
> u_r\cos\theta - \frac{1}{r}u_\theta \sin\theta
> \right)
> =
> \cos^2\theta\,u_{rr}
> - \frac{\sin\theta\cos\theta}{r}u_{r\theta}
> + \frac{\sin\theta\cos\theta}{r^2}u_\theta.
> $$
> 第二部分：
> $$
> -\frac{\sin\theta}{r}\frac{\partial}{\partial \theta}
> \left(
> u_r\cos\theta - \frac{1}{r}u_\theta \sin\theta
> \right)
> =
> \frac{\sin^2\theta}{r}u_r
> - \frac{\sin\theta\cos\theta}{r}u_{r\theta}
> + \frac{\sin\theta\cos\theta}{r^2}u_\theta
> + \frac{\sin^2\theta}{r^2}u_{\theta\theta}.
> $$
> 相加得到
> $$
> u_{xx}
> =
> \cos^2\theta\,u_{rr}
> + \frac{\sin^2\theta}{r}u_r
> + \frac{\sin^2\theta}{r^2}u_{\theta\theta}
> - \frac{2\sin\theta\cos\theta}{r}u_{r\theta}
> + \frac{2\sin\theta\cos\theta}{r^2}u_\theta.
> $$
> 
> 同理，
> $$
> u_{yy}
> =
> \left(
> \sin\theta \frac{\partial}{\partial r}
> + \frac{\cos\theta}{r}\frac{\partial}{\partial \theta}
> \right)
> \left(
> u_r\sin\theta + \frac{1}{r}u_\theta \cos\theta
> \right),
> $$
> 展开后可得
> $$
> u_{yy}
> =
> \sin^2\theta\,u_{rr}
> + \frac{\cos^2\theta}{r}u_r
> + \frac{\cos^2\theta}{r^2}u_{\theta\theta}
> + \frac{2\sin\theta\cos\theta}{r}u_{r\theta}
> - \frac{2\sin\theta\cos\theta}{r^2}u_\theta.
> $$

> [!tip]
> ==第四步：相加并整理==
> 
> 现在把 $u_{xx}$ 与 $u_{yy}$ 相加：
> $$
> \Delta u = u_{xx}+u_{yy}.
> $$
> 注意到其中的混合项和一阶角向项恰好抵消：
> $$
> - \frac{2\sin\theta\cos\theta}{r}u_{r\theta}
> + \frac{2\sin\theta\cos\theta}{r}u_{r\theta}=0,
> $$
> $$
> \frac{2\sin\theta\cos\theta}{r^2}u_\theta
> - \frac{2\sin\theta\cos\theta}{r^2}u_\theta=0.
> $$
> 再利用恒等式 $\sin^2\theta+\cos^2\theta=1$，便得到
> $$
> \Delta u
> =
> (\cos^2\theta+\sin^2\theta)u_{rr}
> + \frac{\sin^2\theta+\cos^2\theta}{r}u_r
> + \frac{\sin^2\theta+\cos^2\theta}{r^2}u_{\theta\theta},
> $$
> 即
> $$
> \boxed{
> \Delta u
> =
> \frac{\partial^2 u}{\partial r^2}
> + \frac{1}{r}\frac{\partial u}{\partial r}
> + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}
> }.
> $$
> 这就是二维 Laplace 算子在极坐标下的标准形式。

> [!important]
> ==方法一：极坐标下的分离变量法==
> 
> 假设我们要在一个圆形区域（如圆盘）内求解二维拉普拉斯方程 $\Delta u = 0$。在直角坐标系下边界条件很难处理，因此我们先利用链式法则将其转换为极坐标 $(r, \theta)$ 形式：
> $$ \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} = 0 $$
> 
> **分离变量 (Separation of Variables)**：
> 我们大胆地猜测，解 $u(r, \theta)$ 可以拆分为一个只与 $r$ 有关的函数和一个只与 $\theta$ 有关的函数的乘积：
> $$ u(r, \theta) = R(r)\Theta(\theta) $$
> 代入方程并分离变量，可以将原偏微分方程撕裂成两个普通的常微分方程（ODE）：
> $$
> \begin{align*}
> \frac{r^2 R''(r) + r R'(r)}{R(r)}
> &= -\frac{\Theta''(\theta)}{\Theta(\theta)} \\
> &= \lambda
> \end{align*}
> $$
> 因为等式左边只依赖 $r$，右边只依赖 $\theta$，它们必须等于同一个常数 $\lambda$。
> 解关于 $\Theta$ 的方程 $\Theta'' + \lambda \Theta = 0$，考虑到圆盘的角度必须是 $2\pi$ 周期的，我们自然而然地得到了**第十三章**学过的正弦和余弦函数！最终的解 $u(r, \theta)$ 恰好就是无穷多个分离解的叠加，即构成了**傅里叶级数**。

> [!important]
> ==方法二：傅里叶变换法 (针对无界区域)==
> 
> 当求解区域是无限大（如整个上半平面）时，我们可以对偏微分方程两边直接取**傅里叶变换**。
> 
> 回顾第十三章傅里叶变换的神奇性质：它能将时域/空域的**求导运算**，直接转化为频域的**代数乘法**！
> 对于方程 $\displaystyle \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$，如果我们对变量 $x$ 进行傅里叶变换 $\mathcal{F}$，则 $\displaystyle \frac{\partial^2}{\partial x^2}$ 在频域中变成了乘以 $(i\omega)^2 = -\omega^2$。
> 原本包含两个变量偏导数的 PDE，瞬间变成了一个只含有 $y$ 导数的常微分方程 (ODE)：
> $$ -\omega^2 U(\omega, y) + \frac{d^2 U(\omega, y)}{dy^2} = 0 $$
> 这个 ODE 非常容易解出 $U(\omega, y) = A(\omega)e^{-\omega y} + B(\omega)e^{\omega y}$。最后再做一次逆傅里叶变换，就能得到原方程的解析解。这是现代偏微分方程理论中最核心的降维武器！

## 偏微分方程的数值方法与 AI 视角

> [!tip]
> 遗憾的是，在实际工程（如复杂形状的发动机散热、流体力学）中，由于边界条件极其复杂，偏微分方程几乎不可能求出解析解。这时，我们就必须借助计算机，使用**数值方法**求近似解。

> [!note]
> ==有限差分法 (Finite Difference Method, FDM)==
> 
> 在**第八章数值方法**中，我们学过利用“中心差商”来近似函数的二阶导数：
> $$ f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} $$
> 我们将这一思想照搬到二维的网格（Grid）上。设网格步长为 $h$，则坐标 $(x,y)$ 处的二阶偏导数可以离散化为：
> $$ \frac{\partial^2 u}{\partial x^2} \approx \frac{u(x+h, y) - 2u(x,y) + u(x-h, y)}{h^2} $$
> $$ \frac{\partial^2 u}{\partial y^2} \approx \frac{u(x, y+h) - 2u(x,y) + u(x, y-h)}{h^2} $$
> 
> 将这两个式子相加并代入拉普拉斯方程 $\Delta u = 0$，经过简单的移项整理，我们会得到一个极其直观的结论：
> $$ u(x,y) \approx \frac{u(x+h, y) + u(x-h, y) + u(x, y+h) + u(x, y-h)}{4} $$
> 
> **物理意义**：在拉普拉斯方程的稳态下，**空间中任意一点的温度，恰好等于它上下左右四个相邻点温度的平均值！** 计算机只需在网格上反复求解这个线性方程组，就能得到整个区域的温度分布。

> [!extension]
> ==AI 视角：拉普拉斯算子与图像卷积核==
> 
> 如果你将上面的差分公式写成矩阵权重（乘以 $h^2$），当前点系数为 $-4$，上下左右为 $1$。这其实就是计算机视觉（CV）中大名鼎鼎的**离散拉普拉斯卷积核 (Laplacian Filter)**：
> $$ \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix} $$
> 在图像处理中，图片可以看成是一个二维函数 $I(x,y)$。当我们将这个核在图片上进行卷积滑动时，本质上就是在计算图像的拉普拉斯算子 $\Delta I$。平缓区域的 $\Delta I \approx 0$（像素等于周围平均值），而在颜色突变的边缘区域 $\Delta I$ 绝对值很大。因此，偏微分方程在 AI 领域被直接跨界用来进行**图像的边缘检测**和**特征提取**！
