---
id: chpt1-ex-006
chapter: 1
tags: [函数极限, epsilon-delta, 极限, 连续性]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 1}(2x-1)$。

## Solution 1

### Hint

$f(x) = 2x-1$ 是多项式函数，在 $x=1$ 处连续，可直接代入。

### Answer

由于 $f(x) = 2x - 1$ 是多项式，在 $x=1$ 处连续，直接代入得：

$$\lim_{x\rightarrow 1}(2x-1) = 2(1) - 1 = 1.$$

## Solution 2

### Hint

用 $\varepsilon$-$\delta$ 定义，从 $|(2x-1)-1| < \varepsilon$ 反推出 $\delta$ 的取法。

### Answer

对任意 $\varepsilon > 0$，需找到 $\delta > 0$ 使得当 $0 < |x-1| < \delta$ 时：

$$|(2x-1) - 1| = 2|x-1| < \varepsilon.$$

取 $\delta = \dfrac{\varepsilon}{2}$，则当 $0 < |x-1| < \delta$ 时：

$$2|x-1| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon.$$

故 $\displaystyle \lim_{x\rightarrow 1}(2x-1) = 1$。
