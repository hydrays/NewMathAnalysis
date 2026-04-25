---
id: chpt5-ex-006
chapter: 5
tags: [中值定理]
difficulty: easy
video:
---

## Problem

求函数 $f(x) = x^2$ 在区间 $[0, 2]$ 上满足积分中值定理的点 $c$。

## Solution 1

### Hint

先计算定积分 $\int_0^2 x^2\,dx$，再由积分中值定理 $\int_a^b f\,dx = f(c)(b-a)$ 解出 $c$。

### Answer

计算积分：

$$
\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}
$$

由积分中值定理，存在 $c \in [0, 2]$ 使得

$$
\frac{8}{3} = f(c)(2 - 0) = 2c^2
$$

解得：

$$
c^2 = \frac{4}{3}, \quad c = \frac{2}{\sqrt{3}} \approx 1.155
$$
