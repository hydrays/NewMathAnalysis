---
id: chpt6-ex-016
chapter: 6
tags: [定积分, 面积]
difficulty: medium
video:
---

## Problem

研究瑕积分 $\displaystyle\int_0^1 \frac{1}{x^p}\,dx$ 的收敛性（$p$ 为实数，$x=0$ 为瑕点）。

## Solution 1

### Hint

$x=0$ 处函数无界，通过令下限趋于 $0^+$ 的极限来判断收敛性。

### Answer

**当 $p \neq 1$ 时**：

$$
\int_0^1 \frac{1}{x^p}\,dx = \lim_{a\to 0^+}\frac{1-a^{1-p}}{1-p}.
$$

- 若 $p < 1$：$a^{1-p} \to 0$，积分收敛于 $\dfrac{1}{1-p}$。
- 若 $p > 1$：$a^{1-p} \to \infty$，积分发散。

**当 $p = 1$ 时**：

$$
\int_0^1 \frac{1}{x}\,dx = \lim_{a\to 0^+}(-\ln a) = \infty.
$$

发散。

**结论**：$p < 1$ 时收敛，$p \geq 1$ 时发散。
