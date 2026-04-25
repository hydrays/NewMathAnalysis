---
id: chpt6-ex-009
chapter: 6
tags: [定积分, 面积]
difficulty: medium
video:
---

## Problem

抽水做功：设圆柱形水箱半径为 $R$，高为 $H$，装满密度为 $\rho$ 的液体，求将液体全部抽出水箱顶部所需做的功。

## Solution 1

### Hint

将水箱沿高度方向分层，距底面高度 $x$ 处的薄层需提升距离为 $H-x$，建立积分。

### Answer

距底面高度 $x$ 处厚度为 $dx$ 的水层的质量为 $\rho\pi R^2\,dx$，需提升距离 $H-x$，故功微元为

$$
dW = \rho\pi R^2(H-x)\,g\,dx.
$$

总功为

$$
W = \int_0^H \rho g\pi R^2(H-x)\,dx = \rho g\pi R^2 \cdot \frac{H^2}{2} = \frac{1}{2}\rho g\pi R^2 H^2.
$$
