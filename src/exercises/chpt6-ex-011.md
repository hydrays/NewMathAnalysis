---
id: chpt6-ex-011
chapter: 6
tags: [定积分, 面积]
difficulty: easy
video:
---

## Problem

计算电场强度：考虑函数 $f(x) = \dfrac{1}{\sqrt{x}}$ 在 $[0,1]$ 上的积分（无界函数的反常积分）。

## Solution 1

### Hint

$x=0$ 处函数无界，通过极限定义反常积分：令下限趋于 $0^+$。

### Answer

$$
\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{a\to 0^+}\int_a^1 \frac{1}{\sqrt{x}}\,dx = \lim_{a\to 0^+}\left[2\sqrt{x}\right]_a^1 = \lim_{a\to 0^+}(2-2\sqrt{a}) = 2.
$$

积分收敛于 $2$。
