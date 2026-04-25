---
id: chpt11-ex-005
chapter: 11
tags: [二重积分, 极坐标, 重积分应用]
difficulty: medium
video:
---

## Problem

如图所示，求

$$
I = \iint_D r^2(\rho,\theta)\,\rho\,\mathrm{d}\rho\,\mathrm{d}\theta,
$$

其中积分区域 $D$ 由极坐标曲线 $\rho = 2\cos\theta$（$\theta \in [-\pi/2, \pi/2]$）围成。

## Solution 1

### Hint

区域 $D$ 为 $0 \leq \rho \leq 2\cos\theta$，$-\pi/2 \leq \theta \leq \pi/2$。这里 $r^2 = \rho^2$（题中 $r(\rho,\theta)=\rho$），先对 $\rho$ 积分再对 $\theta$ 积分，利用 $\cos^4\theta$ 的降幂公式。

### Answer

$$
I = \int_{-\pi/2}^{\pi/2}\!\int_0^{2\cos\theta} \rho^3\,\mathrm{d}\rho\,\mathrm{d}\theta
= \int_{-\pi/2}^{\pi/2}\left[\frac{\rho^4}{4}\right]_0^{2\cos\theta}\mathrm{d}\theta
= \int_{-\pi/2}^{\pi/2} 4\cos^4\theta\,\mathrm{d}\theta.
$$

利用偶函数对称：

$$
I = 8\int_0^{\pi/2}\cos^4\theta\,\mathrm{d}\theta = 8 \cdot \frac{3\pi}{16} = \frac{3\pi}{2}.
$$

（其中 $\displaystyle\int_0^{\pi/2}\cos^4\theta\,\mathrm{d}\theta = \frac{3\pi}{16}$。）
