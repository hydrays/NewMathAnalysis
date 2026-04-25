---
id: chpt1-ex-024
chapter: 1
title: epsilon-delta证明 $\lim_{x\to 2}(x^2+1)=5$
tags: [极限, 极限计算]
difficulty: easy
video:
---

## Problem

用 $\varepsilon$-$\delta$ 语言证明 $\displaystyle\lim_{x \to 2}(x^2 + 1) = 5$。

## Solution 1

### Hint

将 $|f(x)-5|$ 分解为 $|x-2||x+2|$，先限制 $\delta_0=1$ 给 $|x+2|$ 一个上界，再用两者的最小值确定 $\delta$。

### Answer

**证明：** 对于任意给定的 $\varepsilon > 0$，要找到 $\delta$ 使得只要 $0 < |x-2|< \delta$，总有

$$
\begin{align*}
\left|f(x) - 5\right| &= \left| x^2+1 - 5\right| \\
 &= \left| x^2 - 4\right| \\
 &= \left| x - 2\right| \left| x + 2\right|.
\end{align*}
$$

为了把 $\left|x+2\right|$ 用常数束缚住，取 $\delta_0 = 1$。当 $|x-2|<\delta_0$ 时，$1<x<3$，因此

$$
|x+2|<5.
$$

所以在 $|x-2|<1$ 的情况下有

$$
|f(x)-5| = |x-2||x+2| < 5|x-2|.
$$

现在给定任意 $\varepsilon>0$，令

$$
\delta = \min\left\{1,\frac{\varepsilon}{5}\right\}.
$$

若 $0<|x-2|<\delta$，则同时有 $|x-2|<1$（从而 $|x+2|<5$）且 $|x-2|<\varepsilon/5$。因此

$$
|f(x)-5| < 5|x-2| < 5\cdot\frac{\varepsilon}{5} = \varepsilon.
$$

因此对任意 $\varepsilon>0$ 存在上述 $\delta>0$ 使得 $0<|x-2|<\delta$ 蕴含 $|f(x)-5|<\varepsilon$，于是

$$\displaystyle \lim_{x\to2} (x^2+1)=5.$$
