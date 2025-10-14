import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 设定弹簧振动参数（幅值 A，角频率 ω）。选择 ω=2π/3，使 0-3s 正好一周期
A = 2.0
omega = 2 * np.pi / 3.0

# 创建时间范围 (0到3秒)
t = np.linspace(0, 5, 400)

# 定义三个函数
def x_func(t):  # 位移函数 x(t) = A sin(ω t)
    return A * np.sin(omega * t)

def v(t):  # 速度函数 v(t) = x'(t) = A ω cos(ω t)
    return A * omega * np.cos(omega * t)

def a(t):  # 加速度函数 a(t) = v'(t) = x''(t) = - A ω^2 sin(ω t)
    return - A * (omega**2) * np.sin(omega * t)

# 创建三个子图
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 第一个图：位移函数 x(t) = A sin(ω t)
ax = axes[0]
ax.plot(t, x_func(t), 'b-', linewidth=2)
# 将标注左移 15% 的图宽：3 * 0.15 = 0.45
_t1 = 1
ax.text(_t1, x_func(_t1)+1, r'$x(t) = A\,\sin(\omega t)$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.set_xlim(-0.5, 5)
ax.set_ylim(-A-1.0, A+2.0)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$x\,(\mathrm{m})$', fontsize=label_fontsize)

for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 第二个图：速度函数 v(t) = A ω cos(ω t)
ax = axes[1]
ax.plot(t, v(t), 'b-', linewidth=2)
# 左移 0.45
_t2 = 1
ax.text(_t2, 5.65, r'$v(t) = A\,\omega\,\cos(\omega t)$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.set_xlim(-0.5, 5)
ax.set_ylim(-A*omega-1.0, A*omega+4.0)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$v\,(\mathrm{m/s})$', fontsize=label_fontsize)

for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 第三个图：加速度函数 a(t) = -A ω^2 sin(ω t)
ax = axes[2]
ax.plot(t, a(t), 'b-', linewidth=2)
# 将标注左移 0.45：取 t=1.55s 附近并上移
ax.text(1.0, 9.5, r'$a(t) = -A\,\omega^{2}\,\sin(\omega t)$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.set_xlim(-0.5, 5)
ax.set_ylim(-A*(omega**2)-1.0, A*(omega**2)+5.0)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$a\,(\mathrm{m/s^2})$', fontsize=label_fontsize)
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 调整布局并保存
plt.tight_layout()
plt.savefig('./media/img/chpt2_motion_spring.svg', format='svg')
plt.show()