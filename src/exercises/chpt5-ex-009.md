---
id: chpt5-ex-009
chapter: 5
tags: [泰勒展开]
difficulty: easy
video:
---

## Problem

写出指数函数 $e^x$ 在 $x = 0$ 附近的一阶、二阶、三阶多项式近似，并说明各阶近似的形式规律。

## Solution 1

### Hint

泰勒展开系数为 $a_n = \dfrac{f^{(n)}(0)}{n!}$，利用 $e^x$ 的各阶导数在 $0$ 处均为 $1$，逐阶写出近似。

### Answer

由于 $f(x) = e^x$ 的各阶导数满足 $f^{(n)}(0) = 1$，系数 $a_n = \dfrac{1}{n!}$，得：

- 一阶近似：$e^x \approx 1 + x$
- 二阶近似：$e^x \approx 1 + x + \dfrac{x^2}{2}$
- 三阶近似：$e^x \approx 1 + x + \dfrac{x^2}{2} + \dfrac{x^3}{6}$

一般地，$n$ 阶泰勒多项式为 $\displaystyle\sum_{k=0}^n \frac{x^k}{k!}$，每一项均为 $x^k$ 的倍数，系数规律为 $\dfrac{1}{k!}$。
