import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos

# ============================================================
#  豪华可视化：火箭 + 喷焰锥 + 发射塔 + “筷子”夹持臂 + HUD
#  模型：theta'' = k * alpha ；alpha 由 PID(e) 给定（含微分项）
#  交互说明：
#    - 修改“可调参数”区的增益、限幅、风扰动等
#    - 运行后可在窗口中观看精细动画
#    - 如需导出 GIF/MP4，滚动到文末取消注释两行
# ============================================================

# ---------------------- 可调参数 ----------------------
dt = 0.015             # 仿真步长 (s) ；越小越平滑
T  = 14.0              # 总时长 (s)

# 目标姿态（度）
theta_target_deg = 0.0

# 初始状态（度、度/秒）
theta0_deg = 8.0       # 初始倾角，带一点“歪”
omega0_deg = -4.0      # 初始角速度，让画面更有动感

# 被控对象：theta'' = k * alpha
k = 0.75

# PID 增益（可现场调参）
Kp, Ki, Kd = 14.0, 2.0, 1

# 执行器限幅（喷管偏转角，度）
alpha_limit_deg = 10.0

# 推力等级（仅用于喷焰长度视觉）；可随误差衰减
thrust_max = 1.0
thrust_min = 0.15

# 轻微侧风/扰动（度/秒² 等效），让控制更“真实”
wind_torque = 0.10

# 筷子夹持逻辑：当 |theta| < thresh 且 |omega| < thresh_rate 并接近塔心时开始合拢
clamp_theta_thresh_deg = 1.2
clamp_rate_thresh_deg  = 2.0
clamp_start_time       = 7.0     # s，最早可开始“等待夹持”的时刻
clamp_close_time       = 10.0    # s，夹持完成目标时刻（有个缓动）
clamp_open_span        = 1.2     # m，筷子初始张开宽度（两臂间距）
clamp_min_span         = 0.18    # m，夹住时的最小间距

# 场景尺寸（单位：米；只是相对单位，保证比例美观）
SCENE_W, SCENE_H = 18, 22

# 火箭尺寸（米）
R_LEN = 7.5     # 总长
R_W   = 1.2     # 机身最大宽
LEG_W = 1.6     # 底部落脚架外沿宽
NOZZLE_W = 0.6  # 喷口外沿宽
FLAME_BASE_W = 0.8  # 喷焰在喷口处基宽（视觉用）

# 塔与筷子位置（世界坐标）
TOWER_X = 0.0   # 塔/夹持中心 x
TOWER_Y = -6.0  # 塔基准 y（画面中部偏下）

# 火箭底部起始位置（逐步降至塔中心上方）
ROCKET_X0 = 0.0
ROCKET_Y0 = 4.5

# 纵向缓慢下降（仅做背景位移，非动力学）
DESCENT_V = -0.35     # m/s

# 字体设置（避免某些环境中文不显示也不致报错）
HUD_FONT = dict(fontsize=10)

# ============================================================
#           助手函数：几何构造 + 颜色/缓动
# ============================================================
def deg(x): return np.rad2deg(x)
def rad(x): return np.deg2rad(x)

def lerp(a, b, u):  # 线性插值
    return a + (b - a) * np.clip(u, 0.0, 1.0)

def smoothstep(u):  # 平滑缓动
    u = np.clip(u, 0.0, 1.0)
    return u*u*(3-2*u)

