import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos

# ============================================================
#  豪华可视化：火箭 + 喷焰锥 + 发射塔 + “筷子”夹持 + HUD
#  模型：theta'' = k * alpha ；alpha = PID(e)（含微分项）
#  坐标约定：
#    - 画面中 y 轴向上为正
#    - 火箭 θ=0 时竖直向上，推力/火焰在 θ=0, α=0 时竖直向下
# ============================================================

# ---------------------- 可调参数 ----------------------
dt = 0.015             # 仿真步长 (s)
T  = 14.0              # 总时长 (s)

# 目标姿态（度）
theta_target_deg = 0.0

# 初始状态（度、度/秒）
theta0_deg = 8.0       # 初始倾角（稍微歪一点）
omega0_deg = -4.0      # 初始角速度

# 被控对象：theta'' = k * alpha
k = 0.75

# PID 增益（可以现场改着玩）
Kp, Ki, Kd = 14.0, 2.0, 0

# 执行器限幅（喷管偏转角，度）
alpha_limit_deg = 10.0

# 推力等级（只用于火焰长度和宽度视觉效果）
thrust_max = 1.0
thrust_min = 0.15

# 轻微侧风/扰动（度/秒² 等效）
wind_torque_deg = 0.10

# 筷子夹持逻辑参数
clamp_theta_thresh_deg = 1.2    # 姿态误差容忍
clamp_rate_thresh_deg  = 2.0    # 角速度容忍
clamp_start_time       = 7.0    # s，最早开始可以考虑夹持
clamp_close_time       = 10.0   # s，基本夹紧完毕
clamp_open_span        = 1.2    # m，初始筷子间距
clamp_min_span         = 0.18   # m，夹紧时间距

# 场景尺寸（米）
SCENE_W, SCENE_H = 18, 22

# 火箭尺寸（米）
R_LEN = 7.5     # 总长
R_W   = 1.2     # 机身宽
LEG_W = 1.6     # 落脚架宽
NOZZLE_W = 0.6  # 喷口宽
FLAME_BASE_W = 0.8  # 火焰宽度基准系数

# 塔与筷子位置
TOWER_X = 0.0
TOWER_Y = -6.0

# 火箭初始底部位置
ROCKET_X0 = 0.0
ROCKET_Y0 = 4.5

# 火箭整体缓慢下降速度（只是视觉，不参与控制方程）
DESCENT_V = -0.35

HUD_FONT = dict(fontsize=10)

# 筷子竖线的高度范围
CLAMP_PIVOT_Y = TOWER_Y + 7.8
CLAMP_HALF_HEIGHT = 1.8   # 竖线上下长度的一半


# ============================================================
#           助手函数：几何构造 + 插值
# ============================================================
def deg(x): return np.rad2deg(x)
def rad(x): return np.deg2rad(x)

def lerp(a, b, u):
    return a + (b - a) * np.clip(u, 0.0, 1.0)

def smoothstep(u):
    u = np.clip(u, 0.0, 1.0)
    return u*u*(3-2*u)

def poly_body(theta, cx, cy):
    """
    构造火箭机身轮廓（带简单锥形头 + 底部落脚）
    局部坐标系：底部中心为 (0,0)，沿局部 y 轴向上为+，长度 R_LEN
    θ=0 时火箭竖直向上
    """
    s, c = np.sin(theta), np.cos(theta)

    w_mid = R_W * 0.45
    w_base = R_W * 0.5
    w_top  = R_W * 0.15

    # 主体轮廓（局部）
    pts_axial = np.array([
        [-w_base, 0.05*R_LEN], [-w_mid, 0.35*R_LEN], [-w_top, 0.86*R_LEN],
        [ 0.0,    R_LEN],      # 顶点
        [ w_top,  0.86*R_LEN], [ w_mid, 0.35*R_LEN], [ w_base, 0.05*R_LEN]
    ])

    # 落脚架（局部）
    leg = np.array([
        [-LEG_W*0.5, 0.0], [-LEG_W*0.35, 0.04*R_LEN],
        [ LEG_W*0.35, 0.04*R_LEN], [ LEG_W*0.5, 0.0]
    ])

    outline = np.vstack([leg, pts_axial])

    # 局部 → 世界
    Rm = np.array([[ c, -s],
                   [ s,  c]])
    world = outline @ Rm.T + np.array([cx, cy])
    return world[:,0], world[:,1]

