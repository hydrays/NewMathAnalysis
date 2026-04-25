---
id: chpt3-ex-006
chapter: 3
tags: [导数应用, 链式法则]
difficulty: easy
video:
---

## Problem

设 $y = \sqrt{1 + 3x^3}$，求 $\dfrac{dy}{dx}$。

## Solution 1

### Hint

将 $y = (1+3x^3)^{1/2}$ 视为复合函数，令 $u = 1+3x^3$，用链式法则。

### Answer

令 $u = 1+3x^3$，则 $y = u^{1/2}$。

$$
\frac{dy}{du} = \frac{1}{2}u^{-1/2} = \frac{1}{2\sqrt{1+3x^3}}, \quad \frac{du}{dx} = 9x^2.
$$

由链式法则：

$$
\frac{dy}{dx} = \frac{1}{2\sqrt{1+3x^3}} \cdot 9x^2 = \frac{9x^2}{2\sqrt{1+3x^3}}.
$$
