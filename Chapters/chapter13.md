---
title: 新工科数学分析
author: 首师大交叉科学研究院
description: 首都师范大学新工科数学分析
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,数学分析,讲义
vlook-chp-autonum: h1=off
vlook-query: vdl=on
vlook-query: ws=off
vlook-doc-lib:
- [序言](chapter0.html?target=_self "序言")
- [第一章: 极限](chapter1.html?target=_self "第一章")
- [第二章: 导数](chapter2.html?target=_self "第二章")
- [第三章: 微分](chapter3.html?target=_self "第三章")
- [第四章: 积分](chapter4.html?target=_self "第四章")
- [第五章: 微分的应用](chapter5.html?target=_self "第五章")
- [第六章: 积分的应用](chapter6.html?target=_self "第六章")
- [第七章: 常微分方程](chapter7.html?target=_self "第七章")
- [第八章: 数值方法](chapter8.html?target=_self "第八章")
- [第九章: 向量与空间解析几何](chapter9.html?target=_self "第九章")
- [第十章: 多元函数的微分](chapter10.html?target=_self "第十章")
- [第十一章: 多元函数的积分](chapter11.html?target=_self "第十一章")
- [第十二章: 曲线积分和曲面积分](chapter12.html?target=_self "第十二章")
- [第十三章: 无穷级数](chapter13.html?target=_self "第十三章")
- [第十四章: 偏微分方程](chapter14.html?target=_self "第十四章")
---

[toc]

﻿# 无穷级数

> [!tip]
> 本章的内容主要包括 **常数项级数的收敛性** 和 **函数的级数展开**。
> 对 **常数项级数** 的研究可以追溯到古人对极限过程的早期理解（如芝诺悖论、割圆术）。而 **函数项级数** 则是分析学中一项极其重要的工具，它蕴含了深层次的数学思想——即用简单的无穷多项式（或三角函数）的和，来逼近并表示一个复杂的对象。这也是现代计算数学和人工智能中逼近理论的基石。

## 13.1 常数项级数的概念和性质

> [!note]
> ==常数项级数的直观例子==
> 
> **例1：一尺之棰, 日取其半**
> 设每天取走一半的长度，部分和的过程如下：
> $$
> \begin{aligned} 
> S_1 &= \frac{1}{2} \\ 
> S_2 &= \frac{1}{2}+\frac{1}{4}=\frac{3}{4} \\ 
> S_3 &= \frac{1}{2}+\frac{1}{4}+\frac{1}{8}=\frac{7}{8} \\ 
> &\cdots \\ 
> S_n &= \frac{1}{2}+\frac{1}{4}+\cdots+\frac{1}{2^n}=\frac{\frac{1}{2}\left(1-\left(\frac{1}{2}\right)^n\right)}{1-\frac{1}{2}}=1-\frac{1}{2^n} 
> \end{aligned}
> $$
> 当 $n \rightarrow \infty$ 时，$\displaystyle \lim _{n \rightarrow \infty} S_n=1$。这就是一个收敛的级数。
> 
> **例2：割圆法与圆面积**
> 用圆内接正多边形的面积去逼近圆面积，每次增加边数所带来的面积增量之和，最终收敛于 $\pi r^2$。

> [!important]
> ==级数的定义==
> 
> 无穷多个数的和称为 **无穷级数** (Infinite Series)，简称 **级数**。
> 给定数列 $a_n, n = 1, 2, \cdots, \infty$，其前 $n$ 项和 $S_n= \displaystyle \sum_{i=1}^{n} a_i$ 称为该级数的 **部分和** (Partial sum)。
> 如果 $\displaystyle \lim _{n \rightarrow \infty} S_n = S$ 存在（即极限为一个有限常数），则称级数 **收敛 (Convergent)**，并称 $S$ 为级数的和；否则称级数 **发散 (Divergent)**。

