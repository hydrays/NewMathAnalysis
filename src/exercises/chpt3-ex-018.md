---
id: chpt3-ex-018
chapter: 3
tags: [导数应用, 高阶导数]
difficulty: medium
video:
---

## Problem

求指数函数 $y = \mathrm{e}^{kx}$（$k$ 为常数）的 $n$ 阶导数。

## Solution 1

### Hint

逐步计算一阶、二阶、三阶导数，观察规律，归纳出一般公式。

### Answer

$$
y' = k\mathrm{e}^{kx}, \quad y'' = k^2\mathrm{e}^{kx}, \quad y''' = k^3\mathrm{e}^{kx}, \quad y^{(4)} = k^4\mathrm{e}^{kx}.
$$

观察规律：每求导一次多乘一个系数 $k$，故

$$
y^{(n)} = k^n\mathrm{e}^{kx}.
$$
