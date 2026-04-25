---
id: chpt2-ex-005
chapter: 2
tags: [导数, 幂函数, 二项式定理]
difficulty: medium
video:
---

## Problem

求正整数次幂函数 $f(x) = x^m$ 的导数（$m$ 为正整数）。

## Solution 1

### Hint

分 $m=1$ 和 $m>1$ 两种情况，后者利用二项式定理展开 $(x+\Delta x)^m$，提取 $\Delta x$ 后令其趋于零。

### Answer

当 $m = 1$ 时：

$$
f'(x) = \lim_{\Delta x \to 0} \frac{(x+\Delta x) - x}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta x}{\Delta x} = 1.
$$

当 $m > 1$ 时，利用二项式定理：

$$
\begin{align*}
f'(x) &= \lim_{\Delta x \to 0} \frac{(x+\Delta x)^m - x^m}{\Delta x} \\
&= \lim_{\Delta x \to 0} \left[ \frac{x^m + m x^{m-1} \Delta x + \frac{m(m-1)}{2} x^{m-2} (\Delta x)^2 + \cdots + (\Delta x)^m - x^m}{\Delta x} \right]\\
&= \lim_{\Delta x \to 0} \left[ m x^{m-1} + \frac{m(m-1)}{2} x^{m-2} \Delta x + \cdots + (\Delta x)^{m-1} \right] \\
&= m x^{m-1}.
\end{align*}
$$

考虑到 $x^0 = 1$，两种情况统一为：

$$
(x^m)' = m x^{m-1}, \quad m = 1, 2, \cdots
$$
