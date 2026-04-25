---
id: chpt11-ex-004
chapter: 11
tags: [二重积分, 累次积分, 积分顺序交换]
difficulty: hard
video:
---

## Problem

计算 $\displaystyle\iint_{D} y\sqrt{1+x^2-y^2}\,\mathrm{d}\sigma$，其中 $D$ 由直线 $y = x$、$x = -1$ 及 $y = 1$ 围成的闭区域。

## Solution 1

### Hint

选取先对 $y$（从 $x$ 到 $1$）后对 $x$（从 $-1$ 到 $1$）的积分顺序，内层积分对 $y$ 用凑微分法：$y\,\mathrm{d}y = -\dfrac{1}{2}\mathrm{d}(1+x^2-y^2)$。

### Answer

$$
\iint_D y\sqrt{1+x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y
= \int_{-1}^1\!\mathrm{d}x\int_x^1 y\sqrt{1+x^2-y^2}\,\mathrm{d}y.
$$

**内层积分（对 $y$）：** 令 $u = 1+x^2-y^2$，则 $\mathrm{d}u = -2y\,\mathrm{d}y$：

$$
\int_x^1 y\sqrt{1+x^2-y^2}\,\mathrm{d}y
= \left[-\frac{1}{3}(1+x^2-y^2)^{3/2}\right]_x^1
= \frac{1}{3}|x|^3 - \frac{1}{3}\cdot 0 = \frac{1}{3}|x|^3.
$$

（当 $y = 1$：$1+x^2-1 = x^2$，$(x^2)^{3/2} = |x|^3$；当 $y=x$：$1+x^2-x^2 = 1$，$(1)^{3/2}=1$。）

$$
\int_x^1 y\sqrt{1+x^2-y^2}\,\mathrm{d}y = \frac{1}{3}(1 - |x|^3).
$$

**外层积分（对 $x$，利用偶函数对称）：**

$$
\int_{-1}^1 \frac{1}{3}(1-|x|^3)\,\mathrm{d}x
= \frac{2}{3}\int_0^1(1-x^3)\,\mathrm{d}x
= \frac{2}{3}\left[x - \frac{x^4}{4}\right]_0^1
= \frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2}.
$$
