---
id: chpt10-ex-009
chapter: 10
tags: [全微分, 应用, 梯形截面]
difficulty: medium
video:
---

## Problem

设截面积函数

$$
S(x, \theta) = Lx\sin\theta - 2x^2\sin\theta + x^2\sin\theta\cos\theta,
$$

求全微分 $dS$。

## Solution 1

### Hint

分别对 $x$ 和 $\theta$ 求偏导数，然后代入全微分公式；对 $\theta$ 求导时需用 $\cos^2\theta - \sin^2\theta = \cos 2\theta$。

### Answer

求偏导数：

$$
\frac{\partial S}{\partial x} = L\sin\theta - 4x\sin\theta + 2x\sin\theta\cos\theta = \sin\theta(L - 4x + 2x\cos\theta),
$$

$$
\frac{\partial S}{\partial \theta} = Lx\cos\theta - 2x^2\cos\theta + x^2(\cos^2\theta - \sin^2\theta) = x\cos\theta(L - 2x) + x^2\cos 2\theta.
$$

全微分：

$$
dS = \sin\theta(L - 4x + 2x\cos\theta)\,dx + \bigl[x\cos\theta(L - 2x) + x^2\cos 2\theta\bigr]\,d\theta.
$$
