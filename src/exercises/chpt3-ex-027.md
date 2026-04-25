---
id: chpt3-ex-027
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to \frac{\pi}{2}} (\sec x - \tan x)$。

## Solution 1

### Hint

将 $\infty - \infty$ 型通分转化为 $0/0$ 型，再用洛必达法则。

### Answer

$$
\sec x - \tan x = \frac{1-\sin x}{\cos x}.
$$

当 $x \to \dfrac{\pi}{2}$ 时，上式是 $0/0$ 型。

$$
\lim_{x \to \frac{\pi}{2}} \frac{1-\sin x}{\cos x} = \lim_{x \to \frac{\pi}{2}} \frac{-\cos x}{-\sin x} = 0.
$$
