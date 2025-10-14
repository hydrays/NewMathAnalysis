import numpy as np
import matplotlib.pyplot as plt

# 中文与样式设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 函数与区间
def f(x):
    return x**2

x = np.linspace(-2.5, 2.5, 600)
y = f(x)

# 选择两点与中点（Jensen t=1/2）
x1, x2 = -1.8, 1.0
f1, f2 = f(x1), f(x2)
x_mid = 0.5 * (x1 + x2)
f_mid = f(x_mid)
# 弦线（两点连线）
m_chord = (f2 - f1) / (x2 - x1)
b_chord = f1 - m_chord * x1
y_chord = m_chord * x + b_chord
f_mid_on_chord = m_chord * x_mid + b_chord

# 选择一点作切线（凸函数：图像在切线上方）
x0 = 0.6
f0 = f(x0)
fp0 = 2 * x0
y_tangent = f0 + fp0 * (x - x0)

# 绘图
fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))
ax.plot(x, y, 'b-', linewidth=2)

# 弦线与关键点
ax.plot([x1, x2], [f1, f2], color='#DD6B20', linewidth=2, label=r'弦线')
ax.scatter([x1, x2], [f1, f2], color='#DD6B20', s=40, zorder=4)
ax.scatter([x_mid], [f_mid], color='#DD6B20', s=40, zorder=5)
ax.scatter([x_mid], [f_mid_on_chord], color='#DD6B20', s=40, zorder=5)

# 切线
ax.plot(x, y_tangent, color='#2CA02C', linestyle='--', linewidth=2, label=r'切线')
ax.scatter([x0], [f0], color='#2CA02C', s=40, zorder=5)

# 轴线与范围
ax.grid(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.0, 6.5)

# 坐标轴样式
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
ax.set_xlabel('')
ax.set_ylabel('')
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)

plt.tight_layout()
plt.savefig('./media/img/chpt2_convex_function.svg', format='svg')
plt.show()
