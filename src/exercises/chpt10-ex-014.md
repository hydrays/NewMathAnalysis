---
id: chpt10-ex-014
chapter: 10
tags: [多元极值, 无约束极值, 应用题, 最省材料]
difficulty: medium
video:
---

## Problem

某厂要用铁板做成一个体积为 $2\,\text{m}^3$ 的有盖长方体水箱，问当长、宽、高各取怎样的尺寸时，用料最省？

## Solution 1

### Hint

设长为 $x$，宽为 $y$，则高由体积约束确定为 $\frac{2}{xy}$；写出表面积函数 $A(x,y)$，令偏导为零求驻点，再用唯一驻点论证极值。

### Answer

设水箱长为 $x\,\text{m}$，宽为 $y\,\text{m}$，则高为 $\dfrac{2}{xy}\,\text{m}$。

表面积（目标函数）：

$$
A(x,y) = 2\left(xy + \frac{2}{x} + \frac{2}{y}\right), \quad x > 0,\ y > 0.
$$

令偏导数为零：

$$
A_x = 2\left(y - \frac{2}{x^2}\right) = 0, \qquad A_y = 2\left(x - \frac{2}{y^2}\right) = 0.
$$

解方程组：

$$
y = \frac{2}{x^2}, \quad x = \frac{2}{y^2} \implies x = y = \sqrt[3]{2}.
$$

唯一驻点为 $\left(\sqrt[3]{2},\, \sqrt[3]{2}\right)$，此时高为

$$
\frac{2}{\sqrt[3]{2} \cdot \sqrt[3]{2}} = \sqrt[3]{2}\,\text{m}.
$$

由题意最小值在开区域内存在且唯一驻点处取得，故当水箱长、宽、高均为 $\sqrt[3]{2}\approx 1.26\,\text{m}$ 时，用料最省（即正方体形状）。
