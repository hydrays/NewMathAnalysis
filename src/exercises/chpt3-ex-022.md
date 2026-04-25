---
id: chpt3-ex-022
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to 0} \frac{x - \sin x}{x^3}$。

## Solution 1

### Hint

$0/0$ 型，需连续应用洛必达法则三次，每次都先确认仍是未定式。

### Answer

$$
\lim_{x \to 0} \frac{x-\sin x}{x^3} = \lim_{x \to 0} \frac{1-\cos x}{3x^2} = \lim_{x \to 0} \frac{\sin x}{6x} = \frac{1}{6}.
$$
