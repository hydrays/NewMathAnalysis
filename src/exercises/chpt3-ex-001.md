---
id: chpt3-ex-001
chapter: 3
tags: [导数应用, 微分]
difficulty: easy
video:
---

## Problem

对于匀速运动 $s = s_0 + vt$ 和初速度为零的匀加速运动 $s = s_0 + \frac{1}{2}at^2$，利用微分公式分别写出位移微分 $ds$ 与时间微分 $dt$ 之间的关系，并说明线性函数情形下微分给出精确值的原因。

## Solution 1

### Hint

对函数 $s = f(t)$ 应用微分公式 $ds = f'(t)\,dt$，分别对两个运动函数求导。

### Answer

**匀速运动**：$s = s_0 + vt$，求导得 $s'(t) = v$，故

$$
ds = v\,dt.
$$

对于线性函数，$\Delta s = v\Delta t$ 精确成立（无误差），因为线性函数的差分与微分完全相等：$\Delta s - ds = 0$。

**匀加速运动**：$s = s_0 + \frac{1}{2}at^2$，求导得 $s'(t) = at$，故

$$
ds = at\,dt.
$$

此时真实增量 $\Delta s = at\Delta t + \frac{1}{2}a(\Delta t)^2$，而微分预测值为 $at\Delta t$，误差为 $\frac{1}{2}a(\Delta t)^2$。当 $\Delta t \to 0$ 时，误差趋于零，体现了"化曲为直"的思想。
