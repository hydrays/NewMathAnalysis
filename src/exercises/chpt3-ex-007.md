---
id: chpt3-ex-007
chapter: 3
tags: [导数应用, 链式法则]
difficulty: medium
video:
---

## Problem

设 $y = \ln\sin(2x^2)$，求 $\dfrac{dy}{dx}$。

## Solution 1

### Hint

将函数分解为三层复合：$y = \ln u$，$u = \sin v$，$v = 2x^2$，逐层应用链式法则。

### Answer

令 $y = \ln u$，$u = \sin v$，$v = 2x^2$。

$$
\frac{dy}{dx} = \frac{1}{u} \cdot \cos v \cdot 4x = \frac{\cos(2x^2)}{\sin(2x^2)} \cdot 4x = 4x\cot(2x^2).
$$
