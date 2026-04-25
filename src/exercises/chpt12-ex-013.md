---
id: chpt12-ex-013
chapter: 12
tags: [格林公式, 面积公式]
difficulty: easy
video:
---

## Problem

利用格林公式，证明平面区域 $D$ 的面积可表示为

$$
\mathrm{Area}(D) = \oint_C x\,\mathrm{d}y,
$$

其中 $C$ 是 $D$ 的正向边界。

## Solution 1

### Hint

取 $P = 0$，$Q = x$，计算 $Q_x - P_y$，直接用格林公式。

### Answer

令 $P = 0$，$Q = x$，则 $Q_x - P_y = 1 - 0 = 1$。

由格林公式：

$$
\oint_C x\,\mathrm{d}y = \iint_D 1\,\mathrm{d}A = \mathrm{Area}(D). \qquad \square
$$
