---
id: chpt3-ex-024
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: easy
video:
---

## Problem

求 $\displaystyle\lim_{x \to +\infty} \frac{\ln x}{x^n}$（$n > 0$）。

## Solution 1

### Hint

$\infty/\infty$ 型未定式，直接用洛必达法则。

### Answer

$$
\lim_{x \to +\infty} \frac{\ln x}{x^n} = \lim_{x \to +\infty} \frac{\frac{1}{x}}{nx^{n-1}} = \lim_{x \to +\infty} \frac{1}{nx^n} = 0.
$$

这说明对数函数趋于无穷的速度比任何正幂次的幂函数都慢。
