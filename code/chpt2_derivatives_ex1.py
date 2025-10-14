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

# 定义原函数和其导数
def f(x):
    return x**2

def f_prime(x):
    return 2*x

# 创建图形
plt.figure(figsize=(4, 8))

# 绘制原函数 x^2 和其导数 2x
plt.plot(x, f(x), 'b-', linewidth=2)
plt.plot(x, f_prime(x), 'r-', linewidth=2)
plt.ylim([-10, 10])

# 设置坐标轴标签和标题 - 使用Matplotlib的数学文本格式
#plt.xlabel('$x$', fontsize=label_fontsize)
#plt.ylabel('$y$', fontsize=label_fontsize)
#plt.title('$f(x) = x^2$ 的导数', fontsize=label_fontsize)

# 添加网格和坐标轴
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# 设置坐标轴比例相等
plt.gca().set_aspect('equal')
#plt.gca().set_xlabel('')
plt.axis('off')

# 设置坐标轴刻度标签字体大小
plt.tick_params(axis='both', which='major', labelsize=base_fontsize)

# 添加文本标注来替代图例
plt.text(0, 8, '$f(x) = x^2$', fontsize=label_fontsize, color='blue')
plt.text(-2, -5, "$f'(x) = 2x$", fontsize=label_fontsize, color='red')

# 调整布局并显示
plt.tight_layout()
plt.savefig('./media/img/chpt2_derivative_ex1.svg', format='svg')
plt.show()

