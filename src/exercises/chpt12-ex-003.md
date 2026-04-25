---
id: chpt12-ex-003
chapter: 12
tags: [曲线积分, 第二类曲线积分, 参数化]
difficulty: easy
video:
---

## Problem

计算 $\displaystyle W = \int_L \vec{F}\cdot\mathrm{d}\vec{r}$，其中 $\vec{F} = -y\hat{i} + x\hat{j}$，曲线 $L$ 由参数方程 $x = t$，$y = t^2$，$t \in [0,1]$ 给出。

## Solution 1

### Hint

将 $P = -y$，$Q = x$ 和曲线参数化代入公式 $W = \int P\,\mathrm{d}x + Q\,\mathrm{d}y$，化为对 $t$ 的定积分。

### Answer

$\mathrm{d}x = \mathrm{d}t$，$\mathrm{d}y = 2t\,\mathrm{d}t$。

$$
W = \int_L -y\,\mathrm{d}x + x\,\mathrm{d}y
= \int_0^1 \left(-t^2 \cdot 1 + t \cdot 2t\right)\mathrm{d}t
= \int_0^1 t^2\,\mathrm{d}t = \frac{1}{3}.
$$
