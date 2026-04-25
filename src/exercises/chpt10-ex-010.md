---
id: chpt10-ex-010
chapter: 10
tags: [梯度, 偏导数, 二元函数]
difficulty: easy
video:
---

## Problem

求函数 $f(x, y) = \dfrac{1}{x^2 + y^2}$ 的梯度 $\mathrm{grad}\, f$。

## Solution 1

### Hint

分别对 $x$ 和 $y$ 求偏导数，再写成梯度向量 $\nabla f = f_x \mathbf{i} + f_y \mathbf{j}$ 的形式。

### Answer

$$
\frac{\partial f}{\partial x} = -\frac{2x}{(x^2+y^2)^2}, \qquad \frac{\partial f}{\partial y} = -\frac{2y}{(x^2+y^2)^2}.
$$

因此：

$$
\mathrm{grad}\, \frac{1}{x^2+y^2} = -\frac{2x}{(x^2+y^2)^2}\,\mathbf{i} - \frac{2y}{(x^2+y^2)^2}\,\mathbf{j}.
$$
