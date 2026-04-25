---
id: chpt3-ex-004
chapter: 3
tags: [导数应用, 链式法则]
difficulty: easy
video:
---

## Problem

设函数 $y = \cos\dfrac{x^2-1}{3x}$，求 $\dfrac{dy}{dx}$。

## Solution 1

### Hint

令 $u = \dfrac{x^2-1}{3x}$，分别求 $\dfrac{dy}{du}$ 和 $\dfrac{du}{dx}$，再用链式法则合并。

### Answer

令 $u = \dfrac{x^2-1}{3x}$，则 $y = \cos u$。

$$
\frac{dy}{du} = -\sin u,
$$

$$
\frac{du}{dx} = \frac{(2x)(3x) - (x^2-1)(3)}{9x^2} = \frac{6x^2 - 3x^2 + 3}{9x^2} = \frac{x^2+1}{3x^2}.
$$

由链式法则：

$$
\frac{dy}{dx} = -\sin u \cdot \frac{x^2+1}{3x^2} = -\frac{x^2+1}{3x^2}\sin\frac{x^2-1}{3x}.
$$
