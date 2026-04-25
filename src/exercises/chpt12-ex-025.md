---
id: chpt12-ex-025
chapter: 12
tags: [保守场, 势函数, 旋度, 例题]
difficulty: medium
video:
---

## Problem

验证 $\mathbf{F}=(2xy+1,\,x^2-1)$ 是保守场，并求满足 $f(0,0)=0$ 的势函数 $f$。

## Solution 1

### Hint

先验证 $\partial Q/\partial x = \partial P/\partial y$，再对 $P$ 关于 $x$ 积分，利用 $f_y=Q$ 确定待定函数 $g(y)$。

### Answer

$P_y=2x=Q_x$，故 $\operatorname{curl}\mathbf{F}=0$，$\mathbf{F}$ 是保守场。

对 $x$ 积分：$f=\displaystyle\int(2xy+1)\,\mathrm{d}x+g(y)=x^2y+x+g(y)$。

由 $f_y=x^2+g'(y)=x^2-1$，得 $g'(y)=-1$，故 $g(y)=-y+c$。

代入 $f(0,0)=0$：$c=0$，从而 $f(x,y)=x^2y+x-y$。
