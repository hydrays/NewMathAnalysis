---
id: chpt4-ex-011
chapter: 4
tags: [不定积分, 换元法]
difficulty: medium
video:
---

## Problem

计算定积分 $\displaystyle\int_1^4 \frac{\sqrt{x}}{1+\sqrt{x}}\,dx$。

## Solution 1

### Hint

令 $u = 1+\sqrt{x}$，则 $\sqrt{x} = u-1$，$dx = 2(u-1)\,du$，记得同步换算积分限，再将有理函数做多项式除法后逐项积分。

### Answer

令 $u = 1+\sqrt{x}$，则 $du = \dfrac{1}{2\sqrt{x}}\,dx$，即 $dx = 2(u-1)\,du$。

当 $x = 1$ 时，$u = 2$；当 $x = 4$ 时，$u = 3$。

$$
\int_1^4 \frac{\sqrt{x}}{1+\sqrt{x}}\,dx = \int_2^3 \frac{u-1}{u} \cdot 2(u-1)\,du = 2\int_2^3 \frac{(u-1)^2}{u}\,du
$$

展开并化简：

$$
= 2\int_2^3 \left(u - 2 + \frac{1}{u}\right)du = 2\left[\frac{u^2}{2} - 2u + \ln|u|\right]_2^3
$$

$$
= \left[u^2 - 4u + 2\ln u\right]_2^3 = (9 - 12 + 2\ln 3) - (4 - 8 + 2\ln 2)
$$

$$
= 1 + 2\ln\frac{3}{2}
$$
