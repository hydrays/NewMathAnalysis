---
id: chpt12-ex-010
chapter: 12
tags: [格林公式, 旋转场, 面积]
difficulty: easy
video:
---

## Problem

设 $\vec{F} = -y\hat{i}+x\hat{j}$，利用格林公式计算 $\oint_C \vec{F}\cdot\mathrm{d}\vec{r}$，其中 $C$ 是某封闭区域 $D$ 的正向边界。

## Solution 1

### Hint

计算 $\mathrm{curl}\,\vec{F} = Q_x - P_y$，然后用格林公式将曲线积分化为面积分。

### Answer

$$
\mathrm{curl}\,\vec{F} = \frac{\partial x}{\partial x} - \frac{\partial(-y)}{\partial y} = 1 + 1 = 2.
$$

由格林公式：

$$
\oint_C -y\,\mathrm{d}x + x\,\mathrm{d}y = \iint_D 2\,\mathrm{d}A = 2\,\mathrm{Area}(D).
$$
