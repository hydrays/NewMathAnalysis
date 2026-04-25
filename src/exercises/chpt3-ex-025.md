---
id: chpt3-ex-025
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to +\infty} \frac{x^n}{e^{\lambda x}}$（$n$ 为正整数，$\lambda > 0$）。

## Solution 1

### Hint

$\infty/\infty$ 型，对分子连续求导 $n$ 次直到分子变为常数，期间分母始终是指数函数。

### Answer

相继对分子分母求导 $n$ 次：

$$
\lim_{x \to +\infty} \frac{x^n}{e^{\lambda x}} = \lim_{x \to +\infty} \frac{nx^{n-1}}{\lambda e^{\lambda x}} = \cdots = \lim_{x \to +\infty} \frac{n!}{\lambda^n e^{\lambda x}} = 0.
$$

这说明指数函数趋于无穷的速度比任何幂函数都快。
