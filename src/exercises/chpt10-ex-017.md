---
id: chpt10-ex-017
chapter: 10
title: 高阶偏导数的计算
tags: [偏导数, 高阶导数, 混合偏导数]
difficulty: medium
video:
---

## Problem

设函数 $z = x^3 y^2 - 3xy^3 - xy + 1$，求下列高阶偏导数：

$$\frac{\partial^2 z}{\partial x^2},\quad \frac{\partial^2 z}{\partial y \partial x},\quad \frac{\partial^2 z}{\partial x \partial y},\quad \frac{\partial^2 z}{\partial y^2} \quad \text{及}\quad \frac{\partial^3 z}{\partial x^3}.$$

## Solution 1

### Hint

先分别求出对 $x$ 和对 $y$ 的一阶偏导数，再对结果继续求偏导. 注意混合偏导数 $\frac{\partial^2 z}{\partial y \partial x}$ 表示先对 $x$ 求偏导再对 $y$ 求偏导.

### Answer

**第一步：求一阶偏导数.**

$$\frac{\partial z}{\partial x} = 3x^2 y^2 - 3y^3 - y$$

$$\frac{\partial z}{\partial y} = 2x^3 y - 9xy^2 - x$$

**第二步：求二阶偏导数.**

$$\frac{\partial^2 z}{\partial x^2} = \frac{\partial}{\partial x}(3x^2 y^2 - 3y^3 - y) = 6xy^2$$

$$\frac{\partial^2 z}{\partial y \partial x} = \frac{\partial}{\partial y}(3x^2 y^2 - 3y^3 - y) = 6x^2 y - 9y^2 - 1$$

$$\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial}{\partial x}(2x^3 y - 9xy^2 - x) = 6x^2 y - 9y^2 - 1$$

$$\frac{\partial^2 z}{\partial y^2} = \frac{\partial}{\partial y}(2x^3 y - 9xy^2 - x) = 2x^3 - 18xy$$

注意两个混合偏导数相等，这与二阶混合偏导数在连续时与求导次序无关的定理一致.

**第三步：求三阶偏导数.**

$$\frac{\partial^3 z}{\partial x^3} = \frac{\partial}{\partial x}(6xy^2) = 6y^2$$
