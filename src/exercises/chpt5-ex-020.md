---
id: chpt5-ex-020
chapter: 5
title: 利用泰勒展开计算π的近似值
tags: [泰勒展开, 数值计算]
difficulty: medium
video:
---

## Problem

利用 $\arctan x$ 的泰勒展开计算 $\pi$ 的近似值，并估计要达到小数点后 6 位精度需要多少项。

## Solution 1

### Hint

利用 $\arctan 1 = \pi/4$ 以及拉格朗日余项来估计截断误差。

### Answer

利用 $\arctan x$ 的泰勒展开：
$$
\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots
$$

取 $x = 1$，得：
$$
\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
$$

使用拉格朗日余项估计误差：要计算 $\pi$ 到小数点后 6 位，需要：
$$
|R_n(1)| \leq \frac{1}{2n+1} < 10^{-6}
$$

解得 $n > 5 \times 10^5$，即需要约 50 万项。这说明虽然泰勒展开理论上是精确的，但实际计算时收敛速度可能很慢。
