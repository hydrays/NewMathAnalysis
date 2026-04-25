---
id: chpt6-ex-006
chapter: 6
tags: [定积分, 弧长]
difficulty: easy
video:
---

## Problem

用参数方程下的弧长公式计算半径为 $R$ 的圆的周长。

## Solution 1

### Hint

圆的参数方程为 $x = R\cos t$，$y = R\sin t$（$0 \leq t \leq 2\pi$），代入参数弧长公式。

### Answer

$$
\frac{dx}{dt} = -R\sin t, \quad \frac{dy}{dt} = R\cos t.
$$

$$
L = \int_0^{2\pi} \sqrt{(-R\sin t)^2 + (R\cos t)^2}\,dt = \int_0^{2\pi} R\,dt = 2\pi R.
$$
