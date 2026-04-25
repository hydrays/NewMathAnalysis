---
id: chpt4-ex-010
chapter: 4
tags: [不定积分, 换元法]
difficulty: easy
video:
---

## Problem

计算定积分 $\displaystyle\int_0^{\pi/2} \sin^2 x \cos x\,dx$。

## Solution 1

### Hint

令 $u = \sin x$，则 $du = \cos x\,dx$，同时将积分限从 $x$ 变换为 $u$。

### Answer

令 $u = \sin x$，则 $du = \cos x\,dx$。

当 $x = 0$ 时，$u = 0$；当 $x = \dfrac{\pi}{2}$ 时，$u = 1$。

$$
\int_0^{\pi/2} \sin^2 x \cos x\,dx = \int_0^1 u^2\,du = \frac{u^3}{3}\bigg|_0^1 = \frac{1}{3}
$$
