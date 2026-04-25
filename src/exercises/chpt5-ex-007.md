---
id: chpt5-ex-007
chapter: 5
tags: [中值定理]
difficulty: medium
video:
---

## Problem

证明：若 $f(x)$ 在 $[a, b]$ 上连续，且 $\displaystyle\int_a^b f(x)\,dx = 0$，则存在 $c \in [a, b]$ 使得 $f(c) = 0$。

## Solution 1

### Hint

直接应用积分中值定理，得到 $f(c)(b-a) = 0$，再由 $b - a \neq 0$ 得结论。

### Answer

由积分中值定理，存在 $c \in [a, b]$，使得

$$
\int_a^b f(x)\,dx = f(c)(b - a) = 0
$$

由于 $b - a \neq 0$，故 $f(c) = 0$。
