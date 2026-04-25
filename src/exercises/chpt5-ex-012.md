---
id: chpt5-ex-012
chapter: 5
tags: [泰勒展开, L'Hopital法则, 洛必达法则]
difficulty: medium
video:
---

## Problem

利用泰勒展开计算极限 $\displaystyle\lim_{x \to 0} \frac{\sin x - x}{x^3}$。

## Solution 1

### Hint

将 $\sin x$ 展开到三阶（含 $o(x^3)$ 余项），代入后提取 $x^3$ 因子，令 $x\to 0$。

### Answer

将 $\sin x$ 展开到三阶：

$$
\sin x = x - \frac{x^3}{6} + o(x^3)
$$

代入：

$$
\frac{\sin x - x}{x^3} = \frac{-\frac{x^3}{6} + o(x^3)}{x^3} = -\frac{1}{6} + \frac{o(x^3)}{x^3}
$$

令 $x \to 0$，$\dfrac{o(x^3)}{x^3} \to 0$，故

$$
\lim_{x \to 0} \frac{\sin x - x}{x^3} = -\frac{1}{6}
$$