def nozzle_poly(theta, cx, cy):
    """
    喷口多边形（短梯形），紧贴火箭底部
    局部参考点 z0 稍微在底部上方一点（跟火焰 anchor 保持一致）
    """
    s, c = np.sin(theta), np.cos(theta)
    z0 = np.array([0.0, 0.02*R_LEN])
    w0, w1, L = NOZZLE_W*0.5, NOZZLE_W*0.35, 0.55

    loc = np.array([
        [-w0, 0], [ w0, 0],
        [ w1, L], [-w1, L]
    ]) + z0
    Rm = np.array([[ c, -s],
                   [ s,  c]])
    world = loc @ Rm.T + np.array([cx, cy])
    return world[:,0], world[:,1]

def nozzle_anchor(theta, cx, cy):
    """
    喷口中心（作为火焰和推力向量的起点）
    与 nozzle_poly 里 z0 位置一致
    """
    s, c = np.sin(theta), np.cos(theta)
    local = np.array([0.0, 0.02*R_LEN])
    world = np.array([
        c*local[0] - s*local[1] + cx,
        s*local[0] + c*local[1] + cy
    ])
    return world[0], world[1]

def flame_poly_world(theta, alpha, thrust_lvl, base_x, base_y):
    """
    修正版火焰：
    - 以“竖直向下”为基准方向：
        θ = 0, α = 0 → 火焰方向 = 竖直向下 (0, -1)
    - 上端（靠近火箭尾部）窄、紧贴喷口
    - 下端（远离火箭）宽、向外张开
    - 方向 = -(rocket_axis + gimbal) 近似：d = [-sin(θ+α), -cos(θ+α)]
    """
    ang = theta + alpha

    # 推力方向（世界坐标）：θ=0, α=0 时 d = (0, -1)
    d = np.array([-np.sin(ang), -np.cos(ang)])
    # 垂直方向（用于“撑开”火焰宽度）
    n = np.array([d[1], -d[0]])   # 旋转 -90° 或 +90° 都可以，选一个即可

    # 火焰长度 & 上下半宽
    L = lerp(1.2, 5.0, thrust_lvl)
    inner_half = FLAME_BASE_W * 0.20         # 上端窄
    outer_half = lerp(0.4, 1.2, thrust_lvl)  # 下端宽

    p0 = np.array([base_x, base_y])          # 火焰起点 = 喷口中心

    inner1 = p0 + n * inner_half
    inner2 = p0 - n * inner_half
    outer_center = p0 + d * L
    outer1 = outer_center + n * outer_half
    outer2 = outer_center - n * outer_half

    pts = np.vstack([inner1, inner2, outer2, outer1])
    return pts[:,0], pts[:,1]

def tower_geom():
    """发射塔主体与地面平台"""
    tower_w = 1.1
    tower_h = 9.0
    base_y  = TOWER_Y
    x0 = TOWER_X - tower_w*0.5
    y0 = base_y
    tower_poly = np.array([
        [x0, y0],
        [x0 + tower_w, y0],
        [x0 + tower_w, y0 + tower_h],
        [x0, y0 + tower_h]
    ])
    ground_poly = np.array([
        [-SCENE_W*0.48, base_y - 0.3],
        [ SCENE_W*0.48, base_y - 0.3],
        [ SCENE_W*0.48, base_y - 0.7],
        [-SCENE_W*0.48, base_y - 0.7]
    ])
    return tower_poly, ground_poly


# ============================================================
#                 控制 & 场景状态变量
# ============================================================
alpha_limit = rad(alpha_limit_deg)
theta = rad(theta0_deg)
omega = rad(omega0_deg)
theta_target = rad(theta_target_deg)

