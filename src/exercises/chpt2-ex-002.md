---
id: chpt2-ex-002
chapter: 2
tags: [导数, 幂函数]
difficulty: easy
video:
---

## Problem

求函数 $f(x) = x^2$ 在 $x_0 = 2$ 处的导数。

## Solution 1

### Hint

代入导数定义，展开 $(2 + \Delta x)^2$ 后化简，令 $\Delta x \to 0$。

### Answer

根据导数的定义：

$$
\begin{align*}
f'(2) &= \lim_{\Delta x \to 0} \frac{(2 + \Delta x)^2 - 2^2}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{4 + 4\Delta x + (\Delta x)^2 - 4}{\Delta x} \\
&= \lim_{\Delta x \to 0} (4 + \Delta x) = 4.
\end{align*}
$$
