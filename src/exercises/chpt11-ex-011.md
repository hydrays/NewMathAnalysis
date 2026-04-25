---
id: chpt11-ex-011
chapter: 11
tags: [三重积分, 柱面坐标]
difficulty: medium
video:
---

## Problem

利用柱面坐标计算三重积分

$$
\iiint_\Omega z\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z,
$$

其中 $\Omega$ 是由曲面 $z = x^2+y^2$ 与平面 $z = 4$ 围成的闭区域。

## Solution 1

### Hint

在柱面坐标 $x = \rho\cos\theta$，$y = \rho\sin\theta$，$z = z$ 下，体积元 $\mathrm{d}V = \rho\,\mathrm{d}\rho\,\mathrm{d}\theta\,\mathrm{d}z$；区域变为 $0\leq\rho\leq\sqrt{z}$，$0\leq\theta\leq 2\pi$，$0\leq z\leq 4$（先对 $\rho$ 和 $\theta$，再对 $z$）。

### Answer

令 $x = \rho\cos\theta$，$y = \rho\sin\theta$，则 $\mathrm{d}V = \rho\,\mathrm{d}\rho\,\mathrm{d}\theta\,\mathrm{d}z$。

区域在柱面坐标下：$0 \leq \theta \leq 2\pi$，$0 \leq z \leq 4$，$0 \leq \rho \leq \sqrt{z}$。

$$
\iiint_\Omega z\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
= \int_0^4\!\mathrm{d}z\int_0^{2\pi}\!\mathrm{d}\theta\int_0^{\sqrt{z}} z\rho\,\mathrm{d}\rho
= \int_0^4\!\mathrm{d}z\int_0^{2\pi}\frac{z^2}{2}\,\mathrm{d}\theta
= \int_0^4 \pi z^2\,\mathrm{d}z
= \pi\left[\frac{z^3}{3}\right]_0^4 = \frac{64\pi}{3}.
$$
