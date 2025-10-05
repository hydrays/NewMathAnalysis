---
title: 高等数学讲义
author: 胡煜成
description: 首都师范大学高等数学A
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,讲义
vlook-chp-autonum: h1=off
vlook-query: vdl=on
vlook-query: ws=off
---

# 第六章 积分的应用

## 几何应用: 求体积与弧长

### 微元法思想

> [!tip]
>  
> 微元法是积分学中解决几何与物理问题的核心思想，它将复杂的整体问题分解为无穷多个简单的局部问题。
> 
> **基本思路**：
> 
> 1. **分割**：将所求的整体量对应的区域分割成许多微小部分
> 2. **近似**：在每个微小部分上，用简单的几何量近似代替复杂的实际量
> 3. **求和取极限**：将所有微小部分的近似值相加，然后通过取极限得到精确值
>

> [!important]
>  
> ==微元法数学表述==
> 
> 如果要求整体量 $Q$，先找出微元 $dQ = f(x)dx$，然后通过积分得到
> $$
> Q = \int_a^b dQ = \int_a^b f(x)dx
> $$

> [!note]
>  
> **例子**：计算曲线 $y = f(x)$ 在 $[a,b]$ 上与 $x$ 轴围成的面积
> - 分割：将 $[a,b]$ 分成 $n$ 个小区间
> - 近似：每个小区间 $[x, x+dx]$ 上的面积微元 $dA = f(x)dx$
> - 求和取极限：$A = \int_a^b f(x)dx$
> 

### 体积的计算

> [!note]
>  
> **例1** 计算底面积为 $A$，高为 $h$ 的棱柱体积
> 
> **解**：所有截面面积均为 $A$，所以
> $$
> V = \int_0^h A  dx = A \cdot h
> $$
> 
> **例2** 计算底半径为 $R$，高为 $h$ 的圆锥体积
> 
> **解**：在高度 $x$ 处的截面是半径为 $r(x) = R \cdot \frac{x}{h}$ 的圆，面积 $A(x) = \pi r^2(x) = \pi R^2 \frac{x^2}{h^2}$
> 
> 体积：
> $$
> V = \int_0^h A(x)dx = \int_0^h \pi R^2 \frac{x^2}{h^2} dx = \frac{\pi R^2}{h^2} \cdot \frac{h^3}{3} = \frac{1}{3}\pi R^2 h
> $$
> 

> [!note]
> 
> 曲线 $y = f(x)$ 绕 $x$ 轴旋转一周形成的旋转体体积：
> $$
> V = \int_a^b \pi [f(x)]^2 dx
> $$
> 
> **推导**：在 $x$ 处垂直于 $x$ 轴的截面是半径为 $f(x)$ 的圆盘，面积 $A(x) = \pi [f(x)]^2$
> 
> **例3** 计算 $y = \sqrt{x}$ 在 $[0,1]$ 上绕 $x$ 轴旋转形成的体积
> 
> **解**：
> $$
> V = \int_0^1 \pi (\sqrt{x})^2 dx = \pi \int_0^1 x  dx = \pi \cdot \frac{1}{2} = \frac{\pi}{2}
> $$
> 

> [!note]
>  
> 曲线 $y = f(x)$ 绕 $y$ 轴旋转一周形成的旋转体体积：
> $$
> V = \int_a^b 2\pi x f(x) dx
> $$
> 
> **推导**：在 $x$ 处厚度为 $dx$ 的柱壳体积微元 $dV = 2\pi x \cdot f(x) \cdot dx$
> 
> **例4** 计算 $y = x$ 在 $[0,1]$ 上绕 $y$ 轴旋转形成的体积
> 
> **解**：
> $$
> V = \int_0^1 2\pi x \cdot x  dx = 2\pi \int_0^1 x^2 dx = 2\pi \cdot \frac{1}{3} = \frac{2\pi}{3}
> $$
>


### 曲线弧长

