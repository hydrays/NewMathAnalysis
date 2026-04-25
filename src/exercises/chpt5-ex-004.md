---
id: chpt5-ex-004
chapter: 5
tags: [中值定理, 拉格朗日中值定理]
difficulty: easy
video:
---

## Problem

对于 $f(x) = x^3$，取 $x_1 = 0$，$x_2 = 1$，找出满足拉格朗日中值定理的中值点 $c$。

## Solution 1

### Hint

计算 $\dfrac{f(1) - f(0)}{1 - 0}$，令其等于 $f'(c) = 3c^2$，解出 $c \in (0, 1)$。

### Answer

$f(x) = x^3$ 在 $[0, 1]$ 上连续且可导，满足定理条件。

计算差商：

$$
\frac{f(1) - f(0)}{1 - 0} = \frac{1 - 0}{1} = 1
$$

令 $f'(c) = 3c^2 = 1$，解得

$$
c = \frac{1}{\sqrt{3}} \approx 0.577
$$

中值点 $c = \dfrac{1}{\sqrt{3}} \in (0, 1)$，满足定理要求。
