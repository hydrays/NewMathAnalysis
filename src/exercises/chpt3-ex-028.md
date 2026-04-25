---
id: chpt3-ex-028
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to 0^+} x^x$。

## Solution 1

### Hint

$0^0$ 型，取对数转化为 $0 \cdot \infty$ 型，再利用前一个极限结论。

### Answer

设 $y = x^x$，则 $\ln y = x\ln x$。

当 $x \to 0^+$ 时，$\ln y = x\ln x$ 是 $0 \cdot \infty$ 型，由前面的结论（$\lim_{x\to 0^+} x\ln x = 0$，取 $n=1$）：

$$
\lim_{x \to 0^+} \ln y = 0.
$$

因此：

$$
\lim_{x \to 0^+} x^x = \lim_{x \to 0^+} \mathrm{e}^{\ln y} = \mathrm{e}^0 = 1.
$$
