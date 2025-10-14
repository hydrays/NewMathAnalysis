import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 使用Matplotlib内置的数学文本渲染，避免LaTeX问题
rcParams['mathtext.fontset'] = 'stix'  # 使用STIX数学字体，提升LaTeX显示
rcParams['font.family'] = 'STIXGeneral'
# Step 2: 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
base_fontsize = 12
label_fontsize = base_fontsize * 1.4

# 创建x值范围
x = np.linspace(-4, 4, 1000)

# 定义函数 x^{1/3}
def f(x):
    return np.cbrt(x)

# 定义导数 f'(x) = (1/3) * |x|^{-2/3} (x=0 处发散，不绘制该点)
def f_prime(x):
    return (1.0/3.0) * np.power(np.abs(x), -2.0/3.0)

# 创建图形
plt.figure(figsize=(4, 6))

# 绘制 x^{1/3}
plt.plot(x, f(x), 'b-', linewidth=2)
# 绘制导数（避开 x=0 的奇点）
eps = 1e-3
mask_left = x < -eps
mask_right = x > eps
plt.plot(x[mask_left], f_prime(x[mask_left]), 'r-', linewidth=2)
plt.plot(x[mask_right], f_prime(x[mask_right]), 'r-', linewidth=2)
# 在曲线附近添加 x^{1/3} 的 LaTeX 标注（略高于曲线，避免压线）
plt.text(2.0, 1.8, r'$f(x) = x^{\frac{1}{3}}$', color='b', fontsize=label_fontsize,
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

# 去掉边框（隐藏四周脊柱）并关闭四边刻度线
ax = plt.gca()
for side in ['left', 'right', 'top', 'bottom']:
    ax.spines[side].set_visible(False)
ax.tick_params(left=False, right=False, top=False, bottom=False)

# 设置坐标轴刻度标签字体大小
plt.tick_params(axis='both', which='major', labelsize=base_fontsize)

plt.xlim(-4, 4)
plt.ylim(-2, 8)
# 去掉 x、y 轴上的刻度标签
plt.tick_params(axis='x', which='both', labelbottom=False)
plt.tick_params(axis='y', which='both', labelleft=False)

# 调整布局并显示
plt.tight_layout()
plt.savefig('./media/img/chpt2_derivative_ex4.svg', format='svg')
plt.show()
