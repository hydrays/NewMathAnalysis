---
id: chpt13-ex-001
chapter: 13
tags: [级数, 收敛, 几何级数, 部分和]
difficulty: easy
video:
---

## Problem

**"一尺之棰，日取其半"**：设每天取走一半的长度，写出前 $n$ 天的取走量之和 $S_n$，并求极限 $\displaystyle\lim_{n\to\infty} S_n$。

## Solution 1

### Hint

这是公比 $q = \frac{1}{2}$ 的等比级数，利用等比数列求和公式计算部分和。

### Answer

前 $n$ 天取走量的部分和：

$$
S_n = \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}
= \frac{\frac{1}{2}(1-({\frac{1}{2}})^n)}{1-\frac{1}{2}}
= 1 - \frac{1}{2^n}.
$$

当 $n\to\infty$ 时：

$$
\lim_{n\to\infty} S_n = \lim_{n\to\infty}\left(1 - \frac{1}{2^n}\right) = 1.
$$

级数 $\displaystyle\sum_{n=1}^\infty \frac{1}{2^n}$ **收敛**，其和为 $1$（即整根棰的长度）。