e_prev = theta_target - theta
integral = 0.0

t = 0.0
rx, ry = ROCKET_X0, ROCKET_Y0

# 筷子状态：两条竖线之间当前间距
clamp_span = clamp_open_span
clamped = False

# ============================================================
#                         画布
# ============================================================
plt.rcParams["figure.dpi"] = 110
fig, ax = plt.subplots(figsize=(7.5, 9))
ax.set_xlim(-SCENE_W/2, SCENE_W/2)
ax.set_ylim(-SCENE_H/2, SCENE_H/2)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Micro-Differential → PID: Rocket Attitude & Chopsticks Capture", fontsize=12)
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_facecolor("#0b0f18")
ax.grid(alpha=0.18)

# 背景星点
np.random.seed(1)
stars = np.random.uniform([-SCENE_W/2, -SCENE_H/2],
                          [ SCENE_W/2,  SCENE_H/2],
                          size=(180,2))
ax.scatter(stars[:,0], stars[:,1], s=np.random.uniform(2, 7, 180), alpha=0.28)

# 塔 & 地面
tower_poly, ground_poly = tower_geom()
tower_patch = plt.Polygon(tower_poly, closed=True,
                          facecolor="#444c66", edgecolor="#1b1f2a", alpha=0.95)
ground_patch = plt.Polygon(ground_poly, closed=True,
                           facecolor="#434343", edgecolor="#262626", alpha=1.0)
ax.add_patch(ground_patch)
ax.add_patch(tower_patch)

# 筷子：两条红色竖线
left_chop_line,  = ax.plot([], [], color="red", linewidth=2.5)
right_chop_line, = ax.plot([], [], color="red", linewidth=2.5)

# 火箭主体、喷口、火焰
rocket_patch  = plt.Polygon(np.zeros((3,2)), closed=True,
                            facecolor="#e7edf6", edgecolor="#2a313d", linewidth=1.6)
nozzle_patch  = plt.Polygon(np.zeros((3,2)), closed=True,
                            facecolor="#9aa8bf", edgecolor="#2a313d", linewidth=1.2)
flame_patch   = plt.Polygon(np.zeros((3,2)), closed=True,
                            facecolor="#ffcc55", edgecolor="#ff9a2f", alpha=0.78)

ax.add_patch(flame_patch)
ax.add_patch(rocket_patch)
ax.add_patch(nozzle_patch)

# 喷管 / 推力方向线（蓝线）
gimbal_line, = ax.plot([], [], linewidth=2.0, color="#6b9df2")

# HUD 文本
hud = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top", ha="left",
              bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#222", alpha=0.9),
              **HUD_FONT)

# 捕获提示
capture_text = ax.text(0.5, 0.92, "", transform=ax.transAxes, va="top", ha="center",
                       color="#2ecc71", fontsize=12, fontweight="bold")


# ============================================================
#                        动画回调
# ============================================================
def init():
    hud.set_text("")
    capture_text.set_text("")
    left_chop_line.set_data([], [])
    right_chop_line.set_data([], [])
    return (rocket_patch, nozzle_patch, flame_patch,
            gimbal_line, left_chop_line, right_chop_line,
            tower_patch, ground_patch, hud, capture_text)

