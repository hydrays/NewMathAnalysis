---
id: chpt5-ex-013
chapter: 5
tags: [泰勒展开]
difficulty: easy
video:
---

## Problem

利用 $\sin x$ 的泰勒展开计算 $\sin 1°$ 的近似值（精确到小数点后 7 位）。

## Solution 1

### Hint

先将 $1°$ 换算为弧度，再代入 $\sin x \approx x - \dfrac{x^3}{6}$，保留足够精度的项即可。

### Answer

先换算角度为弧度：

$$
1° = \frac{\pi}{180} \approx 0.0174533
$$

使用 $\sin x$ 的展开式：

$$
\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots
$$

代入 $x = 0.0174533$，由于 $x^3/6 \approx 8.8 \times 10^{-7}$，$x^5/120$ 可忽略：

$$
\sin 1° \approx 0.0174533 - \frac{(0.0174533)^3}{6} \approx 0.0174524
$$

与精确值 $0.0174524064$ 相比，误差约为 $10^{-8}$。
