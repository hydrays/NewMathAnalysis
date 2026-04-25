---
id: chpt12-ex-015
chapter: 12
tags: [曲面积分, 高斯公式, 三维散度]
difficulty: easy
video:
---

## Problem

设 $\vec{F} = x\hat{i}+y\hat{j}+z\hat{k}$，利用高斯公式计算通量 $\displaystyle\oiint_\Sigma \vec{F}\cdot\vec{n}\,\mathrm{d}S$，其中 $\Sigma$ 是球面 $x^2+y^2+z^2 = a^2$ 的外侧。

## Solution 1

### Hint

计算 $\mathrm{div}\,\vec{F} = 3$，再用高斯公式化为球体体积分。

### Answer

$$
\mathrm{div}\,\vec{F} = 1 + 1 + 1 = 3.
$$

由高斯公式，设 $D$ 为球体 $x^2+y^2+z^2\leq a^2$（体积 $\dfrac{4}{3}\pi a^3$）：

$$
\oiint_\Sigma \vec{F}\cdot\vec{n}\,\mathrm{d}S = \iiint_D 3\,\mathrm{d}V = 3\cdot\frac{4}{3}\pi a^3 = 4\pi a^3.
$$
