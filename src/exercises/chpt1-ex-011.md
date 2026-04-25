---
id: chpt1-ex-011
chapter: 1
tags: [函数极限, 等价无穷小, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 0}\frac{\arcsin x}{x}$。

## Solution 1

### Hint

令 $t = \arcsin x$，则 $x = \sin t$，当 $x \to 0$ 时 $t \to 0$，用复合函数极限换元法将问题转化为重要极限。

### Answer

令 $t = \arcsin x$，则 $x = \sin t$。当 $x \to 0$ 时，有 $t \to 0$。

由复合函数的极限运算法则：

$$\lim_{x \to 0} \frac{\arcsin x}{x} = \lim_{t \to 0} \frac{t}{\sin t} = \frac{1}{\displaystyle\lim_{t \to 0} \frac{\sin t}{t}} = \frac{1}{1} = 1.$$
