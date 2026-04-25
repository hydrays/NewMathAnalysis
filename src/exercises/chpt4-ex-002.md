---
id: chpt4-ex-002
chapter: 4
tags: [不定积分, 黎曼和]
difficulty: medium
video:
---

## Problem

用定义（黎曼和极限）计算定积分 $\displaystyle\int_0^1 x^2\,dx$。

## Solution 1

### Hint

将 $[0,1]$ 等分为 $n$ 份，取右端点，利用平方和公式 $\sum_{i=1}^n i^2 = \dfrac{n(n+1)(2n+1)}{6}$ 化简黎曼和，令 $n\to\infty$。

### Answer

将 $[0,1]$ $n$ 等分，$\Delta x = \dfrac{1}{n}$，取 $\xi_i = \dfrac{i}{n}$。

黎曼和为：

$$
S_n = \sum_{i=1}^n \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n} = \frac{1}{n^3} \sum_{i=1}^n i^2 = \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6n^2}
$$

令 $n\to\infty$：

$$
\int_0^1 x^2\,dx = \lim_{n\to\infty} \frac{(n+1)(2n+1)}{6n^2} = \frac{1}{3}
$$
