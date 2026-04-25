---
id: chpt6-ex-013
chapter: 6
tags: [定积分, 面积]
difficulty: easy
video:
---

## Problem

公共汽车每10分钟一班，乘客随机到达车站，求等待时间不超过3分钟的概率。

## Solution 1

### Hint

等待时间 $X$ 服从均匀分布 $U(0,10)$，用概率密度函数计算区间概率。

### Answer

$X \sim U(0,10)$，概率密度函数 $f(x) = \dfrac{1}{10}$（$0 \leq x \leq 10$）。

$$
P(0 \leq X \leq 3) = \int_0^3 \frac{1}{10}\,dx = \frac{3}{10}.
$$
