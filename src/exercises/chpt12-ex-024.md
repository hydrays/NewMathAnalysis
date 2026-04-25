---
id: chpt12-ex-024
chapter: 12
tags: [曲线积分, 第二类曲线积分, 例题]
difficulty: easy
video:
---

## Problem

计算 $\displaystyle\int_L y\,\mathrm{d}x - x\,\mathrm{d}y$，其中 $L$ 为从 $(1,0)$ 到 $(-1,0)$ 的上半圆 $x=\cos t,\,y=\sin t,\,t\in[0,\pi]$。

## Solution 1

### Hint

将 $x=\cos t,\,y=\sin t$ 代入，计算 $\mathrm{d}x=-\sin t\,\mathrm{d}t,\,\mathrm{d}y=\cos t\,\mathrm{d}t$，再代入被积表达式。

### Answer

$$\int_L y\,\mathrm{d}x-x\,\mathrm{d}y = \int_0^{\pi}\bigl(\sin t\cdot(-\sin t)-\cos t\cdot\cos t\bigr)\mathrm{d}t = \int_0^{\pi}(-1)\,\mathrm{d}t = -\pi.$$
