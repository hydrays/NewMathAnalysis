# 第四章 常微分方程

> [!tip] 
> 
> 微分方程是解决实际问题的重要数学工具. 现实世界中的很多问题, 如天体运动, 空气和水的流动, 疾病的传播等现象都可以用微分方程来描述, 本章的任务是介绍几个典型的微分方程及其求解方法.

## 什么是微分方程

> [!important]
> 
> 顾名思义, 微分方程就是含有微分的等式. 例如
> 
> $$
> y' = \frac{dy}{dx} = 2xy
> $$
> 

> [!caution]
> 
> ==微分方程的阶数==
> 
> 微分方程中还可能含有高阶导数, 如 $y^{\prime \prime}, y^{\prime \prime \prime},  \cdots, y^{(n)}$, 方程中所包含的最高阶的导数为几阶, 那么我们就称该微分方程为几阶的.
> 

> [!caution]
> 
> ==微分方程的解==
> 
> 满足微分方程的函数 $y(x)$ 称为微分方程的解. 给定 $y(x)$ 很容易判断它是不是一个微分方程的解, 但是反过来却不容易: 事实上, **大部分的微分方程我们是解不出来的**. 接下来我们要介绍几类比较简单的能够求解的微分方程. 

> [!note] 
>
> ==自由落体的小球==
>
> 考虑一个自由落体的小球, 忽略空气阻力, 根据**牛顿第二定律**, 小球在垂直方向上下落的距离 $y$ 随时间 $t$ 变化的函数 $y(t)$ 满足
>
> $$
> \begin{equation}
> y^{\prime \prime}(t)=g
> \end{equation}
> $$
>
> 方程的右边是一个常数 (**重力加速度**), 左边是一个二阶导数, 所以这是一个**二阶微分方程**. 
>
> 下面我们来求解这个微分方程:
>
> Step 1. 
>
> 令 $v(t)=y^{\prime}(t)$, 则原方程可化为:
> $$
> \begin{equation}
> y''(t)=v'(t)=g
> \end{equation}
> $$
>
> 这是一个关于函数 $v(t)$ 的一阶微分方程. 对该方程两边对自变量 $t$ 做不定积分, 得到
>
> $$
> v(t)=g t+C_1
> $$
>
> 容易验证, 这个 $v(t)$ 确实满足上述微分方程, 所以这样我们就求解了该方程.
>
> 但有同学可能注意到了, 这个解中含有一个常数 $C_1$, 那我们该拿这个 $C_1$ 怎么办呢? 单从微分方程本身我们是没有办法确定 $C_1$ 的值的, 但是我们可以根据**物理条件**来确定 $C_1$ 的值, 这样的条件也被称为**定解条件**. 
>
> `定解条件1`: 小球的初速度为 $2m/s$, 即 $t=0$ 时, $ v(0)=2$. 
>
> 带入方程得 $C_1=2$, 于是我们得到 
> 
> $$
> \begin{equation}
> v(t) = gt + 2
> \end{equation}
> $$
> 
> 为满足`定解条件1`的微分方程 (2) 的解.
>
> Step 2. 
>
> 接下来我们在 (3) 式的基础上继续求解微分方程 (1). 此时
> 
> 
> $$
> y'(t)= v(t) = g t + 2 
> $$
> 
> 对等式两边积分得到
> 
> $$
> y(t)=\frac{1}{2} g t^2 + 2t + C_2
> $$
> 
> 为了确定 $C_2$ 的具体数值, 我们需要第二个定解条件
> 
> `定解条件2`: 小球的初始位置在1米处, 即 $t=0$ 时有 $y(0)=1$
> 
> 同`定解条件1`一样, `定解条件2`也是来自于物理而非方程本身.
> 
> 根据`定解条件2`容易确定, $C_2 = 1$, 从而微分方程 (1) 的解为
> $$
> y(t)= \frac{1}{2} g t^2 + 2t + 1.
> $$
> 
> 此时, 方程的解中已经不含有未知数, 也就是说它是微分方程 (1) 和`定解条件1&2`所确定的唯一解.

> [!warning]
>
> 可能有同学已经注意到了, 上个例子中我们所谓的解微分方程不就是在做不定积分吗? 这是对的. 后面我们会体会到, 很多时候求解微分方程都要归结到积分运算.
>


