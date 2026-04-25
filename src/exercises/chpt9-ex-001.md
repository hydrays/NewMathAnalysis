---
id: chpt9-ex-001
chapter: 9
tags: [二重积分, 极坐标]
difficulty: medium
video:
---

## Problem

用对称式方程及参数方程表示直线

$$
\begin{cases} x+y+z+1=0 \\ 2x-y+3z+4=0 \end{cases}
$$

## Solution 1

### Hint

先找直线上一点（令某坐标为已知值求解），再取两平面法向量的叉乘得方向向量，最后写出对称式和参数方程。

### Answer

**第一步**：令 $x=1$，代入方程组得 $y=0, z=-2$，故直线过点 $(1, 0, -2)$。

**第二步**：方向向量为两平面法向量的叉乘：

$$
\mathbf{s} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 2 & -1 & 3 \end{vmatrix} = 4\mathbf{i} - \mathbf{j} - 3\mathbf{k}.
$$

**对称式方程**：

$$
\frac{x-1}{4} = \frac{y}{-1} = \frac{z+2}{-3}.
$$

**参数方程**：令比值为 $t$，得 $x=1+4t,\ y=-t,\ z=-2-3t$。
