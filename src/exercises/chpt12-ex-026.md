---
id: chpt12-ex-026
chapter: 12
tags: [曲面积分, 通量, 球面, 极坐标, 例题]
difficulty: medium
video:
---

## Problem

计算 $\mathbf{F}=z\hat{\mathbf{k}}$ 穿过上半球面 $S:\,x^2+y^2+z^2=a^2,\,z\geq 0$（取朝上法向量）的通量。

## Solution 1

### Hint

令 $z=g(x,y)=\sqrt{a^2-x^2-y^2}$，将曲面积分化为投影区域 $x^2+y^2\leq a^2$ 上的二重积分，再用极坐标计算。

### Answer

$z=g(x,y)=\sqrt{a^2-x^2-y^2}$，$P=Q=0,\,R=z$，$g_x=-x/z,\,g_y=-y/z$，故

$$\iint_S\mathbf{F}\cdot\mathrm{d}\mathbf{S} = \iint_{x^2+y^2\leq a^2} z\,\mathrm{d}x\,\mathrm{d}y = \iint_{x^2+y^2\leq a^2}\sqrt{a^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y.$$

用极坐标 $x=r\cos\theta,\,y=r\sin\theta$：

$$= \int_0^{2\pi}\int_0^a\sqrt{a^2-r^2}\cdot r\,\mathrm{d}r\,\mathrm{d}\theta = 2\pi\cdot\frac{a^3}{3} = \frac{2\pi a^3}{3}.$$
