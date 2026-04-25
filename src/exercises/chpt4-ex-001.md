---
id: chpt4-ex-001
chapter: 4
tags: [不定积分, 黎曼和]
difficulty: medium
video:
---

## Problem

用定义（黎曼和极限）计算定积分 $\displaystyle\int_0^1 x\,dx$。

## Solution 1

### Hint

将 $[0,1]$ 等分为 $n$ 份，取每个小区间的右端点作为 $\xi_i$，写出黎曼和，利用等差数列求和公式化简，然后令 $n\to\infty$。

### Answer

将 $[0,1]$ $n$ 等分，$\Delta x = \dfrac{1}{n}$，取 $\xi_i = \dfrac{i}{n}$（右端点）。

黎曼和为：

$$
S_n = \sum_{i=1}^n \frac{i}{n} \cdot \frac{1}{n} = \frac{1}{n^2} \sum_{i=1}^n i = \frac{1}{n^2} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2n}
$$

令 $n\to\infty$：

$$
\int_0^1 x\,dx = \lim_{n\to\infty} \frac{n+1}{2n} = \frac{1}{2}
$$
