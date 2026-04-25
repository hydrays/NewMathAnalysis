---
id: chpt1-ex-009
chapter: 1
tags: [函数极限, 等价无穷小, 极限]
difficulty: easy
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow 0}\frac{\tan x}{x}$。

## Solution 1

### Hint

将 $\tan x$ 拆成 $\dfrac{\sin x}{x} \cdot \dfrac{1}{\cos x}$，利用重要极限 $\lim_{x\to 0}\dfrac{\sin x}{x}=1$ 及极限的乘法法则。

### Answer

$$\lim_{x \rightarrow 0} \frac{\tan x}{x} = \lim_{x \rightarrow 0} \left( \frac{\sin x}{x} \cdot \frac{1}{\cos x} \right) = \left( \lim_{x \rightarrow 0} \frac{\sin x}{x} \right) \cdot \left( \lim_{x \rightarrow 0} \frac{1}{\cos x} \right) = 1 \cdot 1 = 1.$$