> [!important]
>   
> ==直角坐标系下的弧长==
> 
> 曲线 $y = f(x)$ 在 $[a,b]$ 上的弧长：
> $$
> L = \int_a^b \sqrt{1 + [f'(x)]^2}  dx
> $$
> 
> **推导**：弧长微元 $ds = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx$

> [!note]
>  
> **例5** 计算 $y = x^{3/2}$ 从 $x=0$ 到 $x=1$ 的弧长
> 
> **解**：$f'(x) = \frac{3}{2}x^{1/2}$，所以
> $$
> L = \int_0^1 \sqrt{1 + \left(\frac{3}{2}x^{1/2}\right)^2} dx = \int_0^1 \sqrt{1 + \frac{9}{4}x} dx
> $$
> 
> 令 $u = 1 + \frac{9}{4}x$，则 $du = \frac{9}{4}dx$，当 $x=0$ 时 $u=1$，$x=1$ 时 $u=\frac{13}{4}$
> 
> $$
> L = \frac{4}{9} \int_1^{13/4} \sqrt{u}  du = \frac{4}{9} \cdot \frac{2}{3} u^{3/2} \Big|_1^{13/4} = \frac{8}{27} \left[\left(\frac{13}{4}\right)^{3/2} - 1\right]
> $$

> [!important]
>  
> ==参数方程下的弧长==
> 
> 曲线由参数方程 $x = x(t), y = y(t)$ ($\alpha \leq t \leq \beta$) 给出时，弧长为：
> $$
> L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}  dt
> $$

> [!ntoe]
>  
> **例6** 计算半径为 $R$ 的圆的周长
> 
> **解**：圆的参数方程 $x = R\cos t, y = R\sin t$ ($0 \leq t \leq 2\pi$)
> 
> $\frac{dx}{dt} = -R\sin t, \frac{dy}{dt} = R\cos t$
> 
> $$
> L = \int_0^{2\pi} \sqrt{(-R\sin t)^2 + (R\cos t)^2}  dt = \int_0^{2\pi} R  dt = 2\pi R
> $$
> 

> [!important]
> 
> ==极坐标下的弧长==
> 
> 曲线由极坐标方程 $r = r(\theta)$ ($\alpha \leq \theta \leq \beta$) 给出时，弧长为：
> $$
> L = \int_\alpha^\beta \sqrt{[r(\theta)]^2 + \left[\frac{dr}{d\theta}\right]^2}  d\theta
> $$
> 
> **推导**：利用直角坐标与极坐标的关系 $x = r\cos\theta, y = r\sin\theta$，代入参数方程的弧长公式可得。

> [!note]
>  
> **例7** 计算心形线 $r = a(1 + \cos\theta)$ ($0 \leq \theta \leq 2\pi$) 的周长
> 
> **解**：$\frac{dr}{d\theta} = -a\sin\theta$
> 
> $$
> L = \int_0^{2\pi} \sqrt{[a(1+\cos\theta)]^2 + (-a\sin\theta)^2}  d\theta
> = a\int_0^{2\pi} \sqrt{2 + 2\cos\theta}  d\theta
> $$
> 
> 利用 $1 + \cos\theta = 2\cos^2(\theta/2)$，得
> $$
> L = a\int_0^{2\pi} 2|\cos(\theta/2)| d\theta = 4a\int_0^{\pi} \cos(\theta/2) d\theta = 8a
> $$

## 物理中的应用: 功与能量

> 
> 在物理学中，力沿路径做的功定义为力与位移的乘积。当力是变力时，需要用积分计算。
>

> [!warning]
> 
> ==有限区域内的变力做功==
> 
> **例1** 弹簧压缩做功
> 
> **解**：根据胡克定律，弹簧力 $F(x) = kx$，其中 $k$ 为弹性系数，$x$ 为形变量
> 
> 将弹簧从平衡位置压缩 $L$ 距离做的功：
> $$
> W = \int_0^L kx  dx = \frac{1}{2}kL^2
> $$
> 
> **例2** 抽水做功
> 
> **解**：设圆柱形水箱半径 $R$，高 $H$，充满密度为 $\rho$ 的液体
> 
> 将厚度为 $dx$，距底面高度为 $x$ 的水层抽出需做功：
> $$
> dW = (\rho \pi R^2 dx) \cdot g \cdot (H - x)
> $$
> 
> 总功：
> $$
> W = \int_0^H \rho g \pi R^2 (H - x)  dx = \frac{1}{2} \rho g \pi R^2 H^2
> $$
>

> [!warning]
> 
> ==无穷区域上的做功问题==
> 
> **例3** 万有引力做功
> 
> **解**：质量为 $m$ 的物体从距地心 $r$ 处移动到无穷远处，克服地球引力做的功：
> 
> 根据万有引力定律，引力 $F(x) = \frac{GMm}{x^2}$，其中 $G$ 为引力常数，$M$ 为地球质量
> 
> 功的定义为：
> $$
> W = \int_r^\infty \frac{GMm}{x^2}  dx
> $$
> 
> 通过极限定义：
> $$
> W = \lim_{b \to \infty} \int_r^b \frac{GMm}{x^2}  dx = \lim_{b \to \infty} GMm \left[ -\frac{1}{x} \right]_r^b = \lim_{b \to \infty} GMm \left( \frac{1}{r} - \frac{1}{b} \right) = \frac{GMm}{r}
> $$
> 
> 这就是引力势能公式，它收敛到一个有限值。
>

> [!warning]
> 
> ==无界函数的积分==
> 
> 当被积函数在积分区间内无界时，也需要通过极限来定义积分。
> 
> **例4** 计算电场强度
> 
> **解**：点电荷 $Q$ 在距离 $r$ 处产生的电势：
> $$
> V = \int_r^\infty \frac{Q}{4\pi\epsilon_0 x^2}  dx
> $$
> 
> 在 $x = 0$ 处被积函数无界，但我们的积分从 $r > 0$ 开始，所以没有问题。
> 
> 考虑另一个例子：计算函数 $f(x) = \frac{1}{\sqrt{x}}$ 在 $[0,1]$ 上的积分
> 
> 在 $x=0$ 处函数无界，我们通过极限定义：
> $$
> \int_0^1 \frac{1}{\sqrt{x}}  dx = \lim_{a \to 0^+} \int_a^1 \frac{1}{\sqrt{x}}  dx = \lim_{a \to 0^+} \left[ 2\sqrt{x} \right]_a^1 = \lim_{a \to 0^+} (2 - 2\sqrt{a}) = 2
> $$
> 
> 这个积分收敛到有限值 2。

## 概率中的应用

> [!tip]
> 
> 积分学在概率论中扮演着核心角色，特别是在处理连续型随机变量时。本节将介绍如何用积分来描述和分析连续随机现象。掌握积分在概率中的应用，不仅是学习概率论的基础，也是理解现代统计学、金融工程等领域的必备工具。


> [!important]
> 
> ==概率密度函数==
> 
> 对于连续型随机变量，我们不能像离散情况那样谈论某个具体值的概率，而是使用概率密度函数来描述概率分布。
> 
> **定义**：
> 如果存在非负函数 $f(x)$，使得对任意实数 $a \leq b$，随机变量 $X$ 落在区间 $[a,b]$ 内的概率为
> $$
> P(a \leq X \leq b) = \int_a^b f(x)  dx
> $$
> 则称 $f(x)$ 为 $X$ 的概率密度函数。
> 
> **性质**：
> 1. 非负性：$f(x) \geq 0$ 对所有 $x$ 成立
> 2. 归一性：$\int_{-\infty}^\infty f(x)  dx = 1$
> 
> **例1** 验证函数 $f(x) = \begin{cases} 
> 2x & 0 \leq x \leq 1 \\
> 0 & \text{其他}
> \end{cases}$ 是否为概率密度函数
> 
> **解**：检查非负性：在 $[0,1]$ 上 $2x \geq 0$，满足
> 
> 检查归一性：
> $$
> \int_{-\infty}^\infty f(x)  dx = \int_0^1 2x  dx = [x^2]_0^1 = 1
> $$
> 
> 因此 $f(x)$ 是一个合法的概率密度函数。

> [!note]
> 
> ==均匀分布==
> 
> 均匀分布描述了一个随机变量在某个区间内等可能取值的现象。
> 
> **定义**：
> 如果随机变量 $X$ 在区间 $[a,b]$ 上有概率密度函数
> $$
> f(x) = \begin{cases}
> \frac{1}{b-a} & a \leq x \leq b \\
> 0 & \text{其他}
> \end{cases}
> $$
> 则称 $X$ 服从均匀分布，记作 $X \sim U(a,b)$。
> 
> **例2** 公共汽车到站时间问题
> 
> **解**：假设公共汽车每10分钟一班，乘客随机到达车站，求等待时间不超过3分钟的概率。
> 
> 等待时间 $X \sim U(0,10)$，概率密度函数 $f(x) = \frac{1}{10}$，$0 \leq x \leq 10$
> 
> $$
> P(0 \leq X \leq 3) = \int_0^3 \frac{1}{10}  dx = \frac{3}{10} = 0.3
> $$
> 
>

> [!note]
> 
> ==指数分布==
> 
> 指数分布常用于描述等待时间、寿命等随机现象。
> 
> **定义**：
> 如果随机变量 $X$ 有概率密度函数
> $$
> f(x) = \begin{cases}
> \lambda e^{-\lambda x} & x \geq 0 \\
> 0 & x < 0
> \end{cases}
> $$
> 其中 $\lambda > 0$，则称 $X$ 服从参数为 $\lambda$ 的指数分布。
> 
> **例3** 电子元件寿命问题
> 
> **解**：某电子元件的寿命 $X$（单位：小时）服从参数 $\lambda = 0.001$ 的指数分布，求该元件能工作超过1000小时的概率。
> 
> $$
> P(X > 1000) = \int_{1000}^\infty 0.001 e^{-0.001x}  dx
> $$
> 
> 计算这个反常积分：
> $$
> \lim_{b \to \infty} \int_{1000}^b 0.001 e^{-0.001x}  dx = \lim_{b \to \infty} \left[ -e^{-0.001x} \right]_{1000}^b = e^{-1} \approx 0.3679
> $$
> 

> [!note]
> 
> ==正态分布==
> 
> 正态分布（高斯分布）是概率论与统计学中最重要的分布，它描述了自然界中大量随机现象的分布规律。
> 
> **定义**：
> 如果随机变量 $X$ 有概率密度函数
> $$
> f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
> $$
> 则称 $X$ 服从正态分布，记作 $X \sim N(\mu,\sigma^2)$。
> 
> **参数意义**：
> - $\mu$：均值，决定分布的中心位置
> - $\sigma$：标准差，决定分布的分散程度
> 
> **标准正态分布**：
> 当 $\mu = 0$，$\sigma = 1$ 时，称为标准正态分布，其概率密度函数为
> $$
> \varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
> $$
> 
> **概率计算**：
> 对于 $X \sim N(\mu,\sigma^2)$，$P(a \leq X \leq b) = \int_a^b \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}  dx$
> 
> 这个积分没有初等函数形式的原函数，谜底留到第二册.


