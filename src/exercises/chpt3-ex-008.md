---
id: chpt3-ex-008
chapter: 3
tags: [导数应用, 链式法则]
difficulty: medium
video:
---

## Problem

设 $y = \mathrm{e}^{\cos\sqrt{x}}$，求 $y'$。

## Solution 1

### Hint

将函数分解为三层复合：$y = \mathrm{e}^u$，$u = \cos v$，$v = \sqrt{x}$，逐层求导后相乘。

### Answer

令 $u = \cos\sqrt{x}$，$v = \sqrt{x}$。

$$
\frac{dy}{du} = \mathrm{e}^u = \mathrm{e}^{\cos\sqrt{x}}, \quad \frac{du}{dv} = -\sin v = -\sin\sqrt{x}, \quad \frac{dv}{dx} = \frac{1}{2\sqrt{x}}.
$$

由链式法则：

$$
y' = \mathrm{e}^{\cos\sqrt{x}} \cdot (-\sin\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} = -\frac{\mathrm{e}^{\cos\sqrt{x}}\sin\sqrt{x}}{2\sqrt{x}}.
$$
