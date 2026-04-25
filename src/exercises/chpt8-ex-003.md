---
id: chpt8-ex-003
chapter: 8
tags: [偏导数, 数值方法]
difficulty: easy
video:
---

## Problem

计算 $f(x) = x^3$ 在 $x=1$ 处的二阶导数，取 $h=0.1$，并与精确值 $f''(1) = 6$ 比较。

## Solution 1

### Hint

使用二阶导数数值公式 $f''(x) \approx [f(x+h) - 2f(x) + f(x-h)]/h^2$。

### Answer

$$
\frac{f(1.1) - 2f(1) + f(0.9)}{h^2} = \frac{1.331 - 2 + 0.729}{0.01} = \frac{0.06}{0.01} = 6.
$$

结果与精确值 $f''(1) = 6$ 完全一致。（$f(x)=x^3$ 是三次函数，该公式对三次函数精确成立。）