> [!note]
> 
> ==简谐振动==
> 
> **一维弹簧振子**
> 假设一个质量为 $m$ 的物体连接在弹簧的一端，弹簧另一端固定。当物体受到弹簧的恢复力作用时，它会在平衡位置附近做简谐振动。根据胡克定律，弹簧的恢复力与位移 $x(t)$ 成正比，方向与位移相反，其表达式为：  
> $$
> F_{\text{弹}} = -kx(t)
> $$
> 
> 其中，$k$ 为弹簧常数，$x(t)$ 为物体相对于平衡位置的位移。根据牛顿第二定律，力等于质量乘加速度，因此：  
> 
> $$
> F = ma = m\frac{d^2x(t)}{dt^2}
> $$
> 
> 将两者代入得到弹簧振子的运动方程：  
> 
> $$
> m\frac{d^2x(t)}{dt^2} = -kx(t)
> $$
> 
> 整理得：  
> 
> $$
> \frac{d^2x(t)}{dt^2} + \frac{k}{m}x(t) = 0
> $$
> 
> 令 $\omega^2 = \frac{k}{m}$，方程化为：  
> 
> $$
> \frac{d^2x(t)}{dt^2} + \omega^2 x(t) = 0
> $$
> 
> 这就是简谐振动的微分方程。  
> 
> **方程的解**  
> 
> 接下来我们来"蒙"一个微分方程的解. 你没有听错, 因为微分方程太难解了, 以至于"蒙"也成了一个合理的办法, 总之不管用什么方法, 只要能找到解就行.
> 
> 该二阶线性齐次微分方程的通解为：  
> $$
> x(t) = A\cos(\omega t) + B\sin(\omega t)
> $$
> 
> 其中，$A$ 和 $B$ 是由初始条件决定的常数。  
> 
> **定解条件**  
> 如果初始时刻 $t = 0$ 时，物体的位移为 $x(0) = x_0$，速度为 $v(0) = v_0$，我们可以通过代入初始条件求解 $A$ 和 $B$：  
> 
> 1. **初始位移条件**：  
> $$x(0) = A = x_0$$  
> 2. **初始速度条件**：  
> $$v(0) = x'(0) = -A\omega\sin(0) + B\omega\cos(0) = B\omega = v_0$$  
> 
> 代入初始条件得到：  
> 
> $$
> x(t) = x_0 \cos(\omega t) + \frac{v_0}{\omega} \sin(\omega t)
> $$
> 
> 这个解描述了弹簧振子在简谐运动中的位移随时间的变化情况。

> [!note]
> ==单摆==
> 
> **单摆的描述**  
> 单摆由长度为 $L$ 的细绳和质量为 $m$ 的小球组成，小球在重力作用下绕固定点摆动。假设摆角为 $\theta(t)$，即小球偏离竖直方向的角度，我们将推导其运动方程。  
>  
> **受力分析**  
> 小球所受的力主要包括：  
> 1. **重力** $mg$，方向竖直向下；  
> 2. **绳子的张力** $T$，方向沿绳子向内。  
>  
> 将重力分解为两个方向：  
> - 沿绳方向的分力 $mg\cos\theta$，被张力抵消；  
> - 垂直于绳方向的分力 $mg\sin\theta$，产生恢复力矩。  
>  
> **力矩分析**  
> 恢复力矩 $\tau$ 关于固定点 O 为：  
> $$
> \tau = -mgL\sin\theta
> $$
>  
> 根据牛顿第二定律的角度形式，力矩等于转动惯量 $I$ 乘角加速度 $\alpha$：  
> $$
> \tau = I \alpha
> $$
>  
> 对于单摆，转动惯量 $I = mL^2$，角加速度 $\alpha = \frac{d^2\theta}{dt^2}$，因此：  
> $$
> -mgL\sin\theta = mL^2 \frac{d^2\theta}{dt^2}
> $$
>  
> 消去 $m$ 和 $L$ 后，得到：  
> $$
> \frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0
> $$
>  
> **小角近似**  
> 当 $\theta$ 较小时，$\sin\theta \approx \theta$（弧度制），方程简化为：  
> $$
> \frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0
> $$
>  
> 这就是单摆在小角度近似下的简谐运动方程。  
>  
> **方程的解**  
> 该方程的解跟简谐振动完全一样.
> 

