---
id: chpt7-ex-003
chapter: 7
title: 贷款偿还模型
tags: [常微分方程, 应用, 金融数学]
difficulty: medium
video:
---

## Problem

**简单贷款偿还模型**

贷款偿还模型描述了借款人以恒定利率和固定还款额偿还贷款的过程，其微分方程为：

$$
\frac{dB}{dt} = rB - P
$$

其中：
- $B(t)$：时间 $t$ 时剩余的贷款余额；
- $r$：年利率（常数）；
- $P$：每年固定还款额。

设初始条件为 $B(0) = B_0$，求 $B(t)$，并讨论在何条件下贷款最终能被还清。

## Solution 1

### Hint

方程是一阶线性微分方程，可以用分离变量法处理。令 $u = rB - P$，则 $\frac{du}{dt} = r\frac{dB}{dt} = r(rB - P) = ru$。

### Answer

**求解过程（分离变量法）**

1. 将方程整理为：
$$
\frac{dB}{rB - P} = dt
$$

2. 对两边积分：
$$
\int \frac{dB}{rB - P} = \int dt
$$

3. 积分结果为：
$$
\frac{1}{r} \ln |rB - P| = t + C
$$

4. 解出 $B$：
$$
rB - P = C_1 e^{rt}
$$

其中 $C_1 = e^{rC}$。

5. 利用初始条件 $B(0) = B_0$，求出 $C_1$：
$$
rB_0 - P = C_1
$$

6. 最终解为：
$$
B(t) = \frac{P}{r} + \left( B_0 - \frac{P}{r} \right) e^{rt}
$$

**解释**：如果 $P > rB_0$，余额 $B(t)$ 随时间逐渐减少，最终贷款将被还清；反之，如果 $P \leq rB_0$，贷款余额将持续增长。
