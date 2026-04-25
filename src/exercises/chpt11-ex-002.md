---
id: chpt11-ex-002
chapter: 11
tags: [二重积分, 累次积分, 圆形区域, 三角换元]
difficulty: medium
video:
---

## Problem

已知 $f(x,y) = 1-x^2-y^2$，$D = \{(x,y) \mid x^2+y^2 \leq 1,\ x > 0,\ y > 0\}$，计算

$$
\iint_D f(x,y)\,\mathrm{d}A.
$$

## Solution 1

### Hint

在第一象限单位圆域上，将二重积分化为累次积分：$y$ 的范围从 $0$ 到 $\sqrt{1-x^2}$，内层积分化简后外层用三角换元 $x = \sin\theta$ 求解。

### Answer

$$
\iint_D f(x,y)\,\mathrm{d}A = \int_0^1\!\left[\int_0^{\sqrt{1-x^2}}(1-x^2-y^2)\,\mathrm{d}y\right]\mathrm{d}x.
$$

**内层积分（对 $y$）：**

$$
\int_0^{\sqrt{1-x^2}}(1-x^2-y^2)\,\mathrm{d}y = \left[y - x^2 y - \frac{y^3}{3}\right]_0^{\sqrt{1-x^2}} = \frac{2}{3}(1-x^2)^{3/2}.
$$

**外层积分（对 $x$），令 $x = \sin\theta$，$\mathrm{d}x = \cos\theta\,\mathrm{d}\theta$：**

$$
\int_0^1 \frac{2}{3}(1-x^2)^{3/2}\,\mathrm{d}x
= \frac{2}{3}\int_0^{\pi/2}\cos^4\theta\,\mathrm{d}\theta
= \frac{2}{3} \cdot \frac{3\pi}{16} = \frac{\pi}{8}.
$$

（其中 $\displaystyle\int_0^{\pi/2}\cos^4\theta\,\mathrm{d}\theta = \frac{3\pi}{16}$ 由降幂公式得到。）
