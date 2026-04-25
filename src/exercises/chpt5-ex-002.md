---
id: chpt5-ex-002
chapter: 5
tags: [中值定理, 拉格朗日中值定理]
difficulty: medium
video:
---

## Problem

证明：如果 $f'(x) = 0$ 在某个区间上恒成立，则 $f(x)$ 是常数函数。

## Solution 1

### Hint

任取区间上两点 $a < b$，对 $f$ 在 $[a, b]$ 上应用拉格朗日中值定理，利用 $f'(c) = 0$ 得到 $f(a) = f(b)$。

### Answer

任取区间上两点 $a < b$，由拉格朗日中值定理，存在 $c \in (a, b)$ 使得

$$
f(b) - f(a) = f'(c)(b - a) = 0 \cdot (b - a) = 0
$$

因此 $f(b) = f(a)$。由于 $a, b$ 是任意选取的，$f$ 在整个区间上取值恒等，故 $f(x)$ 是常数函数。