def poly_body(theta, cx, cy):
    """
    构造火箭机身（带锥形头与底部支架）多边形坐标
    机身沿火箭轴向：底部→顶部
    """
    s, c = np.sin(theta), np.cos(theta)

    # 本体框架轴向坐标（以底部中心为 (0,0) 沿着火箭轴向 y+ 指向火箭“上方”）
    base = np.array([0, 0])
    top  = np.array([0, R_LEN])
    w_mid = R_W * 0.45  # 中段半宽
    w_base = R_W * 0.5  # 底部半宽
    w_top  = R_W * 0.15 # 上部半宽（锥形）

    # 轮廓（从左边底部开始，逆时针）
    pts_axial = np.array([
        [-w_base, 0.05*R_LEN], [-w_mid, 0.35*R_LEN], [-w_top, 0.86*R_LEN],
        [ 0.0,    R_LEN],  # 顶点
        [ w_top,  0.86*R_LEN], [ w_mid, 0.35*R_LEN], [ w_base, 0.05*R_LEN]
    ])

    # 落脚“架”伸出（增加一点底部外沿）
    leg = np.array([
        [-LEG_W*0.5, 0.0], [-LEG_W*0.35, 0.04*R_LEN], [LEG_W*0.35, 0.04*R_LEN],
        [ LEG_W*0.5, 0.0]
    ])

    # 合并
    outline = np.vstack([leg, pts_axial])

    # 旋转+平移到世界坐标（火箭轴方向由 theta 定义：x'=x*c - y*s, y'=x*s + y*c）
    R = np.array([[ c, -s],
                  [ s,  c]])
    world = outline @ R.T + np.array([cx, cy])
    return world[:,0], world[:,1]

def nozzle_poly(theta, cx, cy):
    """
    喷口多边形（短小梯形），位于火箭底部沿轴向
    """
    s, c = np.sin(theta), np.cos(theta)
    z0 = np.array([0.0, 0.02*R_LEN])
    w0, w1, L = NOZZLE_W*0.5, NOZZLE_W*0.35, 0.55  # 坐标单位：米

    loc = np.array([
        [-w0, 0], [ w0, 0],
        [ w1, L], [-w1, L]
    ]) + z0
    Rm = np.array([[ c, -s],
                   [ s,  c]])
    world = loc @ Rm.T + np.array([cx, cy])
    return world[:,0], world[:,1]

def flame_poly(theta, alpha, thrust_lvl, cx, cy):
    """
    喷焰锥：长度与开口随 thrust_lvl、alpha 变化；方向 = theta + alpha
    """
    s, c = np.sin(theta+alpha), np.cos(theta+alpha)
    # 喷焰长度（视觉）：误差大→长；收敛→短
    L = lerp(0.8, 4.2, thrust_lvl)
    # 喷焰外扩角（视觉）：随着 thrust_lvl 增加稍微变宽
    base_w = FLAME_BASE_W*0.5
    far_w  = lerp(0.2, 1.0, thrust_lvl) * (1.0 + 0.5*abs(alpha)/rad(alpha_limit_deg))

    # 从喷口底部出发
    z0 = np.array([0.0, 0.02*R_LEN])
    cone = np.array([
        [-base_w, 0], [ base_w, 0],
        [ far_w,  L], [-far_w,  L]
    ]) + z0
    Rm = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta),  np.cos(theta)]])
    # 先转到火箭体，后再绕喷管方向轻转（用小角度近似更快）
    world = cone @ Rm.T
    # 再绕喷管方向补偿（小角度，用 2D 旋转矩阵）
    Ra = np.array([[ c, -s],
                   [ s,  c]])
    world = (world - np.array([cx, cy])) @ Ra.T + np.array([cx, cy])
    return world[:,0], world[:,1]

def tower_geom():
    """
    发射塔主体与平台（静态）
    """
    # 塔身矩形
    tower_w = 1.1
    tower_h = 9.0
    base_y  = TOWER_Y
    x0 = TOWER_X - tower_w*0.5
    y0 = base_y
    poly = np.array([
        [x0, y0],
        [x0 + tower_w, y0],
        [x0 + tower_w, y0 + tower_h],
        [x0, y0 + tower_h]
    ])
    # 平台（地面）
    ground = np.array([
        [-SCENE_W*0.48, base_y - 0.3],
        [ SCENE_W*0.48, base_y - 0.3],
        [ SCENE_W*0.48, base_y - 0.7],
        [-SCENE_W*0.48, base_y - 0.7]
    ])
    return poly, ground

