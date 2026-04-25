---
id: chpt6-ex-002
chapter: 6
tags: [定积分, 体积]
difficulty: easy
video:
---

## Problem

计算底半径为 $R$，高为 $h$ 的圆锥体积。

## Solution 1

### Hint

在高度 $x$ 处截面半径为 $r(x) = R \cdot x/h$，对截面面积从 $0$ 到 $h$ 积分。

### Answer

在高度 $x$ 处，截面是半径为 $r(x) = \dfrac{Rx}{h}$ 的圆，面积为 $A(x) = \pi r^2(x) = \dfrac{\pi R^2 x^2}{h^2}$。

$$
V = \int_0^h \frac{\pi R^2 x^2}{h^2}\,dx = \frac{\pi R^2}{h^2} \cdot \frac{h^3}{3} = \frac{1}{3}\pi R^2 h.
$$
