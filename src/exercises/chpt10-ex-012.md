---
id: chpt10-ex-012
chapter: 10
tags: [梯度, 切平面, 法线, 曲面]
difficulty: medium
video:
---

## Problem

求曲面 $x^2 + y^2 + z = 9$ 在点 $P_0(1, 2, 4)$ 处的切平面方程和法线方程。

## Solution 1

### Hint

将曲面写为 $f(x,y,z) = x^2+y^2+z$，法向量即为梯度 $\nabla f|_{P_0}$，再代入点法式写出切平面和法线。

### Answer

设 $f(x,y,z) = x^2 + y^2 + z$，则梯度为

$$
\nabla f = (2x,\, 2y,\, 1).
$$

在 $P_0(1,2,4)$ 处：

$$
\nabla f\big|_{P_0} = (2, 4, 1),
$$

此向量即为等值面（曲面）在 $P_0$ 处的法向量。

**切平面方程：**

$$
2(x - 1) + 4(y - 2) + (z - 4) = 0,
$$

即

$$
2x + 4y + z = 14.
$$

**法线方程：**

$$
x = 1 + 2t, \quad y = 2 + 4t, \quad z = 4 + t \quad (t \in \mathbb{R}).
$$
