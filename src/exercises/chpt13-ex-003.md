---
id: chpt13-ex-003
chapter: 13
title: 比较判别法（发散）
tags: [级数, 比较判别法, 收敛性]
difficulty: easy
video:
---

## Problem

判断级数 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{\sqrt{n(n+1)}}$ 的收敛性。

## Solution 1

### Hint

将通项与调和级数的通项进行比较，找到合适的放缩。

### Answer

由于

$$
\frac{1}{\sqrt{n(n+1)}} > \frac{1}{\sqrt{(n+1)(n+1)}} = \frac{1}{n+1},
$$

而 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n+1}$（相当于调和级数）是**发散**的，根据比较审敛法，原级数**发散**。
