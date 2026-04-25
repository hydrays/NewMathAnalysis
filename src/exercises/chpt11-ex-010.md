---
id: chpt11-ex-010
chapter: 11
tags: [三重积分, 累次积分]
difficulty: medium
video:
---

## Problem

计算三重积分 $\displaystyle\iiint_\Omega x\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$，其中 $\Omega$ 由平面 $x + 2y + z = 1$ 与三个坐标平面（$x=0$，$y=0$，$z=0$）围成。

## Solution 1

### Hint

先对 $z$（从 $0$ 到 $1-x-2y$），再对 $y$（从 $0$ 到 $\frac{1-z}{2}$ 或 $\frac{1-x}{2}$），最后对 $x$ 积分。

### Answer

$$
\iiint_\Omega x\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
= \int_0^1\!\mathrm{d}z\int_0^{\frac{1-z}{2}}\!\mathrm{d}y\int_0^{1-2y-z} x\,\mathrm{d}x.
$$

**内层（对 $x$）：**

$$
\int_0^{1-2y-z} x\,\mathrm{d}x = \frac{(1-2y-z)^2}{2}.
$$

**中层（对 $y$）：**

$$
\int_0^{\frac{1-z}{2}} \frac{(1-2y-z)^2}{2}\,\mathrm{d}y
= \frac{1}{12}(1-z)^3.
$$

**外层（对 $z$）：**

$$
\int_0^1 \frac{(1-z)^3}{12}\,\mathrm{d}z = \frac{1}{12}\left[-\frac{(1-z)^4}{4}\right]_0^1 = \frac{1}{48}.
$$

## Solution 2

### Hint

改变积分顺序，先对 $z$（从 $0$ 到 $1-x-2y$），再对 $y$（从 $0$ 到 $\frac{1-x}{2}$），最后对 $x$（从 $0$ 到 $1$）。

### Answer

$$
\iiint_\Omega x\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
= \int_0^1 x\,\mathrm{d}x\int_0^{\frac{1-x}{2}}(1-x-2y)\,\mathrm{d}y
= \int_0^1 \frac{x(1-x)^2}{4}\,\mathrm{d}x = \frac{1}{48}.
$$