> [!note]
> **LC电路**  
> 一个理想的LC电路由电感 $L$ 和电容 $C$ 组成。假设电路中无电阻，电感与电容串联。电容的电荷量 $q(t)$ 随时间变化，导致电路中的电流 $i(t)$ 也随时间变化。我们来推导该系统的运动方程。  
>  
> **基本方程**  
> 1. **电容的关系**：  
> 电容两端的电压 $u_C(t)$ 与电荷量 $q(t)$ 的关系为：  
> $$
> u_C(t) = \frac{q(t)}{C}
> $$
>  
> 2. **电感的关系**：  
> 电感两端的电压 $u_L(t)$ 与电流变化率 $\frac{di(t)}{dt}$ 的关系为：  
> $$
> u_L(t) = L \frac{di(t)}{dt}
> $$
> 由于电流 $i(t)$ 是电荷 $q(t)$ 的时间导数：  
> $$
> i(t) = \frac{dq(t)}{dt}
> $$
>  
> **回路方程（基尔霍夫电压定律）**  
> 在LC电路中，总电压为零，即：  
> $$
> u_L(t) + u_C(t) = 0
> $$
> 代入电感和电容的表达式：  
> $$
> L \frac{d^2q(t)}{dt^2} + \frac{q(t)}{C} = 0
> $$
>  
> **LC震荡方程**  
> 将上式整理为标准形式：  
> $$
> \frac{d^2q(t)}{dt^2} + \frac{1}{LC}q(t) = 0
> $$
>  
> 这就是LC电路的微分方程，描述了电容器电荷随时间的简谐振荡过程。  
>  
> **特征频率**  
> LC电路的特征角频率 $\omega_0$ 为：  
> $$
> \omega_0 = \sqrt{\frac{1}{LC}}
> $$
> 这表明LC电路的振荡频率只由电感和电容决定，与初始电荷或电流无关。

> [!note]
> 
> ==地心电梯==
> 
> **牛顿壳层定理**
> 假设一个半径为 $R$、质量为 $M$ 的均匀球壳，质点 $m$ 位于球壳内部或外部，球壳对质点的引力为
> 
> - 当 $r \geq R$ 时，球壳对质点的引力为：  
> $$
> F = G\frac{Mm}{r^2}
> $$
> - 当 $r < R$ 时，球壳对质点的引力为：  
> $$
> F = 0
> $$
> 
> 这表明在球壳内部，质点所受引力为零，而在外部，引力遵循经典的万有引力公式，等效于将球壳质量集中于球心。
> 
> 
> **牛顿壳层定理的微积分推导**
> 
>  1. 外部质点的引力
> 取球壳上一个面积元 $dA = R^2 \sin\theta \, d\theta \, d\phi$，其中 $\theta$ 是极角，$\phi$ 是方位角。  
> 球壳的面密度 $\sigma = \frac{M}{4\pi R^2}$，因此面积元的质量：  
> $$
> dm = \sigma \, dA = \frac{M}{4\pi R^2} \cdot R^2 \sin\theta \, d\theta \, d\phi
> $$
> 质点 $P$ 与面积元 $dm$ 之间的距离为：  
> $$
> s = \sqrt{r^2 + R^2 - 2rR\cos\theta}
> $$
> 微元 $dm$ 对质点 $P$ 产生的引力：  
> $$
> dF = G \frac{dm \cdot m}{s^2}
> $$
> 由于球壳的对称性，垂直于径向的引力分量会相互抵消，仅剩下沿径向的分量：  
> $$
> dF_{\text{径}} = dF \cdot \frac{r - R\cos\theta}{s}
> $$
> 将 $dF_{\text{径}}$ 对整个球壳积分：  
> $$
> F = \int_0^{2\pi} \int_0^\pi G \frac{M m}{4\pi R^2} \cdot \frac{R^2 \sin\theta (r - R\cos\theta)}{(r^2 + R^2 - 2rR\cos\theta)^{3/2}} \, d\theta \, d\phi
> $$
> 计算结果表明，球壳外部的引力等效于质量集中于球心：  
> $$
> F = G \frac{Mm}{r^2}
> $$
> 
> 2. 外层球壳的引力为零 (也可以用积分计算, 但比较繁琐)
> 
> 考虑距球心距离为 $r$ 的质点 $P$，外层的壳质量不影响 $P$。引力微元在 $P$ 点的径向和垂直方向上完全抵消，因此外层壳对 $P$ 的引力为：  
> $$
> F_{\text{外}} = 0
> $$
> 
> 
> **穿过地心的电梯在重力作用下的运动方程推导**  
> 
> 假设一部电梯沿直线穿过地球中心，从地球表面一端移动到另一端，忽略空气阻力和其他阻力，仅考虑重力作用。我们将推导电梯在这种情况下的运动方程。  
> 
> 假设地球是一个半径为 $R$ 的均匀密度球体，总质量为 $M$，密度为 $\rho = \frac{M}{\frac{4}{3} \pi R^3}$。在距离地心 $r$ 处，电梯所受引力只来自半径为 $r$ 的球体部分，质量为：  
> $$
> M(r) = \rho \cdot \frac{4}{3} \pi r^3 = M \cdot \frac{r^3}{R^3}
> $$
> 
> 根据牛顿引力定律，电梯在距离地心 $r$ 处的引力为：  
> $$
> F(r) = G \frac{M(r) \cdot m}{r^2} = G \frac{M \cdot m \cdot r}{R^3}  
> $$
> 因此，重力加速度为：  
> $$
> g(r) = G \frac{M}{R^3} \cdot r  
> $$
> 
> 电梯在重力作用下的加速度为 $-g(r)$，即：  
> $$
>\frac{d^2r}{dt^2} = -G \frac{M}{R^3} \cdot r  
> $$
> 这就是一个简谐振动方程，其形式为：  
> $$
> \frac{d^2r}{dt^2} + \omega^2 r = 0  
> $$
> 其中，角频率 $\omega$ 为：  
> $$
> \omega = \sqrt{\frac{G M}{R^3}}  
> $$
>  

