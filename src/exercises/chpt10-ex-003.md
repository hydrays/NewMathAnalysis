---
id: chpt10-ex-003
chapter: 10
tags: [多元函数, 极限, 等价无穷小]
difficulty: easy
video:
---

## Problem

求极限

$$
\lim_{(x,y) \to (0,2)} \frac{\sin(xy)}{x}.
$$

## Solution 1

### Hint

将 $\dfrac{\sin(xy)}{x}$ 改写为 $\dfrac{\sin(xy)}{xy} \cdot y$，再利用 $\lim_{u \to 0} \dfrac{\sin u}{u} = 1$。

### Answer

函数 $\dfrac{\sin(xy)}{x}$ 的定义域为 $D = \{(x,y) \mid x \neq 0, y \in \mathbb{R}\}$，$P_0(0,2)$ 为 $D$ 的聚点。

$$
\lim_{(x,y) \to (0,2)} \frac{\sin(xy)}{x}
= \lim_{(x,y) \to (0,2)} \left[ \frac{\sin(xy)}{xy} \cdot y \right]
= \lim_{xy \to 0} \frac{\sin(xy)}{xy} \cdot \lim_{y \to 2} y
= 1 \cdot 2 = 2.
$$
