---
id: chpt6-ex-017
chapter: 6
title: 曲线下面积的计算
tags: [定积分, 面积]
difficulty: easy
video:
---

## Problem

计算曲线 $y = f(x)$ 在 $[a,b]$ 上与 $x$ 轴围成的面积。

## Solution 1

### Hint

利用微元法：将区间 $[a,b]$ 分成若干小区间，在每个小区间 $[x, x+dx]$ 上用矩形近似面积微元，再求和取极限。

### Answer

利用微元法：

- **分割**：将 $[a,b]$ 分成 $n$ 个小区间；
- **近似**：每个小区间 $[x, x+dx]$ 上的面积微元为 $dA = f(x)dx$；
- **求和取极限**：

$$
A = \int_a^b f(x)\,dx
$$
