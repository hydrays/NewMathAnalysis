---
id: chpt9-ex-006
chapter: 9
tags: [二重积分, 极坐标]
difficulty: hard
video:
---

## Problem

求过点 $(2,1,3)$ 且与直线 $\dfrac{x+1}{3}=\dfrac{y-1}{2}=\dfrac{z}{-1}$ 垂直相交的直线方程。

## Solution 1

### Hint

设交点为已知直线上的参数点，利用方向向量与已知方向正交（内积为零）求参数，再写出所求直线方程。

### Answer

已知直线参数方程：$x=-1+3t,\ y=1+2t,\ z=-t$。设交点 $M=(-1+3t, 1+2t, -t)$，$P=(2,1,3)$。

方向向量 $\overrightarrow{PM} = (3t-3,\ 2t,\ -t-3)$ 须与已知方向向量 $\mathbf{s}=(3,2,-1)$ 正交：

$$
3(3t-3)+2(2t)-(-t-3)=0 \implies 14t-6=0 \implies t=\frac{3}{7}.
$$

方向向量 $\overrightarrow{PM} = \left(-\dfrac{12}{7}, \dfrac{6}{7}, -\dfrac{24}{7}\right)$，取比例向量 $(2,-1,4)$。

所求直线方程：

$$
\frac{x-2}{2} = \frac{y-1}{-1} = \frac{z-3}{4}.
$$
