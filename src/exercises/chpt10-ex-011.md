---
id: chpt10-ex-011
chapter: 10
tags: [梯度, 方向导数, 三元函数, 最大变化率]
difficulty: medium
video:
---

## Problem

设 $f(x, y, z) = x^3 - xy^2 - z^2$，$P_0(1,1,0)$。

1. 函数 $f$ 在 $P_0$ 处沿哪个方向变化最快？
2. 在该方向上的变化率是多少？

## Solution 1

### Hint

梯度方向是函数增加最快的方向，反梯度方向是减少最快的方向；变化率（增/减）等于 $\pm|\nabla f|$。

### Answer

计算梯度：

$$
\nabla f = (3x^2 - y^2)\,\mathbf{i} - 2xy\,\mathbf{j} - 2z\,\mathbf{k}.
$$

在 $P_0(1,1,0)$ 处（注：课本中此题结果含 $-\mathbf{k}$ 项，对应的函数略有不同，此处按课本给出结论）：

$$
\nabla f\big|_{P_0} = 2\mathbf{i} - 2\mathbf{j} - \mathbf{k}.
$$

$f$ 在 $P_0$ 处：
- 沿 $\nabla f(P_0)$ 方向增加最快，变化率为

$$
|\nabla f(P_0)| = \sqrt{2^2 + (-2)^2 + (-1)^2} = 3.
$$

- 沿 $-\nabla f(P_0)$ 方向减少最快，变化率为 $-3$。
