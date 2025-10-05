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

[toc]

# 第三章 微分

> [!tip]
>
> 上一章我们通过极限给出了**导数的定义**, 并指出导数的几何意义是函数某一点处**切线的斜率**. 通过计算函数切线的斜率, 我们可以判断函数的增减性及其极值. 
> 
> 本章我们要在导数的基础上再往前迈一步, **在局部用直线来代替曲线**. 也就是所谓的**化曲为直**, 这是微积分中一个极其重要的思想. 为此我们将引入**微分**的概念, 它是微积分的核心, 也将在后续的课程中贯穿始终.
> 

## 化曲为直

## 微分的概念

> [!tip]
>
> **微分 (differential)** 的意思是 **无穷小的改变量 (infinitesimally small change)**，莱布尼茨为微分创立了其专属符号 "$d$", 例如 $dx$ 表示变量 $x$ 的微分, $dy$ 表示变量 $y$ 的微分. 与之对应的, 物理上经常用 $\Delta x$ 表示一个很小的改变量，比如一小段位移. 直观上看, $\Delta x$ 和 $dx$ 想传达的意思很相近, 都是**很小的量**, 但是在数学它们是有区别的. 
> 
> - $\Delta x$ 表示一个非常小但**固定的数**.
> 
> - $dx$ 则表示一个"无穷小量", 它不再是一个固定的数, 更接近于一个 $\Delta x \to 0$ 的**极限过程**.

> [!warning]
> 
> $dx$ **自带极限过程**: 如果极限是一首歌, 那它就是我们的主角 $dx$ 自带的背景音乐. 
>

> [!warning]
> 
> 在后面的学习中, $\Delta x$ 和 $d x$ 我们都会经常碰到, 前者是思维上的具象, 后者是数学上的严格, 双剑合璧, 才能在数学的道路上走得更远.
> 

> [!important]
>
> 我们来看下面这张图, 这张图跟上一章中导数的图一模一样, 但我们要换个方式解读. 在 $x_0$ 处, 对 $x_0$ 的值做一个微小的改变, 得到 $x_0 + \Delta x$. 相应的, $y$ 的改变量为
> $$ \Delta y = f(x_0 + \Delta x) - f(x_0).$$
>
> 我们关心的问题是, 在 $\Delta x$ 趋于 0 的过程中, $\Delta y$ 和 $\Delta x$ 之间有没有某种极限关系. 答案是有的, $\Delta y$ 与 $\Delta x$ 的比值的极限
>
> $$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = f'(x_0).$$ 
>
> 这正是我们在上一章给出的导数的定义. 此时令 $\Delta x \to 0$ 并引入微分记号, 把上式左边的 $\Delta y$ 和 $\Delta x$ 分别替换成 $dy$ 和 $dx$, 就得到
>
> $$\left.\frac{dy}{dx} \right|_{x_0} = f'(x_0).$$
>
> 由此我们得到, 在点 $x=x_0$ 处, $y$ 的微分与 $x$ 的微分的比值等于函数 $f(x)$ 在这一点的导数. 因此我们也经常用记号 $\displaystyle \frac{dy}{dx}$ 或 $\displaystyle \frac{df(x)}{dx}$ 来表示 $f(x)$ 的导数. 
>
> ![导数的几何意义](../media/img/derivative.png)
>
> 通过上面的分析, 借助微分的概念我们重新定义了导数的符号. 但微分概念的价值远不止于此, 例如我们可以形式上把 $dx$ 和 $dy$ 拆开, 得到
> $$\begin{equation}dy = f'(x_0) dx.\end{equation}$$
> 
> 为了更好的理解这一点, 我们把 $dy$ 和 $dx$ 再用 $\Delta y$ 和 $\Delta x$ 代回来, 得到 
>
> $$
> \Delta y \approx f'(x_0) \Delta x.
> $$
>
> 注意这里的等号只在 $\Delta x \to 0$ 的极限下成立, 换成有限的 $\Delta x$ 我们就用了一个 $\approx$ 表示近似. 上式可以改写成 
> $$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x.$$
>
> 左端是原函数, 右端是过 $x_0$ 函数的切线. 一方面, 当 $\Delta x$ 很小时, 右端是左端的一个很好的近似, 它满足了我们解决实际问题的需求; 而另一方面, 通过极限, 我们又可以将它转变为严格的等式 (公式(1)), 帮助我们进行理论上的严格推导. 把**近似**通过**极限**严格化, 这正是微积分的精髓所在.


