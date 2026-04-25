---
id: chpt3-ex-026
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to 0^+} x^n \ln x$（$n > 0$）。

## Solution 1

### Hint

将 $0 \cdot \infty$ 型转化为 $\infty/\infty$ 型，再用洛必达法则。

### Answer

$$
x^n \ln x = \frac{\ln x}{x^{-n}}.
$$

当 $x \to 0^+$ 时，上式是 $\infty/\infty$ 型。应用洛必达法则：

$$
\lim_{x \to 0^+} x^n \ln x = \lim_{x \to 0^+} \frac{\ln x}{x^{-n}} = \lim_{x \to 0^+} \frac{\frac{1}{x}}{-nx^{-n-1}} = \lim_{x \to 0^+}\left(-\frac{x^n}{n}\right) = 0.
$$
