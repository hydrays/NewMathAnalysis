---
id: chpt1-ex-010
chapter: 1
tags: [函数极限, 等价无穷小, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 0}\frac{1-\cos x}{x^2}$。

## Solution 1

### Hint

利用半角公式 $1 - \cos x = 2\sin^2\!\dfrac{x}{2}$，或将分子改写为含 $\sin x$ 的形式，再结合重要极限拆分计算。

### Answer

利用恒等式 $1 - \cos x = 2\sin^2\!\dfrac{x}{2}$ 不是唯一方法；这里用 $1-\cos x = \dfrac{\sin^2 x}{1+\cos x}$：

$$\lim_{x \rightarrow 0} \frac{1 - \cos x}{x^{2}} = \lim_{x \rightarrow 0} \frac{\sin^{2}x}{x^{2}(1 + \cos x)} = \lim_{x \rightarrow 0} \left( \frac{\sin x}{x} \right)^{2} \cdot \lim_{x \rightarrow 0} \frac{1}{1 + \cos x} = 1^2 \cdot \frac{1}{2} = \frac{1}{2}.$$