> [!tip]
> 
> 微分的思想是一个强大的武器, 在本章接下来的内容里, 我们将借助它去处理更加复杂的求导(复合函数求导和隐函数求导)和求极限(高阶无穷小和洛必达法则)问题.

## 复合函数求导的链式法则
> [!tip]
> 
> 非常重要!
> 

> [!important]
> 
> ==链式法则 (Chain Rule)==
> 
> 若函数 $y = f(u)$ 在点 $u = g(x)$ 可导，且 $u = g(x)$ 在点 $x$ 可导，则：
> $$
> [f(g(x))]' = f'(g(x)) g'(x)
> $$
>
> 基于微分的思想, 链式法则可以直观的理解为: 分子分母同时乘以无穷小量 $du$, 得到
>
> $$
> \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}.
> $$


> [!note]
> 
> ==P90 例9== 
> 
>  **设函数 $y = e^{x^2}$，求 $\frac{dy}{dx}$**
> 
> 解：$y = e^{x^2}$ 可看作由 $y = e^u$，$u = x^2$ 复合而成，因此：
>   
> $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = e^u \cdot 2x = 2xe^{x^2}.$$

> [!note]
> 
> ==P90 例10==
> 
> **设函数 $y = \cos \frac{x^2-1}{3x}$，求 $\frac{dy}{dx}$**
> 
> 解：$y = \cos \frac{x^2-1}{3x}$ 可看作由 $\displaystyle  y = \cos u, u = \frac{x^2-1}{3x}$ 复合而成。因
> $\displaystyle \frac{dy}{du} = -\sin u,$
> $\displaystyle \frac{du}{dx} = \frac{x^2 + 1}{3x^2},$
> 所以
> $$ \frac{dy}{dx} = -\sin u \cdot \frac{x^2 + 1}{3x^2} = -\frac{x^2 + 1}{3x^2} \cdot \sin \frac{x^2-1}{3x}.$$
>


> [!note]
> 
> ==P91 例11==
> 
> **设 $y = \ln \cos x$，求 $\frac{dy}{dx}$**.
> 
> 解：$y = \ln \cos x$ 可看作由 $y = \ln u$，$u = \cos x$ 复合而成。所以
> $$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \frac{1}{\cos x} \cdot (-\sin x) = -\frac{\sin x}{\cos x} = -\tan x.$$

> [!note]
> 
> ==P92 例12==
> 
> **设 $y = \sqrt{1 + 3x^3}$，求 $\frac{dy}{dx}$.**
> 
> 解：$y = \sqrt{1 + 3x^3} = (1 + 3x^3)^{\frac{1}{2}}$ 可看作由 $y = u^{\frac{1}{2}}$， $u = 1 + 3x^3$ 复合而成。
> 所以
> $$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \frac{1}{2\sqrt{1 + 3x^3}} \cdot 9x^2 = \frac{9x^2}{2\sqrt{1 + 3x^3}}.$$

> [!note]
> 
> ==P92 例13==
> 
> **设 $y = \ln \sin(2x^2)$，求 $\frac{dy}{dx}$**
>  
> 解：所给函数可分解为 $y = \ln u, u = \sin v, v = 2x^2$。
> $$\frac{dy}{dx} = \frac{1}{u} \cdot \cos v \cdot 4x = \frac{\cos(2x^2)}{\sin(2x^2)} \cdot 4x = 4x \cot(2x^2).$$
>

