---
id: chpt10-ex-021
chapter: 10
title: 梯度的计算
tags: [梯度, 方向导数, 多元函数]
difficulty: easy
video:
---

## Problem

求函数 $f(x,y,z) = x^2 + yz$ 在点 $(1,2,3)$ 处的梯度.

## Solution 1

### Hint

分别计算三个偏导数，然后代入给定点的坐标.

### Answer

计算各偏导数：

$$\frac{\partial f}{\partial x} = 2x, \quad \frac{\partial f}{\partial y} = z, \quad \frac{\partial f}{\partial z} = y$$

在点 $(1,2,3)$ 处代入：

$$\nabla f\big|_{(1,2,3)} = \left(2x,\ z,\ y\right)\big|_{(1,2,3)} = (2,\ 3,\ 2)$$

即 $\text{grad}\, f(1,2,3) = 2\,\mathbf{i} + 3\,\mathbf{j} + 2\,\mathbf{k}$.
