---
id: chpt10-ex-018
chapter: 10
title: 复合函数的全导数
tags: [全微分, 复合函数, 链式法则]
difficulty: medium
video:
---

## Problem

设 $z = uv + \sin t$，而 $u = e^t$，$v = \cos t$，求全导数 $\displaystyle\frac{dz}{dt}$.

## Solution 1

### Hint

注意 $z$ 不仅通过中间变量 $u, v$ 依赖于 $t$，还直接依赖于 $t$. 链式法则需增加一项对 $t$ 的直接偏导数.

### Answer

由链式法则，$z$ 对 $t$ 的全导数为：

$$\frac{dz}{dt} = \frac{\partial z}{\partial u}\frac{du}{dt} + \frac{\partial z}{\partial v}\frac{dv}{dt} + \frac{\partial z}{\partial t}$$

计算各偏导数：

$$\frac{\partial z}{\partial u} = v, \quad \frac{\partial z}{\partial v} = u, \quad \frac{\partial z}{\partial t} = \cos t$$

计算中间变量的导数：

$$\frac{du}{dt} = e^t, \quad \frac{dv}{dt} = -\sin t$$

代入得：

$$\begin{aligned}
\frac{dz}{dt} &= v \cdot e^t + u \cdot (-\sin t) + \cos t \\
&= e^t \cos t - e^t \sin t + \cos t \\
&= e^t(\cos t - \sin t) + \cos t.
\end{aligned}$$