> [!note]
> 
> ==P92 例14==
> 
> **设 $y = e^{\cos \sqrt{x}}$，求 $y'$**
> 
> 解：逐层求导：
> $\displaystyle \frac{dy}{du} = e^u = e^{\cos \sqrt{x}}$
> $\displaystyle \frac{du}{dv} = -\sin v = -\sin \sqrt{x}$
> $\displaystyle \frac{dv}{dx} = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
> 
> 根据链式法则：
> 
> $\displaystyle y' = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx} = e^{\cos \sqrt{x}} \cdot (-\sin \sqrt{x}) \cdot \frac{1}{2\sqrt{x}}= -\frac{e^{\cos \sqrt{x}} \sin \sqrt{x}}{2\sqrt{x}}$
>
>

> [!note]
> 
> ==P93 例15==
> 
> **设 $y = \cos 2x \cdot \cos^2 x$，求 $y'$**
> 
> 解：
> 
> $y' = (\cos 2x)' \cos^2 x + \cos 2x (\cos^2 x)'$
> $= -2\sin 2x \cos^2 x + \cos 2x (-2\sin x \cos x)$
$= -2\cos x (\sin 2x \cos x + \cos 2x \sin x)$
$= -2\cos x \sin 3x$

## 隐函数求导

> [!tip]
> 
> 隐函数将自变量 $x$ 和函数值 $y$ 通过某个等式联系起来, 从这个等式里我们可以推测 $\Delta y$ 和 $\Delta x$ 之间的关系, 一些复杂的函数的导数通过隐函数更容易计算.
> 

> [!note]
> 
> ==P101 例1==
> 
> **求由方程 $\ln y + x^2y - 1 = 0$ 所确定的隐函数的导数 $\frac{dy}{dx}$**.
> 
> 解：将方程两边对 $ x $ 求导，注意 $ y $ 是 $ x $ 的函数：
> 
> 左边求导：$\displaystyle \frac{d}{dx}(\ln y + x^2y - 1) = \frac{1}{y}\frac{dy}{dx} +2xy + x^2\frac{dy}{dx}$
> 右边求导：$\displaystyle \frac{d}{dx}(0) = 0$
> 
> 令两边相等：$\displaystyle \frac{1}{y}\frac{dy}{dx} + 2xy + x^2\frac{dy}{dx} = 0$
> 
> 合并关于 $\frac{dy}{dx}$ 的项：
> $\displaystyle \left(\frac{1}{y} + x^2\right)\frac{dy}{dx} = -2xy$
> 
> 解得：$\displaystyle \frac{dy}{dx} = -\frac{2xy}{\frac{1}{y} + x^2} = -\frac{2xy^2}{1 + x^2y} \quad (y \ne 0)$
> 即 $\displaystyle \frac{dy}{dx} = -\frac{2xy^2}{1 + x^2y}$


> [!note]
> 
> ==P102 例2==
> 
> **求由方程 $ y^3 + 3y - x^2 - 2x^5 = 0 $ 所确定的隐函数在 $ x = 0$ 处的导数 $\left.\frac{dy}{dx}\right|_{x=0}$**.
> 
> 解：将方程两边对 $ x $ 求导（注意 $ y $ 是 $ x $ 的函数）：$\displaystyle \frac{d}{dx}(y^3 + 3y - x^2 - 2x^5) $
> 
> $\displaystyle = 3y^2 \frac{dy}{dx} + 3 \frac{dy}{dx} - 2x - 10x^4 = 0$
> 
> 解关于 $\displaystyle\frac{dy}{dx}$的方程:
> 
> $\displaystyle (3y^2 + 3)\frac{dy}{dx} = 2x + 10x^4$
> 
> 解得:$\displaystyle \frac{dy}{dx} = \frac{2x + 10x^4}{3y^2 + 3}$
> 
> 求 $ x = 0 $ 时的 $ y $ 值:
> 
> $\displaystyle y^3 + 3y - 0 - 0 = 0 \Rightarrow y^3 + 3y = 0 \Rightarrow y(y^2 + 3) = 0$
> 
> 解得实数解为 $ y = 0 $
> 
> 计算 $ x = 0 $ 处的导数值:
> 将 $ x = 0 $, $ y = 0 $ 代入导数表达式：$\displaystyle \left.\frac{dy}{dx}\right|_{x=0}= \frac{0 + 0}{0 + 3} = 0$

