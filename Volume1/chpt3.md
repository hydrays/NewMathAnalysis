# 微分

> [!tip]
>
> 上一章我们通过极限给出了**导数的定义**, 并指出导数的几何意义是函数某一点处**切线的斜率**. 通过计算函数切线的斜率, 我们可以判断函数的增减性及其极值. 
> 
> 本章我们将介绍**微分**的概念, 并揭示微分与导数之间的朴实却深刻的联系. 微分是微积分的核心思想, 将在后续的课程中贯穿始终.
> 

## 微分的概念

> [!tip] 
> 
> **微分 (differential)** 的意思是 **无穷小的改变量 (infinitesimally small change)**，莱布尼茨为微分创立了其专属符号 "$d$", 例如 $dx$ 表示变量 $x$ 的微分, $dy$ 表示变量 $y$ 的微分. 与之对应的, 物理上经常用 $\Delta x$ 表示一个很小的改变量，比如一小段位移. 直观上看, $\Delta x$ 和 $dx$ 想传达的意思很相近, 都是**很小的量**, 但是在数学它们是有区别的. 
> 
> - $\Delta x$ 表示一个非常小但**固定的数**.
> 
> - $dx$ 则表示一个"无穷小量", 它不再是一个固定的数, 而是蕴含了某个**极限过程**.
> 

> [!note]
> 
> 如图, 考虑一个做直线运动的物体, 它在经过一小段时间 $\Delta t$ 之后位移的变化量为 $\Delta s = s(t +\Delta t) - s(t)$. 此时我们考虑 $\Delta t \to 0$ 的极限, 就得到**时间的微分** $dt$ 以及对应的**位移的微分** $ds$.
> 
> ![微分的例子1](../media/img/diff_example_1.png)

> [!note]
> 
> 如图, 从原点位置以角度 $\theta$ 发射一束激光, 设激光与直线 $y = b$ 的交点坐标为 $(x, b)$. 如果我们将发射角做一个微小的改变 $\Delta \theta$, 与之对应的激光光斑的位置会在 $x$-轴方向上发生了一个 $\Delta x$ 的偏移. 此时我们考虑 $\Delta \theta \to 0$ 的极限, 就得到**角度的微分** $d\theta$ 以及对应的**x的微分** $dx$.
> 
> ![微分的例子2](../media/img/diff_example_2.png)
> 


### 微分与导数

> [!tip]
> 
> 在研究实际问题的时候, 我们经常关心两个微分之间的关系. 例如, 设想我们需要控制一个机械手臂在黑板上画图, 粉笔移动一个小位移, 机械臂的各个关节也要相应的移动一个小量. 我们可以把关节移动的小量认为是 $dx$, 粉笔移动的小量认为是 $dy$. 很多时候我们关心两个微分之间的联动关系, 比如在机器人控制领域, 给定 $dx$ 计算 $dy$ 叫做**正动力学**, 给定 $dy$ 计算 $dx$ 叫做**逆动力学**. 又比如在例1中 $dx$ 与 $dt$ 的关系反映了物体的位移随时间的变化关系; 例2中 $dx$ 与 $d\theta$ 的关系反映了激光光斑的位置随发射角度之间的变化关系, 这些都是物理中所关心的量.
> 
> 那么如何确定两个微分之间的关系呢? 如果我们能够写出两个变量之间所满足的**函数关系**, 很容易就可以得到这两个变量所对应的微分之间的关系, 这是**微分学**的一个重要成就.


> [!important]
>
> ==微分与导数的关系==
> 
> 一般的, 假定两个变量 $x$, $y$ 满足函数关系 $y = f(x)$, 则 $dy = f'(x) dx$. 

