import numpy as np
import matplotlib.pyplot as plt

# 中文与样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 函数定义
def f(x):
    return x**2

def k(x):
    return 4*x**2 + 4*x + 1  # k(x) = f(2x+1)

# 自变量范围
x = np.linspace(-2.0, 1.5, 700)

# 计算函数值
y_f = f(x)
y_k = k(x)

# 绘图
fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))
ax.plot(x, y_f, color='#1f77b4', linewidth=2, label=r'$f(x)=x^{2}$')
ax.plot(x, y_k, color='#ff7f0e', linewidth=2, label=r'$k(x)=f(2x+1)=4x^{2}+4x+1$')

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
plt.savefig('./media/img/chpt2_convex_ex3.svg', format='svg')
plt.show()
