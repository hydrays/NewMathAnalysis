---
id: chpt1-ex-015
chapter: 1
tags: [连续性, 间断点, 函数极限]
difficulty: easy
video:
---

## Problem

讨论函数 $\displaystyle f(x) = \frac{1}{|x|}$ 的连续性，指出间断点（若有）。

## Solution 1

### Hint

分析 $f(x)$ 的定义域，找出使 $f(x)$ 无定义的点，再检验该点处的极限行为。

### Answer

$f(x) = \dfrac{1}{|x|}$ 在 $x = 0$ 处无定义，因此 $x=0$ 是间断点。

- 当 $x_0 \neq 0$ 时，$|x|$ 在 $x_0$ 附近连续且非零，故 $f(x) = \dfrac{1}{|x|}$ 在所有 $x_0 \neq 0$ 处连续。
- 当 $x \to 0$ 时，$|x| \to 0^+$，故 $\dfrac{1}{|x|} \to +\infty$，极限不存在（趋于无穷大）。

因此，$f(x)$ 在 $(-\infty, 0) \cup (0, +\infty)$ 上连续，在 $x = 0$ 处不连续（第二类间断点，无穷间断点）。