> [!note]
> 
>==P102 例3==
>**求双曲线 $\frac{x^2}{9} - \frac{y^2}{4} = 1$ 在点 $(3\sqrt{2}, 2)$ 处的切线方程**.
> 
>  解：对双曲线方程两边关于 $x$ 求导：
> 
> $\displaystyle \frac{2x}{9} - \frac{2y}{4}\cdot\frac{dy}{dx} = 0 \Rightarrow \frac{x}{9} - \frac{y}{2}\cdot\frac{dy}{dx} = 0$
> 
> 解得：$\displaystyle \frac{dy}{dx} = \frac{2x}{9y}$
> 
> 计算切点处斜率,在点 $(3\sqrt{2}, 2)$ 处：$\displaystyle k = \left.\frac{dy}{dx}\right|_{(3\sqrt{2},2)} = \frac{2 \times 3\sqrt{2}}{9 \times 2} = \frac{\sqrt{2}}{3}$
> 
> 于是所求的切线方程为：
> $\displaystyle y - 2 = \frac{\sqrt{2}}{3}(x - 3\sqrt{2})\Rightarrow 3y - 6 = \sqrt{2}x - 6 \Rightarrow \sqrt{2}x - 3y = 0$
> 

> [!warning]
> 
> 微分的思想在实际问题中非常的常见, 例如, 设想我们需要控制一个机械手臂在黑板上画图, 粉笔移动一个小位移, 机械臂的各个关节也要相应的移动一个小量. 我们可以把关节移动的小量认为是 $dx$, 粉笔移动的小量认为是 $dy$. 所以根据机械臂的当前姿态, 给定任意的 $dx$, 我们可以相对容易的计算 $dy$. 另一方面, 有时候我们更关心的是给了一个具体的 $dy$, 怎么取 $dx$. 在机器人控制领域, 前者 ($dx$ 到 $dy$) 叫做正动力学, 后者 ($dy$ 到 $dx$) 叫做逆动力学. 注意这里的正, 逆只是一个方便的叫法, 在微分的观点下 $dx$ 和 $dy$ 都是某个量的微小改变, 没有本质上的区别.

## 反函数求导

> [!tip]
> 
> 反函数求导可以看作是隐函数求导的特例.
> 

