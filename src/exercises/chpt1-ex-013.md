---
id: chpt1-ex-013
chapter: 1
tags: [函数极限, 等价无穷小, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 0}\frac{\tan 2x}{\sin 5x}$。

## Solution 1

### Hint

将分子和分母分别乘以各自的"参数"，凑出 $\dfrac{\tan u}{u} \to 1$ 和 $\dfrac{\sin v}{v} \to 1$ 的形式，再利用极限的乘除法则。

### Answer

将极限改写，凑出标准形式：

$$\lim_{x\rightarrow 0}\frac{\tan 2x}{\sin 5x} = \lim_{x\rightarrow 0} \frac{\tan 2x}{2x} \cdot \frac{5x}{\sin 5x} \cdot \frac{2x}{5x}.$$

令 $u = 2x$，当 $x \to 0$ 时 $u \to 0$，由重要极限知 $\displaystyle\lim_{u\to 0}\frac{\tan u}{u} = 1$；

令 $v = 5x$，当 $x \to 0$ 时 $v \to 0$，由重要极限知 $\displaystyle\lim_{v\to 0}\frac{\sin v}{v} = 1$。

故

$$\lim_{x\rightarrow 0}\frac{\tan 2x}{\sin 5x} = 1 \cdot 1 \cdot \frac{2}{5} = \frac{2}{5}.$$
