---
id: chpt6-ex-007
chapter: 6
tags: [定积分, 弧长, 极坐标]
difficulty: medium
video:
---

## Problem

计算心形线 $r = a(1+\cos\theta)$（$0 \leq \theta \leq 2\pi$）的周长。

## Solution 1

### Hint

用极坐标弧长公式 $L = \displaystyle\int_0^{2\pi} \sqrt{r^2 + (r')^2}\,d\theta$，利用半角公式 $1+\cos\theta = 2\cos^2(\theta/2)$ 化简被积函数。

### Answer

$\dfrac{dr}{d\theta} = -a\sin\theta$，故

$$
L = \int_0^{2\pi} \sqrt{a^2(1+\cos\theta)^2 + a^2\sin^2\theta}\,d\theta = a\int_0^{2\pi}\sqrt{2+2\cos\theta}\,d\theta.
$$

利用 $1+\cos\theta = 2\cos^2(\theta/2)$：

$$
L = a\int_0^{2\pi} 2\left|\cos\frac{\theta}{2}\right|d\theta = 4a\int_0^{\pi}\cos\frac{\theta}{2}\,d\theta = 8a.
$$
