import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 使用Matplotlib内置的数学文本渲染，避免LaTeX问题
#rcParams['mathtext.fontset'] = 'stix'  # 使用STIX字体，类似于LaTeX
#rcParams['font.family'] = 'STIXGeneral'
# Step 2: 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 创建x值范围
x = np.linspace(-4, 4, 400)

# 定义函数 |x|
def f(x):
    return np.abs(x)

# 定义导数 f'(x) = sign(x) (x=0 处不可导，不绘制该点)
def f_prime(x):
    return np.where(x > 0, 1.0, np.where(x < 0, -1.0, np.nan))

# 创建图形
plt.figure(figsize=(8, 4))

# 绘制 |x| 与其导数
plt.plot(x, f(x), 'b-', linewidth=2)
mask_left = x < 0
mask_right = x > 0
plt.plot(x[mask_left], np.full(np.count_nonzero(mask_left), -1.0), 'r-', linewidth=2)
plt.plot(x[mask_right], np.full(np.count_nonzero(mask_right), 1.0), 'r-', linewidth=2)
plt.scatter([0, 0], [-1, 1], facecolors='none', edgecolors='r', s=60, linewidths=2)
# 在曲线附近添加 |x| 的 LaTeX 标注（略高于曲线，避免压线）
plt.text(2.2, 2.9, r'$|x|$', color='k', fontsize=label_fontsize,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))
#plt.ylim([-10, 10])

# 设置坐标轴标签和标题 - 使用Matplotlib的数学文本格式
#plt.xlabel('$x$', fontsize=label_fontsize)
#plt.ylabel('$y$', fontsize=label_fontsize)
#plt.title('$f(x) = x^2$ 的导数', fontsize=label_fontsize)

# 添加坐标轴（无网格）
plt.grid(False)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# 设置坐标轴比例相等并显示坐标轴（无标签）
plt.gca().set_aspect('equal')
plt.axis('on')

ax = plt.gca()
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)
ax.tick_params(left=False, right=False, top=False, bottom=False)

# 设置坐标轴刻度标签字体大小
plt.tick_params(axis='both', which='major', labelsize=base_fontsize)

plt.xlim(-4, 4)
plt.ylim(-1.2, 4.2)
# 去掉 x、y 轴上的刻度标签
plt.tick_params(axis='x', which='both', labelbottom=False)
plt.tick_params(axis='y', which='both', labelleft=False)

# 调整布局并显示
plt.tight_layout()
plt.savefig('./media/img/chpt2_derivative_ex3.svg', format='svg')
plt.show()
