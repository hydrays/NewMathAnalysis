---
id: chpt6-ex-012
chapter: 6
tags: [定积分, 面积]
difficulty: easy
video:
---

## Problem

验证函数

$$
f(x) = \begin{cases} 2x & 0 \leq x \leq 1 \\ 0 & \text{其他} \end{cases}
$$

是否为概率密度函数。

## Solution 1

### Hint

检查两个条件：非负性（$f(x) \geq 0$）和归一性（积分等于 $1$）。

### Answer

**非负性**：在 $[0,1]$ 上 $2x \geq 0$，满足。

**归一性**：

$$
\int_{-\infty}^\infty f(x)\,dx = \int_0^1 2x\,dx = \left[x^2\right]_0^1 = 1.
$$

两个条件均满足，故 $f(x)$ 是合法的概率密度函数。