> [!note]
> ==几个经典的常数项级数==
> 
> **1. 几何级数 (等比级数)**
> $$
> S_n = \sum_{i=1}^{n} a q^{i-1} \quad (a \neq 0)
> $$
> * 当 $|q| < 1$ 时，级数收敛，和为 $\displaystyle\frac{a}{1-q}$；
> * 当 $|q| \ge 1$ 时，级数发散。
> 
> **2. 调和级数 (发散的经典例子)**
> $$
> \sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots
> $$
> 虽然通项 $\frac{1}{n} \to 0$，但该级数是 **发散** 的。
> 
> **3. 裂项相消级数**
> $$
> \sum_{n=1}^{\infty} \frac{1}{n(n+1)}
> $$
> 计算其部分和：
> $$
> \begin{aligned} 
> S_n &= \frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)} \\
> &= \left(1-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\cdots+\left(\frac{1}{n}-\frac{1}{n+1}\right) \\
> &= 1-\frac{1}{n+1} 
> \end{aligned}
> $$
> 显然 $\lim_{n \rightarrow \infty} S_n = 1$，故该级数 **收敛**。

> [!important]
> ==收敛级数的基本性质==
> 
> **性质1**：若 $\sum u_n = s$，则 $\sum k u_n = k s$（$k$ 为常数）。
> **性质2**：若 $\sum u_n = s$, $\sum v_n = \sigma$，则 $\sum(u_n \pm v_n) = s \pm \sigma$。
> **性质3**：在级数中去掉、增加或改变有限项，不会改变级数的收敛性。
> **性质4 (必要条件)**：如果级数 $\sum u_n$ 收敛，那么必然有 $\displaystyle \lim_{n \rightarrow \infty} u_n = 0$。

> [!warning]
> **注意**：通项趋于零只是级数收敛的 **必要条件**，绝非充分条件！
> 例如调和级数 $\sum \frac{1}{n}$，其通项 $\frac{1}{n} \to 0$，但级数发散。所以，如果在判断时发现 $\lim_{n \to \infty} u_n \neq 0$，则级数必定发散。

## 13.2 常数项级数的审敛法

> [!tip]
> 直接计算部分和 $S_n$ 的极限在多数情况下是不可能的。如果我们只关心级数“是否收敛”（而不求具体的和），可以使用一系列的判别法则，这些法则称为 **审敛法**。

### 13.2.1 正项级数及其审敛法

正项级数是指所有项 $u_n \ge 0$ 的级数。对于正项级数，其部分和 $S_n$ 必定是单调递增的。

> [!important]
> ==定理1：单调有界原理==
> 
> 正项级数 $\displaystyle \sum_{n=1}^{\infty} u_n$ 收敛的充分必要条件是：其部分和数列 $S_n$ **有界**。
> *(注: 本质上这个定理就是上册学过的“单调有界必有极限”)*

> [!important]
> ==定理2：比较审敛法==
> 
> 设 $\sum u_n$ 和 $\sum v_n$ 都是正项级数，且对所有 $n$ 有 $u_n \leqslant v_n$：
> * 如果“大级数” $\sum v_n$ 收敛 $\Rightarrow$ “小级数” $\sum u_n$ 必收敛。
> * 如果“小级数” $\sum u_n$ 发散 $\Rightarrow$ “大级数” $\sum v_n$ 必发散。

> [!note]
> **例：判断级数 $\sum \frac{1}{\sqrt{n(n+1)}}$ 的收敛性**
> **解**：由于
> $$
> \frac{1}{\sqrt{n(n+1)}} > \frac{1}{\sqrt{(n+1)(n+1)}} = \frac{1}{n+1}
> $$
> 而 $\sum \frac{1}{n+1}$（相当于调和级数）是发散的，根据比较审敛法，原级数 **发散**。

> [!important]
> ==定理3：极限比较审敛法==
> 
> 设 $\sum u_n$ 与 $\sum v_n$ 为正项级数，若
> $$
> \lim_{n \rightarrow \infty} \frac{u_n}{v_n} = l \quad (0 < l < \infty)
> $$
> 则这两个级数 **同收敛或同发散**。

> [!note]
> **例：判断 $\displaystyle \sum_{n=1}^{\infty} \sin \frac{1}{n}$ 的收敛性**
> **解**：取发散的调和级数 $v_n = \frac{1}{n}$。因为
> $$
> \lim_{n \to \infty} \frac{\sin \frac{1}{n}}{\frac{1}{n}} = 1 > 0
> $$
> 而 $\sum \frac{1}{n}$ 发散，故 $\sum \sin \frac{1}{n}$ **发散**。

> [!important]
> ==定理4：比值审敛法 (达朗贝尔判别法)——非常重要！==
> 
> 设 $\sum u_n$ 为正项级数，若
> $$
> \lim_{n \rightarrow \infty} \frac{u_{n+1}}{u_n} = \rho
> $$
> 则：
> * 当 $\rho < 1$ 时，级数 **收敛**；
> * 当 $\rho > 1$ 或 $\rho = \infty$ 时，级数 **发散**；
> * 当 $\rho = 1$ 时，方法失效（不确定，需用其他方法）。

> [!note]
> **例：判断 $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n!}$ 的收敛性**
> **解**：
> $$
> \begin{align*}
> \lim_{n \rightarrow \infty} \frac{u_{n+1}}{u_n}
> &= \lim_{n \rightarrow \infty} \frac{n!}{(n+1)!} \\
> &= \lim_{n \rightarrow \infty} \frac{1}{n+1} \\
> &= 0 < 1
> \end{align*}
> $$
> 故级数 **收敛**。

### 13.2.2 交错级数与任意项级数

