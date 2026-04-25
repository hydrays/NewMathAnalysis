---
id: chpt9-ex-011
chapter: 9
tags: [二重积分, 曲线积分]
difficulty: medium
video:
---

## Problem

已知两球面的方程为 $x^2+y^2+z^2=1$ 和 $x^2+(y-1)^2+(z-1)^2=1$，求它们的交线 $C$ 在 $xOy$ 面上的投影的方程。

## Solution 1

### Hint

两球面方程相减消去 $x^2$ 项，得到包含交线且母线平行于 $z$ 轴的柱面方程，即为投影柱面。

### Answer

两方程相减消去 $z$：

$$
(y^2-2y+1)+(z^2-2z+1) - y^2 - z^2 = 0 \implies -2y+1-2z+1=0 \implies y+z=1.
$$

即 $z=1-y$，代入第一个方程：

$$
x^2 + y^2 + (1-y)^2 = 1 \implies x^2+2y^2-2y=0.
$$

交线 $C$ 在 $xOy$ 面上的投影方程为：

$$
\begin{cases} x^2+2y^2-2y=0, \\ z=0. \end{cases}
$$
