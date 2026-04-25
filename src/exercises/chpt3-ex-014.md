---
id: chpt3-ex-014
chapter: 3
tags: [导数应用, 隐函数]
difficulty: easy
video:
---

## Problem

设 $y = \arctan x$（$x \in \mathbb{R}$），用隐函数求导法求 $y'$。

## Solution 1

### Hint

由 $y = \arctan x$ 得 $x = \tan y$，对两边关于 $x$ 求导，利用三角恒等式 $\sec^2 y = 1 + \tan^2 y$ 将结果用 $x$ 表示。

### Answer

由 $y = \arctan x$ 得 $x = \tan y$。对两边关于 $x$ 求导：

$$
1 = \sec^2 y \cdot \frac{dy}{dx}.
$$

利用恒等式 $\sec^2 y = 1 + \tan^2 y = 1 + x^2$，故：

$$
\frac{dy}{dx} = (\arctan x)' = \frac{1}{1+x^2}.
$$

类似可得 $(\text{arccot}\, x)' = -\dfrac{1}{1+x^2}$。
