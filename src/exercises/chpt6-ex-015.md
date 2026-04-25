---
id: chpt6-ex-015
chapter: 6
tags: [定积分, 面积]
difficulty: medium
video:
---

## Problem

研究反常积分 $\displaystyle\int_1^\infty \frac{1}{x^p}\,dx$ 的收敛性（$p$ 为实数）。

## Solution 1

### Hint

对 $p \neq 1$ 和 $p = 1$ 分情况讨论，通过求极限判断收敛发散。

### Answer

**当 $p \neq 1$ 时**：

$$
\int_1^\infty \frac{1}{x^p}\,dx = \lim_{b\to\infty}\frac{b^{1-p}-1}{1-p}.
$$

- 若 $p > 1$：$b^{1-p} \to 0$，积分收敛于 $\dfrac{1}{p-1}$。
- 若 $p < 1$：$b^{1-p} \to \infty$，积分发散。

**当 $p = 1$ 时**：

$$
\int_1^\infty \frac{1}{x}\,dx = \lim_{b\to\infty}\ln b = \infty.
$$

发散。

**结论**：$p > 1$ 时收敛，$p \leq 1$ 时发散。
