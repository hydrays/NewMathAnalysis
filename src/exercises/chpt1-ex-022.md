---
id: chpt1-ex-022
chapter: 1
title: epsilon-delta证明 $\lim_{x\to 2}(5x+1)=11$
tags: [极限, epsilon-delta证明]
difficulty: medium
video:
---

## Problem

用 $\varepsilon$-$\delta$ 语言证明 $\displaystyle\lim_{x \to 2}(5x+1) = 11$。

## Solution 1

### Hint

估计 $|f(x) - 11|$，将其化为含 $|x-2|$ 的形式，再令其小于 $\varepsilon$ 来确定 $\delta$。

### Answer

**证明：** 由于

$$
\begin{align*}
|f(x) - 11| &= |(5x + 1) - 11| \\
 &= 5|x - 2| < \varepsilon
\end{align*}
$$

为了使 $5|x - 2| < \varepsilon$，只要 $\displaystyle |x - 2| < \frac{\varepsilon}{5}$。

取 $\displaystyle \delta = \frac{\varepsilon}{5}$，可知当 $0 < |x - 2| < \delta$ 时，总有 $\displaystyle |f(x) - 11| < \varepsilon$，从而

$$\lim_{x \rightarrow 2} f(x) = 11.$$
