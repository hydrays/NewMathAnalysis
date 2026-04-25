---
id: chpt13-ex-007
chapter: 13
title: 幂级数的收敛半径
tags: [幂级数, 收敛半径, 收敛域]
difficulty: medium
video:
---

## Problem

求幂级数 $\displaystyle\sum_{n=1}^{\infty} \frac{(x-1)^n}{2^n \cdot n}$ 的收敛域。

## Solution 1

### Hint

令 $t = x - 1$，将原级数化为标准幂级数形式，用比值法求收敛半径，再逐一检验端点处的收敛性。

### Answer

令 $t = x - 1$，原级数化为 $\displaystyle\sum_{n=1}^{\infty} \frac{t^n}{2^n n}$，其系数 $a_n = \dfrac{1}{2^n n}$。

**求收敛半径：**

$$
\rho = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \frac{2^n n}{2^{n+1}(n+1)} = \lim_{n \to \infty} \frac{n}{2(n+1)} = \frac{1}{2}.
$$

故收敛半径 $R_t = \dfrac{1}{\rho} = 2$，收敛区间为 $|t| < 2$，即 $|x - 1| < 2$，即 $-1 < x < 3$。

**检查端点：**

- 当 $x = -1$ 时，$t = -2$，级数变为 $\displaystyle\sum_{n=1}^{\infty} \frac{(-2)^n}{2^n n} = \sum_{n=1}^{\infty} \frac{(-1)^n}{n}$，这是交错调和级数，由莱布尼茨定理知其**收敛**。
- 当 $x = 3$ 时，$t = 2$，级数变为 $\displaystyle\sum_{n=1}^{\infty} \frac{2^n}{2^n n} = \sum_{n=1}^{\infty} \frac{1}{n}$，即调和级数，**发散**。

因此原级数的收敛域为 $\boldsymbol{[-1,\ 3)}$。