> [!important]
> ==定理5：莱布尼茨定理 (交错级数审敛法)==
> 
> 对于交错级数
> $$
> \sum_{n=1}^{\infty}(-1)^{n-1} u_n \quad (u_n > 0)
> $$
> 若满足：
> 1. $u_n \geqslant u_{n+1}$ （各项的绝对值单调递减）
> 2. $\displaystyle \lim_{n \rightarrow \infty} u_n = 0$
> 则该交错级数 **收敛**。

> [!note]
> **例：交错调和级数**
> $$
> 1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots+(-1)^{n-1} \frac{1}{n}+\cdots
> $$
> **解**：由于 $u_n=\frac{1}{n}$ 满足单调递减且趋于0，故该级数 **收敛**。

> [!important]
> ==绝对收敛与条件收敛==
> 
> 对于包含正负项的任意级数 $\sum u_n$：
> * **绝对收敛**：如果加上绝对值后的正项级数 $\sum |u_n|$ 收敛，则原级数必然收敛，且称为绝对收敛。
> * **条件收敛**：如果原级数 $\sum u_n$ 收敛，但加了绝对值后的级数 $\sum |u_n|$ 发散，则称原级数为条件收敛（如交错调和级数）。

## 13.3 幂级数及其展开

> [!tip]
> 由常数构成的级数称为 **常数项级数**。如果我们把常数换成函数，就得到了 **函数项级数**。其中最简单、最优美的一类，就是形如多项式无限延伸的 **幂级数**。用幂级数来逼近函数，是微积分泰勒展开的终极形态。

> [!important]
> ==幂级数的形式==
> $$
> \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n + \cdots
> $$
> 其中，常数 $a_0, a_1, \cdots$ 称为幂级数的系数。

> [!important]
> ==定理6：阿贝尔(Abel)定理==
> 
> 如果幂级数 $\sum a_n x^n$ 在 $x=x_0 \ (x_0 \neq 0)$ 处收敛，那么对于所有满足 $|x| < |x_0|$ 的 $x$，幂级数必**绝对收敛**。
> 反之，如果在 $x=x_1$ 处发散，则对于所有满足 $|x| > |x_1|$ 的 $x$，幂级数必**发散**。

> [!warning]
> ==收敛半径与收敛区间==
> 
> 由阿贝尔定理可知，幂级数的收敛域必然是一个以原点为中心的区间 $(-R, R)$。这个正数 $R$ 就称为 **收敛半径**。在 $x=R$ 或 $x=-R$ 的端点处，收敛性需要单独判定。
> 
> **收敛半径的求法：**
> 若
> $$
> \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \rho
> $$
> 则收敛半径 $R = \frac{1}{\rho}$。（若 $\rho=0$ 则 $R=\infty$；若 $\rho=\infty$ 则 $R=0$）。

> [!note]
> **例：求下列幂级数的收敛域**
> $$
> \sum_{n=1}^\infty \frac{(x-1)^n}{2^n \cdot n}
> $$
> 
> **解**：令 $t = x - 1$，考察 $\sum \frac{t^n}{2^n n}$。
> $$
> \begin{align*}
> \rho
> &= \lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| \\
> &= \lim_{n\to\infty} \frac{2^n n }{2^{n+1}(n+1)} \\
> &= \frac{1}{2}
> \end{align*}
> $$
> 故收敛半径 $R_t = 2$。收敛区间为 $|t| < 2$，即 $-1 < x < 3$。
> 检查端点：
> * 当 $x = -1$ 时，级数变为 $\sum \frac{(-1)^n}{n}$，由莱布尼茨定理知其 **收敛**；
> * 当 $x = 3$ 时，级数变为 $\sum \frac{1}{n}$（调和级数），**发散**。
> 因此原级数的收敛域是 **$[-1, 3)$**。

> [!important]
> ==常见函数的麦克劳林(幂级数)展开==
> 
> 这些公式在数值计算和计算机算法中极其基础：
> 1. **指数函数**
>    $$
>    e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \cdots \quad (x \in \mathbb{R})
>    $$
> 2. **正弦函数**
>    $$
>    \sin x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!} \quad (x \in \mathbb{R})
>    $$
> 3. **余弦函数**
>    $$
>    \cos x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!} \quad (x \in \mathbb{R})
>    $$
> 4. **几何级数**
>    $$
>    \frac{1}{1-x} = \sum_{n=0}^\infty x^n \quad (-1 < x < 1)
>    $$
> 5. **对数函数**
>    $$
>    \ln(1+x) = \sum_{n=1}^\infty (-1)^{n-1}\frac{x^n}{n} \quad (-1 < x \leq 1)
>    $$

