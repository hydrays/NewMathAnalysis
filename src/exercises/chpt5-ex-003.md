---
id: chpt5-ex-003
chapter: 5
tags: [中值定理, 拉格朗日中值定理]
difficulty: easy
video:
---

## Problem

对于 $f(x) = x^2$，任取两点 $x_1 < x_2$，找出满足拉格朗日中值定理的中值点 $c$。

## Solution 1

### Hint

计算差商 $\dfrac{f(x_2) - f(x_1)}{x_2 - x_1}$，令其等于 $f'(c) = 2c$，解出 $c$。

### Answer

$f(x) = x^2$ 是多项式，在任意区间 $[x_1, x_2]$ 上连续且可导，满足拉格朗日中值定理的条件。

计算差商：

$$
\frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{x_2^2 - x_1^2}{x_2 - x_1} = x_2 + x_1
$$

令 $f'(c) = 2c = x_2 + x_1$，解得

$$
c = \frac{x_1 + x_2}{2}
$$

中值点 $c$ 恰好为区间中点，满足定理要求。
