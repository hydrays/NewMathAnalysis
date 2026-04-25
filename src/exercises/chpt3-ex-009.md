---
id: chpt3-ex-009
chapter: 3
tags: [导数应用, 链式法则]
difficulty: medium
video:
---

## Problem

设 $y = \cos 2x \cdot \cos^2 x$，求 $y'$。

## Solution 1

### Hint

用乘积法则求导，对 $\cos 2x$ 和 $\cos^2 x$ 分别求导，最后利用二倍角公式化简。

### Answer

$$
\begin{aligned}
y' &= (\cos 2x)'\cos^2 x + \cos 2x(\cos^2 x)' \\
&= -2\sin 2x\cos^2 x + \cos 2x \cdot (-2\sin x\cos x) \\
&= -2\cos x(\sin 2x\cos x + \cos 2x\sin x) \\
&= -2\cos x\sin 3x.
\end{aligned}
$$

（最后一步利用了 $\sin(2x + x) = \sin 2x\cos x + \cos 2x\sin x$。）