## 可分离变量方程

> [!tip]
> 
> 这一节我们介绍一类比较简单的微分方程的解法.

> [!note]
>
> ==速率方程==
>
> 在这个例子中我们考虑一阶微分方程
>
> $$
> \begin{equation}
> \frac{dy}{dt} = k y
> \end{equation}
> $$
>
> 其中 $k$ 为常数. 方程 (4) 是一类非常重要的微分方程, 方程左边是 $y$ 随时间的变化率, 整个方程则表示 $y$ 的瞬时变化率与 $y$ 在当前时刻的值成正比. 这类方程在实际问题中十分常见, 下面我们看两个实例.
>
> **情景1: 传染病**
>
> 考虑一个传染病爆发的场景, 我们用 $y(t)$ 表示 $t$ 时刻感染者的数目. 由于疾病的传播依赖于人和人的接触, 所以当前的感染者 $y(t)$ 约多, 新增的感染人数就会越大. 我们用一个系数 $k$ 来表示这个病的传播能力, 可以理解为在单位时间内一个感染者 (平均) 能够传染 $k$ 个人. 因此在过了 $\Delta t$ 的时间后, $t_0+\Delta t$ 时刻的感染者人数等于 $t_0$ 时刻的感染者人数加上 $\Delta t$ 这段时间内新增的感染者人数, 即
>
> $$
> \begin{equation}
> y(t_0+\Delta t) \approx y(t_0) + k y(t_0) \Delta t
> \end{equation}
> $$
>
> 注意这里时约等于, 因为在 $\Delta$ 这段时间内, 感染者的人数并总是不严格等于 $y(t_0)$ 的, 但是如果 $\Delta t$ 取得很小, 那么 $y$ 的变化也非常小 ($y(t)$ 的连续性), 从而可以近似看成常数 $y(t_0)$.
>
> 通过对公式 (5) 进行变换可以得到
>
> $$
> \frac{y(t_0+\Delta t) - y(t_0)} {\Delta t} \approx  k y(t_0) 
> $$
>
> 根据上面的分析, 当我们让 $\Delta t$ 区域 0 时, 左边趋近于 $y'(t_0)$, 而约等号也会"趋近于"等号, 因此我们得到
>
> $$
> y'(t_0) = k y(t_0)
> $$
>
> 上式中把 $t_0$ 换成 $t$, 就得到微分方程 (4). 
>
> **情景2: 化学反应**
>
> 考虑一个放射性元素的衰变过程，我们用 $y(t)$ 表示 $t$ 时刻剩余的放射性原子数。放射性元素的衰变是一个随机过程，每个原子都有一定的概率在单位时间内发生衰变，因此衰变的速率与当前剩余的原子数成正比。我们用一个常数 $k$ 来表示这种衰变率，称为**衰变常数**，即单位时间内一个原子发生衰变的概率。  
>
> 在时间 $\Delta t$ 之后，剩余的放射性原子数 $y(t_0+\Delta t)$ 可以表示为 $t_0$ 时刻的原子数减去这段时间内衰变的原子数：  
>
> $$
> y(t_0+\Delta t) \approx y(t_0) - k y(t_0) \Delta t
> $$
>
> 注意这里的负号表示原子数目在减小, 而约等于号表示在 $\Delta t$ 时间内，衰变速率近似保持恒定，因为当 $\Delta t$ 很小时，$y(t)$ 变化非常小，$y(t_0)$ 可以被近似看作常数。
>
> 对上式整理并移项得到：
>
> $$
> \frac{y(t_0+\Delta t) - y(t_0)}{\Delta t} \approx -k y(t_0)
> $$
>
> 当我们令 $\Delta t \to 0$ 时，左边趋近于 $y'(t_0)$，约等号也趋近于等号，因此得到：
>
> $$
> y'(t_0) = -k y(t_0)
> $$
>
> 将 $t_0$ 换成一般的 $t$，同样得到微分方程 (4), 只是系数变成了负数.
>
> 
>
> 下面我们来"蒙"方程(4)的解. 我们知道, $\mathrm{e}^t$ 的导数等于它自己, 因此 $\mathrm{e}^t$ 是满足微分方程 $y' = y$ 的一个解. 对 $\mathrm{e}^x$ 进行适当边形, 可以构造出 (4) 的解为
>
> $$
> y(t) = C\mathrm{e}^{kt}
> $$
>
> 其中 $C$ 为一个参数, 依赖于定解条件.
>
> 在**情景1**中, 假设初始时刻 $t=0$ 时感染者的人数 $y(0) = 100$, 可以得到 $C = 100$. 于是 $t$ 时刻的感染者等于
>
> $$
> y(t) = 100\mathrm{e}^{kt}
> $$
>
> 我们经常听到传染病人数"指数型增长"的可怕说法, 背后对应的就是这个数学公式. 当然, 实际情况下指数增长只是在传染病爆发的初期出现, 随着时间的增长, 未感染的群体数目会减小, 还有一部分感染者将被治愈, 这时微分方程 (4) 就不再成立了, 需要用一个新的微分方程来描述.
>
> 在**情景2**中，假设初始时刻 $t=0$ 时放射性原子的数目 $y(0) = N_0$，因此微分方程 
> $$
> y' = -ky
> $$
> 的解为:
>
> $$
> y(t) = N_0 e^{-k t}
> $$
>
> 这个公式描述了放射性原子数目随时间的指数型衰减。与传染病的"指数型增长"相反，放射性衰变是一种**指数型减少**的过程。  
>
> 在实际情况中，放射性衰变是一个非常稳定的过程，不受外界环境的影响，因此微分方程 $y'(t) = -k y(t)$ 可以长期成立，直至几乎所有原子都完成衰变。我们常用**半衰期** $T_{\frac{1}{2}}$ 来描述这个衰变过程，即原子数目减少到初始值一半所需的时间。通过解方程 $y(T_{\frac{1}{2}}) = \frac{N_0}{2}$，可以得到：
>
> $$
> T_{\frac{1}{2}} = \frac{\ln 2}{k}
> $$
>
> 半衰期是一个重要的物理量，它使得我们可以通过简单的实验观测来确定衰变常数 $k$，从而了解放射性物质的衰变特性.

