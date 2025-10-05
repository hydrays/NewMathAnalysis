import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.optimize import fsolve

# 设置中文字体和全局参数
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
rcParams['font.size'] = 14
rcParams['font.weight'] = 'bold'
rcParams['axes.linewidth'] = 2.5

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(12, 6))

# 生成模拟数据 - 横坐标延长到16
x = np.linspace(0, 16, 200)

# 收益曲线 (单调递增的S形曲线，调整参数使最优解在x=8附近)
benefit = 1.2 / (1 + np.exp(-0.5 * (x - 8))) 

# 风险曲线 (单调递减的指数衰减曲线，调整参数使最优解在x=8附近)
risk = 1.1 * np.exp(-0.25 * x) + 0.1

# 定义函数用于寻找交点
def find_intersection():
    def equations(x_val):
        benefit_val = 1.2 / (1 + np.exp(-0.5 * (x_val - 8)))
        risk_val = 1.1 * np.exp(-0.25 * x_val) + 0.1
        return benefit_val - risk_val
    
    # 寻找交点
    intersection_x = fsolve(equations, x0=8)[0]
    intersection_y = 1.2 / (1 + np.exp(-0.5 * (intersection_x - 8)))
    
    return intersection_x, intersection_y

# 找到交点
optimal_x, optimal_y = find_intersection()

# 绘制曲线
ax.plot(x, benefit, 'b-', linewidth=4, label='收益')
ax.plot(x, risk, 'r-', linewidth=4, label='风险')

# 标记最优点（不要箭头和文字说明）
ax.plot(optimal_x, optimal_y, 'ko', markersize=10, markeredgewidth=3)

# 设置坐标轴
ax.set_xlabel('治疗方案', fontsize=18, weight='bold')
ax.set_ylabel('')  # 空ylabel

# 设置坐标轴范围
ax.set_ylim(0, 1.3)
ax.set_xlim(0, 16)

# 设置图例
ax.legend(loc='center right', fontsize=16, frameon=True, 
          fancybox=True, shadow=True)

# 美化图形
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.tick_params(axis='both', which='major', labelsize=14, width=2)

# 添加网格线
ax.grid(True, alpha=0.3, linestyle='--')

# 调整布局并显示
plt.tight_layout()
plt.show()

# 输出最优解位置（仅供验证）
print(f"最优解位置: x = {optimal_x:.2f}")