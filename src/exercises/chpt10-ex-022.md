---
id: chpt10-ex-022
chapter: 10
title: Lagrange乘数法经典例题
tags: [拉格朗日乘数法, 条件极值, 最优化]
difficulty: hard
video:
---

## Problem

求函数 $u = xyz$ 在约束条件 $\displaystyle\frac{1}{x} + \displaystyle\frac{1}{y} + \displaystyle\frac{1}{z} = \displaystyle\frac{1}{a}$（其中 $x,y,z,a > 0$）下的极值.

## Solution 1

### Hint

构造拉格朗日函数，令各偏导数为零得方程组，利用对称性与约束条件解出唯一驻点，再由问题的实际意义判断极值类型.

### Answer

**第一步：构造拉格朗日函数.**

$$L(x,y,z) = xyz + \lambda \left( \frac{1}{x} + \frac{1}{y} + \frac{1}{z} - \frac{1}{a} \right)$$

**第二步：求偏导并令其为零.**

$$\begin{cases}
L_x = yz - \dfrac{\lambda}{x^2} = 0 \\[6pt]
L_y = xz - \dfrac{\lambda}{y^2} = 0 \\[6pt]
L_z = xy - \dfrac{\lambda}{z^2} = 0
\end{cases}$$

**第三步：解方程组.**

将三个方程分别乘以对应的变量 $x$、$y$、$z$，得：

$$xyz = \frac{\lambda}{x}, \quad xyz = \frac{\lambda}{y}, \quad xyz = \frac{\lambda}{z}$$

由此得 $\frac{\lambda}{x} = \frac{\lambda}{y} = \frac{\lambda}{z}$，因为 $\lambda \neq 0$（否则 $xyz=0$ 与 $x,y,z>0$ 矛盾），故 $x = y = z$.

将三个方程相加，代入原约束条件：

$$3xyz = \lambda\left(\frac{1}{x} + \frac{1}{y} + \frac{1}{z}\right) = \frac{\lambda}{a}$$

即 $\lambda = 3axyz$.

再利用约束 $\frac{1}{x}+\frac{1}{y}+\frac{1}{z}=\frac{1}{a}$ 以及 $x=y=z$：

$$\frac{3}{x} = \frac{1}{a} \implies x = 3a$$

从而唯一驻点为 $x = y = z = 3a$.

**第四步：判断极值类型.**

在约束域 $\{x,y,z>0,\ \frac{1}{x}+\frac{1}{y}+\frac{1}{z}=\frac{1}{a}\}$ 上，$u=xyz$ 在边界处（某个变量趋向 $0^+$ 或 $+\infty$ 时）趋向 $0$ 或 $+\infty$. 问题在给定约束下只有一个驻点，且函数值大于边界极限，因此该驻点给出**极小值**.

**结论：**

函数 $u = xyz$ 在点 $(3a, 3a, 3a)$ 处取得极小值：

$$u_{\text{极小}} = (3a)(3a)(3a) = 27a^3$$
