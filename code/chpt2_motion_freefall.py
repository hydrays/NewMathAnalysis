import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 重力加速度
g = 9.8

# 创建时间范围 (0到3秒)
t = np.linspace(0, 3, 400)

# 定义三个函数
def s(t):  # 位移函数
    return 0.5 * g * t**2

def v(t):  # 速度函数 (位移的导数)
    return g * t

def a(t):  # 加速度函数 (速度的导数，位移的二阶导数)
    return g * np.ones_like(t)  # 常数函数

# 创建三个子图
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 第一个图：位移函数 s(t) = 1/2 * g * t^2
ax = axes[0]
ax.plot(t, s(t), 'b-', linewidth=2)
# 将标注左移 15% 的图宽：3 * 0.15 = 0.45
_t1 = 1.2 - 0.45
ax.text(_t1, s(_t1) + 12, r'$s(t) = \frac{1}{2}gt^2$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlim(0, 3)
ax.set_ylim(-2, 45)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$s\,(\mathrm{m})$', fontsize=label_fontsize)

for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 第二个图：速度函数 v(t) = g * t
ax = axes[1]
ax.plot(t, v(t), 'b-', linewidth=2)
# 左移 0.45
_t2 = 1.2 - 0.45
ax.text(_t2, v(_t2) + 8, r'$v(t) = gt$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlim(0, 3)
ax.set_ylim(-2, 30)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$v\,(\mathrm{m/s})$', fontsize=label_fontsize)

for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 第三个图：加速度函数 a(t) = g
ax = axes[2]
ax.plot(t, a(t), 'b-', linewidth=2)
# 将标注左移 0.45：2.0 -> 1.55
ax.text(1.55, g - 2.0, r'$a(t) = g$', color='k', fontsize=label_fontsize,
        ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 设置坐标轴
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlim(0, 3)
ax.set_ylim(-1, 12)
ax.tick_params(axis='x', which='both', labelbottom=True, labelsize=base_fontsize*1.5)
ax.tick_params(axis='y', which='both', labelleft=True, labelsize=base_fontsize*1.5)
ax.set_xlabel(r'$t\,(\mathrm{s})$', fontsize=label_fontsize)
ax.set_ylabel(r'$a\,(\mathrm{m/s^2})$', fontsize=label_fontsize)
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

# 调整布局并保存
plt.tight_layout()
plt.savefig('./media/img/chpt2_motion_freefall.svg', format='svg')
plt.show()