## 反常积分

> [!tip]
> 
> 反常积分处理两类问题：无穷区间上的积分和无界函数的积分。

> [!important]
> 
> ==无穷区间上的反常积分==
> 
> **定义**：
> 1. $\int_a^\infty f(x)  dx = \lim_{b \to \infty} \int_a^b f(x)  dx$
> 2. $\int_{-\infty}^b f(x)  dx = \lim_{a \to -\infty} \int_a^b f(x)  dx$
> 3. $\int_{-\infty}^\infty f(x)  dx = \int_{-\infty}^c f(x)  dx + \int_c^\infty f(x)  dx$（$c$ 为任意实数）
> 
> **收敛判别**：
> 如果极限存在且有限，则称反常积分收敛；否则称发散。

> [!note]
> 
> **例5** 研究 $\int_1^\infty \frac{1}{x^p}  dx$ 的收敛性
> 
> **解**：
> 当 $p \neq 1$ 时：
> $$
> \int_1^\infty \frac{1}{x^p}  dx = \lim_{b \to \infty} \left[ \frac{x^{1-p}}{1-p} \right]_1^b = \lim_{b \to \infty} \frac{b^{1-p} - 1}{1-p}
> $$
> 
> - 当 $p > 1$ 时，$b^{1-p} \to 0$，积分收敛于 $\frac{1}{p-1}$
> - 当 $p < 1$ 时，$b^{1-p} \to \infty$，积分发散
> 
> 当 $p = 1$ 时：
> $$
> \int_1^\infty \frac{1}{x}  dx = \lim_{b \to \infty} [\ln x]_1^b = \lim_{b \to \infty} \ln b = \infty
> $$
> 发散。

