import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置全局字体大小（标题、标签、刻度等）
plt.rcParams.update({'font.size': 16})

# 创建画布和子图 (2行3列)
fig = plt.figure(figsize=(18, 12))

# ------------------- 1. 椭球面 -------------------
ax1 = fig.add_subplot(2, 3, 1, projection='3d')
# 参数：半轴长度 a=2, b=3, c=1
a, b, c = 2.0, 3.0, 1.0
# 生成参数网格
theta = np.linspace(0, np.pi, 30)
phi = np.linspace(0, 2*np.pi, 30)
theta, phi = np.meshgrid(theta, phi)
# 参数方程
x = a * np.sin(theta) * np.cos(phi)
y = b * np.sin(theta) * np.sin(phi)
z = c * np.cos(theta)
ax1.plot_surface(x, y, z, color='c', alpha=0.8, edgecolor='none')
ax1.set_title('椭球面\n$x^2/4 + y^2/9 + z^2 = 1$')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_box_aspect([a, b, c])  # 保持比例

# ------------------- 2. 单叶双曲面 -------------------
ax2 = fig.add_subplot(2, 3, 2, projection='3d')
a, b, c = 1.0, 1.0, 1.0
u = np.linspace(-2, 2, 30)
v = np.linspace(0, 2*np.pi, 30)
u, v = np.meshgrid(u, v)
# 参数方程：x = a cosh(u) cos(v), y = b cosh(u) sin(v), z = c sinh(u)
x = a * np.cosh(u) * np.cos(v)
y = b * np.cosh(u) * np.sin(v)
z = c * np.sinh(u)
ax2.plot_surface(x, y, z, color='m', alpha=0.8, edgecolor='none')
ax2.set_title('单叶双曲面\n$x^2 + y^2 - z^2 = 1$')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_box_aspect([1, 1, 1])

# ------------------- 3. 双叶双曲面 -------------------
ax3 = fig.add_subplot(2, 3, 3, projection='3d')
a, b, c = 1.0, 1.0, 1.0
u = np.linspace(-2, 2, 30)
v = np.linspace(0, 2*np.pi, 30)
u, v = np.meshgrid(u, v)
# 参数方程：x = a cosh(u), y = b sinh(u) cos(v), z = c sinh(u) sin(v)
x = a * np.cosh(u)
y = b * np.sinh(u) * np.cos(v)
z = c * np.sinh(u) * np.sin(v)
ax3.plot_surface(x, y, z, color='orange', alpha=0.8, edgecolor='none')
ax3.set_title('双叶双曲面\n$x^2 - y^2 - z^2 = 1$')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_box_aspect([1, 1, 1])

# ------------------- 4. 椭圆抛物面 -------------------
ax4 = fig.add_subplot(2, 3, 4, projection='3d')
a, b = 2.0, 1.0
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
x, y = np.meshgrid(x, y)
z = x**2 / a**2 + y**2 / b**2
ax4.plot_surface(x, y, z, color='g', alpha=0.8, edgecolor='none')
ax4.set_title('椭圆抛物面\n$z = x^2/4 + y^2$')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_box_aspect([1, 1, 0.5])

# ------------------- 5. 双曲抛物面 -------------------
ax5 = fig.add_subplot(2, 3, 5, projection='3d')
a, b = 1.0, 1.0
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
x, y = np.meshgrid(x, y)
z = x**2 / a**2 - y**2 / b**2
ax5.plot_surface(x, y, z, color='r', alpha=0.8, edgecolor='none')
ax5.set_title('双曲抛物面\n$z = x^2 - y^2$')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
ax5.set_box_aspect([1, 1, 0.5])

# ------------------- 6. 椭圆锥面 -------------------
ax6 = fig.add_subplot(2, 3, 6, projection='3d')
a, b, c = 1.0, 1.0, 1.0
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(-2, 2, 30)
u, v = np.meshgrid(u, v)
# 参数方程：x = a * v * cos(u), y = b * v * sin(u), z = c * v
x = a * v * np.cos(u)
y = b * v * np.sin(u)
z = c * v
ax6.plot_surface(x, y, z, color='b', alpha=0.8, edgecolor='none')
ax6.set_title('椭圆锥面\n$x^2 + y^2 = z^2$')
ax6.set_xlabel('X')
ax6.set_ylabel('Y')
ax6.set_zlabel('Z')
ax6.set_box_aspect([1, 1, 1])

# 调整子图间距，使标题不重叠
plt.tight_layout()
plt.show()