> [!important]
> 
> ==可分离变量方程的求解==
> 
> 方程 (4) 的求解其实可以不通过"蒙", 而是通过一种叫做 "separation of variables" 的技巧求解. 注意到 (4) 可以变形为
> 
> $$
> \frac{dy}{y} = k dx
> $$
> 
> 注意到上式有这么一个特点: 左边只含有变量 $y$, 右边只含有变量 $x$, 具有这个性质的微分方程就是**可分离变量**的微分方程. 这类方程的求解方法为分别对等式左右两边积分, 对上式而言, 可以得到
> 
> $$
> \ln y = k x + \tilde{C}
> $$
> 
> 从而
> 
> $$
> y = \mathrm{e}^{kx +\tilde{C}} = C\mathrm{e}^{kx}
> $$
>
> 这正是我们刚才猜到的解的形式.
> 

> [!note]
> 
> ==例==
> 
> 求解方程 $\displaystyle y' = \frac{y^2}{x^2}$.
> 
> 解: 方程可转换为变量分离的形式:
> 
> $$
> \frac{dy}{y^2} = \frac{dx}{x^2}
> $$
> 
> 对等式两边积分得到
> 
> $$
> -\frac{1}{y} = -\frac{1}{x} + C
> $$
> 
> 即
> 
> $$
> y = \frac{x}{1 + kx}
> $$
> 
> 其中 $k$ 为常数.
> 

## 常系数一阶线性微分方程

> [!tip]
> 
> 本节我们在上一节所介绍的速率方程的基础上进一步扩充, 考虑形如 $ y' = ky + b$ 的方程. 这类方程在实际应用中也经常出现, 属于**一阶线性微分方程**, 它比速率方程多了一个右端项 $b$, 这一节我们首先考虑系数 $k$, $b$ 都是常数的情形. 下一节我们将考虑更加复杂的 $k(x)$, $b(x)$ 随 $x$ 变化的情形.
> 

