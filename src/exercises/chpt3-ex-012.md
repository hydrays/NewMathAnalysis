---
id: chpt3-ex-012
chapter: 3
tags: [导数应用, 隐函数]
difficulty: medium
video:
---

## Problem

求双曲线 $\dfrac{x^2}{9} - \dfrac{y^2}{4} = 1$ 在点 $(3\sqrt{2},\, 2)$ 处的切线方程。

## Solution 1

### Hint

对双曲线方程两边关于 $x$ 隐式求导，解出 $\dfrac{dy}{dx}$，代入切点坐标求斜率，再写切线方程。

### Answer

对方程两边关于 $x$ 求导：

$$
\frac{2x}{9} - \frac{2y}{4}\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = \frac{2x}{9y}.
$$

在点 $(3\sqrt{2}, 2)$ 处的斜率：

$$
k = \frac{2 \times 3\sqrt{2}}{9 \times 2} = \frac{\sqrt{2}}{3}.
$$

切线方程：

$$
y - 2 = \frac{\sqrt{2}}{3}(x - 3\sqrt{2}) \implies \sqrt{2}x - 3y = 0.
$$
