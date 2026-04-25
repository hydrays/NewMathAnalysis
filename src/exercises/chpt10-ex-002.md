---
id: chpt10-ex-002
chapter: 10
tags: [多元函数, 极限, 极限不存在]
difficulty: medium
video:
---

## Problem

考察函数

$$
f(x,y) = \begin{cases} \dfrac{xy}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0 \end{cases}
$$

在点 $(0, 0)$ 处的极限是否存在。

## Solution 1

### Hint

沿坐标轴趋近时极限均为 $0$，但沿直线 $y = kx$ 趋近时极限依赖于 $k$，由此说明极限不存在。

### Answer

沿 $x$ 轴趋近（令 $y = 0$）：

$$
\lim_{x \to 0} f(x, 0) = \lim_{x \to 0} 0 = 0.
$$

沿 $y$ 轴趋近（令 $x = 0$）：

$$
\lim_{y \to 0} f(0, y) = \lim_{y \to 0} 0 = 0.
$$

虽然沿坐标轴趋近时极限均为 $0$，但不能由此断定极限存在。当点 $P(x,y)$ 沿直线 $y = kx$ 趋于 $(0,0)$ 时，

$$
\lim_{x \to 0} f(x, kx) = \lim_{x \to 0} \frac{k x^2}{x^2 + k^2 x^2} = \frac{k}{1 + k^2}.
$$

$k$ 不同时极限值不同，故函数在 $(0, 0)$ 处的极限**不存在**。
