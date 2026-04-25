---
id: chpt6-ex-014
chapter: 6
tags: [定积分, 面积]
difficulty: medium
video:
---

## Problem

某电子元件的寿命 $X$（单位：小时）服从参数 $\lambda = 0.001$ 的指数分布，求该元件能工作超过1000小时的概率。

## Solution 1

### Hint

$P(X > 1000) = \displaystyle\int_{1000}^\infty \lambda e^{-\lambda x}\,dx$，用反常积分计算。

### Answer

$$
P(X > 1000) = \int_{1000}^\infty 0.001\,e^{-0.001x}\,dx = \lim_{b\to\infty}\left[-e^{-0.001x}\right]_{1000}^b = e^{-1} \approx 0.3679.
$$
