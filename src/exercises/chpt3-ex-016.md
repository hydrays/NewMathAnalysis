---
id: chpt3-ex-016
chapter: 3
tags: [导数应用, 对数求导法]
difficulty: medium
video:
---

## Problem

求 $y = \sqrt{\dfrac{(x-1)(x-2)}{(x-4)(x-5)}}$ 的导数（设 $x > 5$）。

## Solution 1

### Hint

两边取对数，将根号和乘除变成加减，再对两边求导。

### Answer

设 $x > 5$，两边取对数：

$$
\ln y = \frac{1}{2}\left[\ln(x-1) + \ln(x-2) - \ln(x-4) - \ln(x-5)\right].
$$

两边对 $x$ 求导：

$$
\frac{y'}{y} = \frac{1}{2}\left(\frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-4} - \frac{1}{x-5}\right).
$$

故：

$$
y' = \frac{1}{2}\sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)}}\left(\frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-4} - \frac{1}{x-5}\right).
$$
