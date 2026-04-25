---
id: chpt12-ex-014
chapter: 12
tags: [曲面积分, 通量, 散度定理]
difficulty: easy
video:
---

## Problem

设 $\vec{F} = x\hat{i}+y\hat{j}$，利用散度定理（格林公式的通量形式）计算通量 $\displaystyle\int_C \vec{F}\cdot\vec{n}\,\mathrm{d}s$，其中 $C$ 是某区域 $D$ 的正向边界。

## Solution 1

### Hint

计算 $\mathrm{div}\,\vec{F} = P_x + Q_y$，再用 $\mathrm{Flux} = \iint_D \mathrm{div}\,\vec{F}\,\mathrm{d}A$。

### Answer

$$
\mathrm{div}\,\vec{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} = 1 + 1 = 2.
$$

由散度定理：

$$
\int_C \vec{F}\cdot\vec{n}\,\mathrm{d}s = \iint_D 2\,\mathrm{d}A = 2\,\mathrm{Area}(D).
$$
