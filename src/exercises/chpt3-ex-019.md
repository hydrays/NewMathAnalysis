---
id: chpt3-ex-019
chapter: 3
tags: [导数应用, 隐函数, 高阶导数]
difficulty: hard
video:
---

## Problem

求由方程 $x + 2y - \dfrac{1}{3}\cos y = 0$ 所确定的隐函数的二阶导数 $\dfrac{d^2y}{dx^2}$。

## Solution 1

### Hint

先对原方程关于 $x$ 求导，解出一阶导数 $\dfrac{dy}{dx}$；再对 $\dfrac{dy}{dx}$ 的表达式关于 $x$ 求导，代入一阶导数化简。

### Answer

对原方程两边关于 $x$ 求导：

$$
1 + 2\frac{dy}{dx} + \frac{1}{3}\sin y \cdot \frac{dy}{dx} = 0,
$$

$$
\frac{dy}{dx}\left(2 + \frac{1}{3}\sin y\right) = -1,
$$

$$
\frac{dy}{dx} = \frac{-3}{6+\sin y}.
$$

对一阶导数再关于 $x$ 求导：

$$
\frac{d^2y}{dx^2} = \frac{3\cos y \cdot \frac{dy}{dx}}{(6+\sin y)^2} = \frac{3\cos y \cdot \frac{-3}{6+\sin y}}{(6+\sin y)^2} = \frac{-9\cos y}{(6+\sin y)^3}.
$$
