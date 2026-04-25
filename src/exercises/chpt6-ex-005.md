---
id: chpt6-ex-005
chapter: 6
tags: [定积分, 弧长, 换元法]
difficulty: medium
video:
---

## Problem

计算曲线 $y = x^{3/2}$ 从 $x=0$ 到 $x=1$ 的弧长。

## Solution 1

### Hint

用弧长公式 $L = \displaystyle\int_0^1 \sqrt{1 + [f'(x)]^2}\,dx$，令 $u = 1 + \dfrac{9}{4}x$ 换元求积分。

### Answer

$f'(x) = \dfrac{3}{2}x^{1/2}$，故

$$
L = \int_0^1 \sqrt{1 + \frac{9}{4}x}\,dx.
$$

令 $u = 1 + \dfrac{9}{4}x$，则 $du = \dfrac{9}{4}dx$；当 $x=0$ 时 $u=1$，当 $x=1$ 时 $u=\dfrac{13}{4}$。

$$
L = \frac{4}{9}\int_1^{13/4} \sqrt{u}\,du = \frac{4}{9} \cdot \frac{2}{3}u^{3/2}\Big|_1^{13/4} = \frac{8}{27}\left[\left(\frac{13}{4}\right)^{3/2} - 1\right].
$$
