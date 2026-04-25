---
id: chpt7-ex-002
chapter: 7
title: 牛顿冷却定律
tags: [常微分方程, 应用, 分离变量法]
difficulty: medium
video:
---

## Problem

**恒定速率的降温过程（牛顿冷却定律）**

牛顿冷却定律描述了物体与周围环境之间的温度变化过程，其微分方程模型为：

$$
\frac{dT}{dt} = -k (T - T_{\text{env}})
$$

其中：
- $T(t)$：物体在时间 $t$ 的温度；
- $T_{\text{env}}$：环境温度（常数）；
- $k$：冷却系数，$k > 0$。

设初始条件为 $T(0) = T_0$，求 $T(t)$。

## Solution 1

### Hint

将方程整理为变量分离形式，令 $u = T - T_{\text{env}}$，则 $\frac{du}{dt} = -ku$，这是一个标准的速率方程。

### Answer

**求解过程（分离变量法）**

1. 将方程整理为：
$$
\frac{dT}{T - T_{\text{env}}} = -k \, dt
$$

2. 对两边积分：
$$
\int \frac{dT}{T - T_{\text{env}}} = \int -k \, dt
$$

3. 积分结果为：
$$
\ln |T - T_{\text{env}}| = -kt + C
$$

4. 通过指数函数解出 $T$：
$$
T - T_{\text{env}} = C_1 e^{-kt}
$$

其中 $C_1 = e^C$ 为任意常数。

5. 利用初始条件 $T(0) = T_0$，求出 $C_1$：
$$
T_0 - T_{\text{env}} = C_1
$$

6. 最终解为：
$$
T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) e^{-kt}
$$

**解释**：物体的温度逐渐趋近于环境温度 $T_{\text{env}}$，冷却速度由系数 $k$ 控制。