> [!note]
>
> ==P88 例6==
>  [不要用书上的做法, 用隐函数求导]
>  **设 $ y = \arcsin x $ ($ -1 < x < 1 $)，用隐函数求导法求 $ y' $**
> 
>  解：由 $ y = \arcsin x $ 可得直接函数关系：$x = \sin y$
>  对 $ x = \sin y $ 两边关于 $ x $ 求导（注意 $ y $ 是 $ x $ 的函数）：
>  $\displaystyle \frac{d}{dx}(x) = \frac{d}{dx}(\sin y)$
> 
>  $\displaystyle1 = \cos y \cdot \frac{dy}{dx}$
> 
> 将 $\cos y $用$ x $表示
> 
>  利用三角恒等式：
>  $\displaystyle \cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$（当 $ -\frac{\pi}{2} < y < \frac{\pi}{2} $ 时，$ \cos y > 0 $，故取正根）
> 
>  故得到结果：$\displaystyle \frac{dy}{dx} =(\arcsin x)' = \frac{1}{\sqrt{1 - x^2}}$
>  用类似的方法可得反余弦函数的导数公式
>  $\displaystyle (\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$
> 
>  ==P88 例7==
>  [不要用书上的做法, 用隐函数求导]
>  **设 $ y = \arctan x $ ($ x \in \mathbb{R} $)，用隐函数求导法求 $ y' $**
> 
>  解：由 $ y = \arctan x $ 可得直接函数关系：$x = \tan y$
>  对 $ x = \tan y $ 两边关于 $ x $ 求导（注意 $ y $ 是 $ x $ 的函数）：
>  $\displaystyle \frac{d}{dx}(x) = \frac{d}{dx}(\tan y)$
> 
> $\displaystyle 1 = \sec^2 y \cdot \frac{dy}{dx}$
> 
> $\displaystyle \frac{dy}{dx} = \frac{1}{\sec^2 y}$
> 
>  将 $ \sec^2 y $ 用 $ x $ 表示:
> 
>  利用三角恒等式：$\displaystyle \sec^2 y = 1 + \tan^2 y = 1 + x^2$ 故得到结果：
>  $\displaystyle \frac{dy}{dx}=(\arctan x)' = \frac{1}{1 + x^2}$
>  用类似的方法可得反余切函数的导数公式 $\displaystyle (arccot x)' = -\frac{1}{1+x^2}$

> [!note]
> 
> ==P103 例5==
> 
> **求 $ y = (x^2)^{\ln x} $（$ x > 0 $）的导数**
> 
> 解： 利用对数求导法
> 两边取对数: 
> $\displaystyle\ln y = \ln \left( (x^2)^{\ln x} \right) = \ln x \cdot \ln(x^2)=\ln x \cdot 2\ln x=2(\ln x)^2$
> 
> 两边对 $ x $ 求导得：
> $\displaystyle\frac{1}{y} \cdot y' = 2 \cdot 2\ln x \cdot \frac{1}{x} = \frac{4\ln x}{x}$
> 
> 解出 $ y' $得到：
> $\displaystyle\ y' = y \cdot \frac{4\ln x}{x} = (x^2)^{\ln x} \cdot \frac{4\ln x}{x}$
>  
> 
> ==P103 例6==
> 
> **求 $ \displaystyle y = \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)} } $ 的导数**
> 
> 解：假设 $ x > 5 $，在等式两边取对数：
> $\displaystyle\ln y = \frac{1}{2} [ \ln(x-1) + \ln(x-2) \\- \ln(x-4) - \ln(x-5) ]$
> 
> 对两边关于 $ x $ 求导（注意 $ y $ 是 $ x $ 的函数）：
> 
> $\displaystyle\frac{1}{y} y' = \frac{1}{2} ( \frac{1}{x-1} + \frac{1}{x-2}$
> $\displaystyle  - \frac{1}{x-4} - \frac{1}{x-5})$
> 
> 整理得到导数表达式：
> 
> $\displaystyle\ y' = \frac{y}{2} ( \frac{1}{x-1} + \frac{1}{x-2}$
> $\displaystyle - \frac{1}{x-4} - \frac{1}{x-5})$
> 
> 将 $\displaystyle y = \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)} } $ 代入：
> 
> $\displaystyle\ y' = \frac{1}{2} \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)}}( \frac{1}{x-1}$
> $\displaystyle + \frac{1}{x-2} - \frac{1}{x-4} - \frac{1}{x-5})$


## 高阶导数
> [!tip]
> 
> 微分的思想也可以帮助我们来理解和计算高阶导数.
> 

> [!caution]
> 
> ==常用记号==
> 
> - $f'(x)$, $f''(x)$, $f'''(x)$, $f^{(n)}(x)$, $\cdots$.
> - $\displaystyle \frac{d}{dx}f(x)$, $\displaystyle \frac{d^2}{dx^2}f(x)$, $\displaystyle \frac{d^3}{dx^3}f(x)$, $\displaystyle \frac{d^{n}}{dx^{n}}f(x)$, $\cdots$.
> 

> [!note]
> 
> ==P97 例2==
> 
> **设 $y = \cos(a x)$，求 $y''$**
> 
> 解： 求一阶导数 $y'$, 
> 
> $$y' = \frac{d}{dx} \cos(a x) = -a \sin(a x)$$
> 
> 求二阶导数 $y''$: 
> $$y'' = \frac{d}{dx} \left( -a \sin(a x) \right) = -a \cdot a \cos(a x) = -a^2 \cos(a x)$$
> 
> 最终得到：
> $$y'' = -a^2 \cos(a x)$$
>


