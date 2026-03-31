import numpy as np
import matplotlib.pyplot as plt

# 时间参数
dt = 0.001
T = 10
t = np.arange(0, T, dt)

# PID参数
Kp, Ki, Kd = 10.0, 10.505, 0.0

# 初始状态
theta = 0.0       # 火箭角度
omega = 0.0       # 角速度
theta_target = 1.0  # 目标角度 (弧度)
e_prev = 0.0
integral = 0.0

thetas = []

for _ in t:
    e = theta_target - theta
    integral += e * dt
    derivative = (e - e_prev) / dt
    alpha = Kp * e + Ki * integral + Kd * derivative
    e_prev = e

    # 火箭动力学方程
    omega += 0.5 * alpha * dt   # dω/dt = k * α, 假设k=0.5
    theta += omega * dt
    thetas.append(theta)

plt.plot(t, thetas, label="θ(t)")
plt.axhline(theta_target, color='r', linestyle='--', label="目标角度")
plt.xlabel("时间 (s)")
plt.ylabel("姿态角 θ(t)")
plt.title("火箭姿态控制中的微分作用示意")
plt.legend()
plt.grid(True)
plt.show()
