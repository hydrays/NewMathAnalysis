---
id: chpt4-ex-008
chapter: 4
tags: [不定积分, 分部积分]
difficulty: easy
video:
---

## Problem

计算不定积分 $\displaystyle\int x e^x\,dx$。

## Solution 1

### Hint

令 $u = x$，$dv = e^x\,dx$，应用分部积分公式 $\int u\,dv = uv - \int v\,du$。

### Answer

令 $u = x$，$dv = e^x\,dx$，则 $du = dx$，$v = e^x$。

$$
\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = (x-1)e^x + C
$$
