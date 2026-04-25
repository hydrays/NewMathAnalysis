---
id: chpt11-ex-009
chapter: 11
tags: [二重积分, 换元法, 雅可比行列式]
difficulty: medium
video:
---

## Problem

已知变量替换 $u = 3x - 2y$，$v = x + y$，求雅可比行列式 $\dfrac{\partial(u,v)}{\partial(x,y)}$，并建立面积元素的关系式。

## Solution 1

### Hint

直接计算 $2\times 2$ 雅可比行列式（偏导数矩阵的行列式）。

### Answer

$$
J = \frac{\partial(u,v)}{\partial(x,y)} =
\begin{vmatrix}
\dfrac{\partial u}{\partial x} & \dfrac{\partial u}{\partial y} \\[6pt]
\dfrac{\partial v}{\partial x} & \dfrac{\partial v}{\partial y}
\end{vmatrix}
=
\begin{vmatrix}
3 & -2 \\ 1 & 1
\end{vmatrix}
= 3 \cdot 1 - (-2) \cdot 1 = 5.
$$

因此面积元素关系为

$$
\mathrm{d}u\,\mathrm{d}v = 5\,\mathrm{d}x\,\mathrm{d}y,
$$

即

$$
\iint_D \mathrm{d}x\,\mathrm{d}y = \iint_{D'} \frac{1}{5}\,\mathrm{d}u\,\mathrm{d}v,
$$

其中 $D'$ 是 $D$ 在 $(u,v)$ 坐标下对应的区域。
