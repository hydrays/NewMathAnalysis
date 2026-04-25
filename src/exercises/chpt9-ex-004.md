---
id: chpt9-ex-004
chapter: 9
tags: [二重积分, 极坐标]
difficulty: medium
video:
---

## Problem

求与两平面 $x-4z=3$ 和 $2x-y-5z=1$ 的交线平行且过点 $(-3,2,5)$ 的直线方程。

## Solution 1

### Hint

所求直线的方向向量必须同时垂直于两平面的法向量，即等于两法向量的叉乘。

### Answer

两平面法向量：$\mathbf{n}_1=(1,0,-4)$，$\mathbf{n}_2=(2,-1,-5)$。

方向向量：

$$
\mathbf{s} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & -4 \\ 2 & -1 & -5 \end{vmatrix} = -4\mathbf{i}-3\mathbf{j}-\mathbf{k},
$$

取 $\mathbf{s} = (4,3,1)$（方向不变）。

结合点 $(-3,2,5)$，直线方程为：

$$
\frac{x+3}{4} = \frac{y-2}{3} = \frac{z-5}{1}.
$$