def update(frame):
    global t, theta, omega, e_prev, integral, rx, ry, clamp_span, clamped

    # 时间推进 & 火箭整体缓慢下降（视觉用）
    t += dt
    ry += DESCENT_V * dt

    # 姿态误差
    e = theta_target - theta
    integral += e * dt
    derivative = (e - e_prev) / dt
    alpha = Kp * e + Ki * integral + Kd * derivative
    e_prev = e

    # 喷管限幅
    alpha = np.clip(alpha, -alpha_limit, alpha_limit)

    # 外部扰动（风 / 耦合），转成弧度
    domega = k * alpha + rad(wind_torque_deg) * np.sin(0.7*t + 0.8*np.cos(0.33*t))

    # 动力学积分
    omega += domega * dt
    theta += omega * dt

    # 推力等级（影响火焰长度/宽度）
    e_deg = abs(deg(e))
    thrust_lvl = smoothstep(np.clip(e_deg / 10.0, 0, 1))
    thrust_lvl = lerp(thrust_min, thrust_max, thrust_lvl)

    # 筷子合拢逻辑
    ok_pointing = (abs(deg(theta)) < clamp_theta_thresh_deg) and (abs(deg(omega)) < clamp_rate_thresh_deg)
    time_gate = (t >= clamp_start_time)
    near_tower_y = (ry <= TOWER_Y + 0.25*R_LEN)
    if (ok_pointing and time_gate and near_tower_y) or (t >= clamp_close_time - 0.8):
        u = smoothstep((t - clamp_start_time) / (clamp_close_time - clamp_start_time))
        clamp_span = lerp(clamp_open_span, clamp_min_span, u)
        if u > 0.99 and not clamped:
            clamped = True

    # 更新筷子两条红色竖线
    x_left  = TOWER_X - clamp_span * 0.5
    x_right = TOWER_X + clamp_span * 0.5
    y1 = CLAMP_PIVOT_Y - CLAMP_HALF_HEIGHT
    y2 = CLAMP_PIVOT_Y + CLAMP_HALF_HEIGHT
    left_chop_line.set_data([x_left, x_left], [y1, y2])
    right_chop_line.set_data([x_right, x_right], [y1, y2])

    # 更新火箭主体和喷口
    rx_body, ry_body = poly_body(theta, rx, ry)
    rocket_patch.set_xy(np.vstack([rx_body, ry_body]).T)
    nx, ny = nozzle_poly(theta, rx, ry)
    nozzle_patch.set_xy(np.vstack([nx, ny]).T)

    # 喷口中心（火焰和推力方向起点）
    ax0, ay0 = nozzle_anchor(theta, rx, ry)

    # 更新火焰：方向与推力方向一致，向下喷
    fx, fy = flame_poly_world(theta, alpha, thrust_lvl, ax0, ay0)
    flame_patch.set_xy(np.vstack([fx, fy]).T)

    # 喷管 / 推力方向线（蓝线）：与火焰方向完全一致
    tip_len = 2.0
    ang = theta + alpha
    # 方向向量：θ=0, α=0 → (0, -1)
    dx = -np.sin(ang)
    dy = -np.cos(ang)
    x1 = ax0 + tip_len * dx
    y1 = ay0 + tip_len * dy
    gimbal_line.set_data([ax0, x1], [ay0, y1])

    # HUD
    hud.set_text(
        f"t   = {t:5.2f} s\n"
        f"θ   = {deg(theta):6.2f} °\n"
        f"ω   = {deg(omega):6.2f} °/s\n"
        f"α   = {deg(alpha):6.2f} °  (gimbal)\n"
        f"|e| = {e_deg:6.2f} °\n"
        f"thrust lvl ≈ {thrust_lvl:4.2f}\n"
        f"clamp span = {clamp_span:4.2f} m"
    )

    # 捕获提示
    if clamped:
        capture_text.set_text("CAPTURED ✓  （筷子已夹住）")
    else:
        capture_text.set_text("")

    return (rocket_patch, nozzle_patch, flame_patch,
            gimbal_line, left_chop_line, right_chop_line,
            tower_patch, ground_patch, hud, capture_text)


# ------------------ 开始动画 ------------------
frames = int(T / dt)
anim = FuncAnimation(fig, update, init_func=init, frames=frames,
                     interval=1000*dt, blit=True, repeat=False)

# ============ 可选：保存（取消注释一行即可） ============
# from matplotlib.animation import PillowWriter
# anim.save("rocket_pid_fancy.gif", writer=PillowWriter(fps=60))

# from matplotlib.animation import FFMpegWriter
# anim.save("rocket_pid_fancy.mp4", writer=FFMpegWriter(fps=60, bitrate=12000))

plt.show()
