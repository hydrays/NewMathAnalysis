---
id: chpt2-ex-020
chapter: 2
title: 凸函数的仿射变换
tags: [凸函数, 极值]
difficulty: easy
video:
---

## Problem

考虑凸函数 $f(x) = x^2$，取 $a = 2, b = 1$，验证 $k(x) = f(2x + 1)$ 也是凸函数。

## Solution 1

### Hint

利用二阶导数判别凸函数。

### Answer

取 $a = 2, b = 1$，则
$$
k(x) = f(2x + 1) = (2x + 1)^2 = 4x^2 + 4x + 1
$$
也是凸函数，因为
$$
k''(x) = 8 > 0
$$
