---
id: chpt10-ex-016
chapter: 10
title: 开集的判断
tags: [多元函数, 点集拓扑, 开集]
difficulty: easy
video:
---

## Problem

证明集合 $D = \{(x,y) \mid 1 < x^2 + y^2 < 2\}$ 为开集.

## Solution 1

### Hint

按开集定义，对 $D$ 中任意一点，找到一个完全包含于 $D$ 的邻域即可.

### Answer

要证 $D$ 是开集，需证 $D$ 中的每一个点都是 $D$ 的内点.

设 $P(x,y) \in D$，即 $1 < x^2 + y^2 < 2$.

令 $r_1 = x^2 + y^2 - 1 > 0$，$r_2 = 2 - x^2 - y^2 > 0$，取

$$\delta = \frac{\min\{r_1, r_2\}}{2} > 0.$$

对 $P$ 的 $\delta$-邻域 $U(P,\delta)$ 中任意一点 $Q(x',y')$，有

$$\left|\sqrt{x'^2+y'^2} - \sqrt{x^2+y^2}\right| \leq \sqrt{(x'-x)^2+(y'-y)^2} < \delta.$$

因此

$$x^2+y^2 - \delta < x'^2+y'^2 < x^2+y^2 + \delta,$$

从而

$$x'^2+y'^2 > x^2+y^2 - \delta \geq 1 + r_1 - \frac{r_1}{2} > 1,$$

$$x'^2+y'^2 < x^2+y^2 + \delta \leq 2 - r_2 + \frac{r_2}{2} < 2.$$

故 $Q \in D$，即 $U(P,\delta) \subset D$. 由此 $P$ 是 $D$ 的内点.

由 $P$ 的任意性，$D$ 的每个点都是内点，所以 $D$ 是**开集**. $\blacksquare$