def chopsticks(span):  # span 为两臂之间距离（米）
    """
    筷子臂：两根细长梁，以塔顶附近为转轴，向内合拢
    """
    arm_len = 4.8
    arm_w   = 0.20
    pivot_y = TOWER_Y + 7.8  # 夹持高度
    left_x  = TOWER_X - 0.55
    right_x = TOWER_X + 0.55

    # 臂的末端离塔中心的半距 = span/2
    tip_half = span * 0.5

    # 构造左右臂多边形
    # 简化成矩形条，末端指向 (±tip_half, pivot_y) 处
    def arm_poly(pivot_x, tip_x):
        dir_vec = np.array([tip_x - pivot_x, 0.0])  # 水平伸出
        L = np.linalg.norm(dir_vec)
        if L < 1e-6:  # 避免除零
            u = np.array([1.0, 0.0])
        else:
            u = dir_vec / L
        v = np.array([-u[1], u[0]])  # 法向
        p0 = np.array([pivot_x, pivot_y])
        # 梁厚 arm_w，长度 arm_len，但只要 tip 对齐就好
        p1 = p0
        p2 = p0 + u * min(arm_len, abs(tip_x - pivot_x)) + v * arm_w*0.5
        p3 = p0 + u * min(arm_len, abs(tip_x - pivot_x)) - v * arm_w*0.5
        p4 = p0 - v * arm_w*0.5
        return np.vstack([p1, p2, p3, p4])

    left  = arm_poly(left_x,  TOWER_X - tip_half)
    right = arm_poly(right_x, TOWER_X + tip_half)
    return left, right

# ============================================================
#                 控制 & 场景状态变量
# ============================================================
alpha_limit = rad(alpha_limit_deg)
theta = rad(theta0_deg)
omega = rad(omega0_deg)
theta_target = rad(theta_target_deg)

e_prev = theta_target - theta
integral = 0.0

# 时间 & 位置
t = 0.0
rx, ry = ROCKET_X0, ROCKET_Y0  # 火箭底部中心坐标

# 筷子状态
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

# 背景微星点（静态）
np.random.seed(1)
stars = np.random.uniform([-SCENE_W/2, -SCENE_H/2],[SCENE_W/2, SCENE_H/2], size=(180,2))
ax.scatter(stars[:,0], stars[:,1], s=np.random.uniform(2, 7, 180), alpha=0.28)

# 静态塔与地面
tower_poly, ground_poly = tower_geom()
tower_patch = plt.Polygon(tower_poly, closed=True, facecolor="#444c66", edgecolor="#1b1f2a", alpha=0.95)
ground_patch = plt.Polygon(ground_poly, closed=True, facecolor="#434343", edgecolor="#262626", alpha=1.0)
ax.add_patch(ground_patch)
ax.add_patch(tower_patch)

# 筷子臂
left_arm_poly, right_arm_poly = chopsticks(clamp_span)
left_arm_patch  = plt.Polygon(left_arm_poly,  closed=True, facecolor="#6a7a96", edgecolor="#2b3240", alpha=0.96)
right_arm_patch = plt.Polygon(right_arm_poly, closed=True, facecolor="#6a7a96", edgecolor="#2b3240", alpha=0.96)
ax.add_patch(left_arm_patch)
ax.add_patch(right_arm_patch)

# 火箭主体、喷口、喷焰
rocket_patch  = plt.Polygon(np.zeros((3,2)), closed=True, facecolor="#e7edf6", edgecolor="#2a313d", linewidth=1.6)
nozzle_patch  = plt.Polygon(np.zeros((3,2)), closed=True, facecolor="#9aa8bf", edgecolor="#2a313d", linewidth=1.2)
flame_patch   = plt.Polygon(np.zeros((3,2)), closed=True, facecolor="#ffcc55", edgecolor="#ff9a2f", alpha=0.78)

ax.add_patch(flame_patch)
ax.add_patch(rocket_patch)
ax.add_patch(nozzle_patch)

# 喷管方向“向量”线（便于强调 alpha）
gimbal_line, = ax.plot([], [], linewidth=2.0)

# HUD 文本
hud = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top", ha="left",
              bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#222", alpha=0.9),
              **HUD_FONT)

# “捕获提示”
capture_text = ax.text(0.5, 0.92, "", transform=ax.transAxes, va="top", ha="center",
                       color="#2ecc71", fontsize=12, fontweight="bold")

# 调色（不硬设具体色名，但示例里用了柔和冷色/暖色）
gimbal_line.set_color("#6b9df2")

