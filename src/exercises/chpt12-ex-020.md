---
id: chpt12-ex-020
chapter: 12
tags: [Stokes公式, 三维曲线积分, 斯托克斯定理]
difficulty: hard
video:
---

## Problem

利用斯托克斯公式计算曲线积分

$$
I = \oint_\Gamma (y^2-z^2)\,\mathrm{d}x + (z^2-x^2)\,\mathrm{d}y + (x^2-y^2)\,\mathrm{d}z,
$$

其中 $\Gamma$ 是平面 $x+y+z=\frac{3}{2}$ 截立方体 $\{0\leq x,y,z\leq 1\}$ 表面所得的截痕，方向为从 $Ox$ 轴正向看去的逆时针方向。

## Solution 1

### Hint

选取 $\Sigma$ 为平面 $x+y+z=\frac{3}{2}$ 被 $\Gamma$ 围住的部分（上侧），法向量 $\mathbf{n} = \frac{1}{\sqrt{3}}(1,1,1)$。计算被积向量场的旋度后代入斯托克斯公式，注意在 $\Sigma$ 上 $x+y+z = \frac{3}{2}$。

### Answer

法向量 $\mathbf{n} = \frac{1}{\sqrt{3}}(1,1,1)$，$\cos\alpha=\cos\beta=\cos\gamma=\frac{1}{\sqrt{3}}$。

斯托克斯公式（旋度行列式展开）：

$$
I = \iint_\Sigma
\begin{vmatrix}
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} \\
\partial_x & \partial_y & \partial_z \\
y^2-z^2 & z^2-x^2 & x^2-y^2
\end{vmatrix}
\mathrm{d}S
= -\frac{4}{\sqrt{3}}\iint_\Sigma(x+y+z)\,\mathrm{d}S.
$$

在 $\Sigma$ 上，$x+y+z = \frac{3}{2}$：

$$
I = -\frac{4}{\sqrt{3}}\cdot\frac{3}{2}\iint_\Sigma\mathrm{d}S = -2\sqrt{3}\iint_{D_{xy}}\sqrt{3}\,\mathrm{d}x\,\mathrm{d}y = -6\sigma_{xy}.
$$

投影区域 $D_{xy}$ 为正六边形，面积 $\sigma_{xy} = 1 - 2\times\frac{1}{8} = \frac{3}{4}$（由立方体截面几何算得）。

$$
I = -6\cdot\frac{3}{4} = -\frac{9}{2}.
$$
