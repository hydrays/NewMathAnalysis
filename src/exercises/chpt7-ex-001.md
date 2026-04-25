---
id: chpt7-ex-001
chapter: 7
title: 可分离变量方程
tags: [常微分方程, 分离变量法]
difficulty: easy
video:
---

## Problem

求解方程 $\displaystyle y' = \frac{y^2}{x^2}$。

## Solution 1

### Hint

将方程整理为变量分离形式，即将含 $y$ 的项移到左边，含 $x$ 的项移到右边，然后两边积分。

### Answer

方程可转换为变量分离的形式：

$$
\frac{dy}{y^2} = \frac{dx}{x^2}
$$

对等式两边积分得到

$$
-\frac{1}{y} = -\frac{1}{x} + C
$$

即

$$
y = \frac{x}{1 + kx}
$$

其中 $k$ 为常数。
