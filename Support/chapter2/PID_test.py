import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ================== 可调参数 ==================
dt = 0.02           # 仿真步长 (s)
T  = 10.0           # 动画时长 (s)
k  = 0.6            # 被控对象: 角加速度 = k * α
theta_target_deg = 15.0  # 目标姿态(度)

# PID 增益（可改后重跑观察差异）
Kp, Ki, Kd = 10.0, 1.4, 3.2

# 喷管角度（执行器）限幅
alpha_limit_deg = 10.0

# ================== 初始化 ==================
theta_target = np.deg2rad(theta_target_deg)
alpha_limit  = np.deg2rad(alpha_limit_deg)

theta = 0.0       # 角度 θ
omega = 0.0       # 角速度 ω
e_prev = theta_target - theta
integral = 0.0

# 记录用
ts, ths, oms, als, es = [], [], [], [], []

# ================== 绘图元素 ==================
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Rocket Attitude • PID Control (微分的工程应用)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

# 曲线/图元
rocket_line, = ax.plot([], [], linewidth=3, label="Rocket")
thrust_line, = ax.plot([], [], linewidth=2, label="Engine gimbal (α)")
target_line, = ax.plot([], [], linestyle='--', linewidth=1.5, label="Target axis")

# 文本框
text_box = ax.text(
    0.02, 0.98, "", transform=ax.transAxes, va='top', ha='left', fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.8)
)
ax.legend(loc="lower right")

base = np.array([0.0, -1.0])  # 火箭底部位置
length = 1.8                  # 火箭长度
thrust_len = 0.9              # 喷管矢量可视长度

def line_from_angle(origin, angle, L):
    d = np.array([np.cos(angle), np.sin(angle)])
    p = origin + d * L
    return np.array([origin[0], p[0]]), np.array([origin[1], p[1]])

# 目标轴（静态）
tx, ty = line_from_angle(base, theta_target, 1.5)
target_line.set_data(tx, ty)

# ================== 动画回调 ==================
t = 0.0
def init():
    rocket_line.set_data([], [])
    thrust_line.set_data([], [])
    text_box.set_text("")
    return rocket_line, thrust_line, target_line, text_box

def update(frame):
    global t, theta, omega, e_prev, integral

    # 误差
    e = theta_target - theta
    # PID
    integral += e * dt
    derivative = (e - e_prev) / dt
    alpha = Kp * e + Ki * integral + Kd * derivative
    e_prev = e

    # 限幅
    alpha = np.clip(alpha, -alpha_limit, alpha_limit)

    # 被控对象 (欧拉法积分)
    omega += (k * alpha) * dt
    theta += omega * dt

    # 几何更新
    rx, ry = line_from_angle(base, theta, length)
    rocket_line.set_data(rx, ry)

    tx2, ty2 = line_from_angle(base, theta + alpha, thrust_len)
    thrust_line.set_data(tx2, ty2)

    # 文本
    text_box.set_text(
        f"t = {t:5.2f} s\n"
        f"θ = {np.rad2deg(theta):6.2f}°\n"
        f"ω = {np.rad2deg(omega):6.2f}°/s\n"
        f"α = {np.rad2deg(alpha):6.2f}°\n"
        f"e = {np.rad2deg(e):6.2f}°"
    )

    # 记录
    ts.append(t); ths.append(theta); oms.append(omega); als.append(alpha); es.append(e)
    t += dt

    return rocket_line, thrust_line, target_line, text_box

frames = int(T / dt)
anim = FuncAnimation(fig, update, init_func=init, frames=frames, interval=1000*dt, blit=True, repeat=False)

# ============ 可选：保存 GIF（需要 Pillow） ============
# from matplotlib.animation import PillowWriter
# anim.save("rocket_pid.gif", writer=PillowWriter(fps=20))
# print("Saved: rocket_pid.gif")

plt.show()
