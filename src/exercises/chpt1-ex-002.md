---
id: chpt1-ex-002
chapter: 1
tags: [极限, 夹逼定理]
difficulty: easy
video:
---

## Problem

求极限 $\displaystyle\lim_{n\to\infty}\frac{\sin n}{n}$.

## Solution 1

### Hint
$|\sin n| \leq 1$ 对所有整数 $n$ 成立. 用夹逼定理.

### Answer
因为 $|\sin n| \leq 1$, 所以

$$-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}.$$

由于 $\displaystyle\lim_{n\to\infty}\frac{1}{n} = 0$, 由夹逼定理得

$$\lim_{n\to\infty}\frac{\sin n}{n} = 0. \quad\blacksquare$$
