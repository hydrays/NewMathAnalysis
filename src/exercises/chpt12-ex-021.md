---
id: chpt12-ex-021
chapter: 12
tags: [Stokes公式, 三维曲线积分, 旋度]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\int_C \vec{F}\cdot\mathrm{d}\vec{r}$，其中 $\vec{F} = (yz, xz, xy)$，曲线 $C: x = t^3, y = t^2, z = t$，$0 \leq t \leq 1$。

## Solution 1

### Hint

直接参数化：将 $P = yz$，$Q = xz$，$R = xy$ 代入 $\int_C P\,\mathrm{d}x + Q\,\mathrm{d}y + R\,\mathrm{d}z$，化为对 $t$ 的积分。

### Answer

$\mathrm{d}x = 3t^2\,\mathrm{d}t$，$\mathrm{d}y = 2t\,\mathrm{d}t$，$\mathrm{d}z = \mathrm{d}t$。

在 $C$ 上：$P = yz = t^2\cdot t = t^3$，$Q = xz = t^3\cdot t = t^4$，$R = xy = t^3\cdot t^2 = t^5$。

$$
\int_C \vec{F}\cdot\mathrm{d}\vec{r}
= \int_0^1\left(t^3\cdot 3t^2 + t^4\cdot 2t + t^5\cdot 1\right)\mathrm{d}t
= \int_0^1 6t^5\,\mathrm{d}t = \left[t^6\right]_0^1 = 1.
$$

**注：** 向量场 $\vec{F} = (yz, xz, xy)$ 是梯度场（势函数 $f = xyz$），所以积分值也可由 $f(1,1,1)-f(0,0,0) = 1$ 直接得出。
