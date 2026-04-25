---
id: chpt1-ex-023
chapter: 1
title: epsilon-delta证明 $\lim_{x\to 1}(2x-1)=1$
tags: [极限, epsilon-delta证明]
difficulty: medium
video:
---

## Problem

用 $\varepsilon$-$\delta$ 语言证明 $\displaystyle\lim_{x \to 1}(2x - 1) = 1$。

## Solution 1

### Hint

估计 $|f(x) - 1|$，化为含 $|x-1|$ 的形式，再确定满足条件的 $\delta$。

### Answer

**证：** 由于

$$
|f(x) - A| = |(2x - 1) - 1| = 2|x - 1|
$$

为了使 $\displaystyle |f(x) - A| < \varepsilon$，只要

$$
|x - 1| < \frac{\varepsilon}{2}
$$

所以，$\forall \varepsilon > 0$，可取 $\displaystyle \delta = \frac{\varepsilon}{2}$，则当 $x$ 适合不等式

$$
0 < |x - 1| < \delta
$$

时，对应的函数值 $f(x)$ 就满足不等式

$$
|f(x) - 1| = |(2x - 1) - 1| < \varepsilon
$$

从而

$$
\lim\limits_{x \to 1}(2x - 1) = 1
$$
