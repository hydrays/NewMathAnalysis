---
id: chpt3-ex-011
chapter: 3
tags: [导数应用, 隐函数]
difficulty: medium
video:
---

## Problem

求由方程 $y^3 + 3y - x^2 - 2x^5 = 0$ 所确定的隐函数在 $x = 0$ 处的导数 $\left.\dfrac{dy}{dx}\right|_{x=0}$。

## Solution 1

### Hint

先对方程两边关于 $x$ 求导得到一般的导数公式，再求 $x=0$ 时对应的 $y$ 值，最后代入求值。

### Answer

对方程两边关于 $x$ 求导：

$$
3y^2\frac{dy}{dx} + 3\frac{dy}{dx} - 2x - 10x^4 = 0.
$$

解得：

$$
\frac{dy}{dx} = \frac{2x + 10x^4}{3y^2 + 3}.
$$

当 $x = 0$ 时，代入原方程 $y^3 + 3y = 0$，即 $y(y^2+3) = 0$，实数解为 $y = 0$。

代入导数公式：

$$
\left.\frac{dy}{dx}\right|_{x=0} = \frac{0}{0+3} = 0.
$$
