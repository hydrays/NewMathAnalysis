---
id: chpt12-ex-023
chapter: 12
tags: [曲线积分, 第一类曲线积分, 弧长, 例题]
difficulty: easy
video:
---

## Problem

计算 $\displaystyle\int_L(x^2+y^2)\,\mathrm{d}s$，其中 $L$ 为圆 $x=\cos t,\,y=\sin t,\,t\in[0,2\pi]$。

## Solution 1

### Hint

在单位圆 $L$ 上，$x^2+y^2=1$，弧长微元 $\mathrm{d}s = \sqrt{x'^2+y'^2}\,\mathrm{d}t = \mathrm{d}t$。

### Answer

$\mathrm{d}s = \sqrt{\sin^2 t+\cos^2 t}\,\mathrm{d}t = \mathrm{d}t$，且在 $L$ 上 $x^2+y^2=1$，故

$$\int_L(x^2+y^2)\,\mathrm{d}s = \int_0^{2\pi}1\cdot\mathrm{d}t = 2\pi.$$
