---
id: chpt12-ex-016
chapter: 12
tags: [曲面积分, 高斯公式, 柱面坐标]
difficulty: hard
video:
---

## Problem

利用高斯公式计算曲面积分

$$
\iint_\Sigma (x-y)\,\mathrm{d}x\,\mathrm{d}y + (y-z)x\,\mathrm{d}y\,\mathrm{d}z,
$$

其中 $\Sigma$ 为柱面 $x^2+y^2=1$ 及平面 $z=0$，$z=3$ 所围成的空间闭区域 $\Omega$ 的整个边界曲面的外侧。

## Solution 1

### Hint

令 $P = (y-z)x$，$Q = 0$，$R = x-y$，计算散度 $P_x+Q_y+R_z$，用高斯公式化为三重积分，再换柱面坐标。

### Answer

$$
P = (y-z)x,\quad Q = 0,\quad R = x-y.
$$

$$
\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = (y-z) + 0 + 0 = y - z.
$$

由高斯公式：

$$
\iint_\Sigma = \iiint_\Omega (y-z)\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z.
$$

换柱面坐标 $x = \rho\cos\theta$，$y = \rho\sin\theta$：

$$
= \int_0^{2\pi}\!\mathrm{d}\theta\int_0^1\rho\,\mathrm{d}\rho\int_0^3(\rho\sin\theta - z)\,\mathrm{d}z.
$$

内层对 $z$：$\displaystyle\int_0^3(\rho\sin\theta-z)\,\mathrm{d}z = 3\rho\sin\theta - \frac{9}{2}$。

对 $\rho$：$\displaystyle\int_0^1\rho(3\rho\sin\theta - \frac{9}{2})\,\mathrm{d}\rho = \sin\theta - \frac{9}{4}$。

对 $\theta$：$\displaystyle\int_0^{2\pi}\left(\sin\theta-\frac{9}{4}\right)\mathrm{d}\theta = 0 - \frac{9\pi}{2} = -\frac{9\pi}{2}$.
