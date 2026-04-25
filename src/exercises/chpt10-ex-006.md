---
id: chpt10-ex-006
chapter: 10
tags: [高阶偏导数, 拉普拉斯方程, 三元函数, 验证]
difficulty: medium
video:
---

## Problem

证明函数 $u = \dfrac{1}{r}$ 满足三维拉普拉斯方程

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} = 0,
$$

其中 $r = \sqrt{x^2 + y^2 + z^2}$。

## Solution 1

### Hint

先对 $x$ 求一阶偏导，利用复合函数求导得 $\dfrac{\partial r}{\partial x} = \dfrac{x}{r}$；再对 $x$ 求二阶偏导；由对称性写出 $y, z$ 方向的结果，最后求和。

### Answer

由 $r = \sqrt{x^2+y^2+z^2}$，有 $\dfrac{\partial r}{\partial x} = \dfrac{x}{r}$。

$$
\frac{\partial u}{\partial x} = -\frac{1}{r^2} \cdot \frac{\partial r}{\partial x} = -\frac{x}{r^3}.
$$

$$
\frac{\partial^2 u}{\partial x^2} = -\frac{r^3 - x \cdot 3r^2 \frac{\partial r}{\partial x}}{r^6} = -\frac{1}{r^3} + \frac{3x^2}{r^5}.
$$

由对称性：

$$
\frac{\partial^2 u}{\partial y^2} = -\frac{1}{r^3} + \frac{3y^2}{r^5}, \qquad \frac{\partial^2 u}{\partial z^2} = -\frac{1}{r^3} + \frac{3z^2}{r^5}.
$$

求和：

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}
= -\frac{3}{r^3} + \frac{3(x^2+y^2+z^2)}{r^5}
= -\frac{3}{r^3} + \frac{3r^2}{r^5}
= 0. \qquad \square
$$
