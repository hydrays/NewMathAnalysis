---
id: chpt11-ex-006
chapter: 11
tags: [二重积分, 极坐标, 重积分应用]
difficulty: medium
video:
---

## Problem

如图所示，求

$$
I = \iint_D (1 + \rho^2 - 2\rho\cos\theta)\,\rho\,\mathrm{d}\rho\,\mathrm{d}\theta,
$$

其中积分区域 $D$ 由极坐标曲线 $\rho = 2\cos\theta$ 围成。

## Solution 1

### Hint

区域为 $0 \leq \rho \leq 2\cos\theta$，$-\pi/2 \leq \theta \leq \pi/2$；展开被积函数后逐项积分。

### Answer

$$
I = \int_{-\pi/2}^{\pi/2}\!\int_0^{2\cos\theta}(1+\rho^2-2\rho\cos\theta)\,\rho\,\mathrm{d}\rho\,\mathrm{d}\theta = \frac{\pi}{2}.
$$

## Solution 2

### Hint

注意 $D$ 是以 $(1,0)$ 为圆心、半径为 $1$ 的圆盘（直角坐标下 $(x-1)^2+y^2=1$），利用直角坐标的对称性直接计算：

$$
I = \int_0^{2\pi}\!\int_0^1 \rho^2 \cdot \rho\,\mathrm{d}\rho\,\mathrm{d}\theta.
$$

### Answer

$$
I = \int_0^{2\pi}\!\int_0^1 \rho^3\,\mathrm{d}\rho\,\mathrm{d}\theta = 2\pi \cdot \frac{1}{4} = \frac{\pi}{2}.
$$
