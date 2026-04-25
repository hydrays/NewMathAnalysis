---
id: chpt11-ex-013
chapter: 11
title: 高斯积分
tags: [二重积分, 极坐标, 广义积分]
difficulty: medium
video:
---

## Problem

计算广义积分

$$
\int_{-\infty}^{+\infty}e^{-x^2}\,\mathrm{d}x.
$$

## Solution 1

### Hint

令 $I=\int_{-\infty}^{+\infty}e^{-x^2}\,\mathrm{d}x$，则 $I^2$ 可以写成关于 $x,y$ 的二重积分，再换成极坐标计算。

### Answer

令 $\displaystyle I=\int_{-\infty}^{+\infty}e^{-x^2}\,\mathrm{d}x$，则

$$
I^2=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}e^{-(x^2+y^2)}\,\mathrm{d}x\,\mathrm{d}y.
$$

令 $x=r\cos\theta$，$y=r\sin\theta$，则

$$
\begin{aligned}
I^2 &=\int_0^{2\pi}\int_0^{+\infty}e^{-r^2}r\,\mathrm{d}r\,\mathrm{d}\theta \\
&=\int_0^{2\pi}\mathrm{d}\theta\cdot\frac{1}{2}\int_0^{+\infty}e^{-r^2}\,\mathrm{d}(r^2) \\
&=\frac{1}{2}\int_0^{2\pi}\left[-e^{-r^2}\right]_0^{+\infty}\mathrm{d}\theta \\
&= \frac{1}{2}\cdot 2\pi\cdot 1 = \pi.
\end{aligned}
$$

故 $\displaystyle\int_{-\infty}^{+\infty}e^{-x^2}\,\mathrm{d}x = \sqrt{\pi}$.
