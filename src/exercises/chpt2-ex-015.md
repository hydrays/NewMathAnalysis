---
id: chpt2-ex-015
chapter: 2
tags: [导数, 极值, 应用题]
difficulty: medium
video:
---

## Problem

假设马以均匀速度行进，现需骑马从点 $A$ 到点 $B$，但必须先去河边（直线）喝一次水。已知点 $A$ 和点 $B$ 在河的同侧，求耗时最短的路径。

建立坐标系：
- 设河边为 $x$ 轴；
- 点 $A$ 坐标为 $(0, h_1)$，点 $B$ 坐标为 $(l, h_2)$，其中 $h_1 > 0, h_2 > 0$；
- 设饮水点为 $P(x, 0)$，其中 $x \in [0, l]$。

![问题](../media/img/chpt2_horse_drinking_problem.png#400w)

## Solution 1

### Hint

路径总长度是 $x$ 的函数，对其求导令导数为零，找到最短路径对应的 $x$。

### Answer

路径总长度 $S(x)$ 为：

$$
S(x) = \sqrt{h_1^2 + x^2} + \sqrt{h_2^2 + (l - x)^2}.
$$

对 $S(x)$ 求导：

$$
S'(x) = \frac{x}{\sqrt{h_1^2 + x^2}} - \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}.
$$

令 $S'(x) = 0$，得：

$$
\frac{x}{\sqrt{h_1^2 + x^2}} = \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}.
$$

解得：

$$
x = \frac{l h_1}{h_1 + h_2}.
$$

## Solution 2

### Hint

将点 $B$ 关于 $x$ 轴作对称点 $B'$，直线 $AB'$ 与 $x$ 轴的交点即为最短路径的饮水点，利用三角形相似得到 $x$。

### Answer

将点 $B$ 关于 $x$ 轴（河边）反射到点 $B'$，坐标为 $(l, -h_2)$。

连接点 $A(0, h_1)$ 和点 $B'(l, -h_2)$，与 $x$ 轴的交点即为饮水点 $P$。根据三角形相似，同样可得：

$$
x = \frac{l h_1}{h_1 + h_2}.
$$

这个方法利用了镜面反射原理，基于直线最短得到了快速直观的解法。

![镜面反射原理](../media/img/chpt2_horse_drinking_problem_2.png#400w)