> [!note]
>
> 我们首先通过数值计算来验证上述关系.
> 
> 例1: 我们分别考虑两种直线运动: **匀速运动** 和 **匀加速运动**. 对于匀速运动,
>  
> $$ s = s_0 + vt $$
> 
> 根据微分公式, 位移的微分与时间的微分满足关系:
> 
> $$ ds = vdt$$
>
> 对于初速度为0的匀加速运动, 其位移随时间的函数为
> 
> $$ s = s_0 + \frac{1}{2} a t^2 $$
>
> 根据微分公式, 位移的微分与时间的微分满足关系:
>
> $$ ds = a t dt$$
> 
> 下表给出了 $\Delta x$ 取不同数值时所对应得 $\Delta s$ 的真实值和微分公式的预测值 ($v = 2m/s, a = 2m/s^2, t=1s$).
>
> ![表格1](..\media\img\table1.png)
> 
> 从表中可以看到, 对于匀速运动, 所有情况下差值均为 0, 这表明对于线性函数，微分给出的是**精确**的, 但这仅限于线性函数的特例. 对于更加一般的匀加速运动, 差值不等于0, 但会随着 Δt 的减小而迅速减小. 这一观察提示我们, 当 $\Delta t\to 0$ 时, 误差的极限也区域0, 由此得到微分公式中的等式成立.
>
> 
> 例2: 在这个例子中, $x$ 与 $\theta$ 的函数关系为
>
> $$
> x = \frac{b}{\tan \theta}
> $$
>
> 根据微分公式, 我们有
> 
> $$
> dx = -b \frac{1}{\sin^2 \theta}d\theta
> $$
>
> 也就是说, 激光出射角度每增加 $d\theta$, 光斑就会左移(负号) $\displaystyle b \frac{1}{\sin^2 \theta}d \theta$.
> 
> 我们再稍微拓展一下, 如果我们关心的不是横坐标 $x$, 而是激光飞行的距离 $l$, 则
> 
> $$
> l = \frac{b}{\sin \theta}
> $$
> 此时的微分公式给出
> $$
> dl = -b \frac{\cos \theta}{\sin^2 \theta}d\theta
> $$
> 也就是说, 激光出射角度每增加 $d\theta$, 激光得飞行距离就会缩短(负号) $\displaystyle -b \frac{\cos \theta}{\sin^2 \theta}d\theta$.
>
> 下表给出了取不同的 $\Delta \theta$ 时 $x$ 和 $l$ 的真实变化量和微分公式预测的变化量的对比($\theta = \pi/3$):
> 
> ![表2](..\media\img\table2.png)
>
> 从表中可以看出, 随着 $\Delta \theta$ 的减小, 微分公式与精确值的误差也迅速减小, 提示当 $\Delta t\to 0$ 时, 误差的极限也区域0.
>
> 综合上面的例子可以得到如下结论: 当 $\Delta x$ 很小时, 近似满足
> $$ \Delta y \approx f'(x) \Delta x$$
>
> 而取 $\Delta x \to 0$ 的极限, 上式约等于变成等于
>
> $$ d y = f'(x) d x$$

> [!warning]
>
> 接下来我们结合导数的定义来理解微分公式. 在上一章中，我们曾从函数图像切线的角度出发，借助极限给出导数的定义：
>
> $$
> f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}.
> $$
>
> 上式的分子就是 $\Delta y$. 因此形式上我们有
>
> $$
> f'(x) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \frac{dy}{dx}
> $$
>  
>
> 由此可见，当 $\Delta x \to 0$ 时，差分商 $\Delta y / \Delta x$ 的极限正是微分之商 $dy/dx$。
>
> 在微积分的逻辑体系内，dy/dx 最初是一个整体符号代表导数。事实上，我们也常用符号 $\dfrac{dy}{dx}$ 表示导数，常见的表达方式包括：
>
> $$
> \frac{dy}{dx} \sim y'(x)
> $$
>
> $$
> \frac{df(x)}{dx} \sim f'(x)
> $$
>
> $$
> \left. \frac{df(x)}{dx} \right\rvert_{x = x_0} \sim f'(x_0)
> $$
> 
> 但这里我们形式上将 dx 和 dy 作为独立的“微分”概念，从而将导数的定义式
>
> $$
> \frac{dy}{dx} = f'(x)
> $$
>
> 变形成等式
> 
> $$
> dy = f'(x) dx
> $$
>

