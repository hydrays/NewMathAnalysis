---
id: chpt12-ex-006
chapter: 12
tags: [曲线积分, 两类曲线积分关系, 保守场]
difficulty: easy
video:
---

## Problem

已知 $\vec{F} = x\hat{i}+y\hat{j}$，求 $W = \displaystyle\int_L \vec{F}\cdot\mathrm{d}\vec{r}$，其中 $L$ 是任意闭合曲线（如图所示）。

## Solution 1

### Hint

$\vec{F} = \nabla f$ 其中 $f = \frac{1}{2}(x^2+y^2)$，保守场沿闭合曲线的积分为零。

### Answer

由于 $\vec{F} = x\hat{i}+y\hat{j} = \nabla\left(\dfrac{x^2+y^2}{2}\right)$ 是一个梯度场（保守场），

$$
W = \oint_L \vec{F}\cdot\mathrm{d}\vec{r} = 0.
$$
