---
id: chpt3-ex-003
chapter: 3
tags: [导数应用, 链式法则]
difficulty: easy
video:
---

## Problem

设函数 $y = \mathrm{e}^{x^2}$，求 $\dfrac{dy}{dx}$。

## Solution 1

### Hint

将 $y = \mathrm{e}^{x^2}$ 看作复合函数，令中间变量 $u = x^2$，再用链式法则。

### Answer

令 $u = x^2$，则 $y = \mathrm{e}^u$，故

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \mathrm{e}^u \cdot 2x = 2x\mathrm{e}^{x^2}.
$$
