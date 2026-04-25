---
id: chpt10-ex-005
chapter: 10
tags: [高阶偏导数, 拉普拉斯方程, 验证]
difficulty: easy
video:
---

## Problem

验证函数 $z = \ln \sqrt{x^2 + y^2}$ 满足拉普拉斯方程

$$
\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 0.
$$

## Solution 1

### Hint

先将 $\ln\sqrt{x^2+y^2}$ 化简为 $\frac{1}{2}\ln(x^2+y^2)$，然后依次求一阶、二阶偏导数，最后相加。

### Answer

化简函数：

$$
z = \frac{1}{2} \ln(x^2 + y^2).
$$

求一阶偏导数：

$$
\frac{\partial z}{\partial x} = \frac{x}{x^2 + y^2}, \qquad \frac{\partial z}{\partial y} = \frac{y}{x^2 + y^2}.
$$

求二阶偏导数：

$$
\frac{\partial^2 z}{\partial x^2} = \frac{(x^2+y^2) - x \cdot 2x}{(x^2+y^2)^2} = \frac{y^2 - x^2}{(x^2+y^2)^2},
$$

$$
\frac{\partial^2 z}{\partial y^2} = \frac{(x^2+y^2) - y \cdot 2y}{(x^2+y^2)^2} = \frac{x^2 - y^2}{(x^2+y^2)^2}.
$$

验证：

$$
\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = \frac{y^2 - x^2 + x^2 - y^2}{(x^2+y^2)^2} = 0. \qquad \square
$$
