---
id: chpt11-ex-008
chapter: 11
tags: [二重积分, 换元法, 椭圆面积]
difficulty: medium
video:
---

## Problem

已知椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$，求椭圆的面积 $\displaystyle\iint_D\mathrm{d}x\,\mathrm{d}y$。

## Solution 1

### Hint

直接将椭圆区域展开为累次积分，内层对 $y$ 积分，外层利用三角换元 $x = a\sin\theta$。

### Answer

$$
\iint_D\mathrm{d}x\,\mathrm{d}y
= 4\int_0^a\int_0^{b\sqrt{1-x^2/a^2}}\mathrm{d}y\,\mathrm{d}x
= 4\int_0^a b\sqrt{1-\frac{x^2}{a^2}}\,\mathrm{d}x.
$$

令 $x = a\sin\theta$，$\mathrm{d}x = a\cos\theta\,\mathrm{d}\theta$：

$$
= 4\int_0^{\pi/2} b\cos\theta \cdot a\cos\theta\,\mathrm{d}\theta
= 4ab\int_0^{\pi/2}\frac{1+\cos 2\theta}{2}\,\mathrm{d}\theta = \pi ab.
$$

## Solution 2

### Hint

用换元 $x = au$，$y = bv$ 将椭圆变为单位圆，再乘以雅可比行列式 $ab$。

### Answer

令 $x = au$，$y = bv$，则 $\mathrm{d}x\,\mathrm{d}y = ab\,\mathrm{d}u\,\mathrm{d}v$，椭圆变为单位圆 $u^2+v^2\leq 1$：

$$
\iint_D\mathrm{d}x\,\mathrm{d}y = ab\iint_{u^2+v^2\leq 1}\mathrm{d}u\,\mathrm{d}v = ab \cdot \pi = \pi ab.
$$
