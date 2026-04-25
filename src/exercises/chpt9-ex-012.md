---
id: chpt9-ex-012
chapter: 9
tags: [二重积分, 曲线积分]
difficulty: medium
video:
---

## Problem

设一个立体由上半球面 $z = \sqrt{4-x^2-y^2}$ 和锥面 $z = \sqrt{3(x^2+y^2)}$ 所围成，求它在 $xOy$ 面上的投影。

## Solution 1

### Hint

令两曲面相等消去 $z$，求出交线在 $xOy$ 面的投影柱面，再确定立体投影区域。

### Answer

由交线条件 $\sqrt{4-x^2-y^2} = \sqrt{3(x^2+y^2)}$ 消去 $z$：

$$
4-x^2-y^2 = 3(x^2+y^2) \implies 4x^2+4y^2=4 \implies x^2+y^2=1.
$$

投影柱面为 $x^2+y^2=1$。立体在 $xOy$ 面上的投影为圆盘：

$$
x^2+y^2 \leq 1.
$$