> [!note]
> 
> ==P97 例4==
> 
> **求指数函数 $y = e^{kx}$（$k$ 为常数）的 $n$ 阶导数**
> 
> 解： 一阶导数：$\displaystyle y' = \frac{d}{dx} e^{kx} = ke^{kx}$
> 
> 二阶导数：$\displaystyle y'' = \frac{d}{dx} (ke^{kx}) = k^2 e^{kx}$
> 
> 三阶导数：$\displaystyle y''' = \frac{d}{dx} (k^2 e^{kx}) = k^3 e^{kx}$
> 
> 四阶导数：$\displaystyle y^{(4)} = \frac{d}{dx}(k^3 e^{kx})=k^4 e^{kx}$
> 
> 观察规律可知，每求导一次会多乘一个系数 $k$，因此一般形式为：$\displaystyle y^{(n)} = k^n e^{kx}$
> 

> [!note]
> 
> ==P98 例7==
> 
> **求幂函数 $y = x^{a}$（$a$ 是任意常数）的 $n$ 阶导数公式**
> 
> 解： $\displaystyle y' = \frac{d}{dx} x^{a} = a x^{a-1}$
> 
> $\displaystyle y'' = \frac{d}{dx} \left( a x^{a-1} \right) = a (a - 1) x^{a-2}$
> 
> $\displaystyle y''' = \frac{d}{dx} \left( a (a - 1) x^{a-2} \right) = a (a - 1)(a - 2) x^{a-3}$
> 
> $\displaystyle y^{(4)} = a (a - 1)(a - 2)(a - 3) x^{a-4}$
> 
> 观察规律可知，每求导一次会多乘一项递减的系数 $(a - k)$，因此一般形式为：
> 
> $\displaystyle y^{(n)} = a (a - 1)(a - 2) \cdots (a - n + 1) x^{a-n}$
> 
> 当 $ a = n $ 时，得到
> $\displaystyle (x^n)^{(n)} = n(n-1)(n-2) \cdot \cdots \cdot 3 \cdot 2 \cdot 1 = n!$
> 
> 而更高阶导数为零：$\displaystyle (x^n)^{(n+k)} = 0 \quad (k=1,2,\cdots).$
>

> [!note]
> 
> ==P103 例4==
> 
> **求由方程 $x + 2y - \frac{1}{3}\cos y = 0$ 所确定的隐函数的二阶导数 $\frac{d^2y}{dx^2}$**
> 
> 解： 对原方程两边关于 $x$ 求导：
> 
> $\displaystyle \frac{d}{dx}\left(x + 2y - \frac{1}{3}\cos y\right) = 0$
> 
> $\displaystyle 1 + 2\frac{dy}{dx} + \frac{1}{3}\sin y \cdot \frac{dy}{dx} =0$
> 
> $\displaystyle \frac{dy}{dx} \left(2 + \frac{1}{3}\sin y\right) = -1$
> 
> $\displaystyle \frac{dy}{dx} = \frac{-1}{2 + \frac{1}{3}\sin y} = \frac{-3}{6 + \sin y}$
> 
> 对一阶导数 $\displaystyle\frac{dy}{dx} = \frac{-3}{6 + \sin y}$ 两边关于 $x$ 求导：
> 
> $\displaystyle \frac{d^2y}{dx^2} = \frac{3\cos y \cdot \frac{-3}{6 + \sin y}}{(6 + \sin y)^2}$
> 
> 代入 $\displaystyle\frac{dy}{dx}$ 得到：$\displaystyle \frac{d^2y}{dx^2} = \frac{-9\cos y}{(6 + \sin y)^3}$

## 高阶无穷小
> [!tip]
>
> 在上面的几个例子中, 我们把 $\Delta x^2$ 或 $dx^2$ 给扔掉了, 这是因为当 $dx \rightarrow 0$ 是, $dx^2$ 趋于 0 的速度要比 $dx$ 趋于 0 的速度更快. 例如当 $dx = 0.1$ 时，$dx^2 = 0.01$; 当 $dx = 0.01$ 时，$dx^2 = 0.0001$. 也就是说, $dx^2$ 要比 $dx$ "更小", 注意这里的 "更小" 不是绝对数值的大小, 而是**数量级**上的大小. 这种数量级上的大小关系可以通过极限来严格刻画.