> [!note]
> 
> ==例: 恒定速率的降温过程(牛顿冷却定律)==
>   
> **模型描述**  
> 牛顿冷却定律描述了物体与周围环境之间的温度变化过程，其微分方程模型为：  
> $$
> \frac{dT}{dt} = -k (T - T_{\text{env}}) 
> $$
> 
> 其中：  
> - $T(t)$：物体在时间 $t$ 的温度。  
> - $T_{\text{env}}$：环境温度（常数）。  
> - $k$：冷却系数，$k > 0$。  
>   
> **求解过程（分离变量法）**  
> 1. 将方程整理为：  
> $$
> \frac{dT}{T - T_{\text{env}}} = -k \, dt
> $$
>   
> 2. 对两边积分：  
> $$
> \int \frac{dT}{T - T_{\text{env}}} = \int -k \, dt
> $$
>   
> 3. 积分结果为：  
> $$
>  \ln |T - T_{\text{env}}| = -kt + C 
> $$
>   
> 4. 通过指数函数解出 $T$：  
> $$
> T - T_{\text{env}} = C_1 e^{-kt} 
> $$
> 
> 其中 $C_1 = e^C$ 为任意常数。  
>   
> 5. 利用初始条件 $T(0) = T_0$，求出 $C_1$：  
> $$
> T_0 - T_{\text{env}} = C_1 
> $$
>   
> 6. 最终解为：  
> $$
> T(t) = T_{\text{env}} + (T_0 - T_{\text{env}}) e^{-kt} 
> $$
>   
> **解释**  
> 物体的温度逐渐趋近于环境温度 $T_{\text{env}}$，冷却速度由系数 $k$ 控制。  

> [!note]
>
> ==例: 简单贷款偿还模型==
>
> **模型描述**  
> 贷款偿还模型描述了借款人以恒定利率和固定还款额偿还贷款的过程，其微分方程为：  
> $$
> \frac{dB}{dt} = rB - P 
> $$
>
> 其中：  
> - $B(t)$：时间 $t$ 时剩余的贷款余额。  
> - $r$：年利率（常数）。  
> - $P$：每年固定还款额。  
>
> **求解过程（分离变量法）**  
>
> 1. 将方程整理为：  
> $$
> \frac{dB}{rB - P} = dt
> $$
>
> 2. 对两边积分：  
> $$
> \int \frac{dB}{rB - P} = \int dt 
> $$
>
> 3. 积分结果为：
>
> $$
>  \frac{1}{r} \ln |rB - P| = t + C 
> $$
>
>   4. 解出 $B$：  
>
> $$
>  rB - P = C_1 e^{rt} 
> $$
>
> 其中 $C_1 = e^{rC}$。  
>
>   5. 利用初始条件 $B(0) = B_0$，求出 $C_1$：  
>
> $$
> rB_0 - P = C_1
> $$
> 6. 最终解为：  
>
> $$
>  B(t) = \frac{P}{r} + \left( B_0 - \frac{P}{r} \right) e^{rt} 
> $$
>
> **解释**  
>   如果 $P > rB_0$，余额 $B(t)$ 随时间逐渐减少，最终贷款将被还清；反之，如果 $P \leq rB_0$，贷款余额将持续增长。

## 变系数一阶线性微分方程

> [!tip]
> 
> 本节考虑更加复杂的 $k(x)$, $b(x)$ 随 $x$ 变化的**一阶线性微分方程**: $ y' = k(x)y + b(x)$.
> 

> [!note] 
>
> ==例: 城市热岛效应模型讲义==
>
> **模型描述**  
>
> 城市热岛效应是指由于人类活动和城市结构导致城市温度显著高于周边郊区的现象。为了描述这种现象，可以使用以下一阶线性微分方程模型：  
>
> $$
> \frac{dT}{dt} = -\alpha(t) T + Q(t)
> $$
>
> 其中：  
> - $T(t)$：城市的平均温度（随时间变化）。  
> - $\alpha(t)$：时间相关的散热系数，表示城市向外部环境散热的效率。  
>   白天，建筑材料吸热，散热效率降低，$\alpha(t)$ 较小。  
>   夜晚，城市散热效率提高，$\alpha(t)$ 较大。  
> - $Q(t)$：时间相关的外部热源，包括：  
> 	太阳辐射：随时间变化呈现周期性。  
>   人类活动：如车辆排放、工业生产、空调使用等。通常在白天达到高峰。   
>
> **模型扩展(通常用在数学建模中)**  
>
> - **加入风速影响：**  
>   散热系数 $\alpha(t)$ 可以扩展为 $\alpha(t, v_w)$，其中 $v_w$ 为风速。风速较大时，散热效果增强。  
>   $$
>   \frac{dT}{dt} = -\alpha(t, v_w) T + Q(t)
>   $$
>
> - **考虑湿度和绿化率：**  
>   可以通过引入湿度和绿化率来模拟更复杂的热交换过程：  
>   $$
>   \frac{dT}{dt} = -(\alpha(t) + \beta H + \gamma G)T + Q(t)
>   $$
>   
> - 
>
>  其中 $H$ 为湿度，$G$ 为绿化率，$\beta$ 和 $\gamma$ 为对应的影响系数。  
>

