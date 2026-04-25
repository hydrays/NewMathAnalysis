---
id: chpt3-ex-010
chapter: 3
tags: [导数应用, 隐函数]
difficulty: medium
video:
---

## Problem

求由方程 $\ln y + x^2y - 1 = 0$ 所确定的隐函数的导数 $\dfrac{dy}{dx}$。

## Solution 1

### Hint

对方程两边关于 $x$ 求导，注意 $y$ 是 $x$ 的函数，对含 $y$ 的项使用链式法则，再解出 $\dfrac{dy}{dx}$。

### Answer

对方程两边关于 $x$ 求导：

$$
\frac{1}{y}\frac{dy}{dx} + 2xy + x^2\frac{dy}{dx} = 0.
$$

合并含 $\dfrac{dy}{dx}$ 的项：

$$
\left(\frac{1}{y} + x^2\right)\frac{dy}{dx} = -2xy.
$$

解得（$y \neq 0$）：

$$
\frac{dy}{dx} = -\frac{2xy}{\frac{1}{y}+x^2} = -\frac{2xy^2}{1+x^2y}.
$$
