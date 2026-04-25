---
id: chpt5-ex-010
chapter: 5
tags: [泰勒展开]
difficulty: easy
video:
---

## Problem

写出正弦函数 $\sin x$ 在 $x = 0$ 附近的一阶、三阶、五阶多项式近似，并说明为何只有奇数次项出现。

## Solution 1

### Hint

利用 $\sin x$ 是奇函数，其泰勒展开只含奇数次幂；各阶导数 $\sin^{(n)}(0)$ 仅当 $n$ 为奇数时非零，且符号交替。

### Answer

$\sin x$ 的各阶导数在 $0$ 处满足 $\sin^{(n)}(0) = 0$（$n$ 为偶数），交替为 $\pm 1$（$n$ 为奇数）：

- 一阶近似：$\sin x \approx x$
- 三阶近似：$\sin x \approx x - \dfrac{x^3}{6}$
- 五阶近似：$\sin x \approx x - \dfrac{x^3}{6} + \dfrac{x^5}{120}$

只有奇数次项出现，这与 $\sin x$ 是奇函数（$\sin(-x) = -\sin(x)$）一致：奇函数的泰勒展开只含奇次幂。