> [!important]
> 
> ==无界函数的反常积分（瑕积分）==
> 
> 如果函数 $f(x)$ 在点 $c$ 的任意邻域内无界，则称 $c$ 为瑕点。
> 
> **定义**：
> 1. 若 $f(x)$ 在 $[a,b)$ 上连续，且 $\lim_{x \to b^-} f(x) = \infty$，则
>    $$
>    \int_a^b f(x)  dx = \lim_{t \to b^-} \int_a^t f(x)  dx
>    $$
> 
> 2. 若 $f(x)$ 在 $(a,b]$ 上连续，且 $\lim_{x \to a^+} f(x) = \infty$，则
>    $$
>    \int_a^b f(x)  dx = \lim_{t \to a^+} \int_t^b f(x)  dx
>    $$
> 
> 3. 若 $c \in (a,b)$ 是瑕点，则
>    $$
>    \int_a^b f(x)  dx = \int_a^c f(x)  dx + \int_c^b f(x)  dx
>    $$

> [!note]
> 
> **例6** 研究 $\int_0^1 \frac{1}{x^p}  dx$ 的收敛性
> 
> **解**：
> 当 $p \neq 1$ 时：
> $$
> \int_0^1 \frac{1}{x^p}  dx = \lim_{a \to 0^+} \left[ \frac{x^{1-p}}{1-p} \right]_a^1 = \lim_{a \to 0^+} \frac{1 - a^{1-p}}{1-p}
> $$
> 
> - 当 $p < 1$ 时，$a^{1-p} \to 0$，积分收敛于 $\frac{1}{1-p}$
> - 当 $p > 1$ 时，$a^{1-p} \to \infty$，积分发散
> 
> 当 $p = 1$ 时：
> $$
> \int_0^1 \frac{1}{x}  dx = \lim_{a \to 0^+} [\ln x]_a^1 = \lim_{a \to 0^+} (-\ln a) = \infty
> $$
> 发散。