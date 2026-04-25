---
id: chpt12-ex-011
chapter: 12
tags: [格林公式, 曲线积分, 圆周]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\oint_L x^2 y\,\mathrm{d}x - xy^2\,\mathrm{d}y$，其中 $L$ 为正向圆周 $x^2+y^2 = a^2$。

## Solution 1

### Hint

令 $P = x^2 y$，$Q = -xy^2$，计算 $Q_x - P_y$，用格林公式化为圆盘上的二重积分，再换极坐标。

### Answer

$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -y^2 - x^2 = -(x^2+y^2).
$$

由格林公式，设 $D$ 为圆盘 $x^2+y^2\leq a^2$：

$$
\oint_L x^2 y\,\mathrm{d}x - xy^2\,\mathrm{d}y = -\iint_D(x^2+y^2)\,\mathrm{d}x\,\mathrm{d}y.
$$

换极坐标：

$$
= -\int_0^{2\pi}\!\mathrm{d}\theta\int_0^a \rho^3\,\mathrm{d}\rho = -2\pi\cdot\frac{a^4}{4} = -\frac{\pi a^4}{2}.
$$
