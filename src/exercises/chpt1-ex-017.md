---
id: chpt1-ex-017
chapter: 1
tags: [连续性, 间断点, 函数极限]
difficulty: medium
video:
---

## Problem

讨论函数 $f(x) = \sin\dfrac{1}{x}$ 在 $x=0$ 处的连续性。若不连续，判断间断点类型，并说明能否通过补充定义使其连续。

## Solution 1

### Hint

考察 $x \to 0$ 时 $\sin\dfrac{1}{x}$ 的极限行为：取特殊数列 $x_n \to 0$ 使得 $\sin\dfrac{1}{x_n}$ 取不同值，说明极限不存在。

### Answer

$f(x) = \sin\dfrac{1}{x}$ 在 $x=0$ 处无定义，故 $x=0$ 是间断点。

当 $x \to 0$ 时，$\dfrac{1}{x} \to \infty$，$\sin\dfrac{1}{x}$ 在 $-1$ 和 $1$ 之间无限振荡，极限不存在。

例如，取 $x_n = \dfrac{1}{n\pi}$，则 $\sin\dfrac{1}{x_n} = \sin(n\pi) = 0$；取 $x_n = \dfrac{2}{(4n+1)\pi}$，则 $\sin\dfrac{1}{x_n} = 1$。

因此 $x=0$ 是**振荡间断点**（第二类间断点），无法通过补充定义一个点值使 $f(x)$ 在 $x=0$ 处连续。