> [!important]
> 微分公式表明函数值 $y$ 的微分与自变量 $x$ 的微分呈线性关系，它的背后体现了**化曲为直**的思想, 具体体现在
>
> $$
> \begin{align*}
> &\boxed{dy = f'(x_0) dx} \\
> &\quad \downarrow \\
> &\boxed{\Delta y \approx f'(x_0) \Delta x} \\
> &\quad \downarrow \\
> &\boxed{f(x_0+ \Delta x) - f(x_0) \approx f'(x_0) \Delta x} \\
> &\quad \downarrow \\
> &\boxed{f(x_0+ \Delta x) \approx f(x_0) + f'(x_0) \Delta x}
> \end{align*}
> $$
>
> ![微分与线性近似](..\media\img\diff_linear_approx.jpg)
>
> 最后一个公式说明，函数在 $x_0$ 附近可近似看作一条过点 $(x_0, f(x_0))$、斜率为 $f'(x_0)$ 的**直线**. **在局部用一条直线来近似函数**也就是所谓的**化曲为直**, 这是微积分中一个极其重要的思想.
>

> [!warning]
> 
> 基于微分符号所建立的导数定义与运算规则非常直观，在后续课程中，我们将进一步领略**微分**思想的强大力量，并体会良好符号系统为数学带来的美感与实用价值。

## 借助微分计算导数

> [!tip]
> 
> 借助微分的思想和符号可以帮助我们去处理更加复杂的求导运算, 包括复合函数求导和隐函数求导.
> 

### 复合函数求导的链式法则

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
>$$ \small\displaystyle\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \frac{1}{\cos x} \cdot (-\sin x) = -\tan x.$$

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
> $$\small\displaystyle\begin{aligned}\frac{dy}{dx} &= \frac{1}{u} \cdot \cos v \cdot 4x \\&= \frac{\cos(2x^2)}{\sin(2x^2)} \cdot 4x \\&= 4x \cot(2x^2).\end{aligned}$$
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
> $$\small\displaystyle\begin{aligned} y'& = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx} \\&= e^{\cos \sqrt{x}} \cdot (-\sin \sqrt{x}) \cdot \frac{1}{2\sqrt{x}}\\&= -\frac{e^{\cos \sqrt{x}} \sin \sqrt{x}}{2\sqrt{x}}\end{aligned}$$
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

### 隐函数求导

> [!tip]
> 
> 隐函数将自变量 $x$ 和函数值 $y$ 通过某个等式联系起来, 从这个等式里我们可以推测 $dy$ 和 $dx$ 之间的关系, 一些复杂的函数的导数通过隐函数更容易计算.
> 

> [!note]
> 
> ==P101 例1==
> 
> **求由方程 $\ln y + x^2y - 1 = 0$ 所确定的隐函数的导数 $\frac{dy}{dx}$**.
> 
> 解：将方程两边对 $ x $ 求导，注意 $ y $ 是 $ x $ 的函数：
> 
> 左边求导：
>$\small\displaystyle \frac{d}{dx}(\ln y + x^2y - 1) = \frac{1}{y}\frac{dy}{dx} +2xy + x^2\frac{dy}{dx}$
>
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
> $$\displaystyle\begin{aligned} y^3 + 3y - 0 - 0 = 0 &\;\Rightarrow \;y^3 + 3y = 0 \\&\;\Rightarrow\; y(y^2 + 3) = 0\end{aligned}$$
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
> $$\small\begin{aligned}\displaystyle y - 2 = \frac{\sqrt{2}}{3}(x - 3\sqrt{2})&\;\Rightarrow 3y - 6 = \sqrt{2}x - 6 \\&\;\Rightarrow \;\sqrt{2}x - 3y = 0\end{aligned}$$
> 

### 反函数求导

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
> **求 $y = (x^2)^{\ln x}$（$x > 0$）的导数**
> 
> 解： 利用对数求导法
> 两边取对数: 
> $$\small\begin{aligned}\displaystyle\ln y &= \ln \left( (x^2)^{\ln x} \right) \\&= \ln x \cdot \ln(x^2)\\&=\ln x \cdot 2\ln x\\&=2(\ln x)^2\end{aligned}$$
> 
> 两边对 $x$ 求导得：
> $\displaystyle\frac{1}{y} \cdot y' = 2 \cdot 2\ln x \cdot \frac{1}{x} = \frac{4\ln x}{x}$
> 
> 解出 $y'$得到:
> 
> $\displaystyle\ y' = y \cdot \frac{4\ln x}{x} = (x^2)^{\ln x} \cdot \frac{4\ln x}{x}$
>  
> 
> ==P103 例6==
> 
> **求 $\displaystyle y = \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)} }$ 的导数**
> 
> 解：假设 $x > 5$，在等式两边取对数：
> $\displaystyle\ln y = \frac{1}{2} [ \ln(x-1) + \ln(x-2) \\- \ln(x-4) - \ln(x-5) ]$
> 
> 对两边关于 $x$ 求导（注意 $y$ 是 $x$ 的函数）：
> 
> $\displaystyle\frac{1}{y} y' = \frac{1}{2} ( \frac{1}{x-1} + \frac{1}{x-2}$
> $\displaystyle  - \frac{1}{x-4} - \frac{1}{x-5})$
> 
> 整理得到导数表达式：
> 
> $\displaystyle\ y' = \frac{y}{2} ( \frac{1}{x-1} + \frac{1}{x-2}$
> $\displaystyle - \frac{1}{x-4} - \frac{1}{x-5})$
> 
> 将 $\displaystyle y = \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)} }$ 代入：
> 
> $\displaystyle\ y' = \frac{1}{2} \sqrt{\frac{(x-1)(x-2)}{(x-4)(x-5)}}( \frac{1}{x-1}$
> $\displaystyle + \frac{1}{x-2} - \frac{1}{x-4} - \frac{1}{x-5})$

### 更多的高阶导数计算

