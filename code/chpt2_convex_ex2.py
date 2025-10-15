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

def f1_alt(x):
    return (x - 1)**2 + 1

# 自变量范围（覆盖两函数交替主导的区间）
x = np.linspace(-2.0, 3.0, 700)

# 计算函数值
y1 = f1(x)
y2 = f1_alt(x)
h = np.maximum(y1, y2)

# 绘图
fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))
ax.plot(x, y1, color='#1f77b4', linewidth=2, label=r'$f_1(x)=x^{2}$')
ax.plot(x, y2, color='#ff7f0e', linewidth=2, label=r'$f_2(x)=(x-1)^{2}+1$')
ax.plot(x, h, color='#2ca02c', linewidth=2.5, label=r'$h(x)=\max\{f_1(x),f_2(x)\}$')

# 样式：去脊柱，保留原点十字轴线；隐藏刻度与数字
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)
ax.axhline(y=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.axvline(x=0, color='k', linewidth=1.5, zorder=5, clip_on=False)
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# 适当范围与留白
ax.set_xlim(x.min(), x.max())
ax.margins(x=0.03, y=0.08)

# 图例
ax.legend(frameon=False, fontsize=base_fontsize*1.2, loc='upper left')

plt.tight_layout()
plt.savefig('./media/img/chpt2_convex_ex2.svg', format='svg')
plt.show()
