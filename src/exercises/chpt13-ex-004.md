---
id: chpt13-ex-004
chapter: 13
title: 极限比较判别法
tags: [级数, 极限比较判别法, 收敛性]
difficulty: easy
video:
---

## Problem

判断级数 $\displaystyle\sum_{n=1}^{\infty} \sin\frac{1}{n}$ 的收敛性。

## Solution 1

### Hint

取调和级数 $v_n = \frac{1}{n}$ 作为比较对象，利用极限比较审敛法，计算 $\lim_{n\to\infty}\frac{u_n}{v_n}$。

### Answer

取 $v_n = \dfrac{1}{n}$（调和级数，发散）。计算极限：

$$
\lim_{n \to \infty} \frac{\sin \frac{1}{n}}{\frac{1}{n}} = 1 > 0.
$$

由极限比较审敛法，$\sum \sin\frac{1}{n}$ 与 $\sum \frac{1}{n}$ **同收敛或同发散**。因为 $\sum \frac{1}{n}$ 发散，故 $\displaystyle\sum_{n=1}^{\infty} \sin\frac{1}{n}$ **发散**。
