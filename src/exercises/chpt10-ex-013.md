---
id: chpt10-ex-013
chapter: 10
tags: [多元极值, 无约束极值, 应用题]
difficulty: medium
video:
---

## Problem

有一宽为 $24\,\text{cm}$ 的长方形铁板，把它两边折起来做成断面为等腰梯形的水槽，问怎样折法才能使断面的面积最大？

## Solution 1

### Hint

设折起边长为 $x$，倾角为 $\alpha$，写出面积函数 $A(x,\alpha)$，令两个偏导数为零联立求解，再判断是否为极大值。

### Answer

设折起来的边长为 $x\,\text{cm}$，倾角为 $\alpha$，则梯形断面的：
- 下底长：$(24 - 2x)\,\text{cm}$
- 上底长：$(24 - 2x + 2x\cos\alpha)\,\text{cm}$
- 高：$x\sin\alpha\,\text{cm}$

断面面积：

$$
A(x,\alpha) = 24x\sin\alpha - 2x^2\sin\alpha + x^2\sin\alpha\cos\alpha, \quad 0 < x < 12,\ 0 < \alpha \leq \frac{\pi}{2}.
$$

令偏导数为零：

$$
\begin{cases}
A_x = 24\sin\alpha - 4x\sin\alpha + 2x\sin\alpha\cos\alpha = 0, \\
A_\alpha = 24x\cos\alpha - 2x^2\cos\alpha + x^2(\cos^2\alpha - \sin^2\alpha) = 0.
\end{cases}
$$

由 $\sin\alpha \neq 0$，$x \neq 0$，化简得：

$$
\begin{cases}
12 - 2x + x\cos\alpha = 0, \\
24\cos\alpha - 2x\cos\alpha + x(\cos^2\alpha - \sin^2\alpha) = 0.
\end{cases}
$$

解方程组，得唯一驻点：

$$
\alpha = \frac{\pi}{3} = 60°, \quad x = 8.
$$

由题意，面积最大值在开区域内取得，且只有此一个驻点，验证端点值更小，故当 $x = 8\,\text{cm}$，$\alpha = 60°$ 时，断面面积最大。
