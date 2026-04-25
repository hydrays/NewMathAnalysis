---
id: chpt4-ex-012
chapter: 4
tags: [不定积分, 分部积分]
difficulty: easy
video:
---

## Problem

计算定积分 $\displaystyle\int_0^1 x e^x\,dx$。

## Solution 1

### Hint

令 $u = x$，$dv = e^x\,dx$，应用定积分的分部积分公式，注意 $uv$ 项需代入上下限。

### Answer

令 $u = x$，$dv = e^x\,dx$，则 $du = dx$，$v = e^x$。

$$
\int_0^1 x e^x\,dx = [x e^x]_0^1 - \int_0^1 e^x\,dx = (e - 0) - [e^x]_0^1 = e - (e - 1) = 1
$$
