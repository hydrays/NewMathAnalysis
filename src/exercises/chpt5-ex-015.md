---
id: chpt5-ex-015
chapter: 5
tags: [泰勒展开]
difficulty: medium
video:
---

## Problem

证明：当 $0 < x < \dfrac{\pi}{2}$ 时，$\displaystyle\sin x > x - \frac{x^3}{6}$。

## Solution 1

### Hint

将 $\sin x$ 用带拉格朗日余项的泰勒公式展开到五阶，利用 $\cos\xi > 0$（$\xi \in (0, x) \subset (0, \pi/2)$）得出不等式。

### Answer

用带拉格朗日余项的泰勒公式展开 $\sin x$ 到五阶，存在 $\xi \in (0, x)$ 使得：

$$
\sin x = x - \frac{x^3}{6} + \frac{\cos\xi}{120}x^5
$$

当 $0 < x < \dfrac{\pi}{2}$ 时，$\xi \in \left(0, \dfrac{\pi}{2}\right)$，故 $\cos\xi > 0$，从而 $\dfrac{\cos\xi}{120}x^5 > 0$，因此：

$$
\sin x = x - \frac{x^3}{6} + \frac{\cos\xi}{120}x^5 > x - \frac{x^3}{6}
$$

证毕。