## 13.4 傅里叶级数与傅里叶变换
> [!tip]
> **WHY：我们为什么需要傅里叶级数？**
> 
> 幂级数（泰勒展开）是用 $x^n$ 这样的代数多项式来逼近函数，它非常适合在**某一个点附近**做局部逼近。但是在现实世界中，我们经常遇到**周期性**的信号（比如声波、脑电波、图像纹理）。对于周期信号，用 $x^n$ 去逼近是极其困难且低效的。
> 19世纪，法国数学家傅里叶提出了一项颠覆性的见解：**任何周期函数，都可以展开为一系列不同频率的正弦波和余弦波的叠加！** 这就是傅里叶级数。它是现代信号处理、通信工程以及 AI 图像/音频处理的绝对基石。

### 13.4.1 三角级数与傅里叶展开

> [!important]
> ==傅里叶级数 (Fourier Series)==
> 
> 设 $f(x)$ 是以 $2\pi$ 为周期的周期函数，它可以被展开为如下的 **三角级数**：
> $$
> f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
> $$
> 其中，常数项和三角函数的系数（称为**傅里叶系数**）通过积分计算得出：
> * $a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx$ （代表信号的直流/平均分量）
> * $a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx$
> * $b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx$
> 
> > *注：上述公式的基础在于三角函数族 $\{1, \cos x, \sin x, \cos 2x, \sin 2x, \cdots \}$ 在区间 $[-\pi, \pi]$ 上构成了**正交基**（即任意两个不同基函数的乘积积分为0）。*

### 13.4.2 引入欧拉公式与复数形式

> [!tip]
> 
> 使用 $\cos$ 和 $\sin$ 两个函数写起来又长又繁琐。伟大的数学家欧拉（Leonhard Euler）为我们提供了一把连通三角函数和指数函数的钥匙，让傅里叶级数发生了质的飞跃。

> [!important]
> ==欧拉公式 (Euler's Formula)==
> 
> 被誉为数学中最美的公式，它将复数、指数与三角函数完美统一：
> $$ e^{ix} = \cos x + i \sin x $$
> > *推论：当 $x=\pi$ 时，得到 $e^{i\pi} + 1 = 0$，这个等式将数学中最重要的五个常数 $0, 1, i, \pi, e$ 融为一体。*
> 
> 利用欧拉公式，我们可以反向表示正弦和余弦：
> $$
> \cos(nx) = \frac{e^{inx} + e^{-inx}}{2}, \quad \sin(nx) = \frac{e^{inx} - e^{-inx}}{2i}
> $$
> 
> 将这两个式子代入传统的傅里叶级数中，经过简单的代数合并整理，原本分为三项（常数项、$a_n$项、$b_n$项）的冗长公式，可以被压缩成一个极其优雅的复数形式！

> [!important]
> ==傅里叶级数的复数形式==
> 
> $$ f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx} $$
> 此时，统一的傅里叶系数 $c_n$ 为：
> $$ c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx $$
> 
> 在这里，$n$ 包含了负整数、0 和正整数，它代表了信号中离散的**频率**成分。$c_n$ 是一个复数，它的**模**代表了该频率成分的**振幅**（能量大小），它的**幅角**代表了该频率成分的**相位**。

### 13.4.3 从傅里叶级数走向傅里叶变换

> [!extension]
> ==傅里叶变换 (Fourier Transform)==
> 
> 傅里叶级数非常完美，但它有一个致命的限制：**它只能处理周期函数**。如果我们在现实中录制了一段只有几秒钟的离散语音，或者一张有限尺寸的图像（它们并非无限循环的周期信号），还能用傅里叶分析吗？
> 
> **微积分的极限思想在这里再次闪耀！**
> 我们可以把一个**非周期信号**，看作是一个**周期无限大（即 $T \to \infty$）的周期信号**！
> 
> * 当周期 $T$ 是有限的时候，频率的取值是离散的（即 $n=1,2,3,\cdots$），频谱是一根根分立的柱子。
> * 当我们让 $T \to \infty$（极限过程）时，相邻频率之间的间隔 $\Delta \omega \to 0$。于是，**离散的求和 $\sum$ 就蜕变成了连续的积分 $\int$**！
> 
> 由此，我们得出了工程界最伟大的公式之一——**连续傅里叶变换**：
> 
> **1. 傅里叶变换（从时域到频域）：**
> $$ F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt $$
> *这里，$f(t)$ 是我们在时间上观察到的信号波形，$F(\omega)$ 就是提取出来的包含连续频率 $\omega$ 成分的频谱图！*
> 
> **2. 逆傅里叶变换（从频域还原回时域）：**
> $$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega $$
> 
> **在人工智能中的应用：**
> 无论是计算机视觉中的图像滤波（比如提取图像的边缘特征），还是语音识别系统（如让 AI 听懂人话，往往需要先用傅里叶变换将语音转化为声谱图 Spectrogram），傅里叶变换及其离散形式（DFT / FFT）都是不可或缺的基石工具。
