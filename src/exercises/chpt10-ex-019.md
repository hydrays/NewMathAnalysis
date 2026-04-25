---
id: chpt10-ex-019
chapter: 10
title: 全微分形式不变性
tags: [全微分, 微分形式不变性]
difficulty: medium
video:
---

## Problem

设 $z = e^u \sin v$，而 $u = xy$，$v = x+y$，利用全微分形式不变性求偏导数 $\displaystyle\frac{\partial z}{\partial x}$ 和 $\displaystyle\frac{\partial z}{\partial y}$.

## Solution 1

### Hint

先写出外层函数关于中间变量 $u, v$ 的全微分，再将 $du$、$dv$ 用 $dx$、$dy$ 表示并代入，比较系数即可直接读出偏导数.

### Answer

**第一步：写出外层函数的全微分.**

$$dz = d(e^u \sin v) = e^u \sin v \, du + e^u \cos v \, dv$$

**第二步：计算中间变量的微分.**

$$du = d(xy) = y \, dx + x \, dy$$

$$dv = d(x+y) = dx + dy$$

**第三步：将 $du$、$dv$ 代入 $dz$ 并合并同类项.**

$$\begin{aligned}
dz &= e^u \sin v (y \, dx + x \, dy) + e^u \cos v (dx + dy) \\
&= \left[y e^u \sin v + e^u \cos v\right] dx + \left[x e^u \sin v + e^u \cos v\right] dy
\end{aligned}$$

**第四步：比较系数，回代 $u = xy$，$v = x+y$，直接读出偏导数.**

$$\frac{\partial z}{\partial x} = e^{xy}\left[y \sin(x+y) + \cos(x+y)\right]$$

$$\frac{\partial z}{\partial y} = e^{xy}\left[x \sin(x+y) + \cos(x+y)\right]$$
