import numpy as np
import matplotlib.pyplot as plt

# 中文与样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 函数定义
def f1(x):
    return x**2

def f2(x):
    return np.exp(x)

def g(x):
    return 2 * x**2 + np.exp(x)

# 自变量范围（控制 e^x 不致过大）
x = np.linspace(-2.0, 1.2, 600)

# 计算函数值
y1 = f1(x)
y2 = f2(x)
yg = g(x)

# 绘图
fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))
ax.plot(x, y1, color='#1f77b4', linewidth=2, label=r'$f_1(x)=x^{2}$')
ax.plot(x, y2, color='#ff7f0e', linewidth=2, label=r'$f_2(x)=e^{x}$')
ax.plot(x, yg, color='#2ca02c', linewidth=2, label=r'$g(x)=2x^{2}+e^{x}$')

# 去除边框，保留原点十字坐标轴
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# 适当留白
ax.margins(x=0.03, y=0.05)

# 图例
ax.legend(frameon=False, fontsize=base_fontsize*1.2, loc='upper right')

plt.tight_layout()
plt.savefig('./media/img/chpt2_convex_ex1.svg', format='svg')
plt.show()
