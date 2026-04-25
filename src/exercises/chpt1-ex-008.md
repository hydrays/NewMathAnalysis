---
id: chpt1-ex-008
chapter: 1
tags: [函数极限, 极限]
difficulty: easy
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 3}\frac{x-3}{x^2-9}$。

## Solution 1

### Hint

直接代入得 $\dfrac{0}{0}$ 型不定式，先对分母进行因式分解，约去公因式后再求极限。

### Answer

直接代入 $x=3$ 得分子分母均为 $0$，是 $\dfrac{0}{0}$ 型不定式，需进一步处理。

对分母因式分解：

$$x^2 - 9 = (x-3)(x+3).$$

在 $x \neq 3$ 时约去公因式 $(x-3)$：

$$\frac{x-3}{x^2-9} = \frac{x-3}{(x-3)(x+3)} = \frac{1}{x+3}.$$

计算简化后的极限：

$$\lim_{x\rightarrow 3}\frac{x-3}{x^2-9} = \lim_{x\rightarrow 3}\frac{1}{x+3} = \frac{1}{3+3} = \frac{1}{6}.$$
