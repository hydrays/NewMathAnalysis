---
id: chpt5-ex-008
chapter: 5
tags: [中值定理]
difficulty: medium
video:
figures:
  - file: chpt5_ex008.png
    alt: $\int_0^1 e^{-x^2}\,dx$ 的下界 $e^{-1}$ (红虚) 与上界 $1$ (绿虚) 之间夹住真实值
    where: problem
---

## Problem

估计积分 $\displaystyle\int_0^1 e^{-x^2}\,dx$ 的值范围。

## Solution 1

### Hint

在 $[0, 1]$ 上确定 $f(x) = e^{-x^2}$ 的最大值和最小值，用积分的比较性质（或积分中值定理）夹出积分范围。

### Answer

函数 $f(x) = e^{-x^2}$ 在 $[0, 1]$ 上连续，且由于 $0 \leq x^2 \leq 1$，有

$$
e^{-1} \leq e^{-x^2} \leq 1
$$

由积分中值定理，存在 $c \in [0, 1]$，使得

$$
\int_0^1 e^{-x^2}\,dx = e^{-c^2}
$$

由 $e^{-1} \leq e^{-c^2} \leq 1$，得

$$
\frac{1}{e} \leq \int_0^1 e^{-x^2}\,dx \leq 1
$$
