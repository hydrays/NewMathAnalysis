---
id: chpt11-ex-007
chapter: 11
tags: [二重积分, 极坐标, 体积, 重积分应用]
difficulty: hard
video:
---

## Problem

求球体 $x^2 + y^2 + z^2 \leq 4a^2$ 被圆柱面 $x^2 + y^2 = 2ax$（$a > 0$）截得的含在圆柱面内的立体体积。

## Solution 1

### Hint

利用对称性，体积为上半部分的 4 倍：$V = 4\iint_D \sqrt{4a^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y$，其中 $D$ 为圆柱截面在 $xy$ 平面的投影。换极坐标：$x^2+y^2=2ax$ 变为 $\rho = 2a\cos\theta$，内层对 $\rho$ 积分用凑微分。

### Answer

利用上下对称性：

$$
V = 4\iint_D \sqrt{4a^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y,
$$

其中 $D: x^2+y^2 \leq 2ax$，即极坐标下 $0 \leq \rho \leq 2a\cos\theta$，$-\pi/2 \leq \theta \leq \pi/2$。

$$
V = 4\int_0^{\pi/2}\!\int_0^{2a\cos\theta}\sqrt{4a^2-\rho^2}\,\rho\,\mathrm{d}\rho\,\mathrm{d}\theta.
$$

**内层积分（令 $u = 4a^2-\rho^2$）：**

$$
\int_0^{2a\cos\theta}\sqrt{4a^2-\rho^2}\,\rho\,\mathrm{d}\rho
= \left[-\frac{1}{3}(4a^2-\rho^2)^{3/2}\right]_0^{2a\cos\theta}
= \frac{8a^3}{3}(1 - \sin^3\theta).
$$

**外层积分：**

$$
V = 4\int_0^{\pi/2}\frac{8a^3}{3}(1-\sin^3\theta)\,\mathrm{d}\theta
= \frac{32a^3}{3}\left[\frac{\pi}{2} - \frac{2}{3}\right]
= \frac{32a^3}{3}\left(\frac{\pi}{2}-\frac{2}{3}\right).
$$
