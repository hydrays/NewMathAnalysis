---
id: chpt5-ex-014
chapter: 5
tags: [泰勒展开]
difficulty: medium
video:
---

## Problem

证明：当 $x > 0$ 时，$\displaystyle e^x > 1 + x + \frac{x^2}{2}$。

## Solution 1

### Hint

将 $e^x$ 用带拉格朗日余项的泰勒公式展开到三阶，利用余项中 $e^\xi > 0$（$\xi \in (0, x)$）得出不等式。

### Answer

用带拉格朗日余项的泰勒公式展开 $e^x$ 到三阶，存在 $\xi \in (0, x)$ 使得：

$$
e^x = 1 + x + \frac{x^2}{2} + \frac{e^\xi}{6}x^3
$$

由于 $e^\xi > 0$ 且 $x > 0$，故 $\dfrac{e^\xi}{6}x^3 > 0$，从而：

$$
e^x = 1 + x + \frac{x^2}{2} + \frac{e^\xi}{6}x^3 > 1 + x + \frac{x^2}{2}
$$

证毕。
