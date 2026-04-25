---
id: chpt12-ex-009
chapter: 12
tags: [梯度场, 旋度, 保守场判断]
difficulty: easy
video:
---

## Problem

判断以下向量场是否为梯度场（保守场）：

1. $\vec{F} = \langle y^2, 0\rangle$
2. $\vec{F} = \langle 2xy, x^2\rangle$
3. $\vec{F} = \langle y, x\rangle$

## Solution 1

### Hint

对于 $\vec{F} = \langle P, Q\rangle$，是梯度场的充要条件为 $\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}$。

### Answer

**(1) $P = y^2$，$Q = 0$：**

$$
P_y = 2y \neq Q_x = 0.
$$

不是梯度场。

**(2) $P = 2xy$，$Q = x^2$：**

$$
P_y = 2x = Q_x = 2x. \quad \checkmark
$$

是梯度场（势函数 $f = x^2 y$）。

**(3) $P = y$，$Q = x$：**

$$
P_y = 1 = Q_x = 1. \quad \checkmark
$$

是梯度场（势函数 $f = xy$）。
