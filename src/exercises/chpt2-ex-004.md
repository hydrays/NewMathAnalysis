---
id: chpt2-ex-004
chapter: 2
tags: [导数, 导函数, 三角函数]
difficulty: medium
video:
---

## Problem

求函数 $f(x) = \cos x$ 的导数。

## Solution 1

### Hint

代入导数定义，用和差化积公式将 $\cos(x+\Delta x) - \cos x$ 变形，再利用 $\displaystyle\lim_{\theta\to 0}\frac{\sin\theta}{\theta}=1$。

### Answer

$$
\begin{align*}
f'(x) &= \lim_{\Delta x \to 0} \frac{\cos(x + \Delta x) - \cos x}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{-2 \sin\left( x + \frac{\Delta x}{2} \right) \sin\left( \frac{\Delta x}{2} \right)}{\Delta x} \\
&= - \lim_{\Delta x \to 0} \sin\left( x + \frac{\Delta x}{2} \right) \cdot \lim_{\Delta x \to 0} \frac{\sin \frac{\Delta x}{2}}{\frac{\Delta x}{2}} \\
&= -\sin x.
\end{align*}
$$