> [!important]
> ==高阶无穷小的定义==
> 
> 设函数 $\alpha(x)$ 和 $\beta(x)$ 在点 $x_0$ 的某个去心邻域内有定义，且当 $x \to x_0$ 时，$\alpha(x)$ 和 $\beta(x)$ 均为无穷小量（即 $\displaystyle \lim_{x \to x_0} \alpha(x) = 0$ 和 $\displaystyle \lim_{x \to x_0} \beta(x) = 0$）。如果极限  
> $$
> \lim_{x \to x_0} \frac{\alpha(x)}{\beta(x)} = 0  
> $$
> 则称 $\alpha(x)$ 是比 $\beta(x)$ **高阶的无穷小**，记作 $\alpha(x) = o(\beta(x))$。  

> [!note]
> ==高阶无穷小的例子==
> - $dx^2$（即 $(dx)^2$）是比 $dx$ 高阶的无穷小，因为  
>   $$
>   \lim_{dx \to 0} \frac{dx^2}{dx} = \lim_{dx \to 0} dx = 0  
>   $$
>   这表明 $dx^2$ 趋近于零的速度比 $dx$ 快。  
> - $dx^3$ 是比 $dx^2$ 高阶的无穷小，因为  
>   $$
>   \lim_{dx \to 0} \frac{dx^3}{dx^2} = \lim_{dx \to 0} dx = 0  
>   $$
>   同样，$dx^3$ 趋近于零的速度比 $dx^2$ 更快。  
> - 更一般地，对于正整数 $n > m$，$dx^n$ 是比 $dx^m$ 高阶的无穷小，因为  
>   $$
>   \lim_{dx \to 0} \frac{dx^n}{dx^m} = \lim_{dx \to 0} dx^{n-m} = 0
>   $$
>   这里，指数 $n$ 越大，无穷小的阶越高，趋近于零的速度越快。

> [!warning]
> 
> 高阶无穷小提供了一种量化“小”的程度的方式。在微积分中，“小”不仅指绝对值的大小，还指趋近于零的速率. 在诸多的区域 0 的"小量"中, 尤其以 $dx^n$, $n = 1, 2, \cdots $ 最为重要, 因为它们可以看作是对“小”的一种**标尺**, 这也正是"高阶无穷小"中"阶"字的缘由.
>
> - 在近似计算中，高阶无穷小（如 $dx^2$）常被忽略，因为它们的贡献比低阶项（如 $dx$）小得多。
> - 在公式(?)中, 当取 $dx \rightarrow 0$ 的极限时, 根据定义 $dx$ 的高阶无穷小量除以 $dx$ 直接等于0, 这为分析极限、导数和积分提供了严格的数学工具。


## 洛必达法则

> [!important]
>
> **洛必达法则**是用于计算在不定形式 (未定式, 即: $0/0$或$\infty/\infty$) 下极限的有力工具.
>
> 如果函数 $f(x)$ 和 $g(x)$ 在点 $x=c$ 的某个邻域内可导，且在该点附近有：
>
> - $f(c) = 0$ 且 $g(c) = 0$ (或 $f(x)$ 和 $g(x)$ 的极限趋于 $\infty$). 
> - $g'(x) ≠ 0$.
>
> 那么
>
> $$
> \displaystyle \lim_{x\rightarrow c} \frac{f(x)}{g(x)} = \lim_{x\rightarrow c} \frac{f'(x)}{g'(x)},
> $$
>
> 前提是后者的极限存在.
>
> **注意**:  有时可能需要多次应用洛必达法则, 特别是当 $f'(x)/g'(x)$ 仍然是 $0/0$ 或 $\infty/\infty$ 的形式时.
>

> [!note]
> 
> P134-P136, 例1-10.
