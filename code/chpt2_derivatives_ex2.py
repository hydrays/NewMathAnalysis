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
x = np.linspace(-3*np.pi/2, 3*np.pi/2, 400)

# 定义原函数和其导数
def f(x):
    return np.cos(x)

def f_prime(x):
    return np.sin(x)

# 创建图形
plt.figure(figsize=(8, 4))

# 绘制原函数 x^2 和其导数 2x
plt.plot(x, f(x), 'b-', linewidth=2, label=r'$\cos x$')
plt.plot(x, f_prime(x), 'r-', linewidth=2, label=r'$\sin x$')
#plt.ylim([-10, 10])

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
plt.axis('on')

# 设置坐标轴刻度标签字体大小
plt.tick_params(axis='both', which='major', labelsize=base_fontsize)

xmin, xmax = plt.xlim()
step = np.pi / 2
k_min = int(np.ceil(xmin / step))
k_max = int(np.floor(xmax / step))
ticks = [k * step for k in range(k_min, k_max + 1)]

def _fmt_pi_over2(val):
    k = int(round(val / step))
    if k == 0:
        return r'$0$'
    sign = '-' if k < 0 else ''
    k_abs = abs(k)
    if k_abs == 1:
        return rf'${sign}\frac{{\pi}}{{2}}$'
    if k_abs % 2 == 0:
        n = k_abs // 2
        if n == 1:
            return rf'${sign}\pi$'
        else:
            return rf'${sign}{n}\pi$'
    else:
        n = k_abs
        return rf'${sign}\frac{{{n}\pi}}{{2}}$'

labels = [_fmt_pi_over2(t) for t in ticks]
plt.xticks(ticks, labels)
plt.tick_params(axis='x', which='major', labelsize=base_fontsize*1.5)
plt.tick_params(axis='y', which='major', labelsize=base_fontsize*1.5)

plt.legend(fontsize=base_fontsize*1.275)

# 调整布局并显示
plt.tight_layout()
plt.savefig('./media/img/chpt2_derivative_ex2.svg', format='svg')
plt.show()

