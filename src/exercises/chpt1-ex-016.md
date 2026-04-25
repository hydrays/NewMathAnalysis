---
id: chpt1-ex-016
chapter: 1
tags: [连续性, 间断点, 函数极限]
difficulty: easy
video:
---

## Problem

讨论函数 $\displaystyle f(x) = \frac{\sin x}{x}$ 的连续性。若存在间断点，判断其类型，并说明能否通过补充定义使其成为连续函数。

## Solution 1

### Hint

$f(x)$ 在 $x=0$ 处没有定义，但计算 $\lim_{x\to 0}\dfrac{\sin x}{x}$ 可以判断该间断点是否可去。

### Answer

$f(x) = \dfrac{\sin x}{x}$ 在 $x=0$ 处无定义，故 $x=0$ 是间断点。

由重要极限：

$$\lim_{x\rightarrow 0} \frac{\sin x}{x} = 1.$$

由于极限存在但函数在该点无定义，$x=0$ 是**可去间断点**。

只要令 $f(0) = 1$，即补充定义

$$\tilde{f}(x) = \begin{cases} \dfrac{\sin x}{x}, & x \neq 0, \\ 1, & x = 0, \end{cases}$$

则 $\tilde{f}(x)$ 在 $(-\infty, +\infty)$ 上处处连续。
