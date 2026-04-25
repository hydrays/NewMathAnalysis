---
id: chpt12-ex-019
chapter: 12
tags: [Stokes公式, 三维曲线积分, 斯托克斯定理]
difficulty: medium
video:
---

## Problem

利用斯托克斯公式计算曲线积分 $\displaystyle\oint_\Gamma z\,\mathrm{d}x + x\,\mathrm{d}y + y\,\mathrm{d}z$，其中 $\Gamma$ 为平面 $x+y+z=1$ 被三个坐标面所截成的三角形的整个边界，正向与三角形上侧的法向量符合右手规则。

## Solution 1

### Hint

用斯托克斯公式将曲线积分化为三角形曲面 $\Sigma$ 上的曲面积分，再分别计算三个投影积分（每个投影区域为直角三角形，面积为 $\frac{1}{2}$）。

### Answer

由斯托克斯公式，设 $\Sigma$ 为三角形曲面（上侧）：

$$
\oint_\Gamma z\,\mathrm{d}x+x\,\mathrm{d}y+y\,\mathrm{d}z
= \iint_\Sigma \mathrm{d}y\,\mathrm{d}z + \mathrm{d}z\,\mathrm{d}x + \mathrm{d}x\,\mathrm{d}y.
$$

（由旋度 $\mathrm{curl}(z, x, y) = (1,1,1)$ 与法向量 $\frac{1}{\sqrt{3}}(1,1,1)$ 点积后化简可得。）

各投影积分均为对应坐标面上的三角形面积 $\frac{1}{2}$：

$$
\iint_\Sigma \mathrm{d}y\,\mathrm{d}z = \iint_{D_{yz}}\mathrm{d}\sigma = \frac{1}{2},\quad
\iint_\Sigma \mathrm{d}z\,\mathrm{d}x = \frac{1}{2},\quad
\iint_\Sigma \mathrm{d}x\,\mathrm{d}y = \frac{1}{2}.
$$

故

$$
\oint_\Gamma z\,\mathrm{d}x+x\,\mathrm{d}y+y\,\mathrm{d}z = \frac{3}{2}.
$$
