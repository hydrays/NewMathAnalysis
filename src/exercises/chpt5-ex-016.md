---
id: chpt5-ex-016
chapter: 5
tags: [泰勒展开]
difficulty: easy
video:
---

## Problem

用大 $O$ 符号写出 $e^x$ 和 $\cos x$ 的三阶截断展开式，并比较它们的余项阶数。

## Solution 1

### Hint

将 $e^x$ 展开到 $x^2$ 项（余项为 $O(x^3)$），将 $\cos x$ 展开到 $x^2$ 项（余项为 $O(x^4)$），注意 $\cos x$ 没有 $x^3$ 项。

### Answer

$e^x$ 展开到二阶，余项为 $O(x^3)$：

$$
e^x = 1 + x + \frac{x^2}{2} + O(x^3)
$$

$\cos x$ 展开到二阶，由于 $x^3$ 项系数为零，余项直接跃升到 $O(x^4)$：

$$
\cos x = 1 - \frac{x^2}{2} + O(x^4)
$$

比较：
- $e^x$ 的三阶误差为 $O(x^3)$
- $\cos x$ 的三阶误差为 $O(x^4)$，实际上更小

这说明对于同样截断到 $x^2$ 的近似，$\cos x$ 的近似精度更高。
