---
id: chpt12-ex-001
chapter: 12
tags: [曲线积分, 第一类曲线积分, 弧长]
difficulty: medium
video:
---

## Problem

计算曲线积分

$$
\int_L \sqrt{y}\,\mathrm{d}s,
$$

其中 $L$ 是抛物线 $y = x^2$ 上从点 $O(0,0)$ 到点 $B(1,1)$ 之间的一段弧。

## Solution 1

### Hint

将 $L$ 表示为 $y = x^2$（$0 \leq x \leq 1$），则 $\mathrm{d}s = \sqrt{1+(y')^2}\,\mathrm{d}x = \sqrt{1+4x^2}\,\mathrm{d}x$，代入积分后用换元法。

### Answer

$$
\int_L \sqrt{y}\,\mathrm{d}s
= \int_0^1 \sqrt{x^2}\sqrt{1+\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\,\mathrm{d}x
= \int_0^1 x\sqrt{1+4x^2}\,\mathrm{d}x.
$$

令 $u = 1+4x^2$，$\mathrm{d}u = 8x\,\mathrm{d}x$：

$$
= \left[\frac{1}{12}(1+4x^2)^{3/2}\right]_0^1 = \frac{1}{12}(5\sqrt{5} - 1).
$$
