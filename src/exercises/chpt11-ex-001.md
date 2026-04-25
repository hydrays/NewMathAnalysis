---
id: chpt11-ex-001
chapter: 11
title: 矩形区域上的二重积分
tags: [二重积分, 累次积分, 矩形区域]
difficulty: easy
video:
---

## Problem

已知 $f(x,y) = 1 - x^2 - y^2$，$D = \{(x,y) \mid 0 \leq x \leq 1,\ 0 \leq y \leq 1\}$，计算

$$
\iint_D f(x,y)\,\mathrm{d}A.
$$

## Solution 1

### Hint

矩形区域上，将二重积分化为累次积分，先对 $x$ 积分（内层），再对 $y$ 积分（外层）。

### Answer

$$
\iint_D f(x,y)\,\mathrm{d}A = \int_0^1\!\int_0^1 (1-x^2-y^2)\,\mathrm{d}x\,\mathrm{d}y.
$$

**内层积分（对 $x$）：**

$$
\int_0^1(1-x^2-y^2)\,\mathrm{d}x = \left[x - \frac{x^3}{3} - y^2 x\right]_0^1 = \frac{2}{3} - y^2.
$$

**外层积分（对 $y$）：**

$$
\int_0^1\left(\frac{2}{3} - y^2\right)\mathrm{d}y = \left[\frac{2}{3}y - \frac{y^3}{3}\right]_0^1 = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}.
$$

两种积分顺序结果相同（可验证先对 $y$ 后对 $x$ 同样得 $\dfrac{1}{3}$）。
