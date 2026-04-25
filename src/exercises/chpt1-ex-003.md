---
id: chpt1-ex-003
chapter: 1
tags: [数列极限, epsilon-N, 极限]
difficulty: medium
video:
---

## Problem

用 $\varepsilon$-$N$ 定义证明 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$。

## Solution 1

### Hint

从 $\left|\dfrac{1}{n} - 0\right| < \varepsilon$ 出发，解出 $n$ 的条件，进而确定 $N$ 的取法。

### Answer

对任意给定的 $\varepsilon > 0$，需要找到正整数 $N$，使得当 $n > N$ 时：

$$\left| \frac{1}{n} - 0 \right| = \frac{1}{n} < \varepsilon.$$

解不等式 $\dfrac{1}{n} < \varepsilon$ 得 $n > \dfrac{1}{\varepsilon}$。

取 $N = \left\lfloor \dfrac{1}{\varepsilon} \right\rfloor + 1$（即大于 $\dfrac{1}{\varepsilon}$ 的最小正整数），则当 $n > N$ 时，必有 $\dfrac{1}{n} < \varepsilon$。

故 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$。
