---
id: chpt11-ex-012
chapter: 11
title: 极坐标下的积分
tags: [二重积分, 极坐标, 换元]
difficulty: medium
video:
---

## Problem

已知 $f(x,y)=1-x^2-y^2$，$D= \{(x,y)\mid x^2+y^2\leq 1,\,x\geq 0,\,y\geq 0\}$，计算

$$
\iint_D f(x,y)\,\mathrm{d}A.
$$

## Solution 1

### Hint

区域 $D$ 是单位圆盘在第一象限的部分，天然适合用极坐标。令 $x=r\cos\theta$，$y=r\sin\theta$，则面积元变为 $\mathrm{d}A=r\,\mathrm{d}r\,\mathrm{d}\theta$，积分区域变为 $0\leq\theta\leq\dfrac{\pi}{2}$，$0\leq r\leq 1$。

### Answer

由于面积元 $\mathrm{d}A=\mathrm{d}x\mathrm{d}y=r\,\mathrm{d}r\,\mathrm{d}\theta$，令 $x=r\cos\theta$，$y=r\sin\theta$，积分化为

$$
\begin{aligned}
\iint_D (1-x^2-y^2)\,\mathrm{d}x\mathrm{d}y
&= \iint_D (1-r^2)\,r\,\mathrm{d}r\,\mathrm{d}\theta \\
&= \int_0^{\frac{\pi}{2}}\left[\int_0^1(1-r^2)r\,\mathrm{d}r\right]\mathrm{d}\theta \\
&= \frac{\pi}{2}\left[\frac{r^2}{2}-\frac{r^4}{4}\right]_0^1 \\
&= \frac{\pi}{2}\cdot\frac{1}{4} = \frac{\pi}{8}.
\end{aligned}
$$
