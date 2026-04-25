---
id: chpt12-ex-008
chapter: 12
tags: [曲线积分, 第二类曲线积分, 路径无关]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\int_L 2xy\,\mathrm{d}x + x^2\,\mathrm{d}y$，其中 $L$ 为：

1. 抛物线 $y = x^2$ 上从 $O(0,0)$ 到 $B(1,1)$ 的一段弧。
2. 抛物线 $x = y^2$ 上从 $O(0,0)$ 到 $B(1,1)$ 的一段弧。
3. 有向折线 $O(0,0) \to A(1,0) \to B(1,1)$。

## Solution 1

### Hint

注意 $P = 2xy$，$Q = x^2$，有 $\frac{\partial Q}{\partial x} = 2x = \frac{\partial P}{\partial y}$，故积分路径无关，三条路径结果相同。可用任意一条计算。

### Answer

**路径 (1)（$y = x^2$，$x \in [0,1]$）：**

$$
\int_L 2xy\,\mathrm{d}x+x^2\,\mathrm{d}y
= \int_0^1\left(2x\cdot x^2 + x^2\cdot 2x\right)\mathrm{d}x
= \int_0^1 \left(2x^{\frac{3}{2}+1} + \frac{1}{2}x^{\frac{3}{2}}\right)\mathrm{d}x.
$$

更直接地：$\mathrm{d}y = 2x\,\mathrm{d}x$，

$$
= \int_0^1(2x^3 + 2x^3)\,\mathrm{d}x = \ldots
$$

令 $y=x^2$，则 $dy = 2x\,dx$：

$$
= \int_0^1\left(2x\cdot x^2 + x^2 \cdot 2x\right)\mathrm{d}x = \int_0^1 4x^3\,\mathrm{d}x.
$$

但最简单的方式：$P\,dx+Q\,dy = d(x^2 y)$（因为 $Q = x^2$ 是 $P\,dx + Q\,dy$ 的势函数 $f = x^2 y$ 的全微分），

$$
\int_O^B d(x^2 y) = \left[x^2 y\right]_{(0,0)}^{(1,1)} = 1.
$$

**结论：三条路径的积分值均为 $1$，积分路径无关。**
