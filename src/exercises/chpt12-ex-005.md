---
id: chpt12-ex-005
chapter: 12
tags: [曲线积分, 第二类曲线积分, 物理应用, 做功]
difficulty: medium
video:
---

## Problem

一个质点在点 $M(x,y)$ 处受到力 $\vec{F}$ 的作用，$\vec{F}$ 的大小与点 $M$ 到原点 $O$ 的距离成正比，方向恒指向原点。质点由 $A(a,0)$ 沿椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ 按逆时针方向移动到 $B(0,b)$，求力 $\vec{F}$ 所做的功 $W$。

## Solution 1

### Hint

力的表达式为 $\vec{F} = -k(x\hat{i}+y\hat{j})$（$k>0$）。用椭圆参数方程 $x = a\cos\theta$，$y = b\sin\theta$，$\theta \in [0, \pi/2]$，代入做功积分。

### Answer

$$
\vec{F} = -k(x\hat{i} + y\hat{j}), \quad W = -k\int_{AB}(x\,\mathrm{d}x + y\,\mathrm{d}y).
$$

参数化：$\mathrm{d}x = -a\sin\theta\,\mathrm{d}\theta$，$\mathrm{d}y = b\cos\theta\,\mathrm{d}\theta$，$\theta: 0 \to \pi/2$：

$$
W = -k\int_0^{\pi/2}\bigl[a\cos\theta(-a\sin\theta) + b\sin\theta(b\cos\theta)\bigr]\mathrm{d}\theta
= k(a^2-b^2)\int_0^{\pi/2}\sin\theta\cos\theta\,\mathrm{d}\theta.
$$

$$
W = k(a^2-b^2)\cdot\frac{1}{2}\int_0^{\pi/2}\sin 2\theta\,\mathrm{d}\theta
= k(a^2-b^2)\cdot\frac{1}{2}\left[-\frac{\cos 2\theta}{2}\right]_0^{\pi/2}
= \frac{k(a^2-b^2)}{2}.
$$
