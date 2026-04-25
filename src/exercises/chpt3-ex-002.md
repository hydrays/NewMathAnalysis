---
id: chpt3-ex-002
chapter: 3
tags: [导数应用, 微分]
difficulty: easy
video:
---

## Problem

激光从原点以角度 $\theta$ 射出，与直线 $y = b$ 的交点横坐标为 $x = \dfrac{b}{\tan\theta}$，激光飞行距离为 $l = \dfrac{b}{\sin\theta}$。利用微分公式，分别求 $dx$ 与 $d\theta$、$dl$ 与 $d\theta$ 的关系，并由此计算 $\dfrac{dx}{dl}$。

## Solution 1

### Hint

对 $x$ 和 $l$ 分别关于 $\theta$ 求导，再用微分之比直接求 $dx/dl$。

### Answer

**$dx$ 与 $d\theta$ 的关系**：

对 $x = b/\tan\theta = b\cot\theta$ 求导：

$$
\frac{dx}{d\theta} = -\frac{b}{\sin^2\theta},
$$

故

$$
dx = -\frac{b}{\sin^2\theta}\,d\theta.
$$

**$dl$ 与 $d\theta$ 的关系**：

对 $l = b/\sin\theta$ 求导：

$$
\frac{dl}{d\theta} = -\frac{b\cos\theta}{\sin^2\theta},
$$

故

$$
dl = -\frac{b\cos\theta}{\sin^2\theta}\,d\theta.
$$

**计算 $dx/dl$（利用微分之比）**：

$$
\frac{dx}{dl} = \frac{-\dfrac{b}{\sin^2\theta}\,d\theta}{-\dfrac{b\cos\theta}{\sin^2\theta}\,d\theta} = \frac{1}{\cos\theta}.
$$

因此 $dx = \dfrac{1}{\cos\theta}\,dl$，即出射角每变化 $dl$ 长度时，光斑横坐标变化 $\dfrac{1}{\cos\theta}\,dl$。
