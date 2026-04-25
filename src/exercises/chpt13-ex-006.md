---
id: chpt13-ex-006
chapter: 13
title: 交错调和级数
tags: [交错级数, Leibniz判别法, 收敛性]
difficulty: easy
video:
---

## Problem

判断交错调和级数 $\displaystyle 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots + (-1)^{n-1}\frac{1}{n} + \cdots$ 的收敛性。

## Solution 1

### Hint

验证莱布尼茨定理（交错级数审敛法）的两个条件：各项绝对值单调递减，且通项趋于零。

### Answer

该级数是交错级数 $\displaystyle\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{n}$，令 $u_n = \dfrac{1}{n}$。

验证莱布尼茨定理的两个条件：

1. **单调递减**：$u_n = \dfrac{1}{n} \geqslant \dfrac{1}{n+1} = u_{n+1}$，各项绝对值单调递减。
2. **趋于零**：$\displaystyle\lim_{n \to \infty} u_n = \lim_{n \to \infty} \frac{1}{n} = 0$。

两个条件均满足，由莱布尼茨定理，该交错调和级数**收敛**。

注意：该级数只是**条件收敛**（加绝对值后变为调和级数，发散），而非绝对收敛。
