---
id: chpt1-ex-004
chapter: 1
tags: [数列极限, epsilon-N, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{2n}$。

## Solution 1

### Hint

利用极限的数乘性质，将问题归结为已知的 $\lim_{n\to\infty}\frac{1}{n}=0$。

### Answer

由极限的数乘性质及 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$，得：

$$\lim_{n\rightarrow \infty}\frac{1}{2n} = \frac{1}{2} \cdot \lim_{n\rightarrow \infty}\frac{1}{n} = \frac{1}{2} \cdot 0 = 0.$$

## Solution 2

### Hint

直接用 $\varepsilon$-$N$ 定义，解出 $n$ 需满足的条件，给出 $N$ 的取法。

### Answer

对任意 $\varepsilon > 0$，需找到 $N$ 使得当 $n > N$ 时：

$$\left| \frac{1}{2n} - 0 \right| = \frac{1}{2n} < \varepsilon.$$

解不等式得 $n > \dfrac{1}{2\varepsilon}$，取 $N = \left\lfloor \dfrac{1}{2\varepsilon} \right\rfloor + 1$，则当 $n > N$ 时必满足 $\dfrac{1}{2n} < \varepsilon$。

故极限为 $0$。
