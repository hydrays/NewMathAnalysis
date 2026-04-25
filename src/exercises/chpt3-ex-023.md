---
id: chpt3-ex-023
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to +\infty} \frac{\dfrac{\pi}{2} - \arctan x}{\dfrac{1}{x}}$。

## Solution 1

### Hint

当 $x \to +\infty$ 时，分子 $\dfrac{\pi}{2} - \arctan x \to 0$，分母 $\dfrac{1}{x} \to 0$，构成 $0/0$ 型，直接用洛必达法则。

### Answer

$$
\lim_{x \to +\infty} \frac{\frac{\pi}{2}-\arctan x}{\frac{1}{x}} = \lim_{x \to +\infty} \frac{-\frac{1}{1+x^2}}{-\frac{1}{x^2}} = \lim_{x \to +\infty} \frac{x^2}{1+x^2} = 1.
$$
