---
id: chpt3-ex-029
chapter: 3
tags: [导数应用, 洛必达法则]
difficulty: medium
video:
---

## Problem

求 $\displaystyle\lim_{x \to 0} \frac{\tan x - x}{x^2 \sin x}$。

## Solution 1

### Hint

先用等价无穷小 $\sin x \sim x$（$x \to 0$）替换分母中的 $\sin x$，简化分母后再用洛必达法则。

### Answer

当 $x \to 0$ 时，$\sin x \sim x$，故：

$$
\lim_{x \to 0} \frac{\tan x - x}{x^2\sin x} = \lim_{x \to 0} \frac{\tan x - x}{x^3}.
$$

对 $0/0$ 型连续应用洛必达法则：

$$
= \lim_{x \to 0} \frac{\sec^2 x - 1}{3x^2} = \lim_{x \to 0} \frac{2\sec^2 x\tan x}{6x} = \frac{1}{3}\lim_{x \to 0}\frac{\tan x}{x} = \frac{1}{3}.
$$
