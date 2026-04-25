---
id: chpt7-ex-004
chapter: 7
title: 城市热岛效应模型
tags: [常微分方程, 应用, 环境]
difficulty: hard
video:
---

## Problem

**城市热岛效应模型**

城市热岛效应是指由于人类活动和城市结构导致城市温度显著高于周边郊区的现象。为了描述这种现象，可以使用以下一阶线性微分方程模型：

$$
\frac{dT}{dt} = -\alpha(t) T + Q(t)
$$

其中：
- $T(t)$：城市的平均温度（随时间变化）；
- $\alpha(t)$：时间相关的散热系数，表示城市向外部环境散热的效率。
  白天，建筑材料吸热，散热效率降低，$\alpha(t)$ 较小；
  夜晚，城市散热效率提高，$\alpha(t)$ 较大；
- $Q(t)$：时间相关的外部热源，包括：
  太阳辐射（随时间变化呈现周期性）以及人类活动（如车辆排放、工业生产、空调使用等，通常在白天达到高峰）。

**模型扩展（通常用在数学建模中）**

- **加入风速影响：**
  散热系数 $\alpha(t)$ 可以扩展为 $\alpha(t, v_w)$，其中 $v_w$ 为风速。风速较大时，散热效果增强：
  $$
  \frac{dT}{dt} = -\alpha(t, v_w) T + Q(t)
  $$

- **考虑湿度和绿化率：**
  可以通过引入湿度和绿化率来模拟更复杂的热交换过程：
  $$
  \frac{dT}{dt} = -(\alpha(t) + \beta H + \gamma G)T + Q(t)
  $$
  其中 $H$ 为湿度，$G$ 为绿化率，$\beta$ 和 $\gamma$ 为对应的影响系数。

利用常数变异法，写出上述一阶线性微分方程的通解。

## Solution 1

### Hint

方程 $\frac{dT}{dt} = -\alpha(t) T + Q(t)$ 是变系数一阶线性微分方程，对应 $k(x) = -\alpha(t)$，$b(x) = Q(t)$。先求齐次方程的解，再用常数变异法求特解。

### Answer

利用常数变异法，通解为：

$$
T = Ce^{\int k(t) dt} + e^{\int k(t) dt} \int b(t) e^{-\int k(t) dt} dt
$$

对本题，$k(t) = -\alpha(t)$，$b(t) = Q(t)$，代入得：

**Step 1**：求齐次方程 $\frac{dT}{dt} = -\alpha(t) T$ 的解：

$$
\frac{dT}{T} = -\alpha(t)\,dt \implies \ln|T| = -\int \alpha(t)\,dt + C
$$

齐次解：

$$
T_h = Ce^{-\int \alpha(t)\,dt}
$$

**Step 2**：设特解形式为 $T_p = u(t) e^{-\int \alpha(t)\,dt}$，代入原方程：

$$
u'(t) e^{-\int \alpha(t)\,dt} = Q(t)
$$

故：

$$
u'(t) = Q(t) e^{\int \alpha(t)\,dt}
$$

积分得：

$$
u(t) = \int Q(t) e^{\int \alpha(t)\,dt}\,dt
$$

**Step 3**：通解为：

$$
T(t) = e^{-\int \alpha(t)\,dt}\left(C + \int Q(t) e^{\int \alpha(t)\,dt}\,dt\right)
$$

其中 $C$ 由初始条件 $T(0) = T_0$ 确定。这个解描述了城市温度在散热系数和外部热源共同作用下随时间的演化规律。
