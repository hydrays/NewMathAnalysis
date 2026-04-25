---
id: chpt2-ex-016
chapter: 2
tags: [导数, 极值, 应用题, 链式法则]
difficulty: hard
video:
---

## Problem

现需骑马从点 $A$ 到点 $B$，但必须先去河边（直线）喝一次水。已知点 $A$ 和点 $B$ 在河的同侧，且马在喝水前速度为 $v_1$，喝水后速度为 $v_2 < v_1$，求耗时最短的路径。

坐标系同上：$A = (0, h_1)$，$B = (l, h_2)$，饮水点 $P = (x, 0)$，$x \in [0, l]$。

**注意**：对这个题目而言，镜面反射原理不适用，但微积分方法仍然适用。

## Solution 1

### Hint

总时间 $T(x)$ 是路程除以速度的和，对 $T(x)$ 求导令其为零，分析令 $T'(x) = 0$ 的几何意义。

### Answer

总时间为：

$$
T(x) = \frac{\sqrt{h_1^2 + x^2}}{v_1} + \frac{\sqrt{h_2^2 + (l - x)^2}}{v_2}.
$$

对 $T(x)$ 求导得：

$$
\begin{align*}
T'(x) &= \frac{1}{v_1} \cdot \frac{x}{\sqrt{h_1^2 + x^2}} - \frac{1}{v_2} \cdot \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}.
\end{align*}
$$

令 $T'(x) = 0$，得：

$$
\frac{1}{v_1} \cdot \frac{x}{\sqrt{h_1^2 + x^2}} = \frac{1}{v_2} \cdot \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}.
$$

设 $\theta_1$ 为 $AP$ 与竖直方向的夹角，$\theta_2$ 为 $PB$ 与竖直方向的夹角，则 $\sin\theta_1 = \dfrac{x}{\sqrt{h_1^2+x^2}}$，$\sin\theta_2 = \dfrac{l-x}{\sqrt{h_2^2+(l-x)^2}}$，上式即：

$$
\frac{\sin \theta_1}{v_1} = \frac{\sin \theta_2}{v_2}.
$$

这正是**斯涅耳定律（Snell's Law）**，说明耗时最短的路径满足与光的折射相同的规律。

![问题2](../media/img/chpt2_specular_reflection.png#400w)
