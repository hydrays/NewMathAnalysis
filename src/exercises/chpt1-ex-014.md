---
id: chpt1-ex-014
chapter: 1
tags: [连续性, 函数极限]
difficulty: easy
video:
---

## Problem

讨论函数 $f(x) = |x|$ 的连续性。

## Solution 1

### Hint

分 $x_0 > 0$、$x_0 < 0$、$x_0 = 0$ 三种情况，验证各点处 $\lim_{x\to x_0}f(x) = f(x_0)$ 成立。

### Answer

函数 $f(x) = |x|$ 在 $(-\infty, +\infty)$ 上处处连续。

- 当 $x_0 > 0$ 时，在 $x_0$ 的某邻域内 $f(x) = x$，故 $\lim_{x\to x_0}|x| = x_0 = f(x_0)$，连续。
- 当 $x_0 < 0$ 时，在 $x_0$ 的某邻域内 $f(x) = -x$，故 $\lim_{x\to x_0}|x| = -x_0 = f(x_0)$，连续。
- 当 $x_0 = 0$ 时，左极限 $\lim_{x\to 0^-}|x| = \lim_{x\to 0^-}(-x) = 0$，右极限 $\lim_{x\to 0^+}|x| = \lim_{x\to 0^+}x = 0$，且 $f(0)=0$，故连续。

因此 $f(x) = |x|$ 在 $(-\infty, +\infty)$ 上连续。
