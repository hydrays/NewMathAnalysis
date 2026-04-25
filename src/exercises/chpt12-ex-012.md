---
id: chpt12-ex-012
chapter: 12
tags: [格林公式, 奇点, 复连通区域]
difficulty: hard
video:
---

## Problem

计算 $\displaystyle\oint_L \frac{x\,\mathrm{d}y - y\,\mathrm{d}x}{x^2+y^2}$，其中 $L$ 为一条无重点、分段光滑且不经过原点的连续闭曲线，$L$ 方向为逆时针。

## Solution 1

### Hint

令 $P = \frac{-y}{x^2+y^2}$，$Q = \frac{x}{x^2+y^2}$，验证 $P_y = Q_x$（在 $x^2+y^2\neq 0$ 时）。分两种情形：原点在曲线围成区域内与否。当原点在区域内时，挖去小圆 $l: x^2+y^2=r^2$，在复连通区域上用格林公式。

### Answer

令 $P = \dfrac{-y}{x^2+y^2}$，$Q = \dfrac{x}{x^2+y^2}$。当 $x^2+y^2\neq 0$ 时：

$$
Q_x = \frac{y^2-x^2}{(x^2+y^2)^2} = P_y.
$$

**情形 (1)：原点不在 $L$ 围成的区域 $D$ 内。**

由格林公式：

$$
\oint_L \frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2} = 0.
$$

**情形 (2)：原点在 $D$ 内。**

取小圆 $l: x^2+y^2=r^2$（$r$ 足够小，位于 $D$ 内），对 $L$ 和 $l$ 围成的复连通区域 $D_1$ 用格林公式（两条边界均逆时针）：

$$
\oint_L \frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2} - \oint_l \frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2} = 0.
$$

在 $l$ 上参数化 $x = r\cos\theta$，$y = r\sin\theta$，$\theta: 0\to 2\pi$：

$$
\oint_l \frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2} = \int_0^{2\pi}\frac{r^2(\cos^2\theta+\sin^2\theta)}{r^2}\,\mathrm{d}\theta = 2\pi.
$$

故

$$
\oint_L \frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2} = 2\pi.
$$
