---
id: chpt12-ex-022
chapter: 12
tags: [旋度, 梯度场, 三维向量场]
difficulty: easy
video:
---

## Problem

判断向量场 $\vec{F} = (yz, xz, xy)$ 是否为梯度场，并计算其旋度。

## Solution 1

### Hint

对 $\vec{F} = (P, Q, R)$，计算 $\nabla\times\vec{F} = (R_y-Q_z, P_z-R_x, Q_x-P_y)$；若旋度为零则为梯度场。

### Answer

$P = yz$，$Q = xz$，$R = xy$。

$$
Q_x = z = P_y, \quad R_y = x = Q_z, \quad R_x = y = P_z.
$$

所有混合偏导相等，故 $\mathrm{curl}\,\vec{F} = \nabla\times\vec{F} = \mathbf{0}$。

$\vec{F}$ 是梯度场，势函数 $f = xyz$（可验证 $\nabla(xyz) = (yz, xz, xy)$）。
