---
id: chpt10-ex-020
chapter: 10
title: 隐函数的求导
tags: [隐函数, 隐函数定理, 偏导数]
difficulty: medium
video:
---

## Problem

验证方程 $x^2 + y^2 - 1 = 0$ 确定了一个隐函数，并求其一阶与二阶导数 $\displaystyle\frac{dy}{dx}$ 和 $\displaystyle\frac{d^2y}{dx^2}$.

## Solution 1

### Hint

令 $F(x,y) = x^2 + y^2 - 1$，用隐函数求导公式 $\frac{dy}{dx} = -\frac{F_x}{F_y}$，再对一阶导数关于 $x$ 求导（注意 $y$ 是 $x$ 的函数）得到二阶导数.

### Answer

设 $F(x,y) = x^2 + y^2 - 1$.

计算偏导数：$F_x = 2x$，$F_y = 2y$.

**一阶导数：**

当 $F_y = 2y \neq 0$（即 $y \neq 0$）时，由一元隐函数求导公式得：

$$\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}$$

**二阶导数：**

对一阶导数关于 $x$ 再求导，注意 $y$ 是 $x$ 的函数：

$$\begin{aligned}
\frac{d^2y}{dx^2} &= \frac{d}{dx}\left(-\frac{x}{y}\right) = -\frac{1 \cdot y - x \cdot \frac{dy}{dx}}{y^2} \\
&= -\frac{y - x\left(-\dfrac{x}{y}\right)}{y^2} = -\frac{y^2 + x^2}{y^3}
\end{aligned}$$

因为原方程给出 $x^2 + y^2 = 1$，代入后化简得最终结果：

$$\frac{d^2y}{dx^2} = -\frac{1}{y^3}$$
