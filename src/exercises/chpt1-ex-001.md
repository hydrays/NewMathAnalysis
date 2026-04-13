---
id: chpt1-ex-001
chapter: 1
tags: [极限, epsilon-delta]
difficulty: medium
video:
---

## Problem

用 $\varepsilon$-$\delta$ 定义证明 $\displaystyle \lim_{x \to 2}(3x-1) = 5$.

## Solution 1

### Hint
从 $|f(x) - L| < \varepsilon$ 反推出 $\delta$ 的取法.

### Answer
设 $\varepsilon > 0$. 注意到 $|(3x-1)-5| = |3x-6| = 3|x-2|$.

取 $\delta = \varepsilon/3$, 则当 $0 < |x-2| < \delta$ 时,

$$|(3x-1)-5| = 3|x-2| < 3\delta = \varepsilon.$$

由极限定义, $\displaystyle\lim_{x\to 2}(3x-1)=5$. $\blacksquare$

## Solution 2

### Hint
直接利用极限的线性性质.

### Answer
由极限的线性性质:

$$\lim_{x\to 2}(3x-1) = 3\lim_{x\to 2}x - \lim_{x\to 2}1 = 3\cdot 2 - 1 = 5. \quad\blacksquare$$
