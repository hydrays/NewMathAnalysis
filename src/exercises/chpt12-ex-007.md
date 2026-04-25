---
id: chpt12-ex-007
chapter: 12
tags: [曲线积分, 第二类曲线积分, 路径相关]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\int_L y^2\,\mathrm{d}x$，其中 $L$ 为：

1. 半径为 $a$、圆心在原点、按逆时针方向绕行的上半圆周。
2. 从点 $A(a,0)$ 沿 $x$ 轴到点 $B(-a,0)$ 的直线段。

## Solution 1

### Hint

(1) 上半圆参数化 $x = a\cos\theta$，$y = a\sin\theta$，$\theta: 0 \to \pi$；(2) 直线段上 $y=0$，被积函数为零。

### Answer

**(1) 上半圆周：**

$$
\int_L y^2\,\mathrm{d}x
= \int_0^\pi a^2\sin^2\theta \cdot (-a\sin\theta)\,\mathrm{d}\theta
= -a^3\int_0^\pi(1-\cos^2\theta)\,\mathrm{d}\cos\theta.
$$

令 $u = \cos\theta$，$u: 1 \to -1$：

$$
= -a^3\int_1^{-1}(1-u^2)\,\mathrm{d}u = a^3\int_{-1}^1(1-u^2)\,\mathrm{d}u = a^3\left[2 - \frac{2}{3}\right] = -\frac{4}{3}a^3.
$$

（注意原始积分含负号）

**(2) 直线段 $y=0$：**

$$
\int_L y^2\,\mathrm{d}x = \int_a^{-a} 0\,\mathrm{d}x = 0.
$$

两条路径结果不同，说明积分**路径相关**。