> [!important]
> 
> ==常数变异法==
> 
> 求解变系数的一阶线性微分方程可以使用常数变异法. 过程如下:
> 
> `step 1`
> 将方程的非齐次项 $b(x)$ 去掉，得到齐次方程：  
> $y' = k(x)y$  
> 这个方程是可分离变量的，解法为：  
> $$
> \frac{dy}{y} = k(x)dx
> $$
> 积分得到：  
> $$
> \ln|y| = \int k(x) dx + C
> $$
> 进一步简化：  
> $$
> y_h = Ce^{\int k(x) dx}
> $$
> 这是齐次方程的一般解。
>
> `step 2`
> 假设非齐次方程的特解形式为：  
> $$
> y_p = u(x)e^{\int k(x) dx}
> $$
> 其中 $u(x)$ 是待定函数。
>
> `step 3`
> 将 $y_p = u(x)e^{\int k(x) dx}$ 代入原方程 $y' = k(x)y + b(x)$，利用链式法则：  
> $$
> y_p' = u'(x)e^{\int k(x) dx} + u(x)k(x)e^{\int k(x) dx}
> $$
> 将 $y_p$ 和 $y_p'$ 代入原方程：  
> $$
> u'(x)e^{\int k(x) dx} + u(x)k(x)e^{\int k(x) dx} = k(x)u(x)e^{\int k(x) dx} + b(x)
> $$
> 化简后得：  
> $$
> u'(x)e^{\int k(x) dx} = b(x)
> $$
> 两边同时除以 $e^{\int k(x) dx}$：  
> $$
> u'(x) = b(x)e^{-\int k(x) dx}
> $$
> 积分求解 $u(x)$：  
> $$
> u(x) = \int b(x)e^{-\int k(x) dx} dx + C
> $$
>
> 通解为齐次解与特解的叠加：  
> $$
> y = y_h + y_p = Ce^{\int k(x) dx} + \left(\int b(x)e^{-\int k(x) dx} dx\right)e^{\int k(x) dx}
> $$
>
> > 最后得到方程的解为:
> > $$
> > y = Ce^{\int k(x) dx} + e^{\int k(x) dx} \int b(x)e^{-\int k(x) dx} dx
> > $$
> > 其中 $C$ 是任意常数。
> 

## 二阶线性微分方程和微分方程组

> [!tip]
> 
> 实际问题中经常出现形如
> $$
> y''(x) + Q(x) \cdot y'(x) + R(x) \cdot y(x) = f(x) 
> $$
> 的微分方程. 这类方程属于**二阶线性微分方程**.
> 

