---
id: chpt8-ex-005
chapter: 8
tags: [偏导数, 数值方法]
difficulty: easy
video:
---

## Problem

用梯形法计算 $\displaystyle\int_0^1 x^2\,dx$，取 $n=4$，并与精确值 $\dfrac{1}{3}$ 比较。

## Solution 1

### Hint

梯形公式：$\dfrac{h}{2}[f(a) + 2\sum_{i=1}^{n-1}f(x_i) + f(b)]$，$h=0.25$。

### Answer

$$
\frac{0.25}{2}[f(0) + 2f(0.25) + 2f(0.5) + 2f(0.75) + f(1.0)]
$$

$$
= 0.125 \times [0 + 2(0.0625) + 2(0.25) + 2(0.5625) + 1.0] = 0.125 \times 2.75 = 0.34375.
$$

与精确值 $0.3333$ 相比，误差约 $0.0104$，比矩形法有明显改进。