# ============================================================
#                        动画回调
# ============================================================
def init():
    hud.set_text("")
    capture_text.set_text("")
    return (rocket_patch, nozzle_patch, flame_patch,
            gimbal_line, left_arm_patch, right_arm_patch,
            tower_patch, ground_patch, hud, capture_text)

def update(frame):
    global t, theta, omega, e_prev, integral, rx, ry, clamp_span, clamped

    # 时间推进
    t += dt
    # 背景“被动下降”（只是位移，不参与姿态动力学）
    ry += DESCENT_V * dt

    # 误差
    e = theta_target - theta
    integral += e * dt
    derivative = (e - e_prev) / dt
    alpha = Kp * e + Ki * integral + Kd * derivative
    e_prev = e
    # 限幅
    alpha = np.clip(alpha, -alpha_limit, alpha_limit)

    # 简单扰动（风/残余耦合）
    domega = k * alpha + rad(wind_torque) * np.sin(0.7*t + 0.8*np.cos(0.33*t))

    # 状态积分（欧拉）
    omega += domega * dt
    theta += omega * dt

    # 推力可视等级：误差大时更强，趋近目标时衰减
    # 使用平滑映射，避免突兀
    e_deg = abs(deg(e))
    thrust_lvl = smoothstep(np.clip(e_deg / 10.0, 0, 1))  # 0~1
    thrust_lvl = lerp(thrust_min, thrust_max, thrust_lvl)

    # 筷子合拢逻辑：满足条件后，在 [clamp_start_time, clamp_close_time] 之间平滑收紧
    ok_pointing = (abs(deg(theta)) < clamp_theta_thresh_deg) and (abs(deg(omega)) < clamp_rate_thresh_deg)
    time_gate = (t >= clamp_start_time)
    # 与塔中心的“垂直对齐”程度（越靠近塔中心 y 越接近参考值）
    near_tower_y = (ry <= TOWER_Y + 0.25*R_LEN)
    if (ok_pointing and time_gate and near_tower_y) or (t >= clamp_close_time - 0.8):
        # 缓动到最小间距
        u = smoothstep((t - clamp_start_time) / (clamp_close_time - clamp_start_time))
        clamp_span = lerp(clamp_open_span, clamp_min_span, u)
        if u > 0.99 and not clamped:
            clamped = True

    # 更新筷子臂多边形
    L, R = chopsticks(clamp_span)
    left_arm_patch.set_xy(L)
    right_arm_patch.set_xy(R)

    # 更新火箭主体与喷口多边形
    rx_body, ry_body = poly_body(theta, rx, ry)
    rocket_patch.set_xy(np.vstack([rx_body, ry_body]).T)
    nx, ny = nozzle_poly(theta, rx, ry)
    nozzle_patch.set_xy(np.vstack([nx, ny]).T)

    # 更新喷焰
    fx, fy = flame_poly(theta, alpha, thrust_lvl, rx, ry)
    flame_patch.set_xy(np.vstack([fx, fy]).T)

    # 喷管方向“矢量线”，长度与 alpha 成比例
    tip_len = 2.0
    x0, y0 = rx, ry + 0.02*R_LEN
    x1 = x0 + tip_len * cos(theta + alpha)
    y1 = y0 + tip_len * sin(theta + alpha)
    gimbal_line.set_data([x0, x1], [y0, y1])

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
            gimbal_line, left_arm_patch, right_arm_patch,
            tower_patch, ground_patch, hud, capture_text)

# ------------------ 开始动画 ------------------
frames = int(T / dt)
ax.set_facecolor("#0b0f18")
ax.grid(alpha=0.18)
anim = FuncAnimation(fig, update, init_func=init, frames=frames,
                     interval=1000*dt, blit=True, repeat=False)

# ============ 可选：保存（取消注释一行即可） ============
# from matplotlib.animation import PillowWriter
# anim.save("rocket_pid_fancy.gif", writer=PillowWriter(fps=60))  # 高帧率 GIF（体积较大）

# from matplotlib.animation import FFMpegWriter
# anim.save("rocket_pid_fancy.mp4", writer=FFMpegWriter(fps=60, bitrate=12000))  # 高清 MP4（推荐）

plt.show()
