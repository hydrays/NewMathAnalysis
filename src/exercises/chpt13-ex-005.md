---
id: chpt13-ex-005
chapter: 13
title: 阶乘级数的收敛性
tags: [级数, 比值判别法, 收敛性]
difficulty: easy
video:
---

## Problem

判断级数 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n!}$ 的收敛性。

## Solution 1

### Hint

使用比值审敛法（达朗贝尔判别法），计算相邻两项之比的极限。

### Answer

令 $u_n = \dfrac{1}{n!}$，计算相邻两项之比的极限：

$$
\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = \lim_{n \to \infty} \frac{n!}{(n+1)!} = \lim_{n \to \infty} \frac{1}{n+1} = 0 < 1.
$$

由比值审敛法，$\rho = 0 < 1$，故级数 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n!}$ **收敛**。
