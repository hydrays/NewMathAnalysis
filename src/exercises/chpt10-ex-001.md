---
id: chpt10-ex-001
chapter: 10
tags: [多元函数, 极限, epsilon-delta证明]
difficulty: medium
video:
---

## Problem

设 $f(x,y) = (x^2 + y^2) \displaystyle\sin \frac{1}{x^2 + y^2}$，求证：

$$
\lim_{(x,y) \to (0,0)} f(x,y) = 0.
$$

## Solution 1

### Hint

利用夹逼定理：对正弦函数用绝对值不等式 $|\sin(\cdot)| \le 1$，将 $|f(x,y)|$ 用 $x^2+y^2$ 上界控制，再用 $\varepsilon$-$\delta$ 语言严格证明。

### Answer

函数 $f(x,y)$ 的定义域为 $D = \mathbb{R}^2 \backslash \{(0,0)\}$，点 $O(0,0)$ 为 $D$ 的聚点。

因为

$$
|f(x,y) - 0| = \left| (x^2 + y^2) \sin \frac{1}{x^2 + y^2} \right| \leq x^2 + y^2,
$$

可见，$\forall \varepsilon > 0$，取 $\delta = \sqrt{\varepsilon}$，则当 $0 < \sqrt{(x-0)^2 + (y-0)^2} < \delta$ 时，即 $P(x,y) \in D \cap U(O, \delta)$ 时，总有

$$
|f(x,y) - 0| \leq x^2 + y^2 < \delta^2 = \varepsilon
$$

成立，所以

$$
\lim_{(x,y) \to (0,0)} f(x,y) = 0.
$$
