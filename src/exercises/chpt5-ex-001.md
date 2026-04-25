---
id: chpt5-ex-001
chapter: 5
tags: [中值定理, 拉格朗日中值定理]
difficulty: medium
video:
---

## Problem

证明不等式：$|\sin x - \sin y| \leq |x - y|$。

## Solution 1

### Hint

对 $f(t) = \sin t$ 在以 $x, y$ 为端点的区间上应用拉格朗日中值定理，利用 $|\cos c| \leq 1$。

### Answer

对函数 $f(t) = \sin t$ 在区间 $[x, y]$（或 $[y, x]$）上应用拉格朗日中值定理：存在 $c$ 介于 $x, y$ 之间，使得

$$
\frac{\sin x - \sin y}{x - y} = \cos c
$$

由于 $|\cos c| \leq 1$，故

$$
\left|\frac{\sin x - \sin y}{x - y}\right| = |\cos c| \leq 1
$$

即 $|\sin x - \sin y| \leq |x - y|$。
