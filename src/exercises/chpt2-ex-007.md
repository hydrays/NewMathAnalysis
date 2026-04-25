---
id: chpt2-ex-007
chapter: 2
tags: [导数, 乘积法则, 三角函数]
difficulty: medium
video:
---

## Problem

求函数 $y = 2e^{x}(\sin x + 2\cos x)$ 的导数。

## Solution 1

### Hint

把 $2e^x$ 和 $(\sin x + 2\cos x)$ 看作两个因子，应用乘积法则 $(uv)' = u'v + uv'$。

### Answer

$$
\begin{align*}
y' &= (2e^{x})'(\sin x + 2\cos x) + 2e^{x}(\sin x + 2\cos x)' \\
&= 2e^{x}(\sin x + 2\cos x) + 2e^{x}(\cos x - 2\sin x) \\
&= 2e^{x}\sin x + 4e^{x}\cos x + 2e^{x}\cos x - 4e^{x}\sin x \\
&= 6e^{x}\cos x - 2e^{x}\sin x \\
&= 2e^{x}(3\cos x - \sin x).
\end{align*}
$$