> [!note]
> 
> ==带有阻尼和外力的振动方程==
>  
> 考虑一个质量为 $ m $ 的物体，固定在弹簧上，弹簧常数为 $ k $，并且系统中存在阻力（或阻尼），阻力与速度成正比，比例常数为 $c $。此外，系统受到一个外力 $ F(t) $ 的作用。我们的目标是建立该系统的运动方程。
>
> 系统的受力分析为: 
>  
> - **弹簧力**：根据胡克定律，弹簧的恢复力是与物体的位移 $ x(t) $ 成正比的，方向与位移相反，表达式为：  
>   $$
>   F_{\text{spring}} = -k \cdot x(t)
>   $$
>  
> - **阻尼力**：阻尼力与物体的速度 $ \frac{dx}{dt} $ 成正比，方向与速度相反，表达式为：  
>   $$
>    F_{\text{damping}} = -c \cdot \frac{dx}{dt} 
>   $$
>  
> - **外力**：外力 $F(t)$ 是已知的外部作用力。  
>  
> 根据牛顿第二定律，物体的加速度 $ \frac{d^2x}{dt^2} $ 与合力之比为物体的质量：  
> $$
> m \cdot \frac{d^2x}{dt^2} = F_{\text{spring}} + F_{\text{damping}} + F(t) 
> $$
>  
> 将各个力代入:
> $$
> m \cdot \frac{d^2x}{dt^2} = -k \cdot x(t) - c \cdot \frac{dx}{dt} + F(t)
> $$
>  
> 将上式整理得到标准形式的二阶线性微分方程：  
> $$
>  \frac{d^2x}{dt^2} + \frac{c}{m} \cdot \frac{dx}{dt} + \frac{k}{m} \cdot x(t) = \frac{F(t)}{m} 
> $$
>  
> 这就是有外力的阻尼震荡方程.
> - 当 $F(t) = 0$ 时，方程为齐次方程，描述的是自由阻尼振动：  
>   $$
>   \frac{d^2x}{dt^2} + \frac{c}{m} \cdot \frac{dx}{dt} + \frac{k}{m} \cdot x(t) = 0 
>   $$
>  
> - 当 $ F(t) \neq 0 $ 时，如 $F(t) = h\sin( \omega t)$, 方程为非齐次方程，描述的是有外力作用下的阻尼振动。
> 
>   $$
>   \frac{d^2x}{dt^2} + \frac{c}{m} \cdot \frac{dx}{dt} + \frac{k}{m} \cdot x(t) = \frac{h}{m} \sin( \omega t)
>   $$

> [!warning]
> 
> 前面我们考虑的简谐振动方程可以看成是二阶线性微分方程的特例, 但一般的二阶线性微分方程求解是非常困难的, 需要通过引入新变量的方法将**高阶(二阶)线性微分方程**转化为**一阶线性线性微分方程组**.
> 
> 例如对方程
> 
> $$
>   y'' + p y' + q y = 0
> $$
> 我们可以令 $v(t) = y'(t)$, 则
>   $$
>   \left\{
>   \begin{align*}
>   &y' = u \\
>   &u' = -p u - q y
>   \end{align*}
>   \right.
>   $$
>   
> 求解这类**一阶线性线性微分方程组**需要在高维线性空间中进行, 需要一些线性代数的知识, 因此这部分内容我们将在下学期再介绍.

> [!tip]
> 
> 由多个微分方程联立得到**微分方程组**, 刚才的例子就是一个微分方程组. 实际问题中微分方程组也十分的常见.
> 

> [!note]
> 
> ==Lotka-Volterra 模型==
> 
> Lotka-Volterra 模型是一个经典的捕食-猎物模型，用于描述捕食者与猎物之间的相互作用。该模型由两个微分方程组成，分别描述猎物和捕食者的动态变化。模型的标准形式为：  
>  
> $$
> \frac{dx}{dt} = \alpha x - \beta xy
> $$
> $$
> \frac{dy}{dt} = \delta xy - \gamma y
> $$
>  
> 其中：  
> - $x(t)$ 是猎物（兔子）的数量，  
> - $y(t)$ 是捕食者（狼）的数量，  
> - $\alpha$ 是猎物的自然增长率（不受捕食者影响时），  
> - $\beta$ 是捕食者捕食猎物的效率，  
> - $\delta$ 是捕食者的繁殖率（每捕食一只猎物，捕食者的种群数量增加的比例），  
> - $\gamma$ 是捕食者的死亡率（不受食物影响时）。  
>  
> 这个模型是一个非线性方程组，常用于描述生态系统中捕食者和猎物的动态交互关系。

> [!note]
> 
> ==行星运动方程==
> 
> $$
> \frac{d^2 x}{dt^2} = -G \frac{M}{(x^2 + y^2 + z^2)^{3/2}} x
> $$
> $$
> \frac{d^2 y}{dt^2} = -G \frac{M}{(x^2 + y^2 + z^2)^{3/2}} y
> $$
> $$
> \frac{d^2 z}{dt^2} = -G \frac{M}{(x^2 + y^2 + z^2)^{3/2}} z
> $$
>  
> 该方程组描述了行星在三维空间中的运动。
> 

## 微分方程的数值求解

> [!tip]
> 
> 大部分微分方程都无法解析求解, 运用计算机, 我们可以对微分方程进行数值求解.
> 

> [!note]
> 
> ==Lotka-Volterra方程==
> 
> [课堂展示] 我们可以很容易的用AI帮助我们写程序, 然后画图.

> [!note]
> 
> ==行星运动方程==
> 
> [课堂展示] 我们可以很容易的用AI帮助我们写程序, 然后画图.


[回到主页面](index.html)