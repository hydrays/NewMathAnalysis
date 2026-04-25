---
id: chpt2-ex-011
chapter: 2
tags: [高阶导数, 幂函数]
difficulty: hard
video:
---

## Problem

求幂函数 $y = x^{a}$（$a$ 是任意常数）的 $n$ 阶导数 $y^{(n)}$。

## Solution 1

### Hint

逐次求导，观察规律：每次求导乘以递减的因子，指数减 1；对整数次幂的情形讨论 $m \le n$ 与 $m > n$ 两种情况。

### Answer

逐次求导：

$$
\begin{align*}
y' &= a x^{a-1},\\
y'' &= a (a - 1) x^{a-2},\\
y''' &= a (a - 1)(a - 2) x^{a-3}.
\end{align*}
$$

一般的：

$$
y^{(n)} = a (a - 1)(a - 2) \cdots (a - n + 1) x^{a-n}.
$$

特别地，当 $a = n$ 为正整数时：

$$
(x^n)^{(m)} =
\begin{cases}
C_n^m \, m! \, x^{n-m}, & m \le n, \\
0, & m > n.
\end{cases}
$$
