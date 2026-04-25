---
id: chpt3-ex-015
chapter: 3
tags: [导数应用, 对数求导法]
difficulty: medium
video:
---

## Problem

求 $y = (x^2)^{\ln x}$（$x > 0$）的导数。

## Solution 1

### Hint

两边取对数，利用 $\ln y = 2(\ln x)^2$，再对两边关于 $x$ 求导。

### Answer

两边取对数：

$$
\ln y = \ln x \cdot \ln(x^2) = 2(\ln x)^2.
$$

两边对 $x$ 求导：

$$
\frac{1}{y}y' = 4\ln x \cdot \frac{1}{x} = \frac{4\ln x}{x}.
$$

故：

$$
y' = y \cdot \frac{4\ln x}{x} = (x^2)^{\ln x} \cdot \frac{4\ln x}{x}.
$$
