---
id: chpt3-ex-013
chapter: 3
tags: [导数应用, 隐函数]
difficulty: easy
video:
---

## Problem

设 $y = \arcsin x$（$-1 < x < 1$），用隐函数求导法求 $y'$。

## Solution 1

### Hint

由 $y = \arcsin x$ 得 $x = \sin y$，对两边关于 $x$ 求导，利用 $\cos y > 0$（当 $-\pi/2 < y < \pi/2$）将结果用 $x$ 表示。

### Answer

由 $y = \arcsin x$ 得 $x = \sin y$。对两边关于 $x$ 求导：

$$
1 = \cos y \cdot \frac{dy}{dx}.
$$

当 $-\dfrac{\pi}{2} < y < \dfrac{\pi}{2}$ 时，$\cos y > 0$，故 $\cos y = \sqrt{1-\sin^2 y} = \sqrt{1-x^2}$。

因此：

$$
\frac{dy}{dx} = (\arcsin x)' = \frac{1}{\sqrt{1-x^2}}.
$$

类似可得 $(\arccos x)' = -\dfrac{1}{\sqrt{1-x^2}}$。
