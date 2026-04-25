---
id: chpt3-ex-021
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to 1} \frac{x^3 - 3x + 2}{x^3 - x^2 - x + 1}$。

## Solution 1

### Hint

当 $x \to 1$ 时，分子分母均为零（$0/0$ 型），需多次应用洛必达法则，但每次应用前先验证仍是未定式。

### Answer

$$
\lim_{x \to 1} \frac{x^3-3x+2}{x^3-x^2-x+1} = \lim_{x \to 1} \frac{3x^2-3}{3x^2-2x-1} = \lim_{x \to 1} \frac{6x}{6x-2} = \frac{6}{4} = \frac{3}{2}.
$$

注意：第二次求导后 $\displaystyle\lim_{x\to 1}\frac{6x}{6x-2} = \frac{3}{2}$ 已不是未定式，不能再次应用洛必达法则。
