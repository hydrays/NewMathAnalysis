---
id: chpt1-ex-005
chapter: 1
tags: [数列极限, epsilon-N, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n^2}$。

## Solution 1

### Hint

用 $\varepsilon$-$N$ 定义，从 $\dfrac{1}{n^2} < \varepsilon$ 解出对 $n$ 的要求，进而确定 $N$。

### Answer

对任意 $\varepsilon > 0$，需找到 $N$ 使得当 $n > N$ 时：

$$\left| \frac{1}{n^2} - 0 \right| = \frac{1}{n^2} < \varepsilon.$$

解不等式得 $n > \dfrac{1}{\sqrt{\varepsilon}}$，取 $N = \left\lfloor \dfrac{1}{\sqrt{\varepsilon}} \right\rfloor + 1$，则当 $n > N$ 时必有 $\dfrac{1}{n^2} < \varepsilon$。

故 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n^2} = 0$。
