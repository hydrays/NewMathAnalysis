---
id: chpt10-ex-004
chapter: 10
tags: [偏导数, 分段函数, 定义法求导]
difficulty: medium
video:
---

## Problem

求分段函数

$$
z = f(x, y) = \begin{cases} \dfrac{xy}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0 \end{cases}
$$

在点 $(0, 0)$ 处的偏导数 $f_x(0,0)$ 和 $f_y(0,0)$。

## Solution 1

### Hint

在原点处不能用求导公式，需回到偏导数的定义，用差商极限直接计算。

### Answer

**计算 $f_x(0,0)$：**

$$
f_x(0, 0) = \lim_{\Delta x \to 0} \frac{f(0 + \Delta x,\, 0) - f(0, 0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{0 - 0}{\Delta x} = 0.
$$

**计算 $f_y(0,0)$：**

$$
f_y(0, 0) = \lim_{\Delta y \to 0} \frac{f(0,\, 0 + \Delta y) - f(0, 0)}{\Delta y} = \lim_{\Delta y \to 0} \frac{0 - 0}{\Delta y} = 0.
$$

故 $f_x(0,0) = f_y(0,0) = 0$。

**注意：** 尽管偏导数在原点存在，但由例 chpt10-ex-002 知该函数在原点的极限不存在，故函数在原点不连续，这说明偏导数存在不能保证函数连续。
