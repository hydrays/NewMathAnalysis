---
id: chpt1-ex-019
chapter: 1
tags: [连续性, 间断点]
difficulty: easy
video:
---

## Problem

符号函数 $\mathrm{sgn}(x) = \begin{cases} 1, & x>0, \\ 0, & x=0, \\ -1, & x<0 \end{cases}$ 是否在闭区间 $[-1, 1]$ 上连续？若不连续，说明原因，并说明维尔斯特拉斯极值定理是否适用。

## Solution 1

### Hint

检验 $\mathrm{sgn}(x)$ 在 $x=0$ 处的左右极限是否相等。

### Answer

$\mathrm{sgn}(x)$ 在 $x=0$ 处不连续：

$$\lim_{x \to 0^-} \mathrm{sgn}(x) = -1, \qquad \lim_{x \to 0^+} \mathrm{sgn}(x) = 1.$$

左右极限不相等，故极限不存在，$x=0$ 是**跳跃间断点**（第一类间断点）。

由于 $\mathrm{sgn}(x)$ 在 $[-1,1]$ 上不连续，维尔斯特拉斯极值定理的条件不满足，定理不适用。

注意：尽管如此，$\mathrm{sgn}(x)$ 在 $[-1,1]$ 上实际上是有界的（值域为 $\{-1, 0, 1\}$），且最大值和最小值均存在，这说明定理的条件是充分条件而非必要条件。
