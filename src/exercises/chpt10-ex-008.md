---
id: chpt10-ex-008
chapter: 10
tags: [全微分, 高阶无穷小]
difficulty: easy
video:
---

## Problem

求函数 $z(x,y) = x^2 + 2y^3$ 的全微分 $dz$。

## Solution 1

### Hint

展开增量 $\Delta z$，保留一阶项（线性主部），高阶无穷小项舍去，即得全微分。

### Answer

考虑自变量的微小变化 $x \to x+dx$，$y \to y+dy$：

$$
z(x+dx, y+dy) = (x+dx)^2 + 2(y+dy)^3.
$$

展开并识别各阶项：

$$
\Delta z = 2x\,dx + 6y^2\,dy + \underbrace{dx^2 + 6y\,dy^2 + 2\,dy^3}_{\text{高阶无穷小}}.
$$

偏导数：$\dfrac{\partial z}{\partial x} = 2x$，$\dfrac{\partial z}{\partial y} = 6y^2$。

全微分（取线性主部）：

$$
dz = 2x\,dx + 6y^2\,dy.
$$
