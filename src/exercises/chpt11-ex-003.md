---
id: chpt11-ex-003
chapter: 11
tags: [二重积分, 累次积分, 积分顺序交换]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle\iint_{D} xy\,\mathrm{d}x\,\mathrm{d}y$，其中积分区域 $D$ 由直线 $y = 1$、$x = 2$ 及 $y = x$ 围成。

## Solution 1

### Hint

先画出区域 $D$：三角形，顶点为 $(1,1)$，$(2,1)$，$(2,2)$。选取以 $x$ 为外积分变量时，$y$ 从 $1$ 到 $x$；以 $y$ 为外变量时，$x$ 从 $y$ 到 $2$。

### Answer

**解法一：先对 $y$ 后对 $x$**

$$
\iint_D xy\,\mathrm{d}x\,\mathrm{d}y
= \int_1^2\!\left[\int_1^x xy\,\mathrm{d}y\right]\mathrm{d}x
= \int_1^2\left[\frac{xy^2}{2}\right]_1^x\mathrm{d}x
= \int_1^2\left(\frac{x^3}{2} - \frac{x}{2}\right)\mathrm{d}x
= \left[\frac{x^4}{8} - \frac{x^2}{4}\right]_1^2 = \frac{9}{8}.
$$

**解法二：先对 $x$ 后对 $y$**

$$
\iint_D xy\,\mathrm{d}x\,\mathrm{d}y
= \int_1^2\!\left[\int_y^2 xy\,\mathrm{d}x\right]\mathrm{d}y
= \int_1^2\left[\frac{x^2 y}{2}\right]_y^2\mathrm{d}y
= \int_1^2\left(2y - \frac{y^3}{2}\right)\mathrm{d}y
= \left[y^2 - \frac{y^4}{8}\right]_1^2 = \frac{9}{8}.
$$

两种顺序结果一致。

## Solution 2

### Hint

可直接交换积分顺序验证结果相同，适合练习区域描述的两种表达方式。

### Answer

同解法一、二，见上。
