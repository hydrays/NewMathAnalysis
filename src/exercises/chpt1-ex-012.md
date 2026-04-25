---
id: chpt1-ex-012
chapter: 1
tags: [函数极限, 极限]
difficulty: medium
video:
---

## Problem

计算 $\displaystyle \lim_{x\rightarrow \infty}\left( 1-\frac{1}{x}\right)^{x}$。

## Solution 1

### Hint

令 $t = -x$，当 $x \to \infty$ 时 $t \to -\infty$，将表达式化为含 $\left(1+\dfrac{1}{t}\right)^t$ 的形式，利用重要极限 $\lim_{t\to\infty}\left(1+\dfrac{1}{t}\right)^t = \mathrm{e}$。

### Answer

令 $t = -x$，则当 $x \to \infty$ 时，$t \to -\infty$，且

$$\left(1 - \frac{1}{x}\right)^x = \left(1 + \frac{1}{t}\right)^{-t} = \frac{1}{\left(1 + \frac{1}{t}\right)^{t}}.$$

由重要极限，当 $t \to -\infty$ 时 $\left(1+\dfrac{1}{t}\right)^t \to \mathrm{e}$（该极限对 $t \to \pm\infty$ 均成立），故

$$\lim_{x \to \infty} \left( 1 - \frac{1}{x} \right)^{x} = \lim_{t \to -\infty} \frac{1}{\left( 1 + \frac{1}{t} \right)^{t}} = \frac{1}{\mathrm{e}} = \mathrm{e}^{-1}.$$
