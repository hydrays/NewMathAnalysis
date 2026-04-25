---
id: chpt9-ex-002
chapter: 9
tags: [二重积分, 极坐标]
difficulty: easy
video:
---

## Problem

求两直线

$$
L_1: \frac{x-1}{1}=\frac{y}{-4}=\frac{z+3}{1}, \quad L_2: \frac{x}{2}=\frac{y+2}{-2}=\frac{z}{-1}
$$

的夹角。

## Solution 1

### Hint

两直线夹角等于其方向向量夹角（取锐角），用内积公式计算余弦。

### Answer

方向向量：$\mathbf{s}_1=(1,-4,1)$，$\mathbf{s}_2=(2,-2,-1)$。

$$
\cos\varphi = \frac{|\mathbf{s}_1 \cdot \mathbf{s}_2|}{|\mathbf{s}_1||\mathbf{s}_2|} = \frac{|2+8-1|}{\sqrt{18}\cdot\sqrt{9}} = \frac{9}{3\sqrt{18}} = \frac{1}{\sqrt{2}}.
$$

故夹角 $\varphi = \dfrac{\pi}{4}$。