> [!tip]
> 
> 微分的思想也可以帮助我们来理解和计算高阶导数, 结合链式法则, 我们可以进行更加复杂的计算.
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
> $$\small\begin{aligned}y'' &= \frac{d}{dx} \left( -a \sin(a x) \right) \\&= -a \cdot a \cos(a x) \\&= -a^2 \cos(a x)\end{aligned}$$
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

> [!note]
>
> 最后我们回过头来看一下图2中所给出的例子. 上面我们已经得到
> $$
> dx = -b \frac{1}{\sin^2 \theta}d\theta, \quad dl = -b \frac{\cos \theta}{\sin^2 \theta}d\theta
> $$
>
> 如果我们希望计算 $dx$ 与 $dl$ 的关系，即 $\dfrac{dx}{dl}$，可以采用以下两种方法：
>
> **方法一：建立 x 与 l 的显式函数关系**
>
> 由 $l = \dfrac{b}{\sin \theta}$ 可得 $\sin \theta = \dfrac{b}{l}$，代入 $x = \dfrac{b}{\tan \theta} = b\dfrac{\cos \theta}{\sin \theta}$ 得：
> $$
> x = b \cdot \frac{\cos \theta}{\sin \theta} = b \cdot \frac{\sqrt{1 - \sin^2 \theta}}{\sin \theta} = b \cdot \frac{\sqrt{1 - (b/l)^2}}{b/l} = l \cdot \sqrt{1 - \left(\frac{b}{l}\right)^2}
> $$
>
> 对 $l$ 求导得：
> $$
> \frac{dx}{dl} = \sqrt{1 - \left(\frac{b}{l}\right)^2} + l \cdot \frac{1}{2\sqrt{1 - (b/l)^2}} \cdot \frac{2b^2}{l^3} = \frac{1}{\sqrt{1 - (b/l)^2}} = \frac{1}{\cos \theta}
> $$
>
> 因此 $dx = \dfrac{1}{\cos \theta} dl$。
>
> **方法二：直接利用微分之比**
>
> 由 $dx$ 和 $dl$ 的表达式直接相除：
> $$
> \frac{dx}{dl} = \frac{-b \frac{1}{\sin^2 \theta}d\theta}{-b \frac{\cos \theta}{\sin^2 \theta}d\theta} = \frac{1}{\cos \theta}
> $$
>
> 同样得到 $dx = \dfrac{1}{\cos \theta} dl$。
>
> 两种方法结果一致，但第二种方法通过直接操作微分，避免了复杂的函数关系和求导过程，显示了微分运算的简洁性与灵活性。在实际问题中，灵活运用微分关系可以大大简化计算，这正是微分思想的强大之处。


## 借助微分计算极限

> [!tip]
> 
> 借助微分的思想和符号还可以帮助我们去理解一个较为使用的求极限方法: 洛必达法则.
>

### 洛必达法则

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

> [!warning]
> 
> 下面我们借助微分的思想来理解洛必达法则.

> 当 $x$ 充分接近 $c$ 时，我们可以用函数的线性近似（即微分）来替代原函数。由于 $f(c) = g(c) = 0$，在点 $c$ 附近有：
> 
> $$
> f(x) \approx f(c) + f'(c)(x - c) = f'(c)(x - c)
> $$
> 
> $$
> g(x) \approx g(c) + g'(c)(x - c) = g'(c)(x - c)
> $$
> 
> 因此，原比式的极限可近似表示为：
> 
> $$
> \frac{f(x)}{g(x)} \approx \frac{f'(c)(x - c)}{g'(c)(x - c)} = \frac{f'(c)}{g'(c)}
> $$
> 
> 当 $x \to c$ 时，这一近似将趋于精确。这正是洛必达法则的直观含义——在极限过程中，分子与分母的**变化趋势**由它们在该点的导数之比决定。
> 
> 对于 $\infty/\infty$ 型未定式，虽然不能直接使用上述推导，但微分思想仍然适用：此时我们比较的是 $f(x)$ 与 $g(x)$ 在 $x \to c$ 过程中的**相对变化速率**，而导数正是刻画这种瞬时变化率的工具。
> 
> 需要强调的是，上述推导仅为理解洛必达法则提供了直观的几何图像。严格证明需依赖**柯西中值定理**，该定理能够将 $\dfrac{f'(c)}{g'(c)}$ 替换成 $\dfrac{f'(\xi)}{g'(\xi)}$，其中 $\xi$ 位于 $x$ 与 $c$ 之间, 从而得到使用起来更加灵活的洛必达法则。这部分内容我们放在了后面的章节中. 
>
> 
> [!note]
> 
> P134-P136, 例1-10.


> [!warning]
> 
> 后面的章节中, 我们会介绍更加强大的计算极限的工具---泰勒展开. 而泰勒展开体现的也是微分的思想.