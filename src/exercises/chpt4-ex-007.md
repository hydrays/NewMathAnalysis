---
id: chpt4-ex-007
chapter: 4
tags: [不定积分, 换元法]
difficulty: easy
video:
---

## Problem

计算不定积分 $\displaystyle\int x\sqrt{x^2+1}\,dx$。

## Solution 1

### Hint

令 $u = x^2+1$，则 $du = 2x\,dx$，将被积式化为 $\sqrt{u}$ 的积分。

### Answer

令 $u = x^2+1$，则 $du = 2x\,dx$，即 $x\,dx = \dfrac{du}{2}$。

$$
\int x\sqrt{x^2+1}\,dx = \int \sqrt{u} \cdot \frac{du}{2} = \frac{1}{2}\int u^{1/2}\,du = \frac{1}{2} \cdot \frac{2}{3} u^{3/2} + C = \frac{1}{3}(x^2+1)^{3/2} + C
$$
