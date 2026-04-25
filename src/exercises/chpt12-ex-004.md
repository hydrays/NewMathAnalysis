---
id: chpt12-ex-004
chapter: 12
tags: [曲线积分, 第二类曲线积分, 路径相关]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\int_L xy\,\mathrm{d}x$，其中 $L$ 为抛物线 $y^2 = x$ 上从点 $A(1,-1)$ 到点 $B(1,1)$ 的一段弧。

## Solution 1

### Hint

分拆路径为 $AO$（$y$ 从 $-1$ 到 $0$）和 $OB$（$y$ 从 $0$ 到 $1$），或直接用 $y$ 参数化整条弧：$x = y^2$，$\mathrm{d}x = 2y\,\mathrm{d}y$，$y \in [-1,1]$。

### Answer

**解法一（分拆路径）：**

$$
\int_L xy\,\mathrm{d}x = \int_{AO} xy\,\mathrm{d}x + \int_{OB} xy\,\mathrm{d}x
= \int_1^0 x(-\sqrt{x})\,\mathrm{d}x + \int_0^1 x\sqrt{x}\,\mathrm{d}x
= 2\int_0^1 x^{3/2}\,\mathrm{d}x = \frac{4}{5}.
$$

**解法二（$y$ 参数化）：**

$x = y^2$，$\mathrm{d}x = 2y\,\mathrm{d}y$，$y \in [-1,1]$：

$$
\int_L xy\,\mathrm{d}x = \int_{-1}^1 y^2 \cdot y \cdot 2y\,\mathrm{d}y = 2\int_{-1}^1 y^4\,\mathrm{d}y = 4\int_0^1 y^4\,\mathrm{d}y = \frac{4}{5}.
$$
