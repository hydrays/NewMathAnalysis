---
id: chpt5-ex-018
chapter: 5
title: 无穷小量的阶与等价无穷小
tags: [无穷小, 等价无穷小, 大O记号]
difficulty: easy
video:
---

## Problem

验证以下无穷小量的阶关系（当 $x \to 0$ 时）：

1. $x^2 = o(x)$
2. $\sin x \sim x$
3. $1 - \cos x \sim \dfrac{1}{2}x^2$

## Solution 1

### Hint

根据高阶无穷小和等价无穷小的定义，计算相应的极限。

### Answer

**1.** 当 $x \to 0$ 时，$x^2 = o(x)$，因为
$$
\lim_{x \to 0} \frac{x^2}{x} = \lim_{x \to 0} x = 0
$$

**2.** 当 $x \to 0$ 时，$\sin x \sim x$，因为
$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

**3.** 当 $x \to 0$ 时，$1 - \cos x \sim \dfrac{1}{2}x^2$，因为
$$
\lim_{x \to 0} \frac{1 - \cos x}{\dfrac{1}{2}x^2} = 1
$$
