---
id: chpt6-ex-004
chapter: 6
tags: [定积分, 体积]
difficulty: easy
video:
figures:
  - file: chpt6_ex004.png
    alt: 直线 $y=x$ 在 $[0,1]$ 上绕 $y$ 轴旋转 — 形成顶端在原点的倒置圆锥, 高度 $y$ 处的圆半径等于 $y$
    where: problem
---

## Problem

计算曲线 $y = x$ 在 $[0,1]$ 上绕 $y$ 轴旋转一周所形成的旋转体体积。

## Solution 1

### Hint

用柱壳法（薄壳公式）：$V = \displaystyle\int_a^b 2\pi x f(x)\,dx$。

### Answer

$$
V = \int_0^1 2\pi x \cdot x\,dx = 2\pi\int_0^1 x^2\,dx = 2\pi \cdot \frac{1}{3} = \frac{2\pi}{3}.
$$
