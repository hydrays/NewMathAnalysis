---
id: chpt6-ex-010
chapter: 6
tags: [定积分, 面积]
difficulty: medium
video:
---

## Problem

万有引力做功：质量为 $m$ 的物体从距地心 $r$ 处移动到无穷远处，求克服地球引力所做的功（地球质量 $M$，引力常数 $G$）。

## Solution 1

### Hint

引力 $F(x) = GMm/x^2$，对变力沿路径积分，上限取 $\infty$（反常积分）。

### Answer

$$
W = \int_r^\infty \frac{GMm}{x^2}\,dx = \lim_{b\to\infty} GMm\left[-\frac{1}{x}\right]_r^b = \lim_{b\to\infty} GMm\left(\frac{1}{r} - \frac{1}{b}\right) = \frac{GMm}{r}.
$$

这就是引力势能公式，积分收敛于有限值。
