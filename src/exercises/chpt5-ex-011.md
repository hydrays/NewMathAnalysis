---
id: chpt5-ex-011
chapter: 5
tags: [泰勒展开, L'Hopital法则, 洛必达法则]
difficulty: medium
video:
---

## Problem

利用泰勒展开计算极限 $\displaystyle\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$。

## Solution 1

### Hint

将 $e^x$ 展开到二阶（含 $o(x^2)$ 余项），代入后约去分子分母的公因子 $x^2$，令 $x\to 0$。

### Answer

将 $e^x$ 展开到二阶：

$$
e^x = 1 + x + \frac{x^2}{2} + o(x^2)
$$

代入：

$$
\frac{e^x - 1 - x}{x^2} = \frac{\frac{x^2}{2} + o(x^2)}{x^2} = \frac{1}{2} + \frac{o(x^2)}{x^2}
$$

令 $x \to 0$，$\dfrac{o(x^2)}{x^2} \to 0$，故

$$
\lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \frac{1}{2}
$$
