---
id: chpt2-ex-003
chapter: 2
tags: [导数, 导函数, 幂函数]
difficulty: easy
video:
---

## Problem

求函数 $f(x) = x^2$ 的导函数。

## Solution 1

### Hint

代入导数定义，对一般的 $x$ 展开并化简，令 $\Delta x \to 0$。

### Answer

$$
\begin{align*}
f'(x) &= \lim_{\Delta x\to 0} \frac{(x+\Delta x)^2 - x^2}{\Delta x}\\
&= \lim_{\Delta x\to 0} \frac{2x\Delta x + \Delta x^2}{\Delta x} \\
&= \lim_{\Delta x\to 0} (2x + \Delta x) = 2x.
\end{align*}
$$
