---
id: chpt4-ex-013
chapter: 4
tags: [不定积分, 分部积分]
difficulty: easy
video:
---

## Problem

计算定积分 $\displaystyle\int_1^e \ln x\,dx$。

## Solution 1

### Hint

令 $u = \ln x$，$dv = dx$，应用定积分的分部积分公式，$uv$ 项代入上下限 $[1, e]$。

### Answer

令 $u = \ln x$，$dv = dx$，则 $du = \dfrac{1}{x}\,dx$，$v = x$。

$$
\int_1^e \ln x\,dx = [x\ln x]_1^e - \int_1^e x \cdot \frac{1}{x}\,dx = (e \cdot 1 - 1 \cdot 0) - \int_1^e dx = e - [x]_1^e = e - (e-1) = 1
$$
