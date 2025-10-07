# 导数

> [!tip]
> 
> ==导数是一种通过极限定义的运算==
> 
> 实际问题中人们经常会考虑某个函数的**极值**, 函数的**切线方向**是分析函数极值的有力工具: 
> - 切线斜率为正时函数单调递增
> - 切线斜率为负时函数单调递减
> - 切线斜率为零时函数取到极值
>
> 那么怎么求函数在某处**切线的斜率**呢? 这个问题困扰了数学家好多年, 直到后来有人发现**切线斜率可以看作是一个极限**, 这个极限也叫做**导数**.
> 
> 由此我们也可以进一步体会到**极限**的重要性. 而在后面的章节中, 我们会再次运用**极限**来构造**积分**. 因此极限的概念相当于整个微积分的基础. 
> 
> 右图给出了课本各部分内容之间的关系.
> 
> ==思维导图==
> 
> ![微积分思维导图](../media/img/chpt2_derivative.png#400h)

## 导数和导函数

> [!tip]
>
> - 导数是函数的**瞬时变化率**.
> - 导数是函数某处的**切线斜率**.
> 
>  ==**导数**是研究函数性质的重要工具==
> 
>  **问题**: 计算 $\displaystyle f(x) = \sin(x) - \frac{2x}{\pi}$在$\displaystyle [0,{\pi}]$的最大值.
> 
>  **求解**: 函数 $f(x)$ 的图像如下图, 问题要求我们找到图像的最高点. 运用导数我们可以很方便的得到最高点的坐标, 我们中学学过: 函数在一点的导数等于函数图像在这一点处的切线斜率, 从图像上看函数的最大值对应切线水平(即斜率为0)的位置. 因此我们可以对函数求导, 得到：
> $$
> \displaystyle f'(x) = \cos(x) - \frac{2}{\pi}.
> $$
> 令 $f'(x) = 0$，所得的解处的切线斜率为0, 由此解得极值点：
> $$
> \displaystyle x^* = \arccos\left(\frac{2}{\pi}\right),
> $$
> 所对应的函数值为 $\displaystyle f(x^*)$.
>  
>  ![导数的作用](../media/img/chap2_0.png)

### 导数的定义

> [!important]
>
> 
>  ==导数的定义==
>
> 导数是切线的斜率，而切线的斜率可以定义为割线斜率在割点趋于该点时的极限。
> 
> 设函数 $f(x)$ 在点 $x_0$ 附近有定义，则过点 $(x_0, f(x_0))$ 和 $(x_0 + \Delta x, f(x_0 + \Delta x))$ 的割线斜率为 $\displaystyle \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$, 当 $\Delta x \to 0$ 时，这个割线斜率的极限（若存在）就是切线的斜率，也即导数：
> $$
> f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} =\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}.
> $$
> 这样，切线的斜率和导数都通过极限的方式被严格定义。

>  ![导数的几何意义](../media/img/derivative.png)
>  

> [!extension]
>
> ==切线的数学定义==
> 
> 早期，古希腊数学家如欧几里得和阿波罗尼斯主要用几何方法描述切线，把切线看作“只与曲线在一点相交且不过该点的直线”。但这种定义对复杂曲线（如圆外的曲线）不适用。
> 
> 直到17世纪，笛卡尔和费马等人提出了代数方法，尝试用斜率和代数方程描述切线。牛顿和莱布尼茨发明微积分后，才用“割线的极限”来严格定义切线斜率，也就是现代导数的定义。
> 
> 所以，现代切线的定义必须依靠极限，因为只有极限才能精确描述“割线趋近于切线”的过程，从而适用于所有光滑曲线。没有极限，切线的定义就不够一般和严密。
>

> [!note]
> 
> ==由定义计算导数==
> 
> 
> 
>  ==例1==
>  
>  **求 $f(x) = C$ 在 $x_0=1$ 处的导数.**
> 
>  解：根据导数的定义：
> $$
> f'(1) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{C - C}{\Delta x} = \lim_{\Delta x \to 0} \frac{0}{\Delta x} = 0.
> $$
> 
>  ==例2==
>  
>  **求 $f(x) = x^2$ 在 $x_0=2$ 处的导数.**
>  
> 解：根据导数的定义：
> 
> $$
> \begin{align*}
> \displaystyle f'(2) &= \lim_{\Delta x \to 0} \frac{(2 + \Delta x)^2 - 2^2}{\Delta x} \\ 
> & = \lim_{\Delta x \to 0} \frac{4 + 4\Delta x + (\Delta x)^2 - 4}{\Delta x} \\
> & = \lim_{\Delta x \to 0} \frac{\Delta x(4 + \Delta x)}{\Delta x} \\
> & = \lim_{\Delta x \to 0} (4 + \Delta x) \\
> & = 4
> \end{align*}
> $$

### 导函数

> [!tip]
> 
> 对函数 $f(x)$ 定义域上的每一点都求导 (假设每一点的导数都存在), 得到一个新的函数, 称为**导函数**, 记作 $f'(x)$. 导函数是由 $f(x)$ **衍生**出来的, 正好和 Derivative (导数) 的意思一致.


> [!extension]
>
> ==Derivative(金融衍生品)==
>
> 数学中的“导数”（Derivative）是由原函数“衍生”出来的新函数，反映原函数的变化率。
>
> 金融中的“衍生品”（Derivative）是指价值依赖于其他基础资产（如股票、债券等）的金融工具。期权（Option）是一种金融衍生品，允许持有者以指定价格来购买股票。
> - 如果股票价格上涨（函数递增），看涨期权的价值增加（导数为正）。
> - 如果股票价格下跌（函数递减），看涨期权的价值减少（导数为负）。
>
> 类比：
> - 数学导数：$f'(x)$ 依赖于 $f(x)$，描述 $f(x)$ 的变化率，是由 $f(x)$ “衍生”出来的。
> - 金融期权：期权的价格依赖于股票价格，是由股票“衍生”出来的金融产品。
> 
> [!note]
>
>  ==例3==
>  
>  **求函数 $f(x) = x^2$ 的导函数.**
>  
>  解： 
> $$
> \begin{align*}
> f'(x) & = \lim_{\Delta x\to 0} \frac{(x+\Delta x)^2 - x^2}{\Delta x}\\
> & = \lim_{\Delta x\to 0} \frac{2x\Delta x + \Delta x^2}{\Delta x} \\
> & = \lim_{\Delta x\to 0} 2x + \Delta x \\
> & = x.
> \end{align*}
> $$
>
>  ==例4(P78例4)==
>  
>  **求函数 $f(x) = \cos x$ 的导数.**
>
>  解：
> $$
> \begin{align*}
> f'(x) & = \lim_{\Delta x \to 0} \frac{\cos(x + \Delta x) - \cos x}{\Delta x} \\
> & = \lim_{\Delta x \to 0} \frac{-2 \sin\left( x + \frac{\Delta x}{2} \right) \sin\left( \frac{\Delta x}{2} \right)}{\Delta x} \\
> & = - \lim_{\Delta x \to 0} \sin\left( x + \frac{\Delta x}{2} \right) \cdot \lim_{\Delta x \to 0} \frac{\sin\left( \frac{\Delta x}{2} \right)}{\frac{\Delta x}{2}} \\
> & = \sin{x}.
> \end{align*}
> $$
>


> [!warning]
> 
> 在物理中, 给定位移关于时间的函数 $s(t)$, 物体的速度 $v(t)$ 便是 $s(t)$ 的导数. 以自由落体为例, 设物体从静止开始自由下落，重力加速度为 $g$，则
> 
> - 位移函数为 $s(t) = \frac{1}{2}gt^2$。
> 
> - 速度为位移的导数：$v(t) = s'(t) = gt$。
> 
> - 加速度为速度的导数：$a(t) = v'(t) = g$，为常数。
> 

### 幂函数, 对数函数和指数函数的导数

> [!note]
>
>  ==幂函数的导数== 
> 
> **求正整数次幂函数 $ f(x) = x^m $ 的导数.**
> 
> 解：当 $m = 1$ 时：
> $$
> \displaystyle f'(x) = \lim_{\Delta x \to 0} \frac{(x+\Delta x) - x}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta x}{\Delta x} = 1
>$$
> 
> 当 $m > 1$ 时：
> $$
> \begin{align*}
> \displaystyle f'(x) & = \lim_{\Delta x \to 0} \frac{(x+\Delta x)^m - x^m}{\Delta x} \\
>   & = \lim_{\Delta x \to 0} \left[ \frac{x^m + m x^{m-1} \Delta x + \frac{m(m-1)}{2} x^{m-2} (\Delta x)^2 + \cdots + (\Delta x)^m - \Delta x^m}{\Delta x} \right]\\
>   & = \lim_{\Delta x \to 0} \left[ m x^{m-1} + \frac{m(m-1)}{2} x^{m-2} \Delta x + \cdots + (\Delta x)^{m-1} \right] \\ 
> & = m x^{m-1}
> \end{align*}
> $$
> 
> 考虑到 $x^0 = 1$, 上面两种情况可以统一为
> $$
> (x^m)' = m x^{m-1}, \ m = 1, 2, \cdots
> $$


> [!warning]
> 我们不加证明的指出, 上述公式对任意的 $m \in \mathbb{R}$ 都成立, 即
> $$
> \boxed{
> (x^m)' = m x^{m-1}, \ m \in \mathbb{R}.
> }
> $$
> 


> [!warning]
> 
> ==先导结论==
>
> 在计算指数函数和对数函数的导数时我们需要用到下面的一些结论.
>
> - $\displaystyle \lim_{x \to 0} \frac{\ln(1+ x)}{x} = 1$
> 
> **证明:** [待补充]
>
> - $\displaystyle \lim_{x \to 0} \frac{\log_a(1+ x)}{x} = \frac{1}{\ln a}$
>
> **证明:** [待补充]
> 


> [!important]
> 
>  ==对数函数的导数== 
> 
> **求对数函数 $f(x) = \log_u x$ 的导数, 其中 $u$ 是大于 0 且不等于 1 的常数.**
> 
> 解：
> $$
> f'(x) = \lim_{\Delta x \to 0} \frac{\log_u (x + \Delta x) - \log_u x}{\Delta x}
> $$
> 
> 利用换底公式 $\displaystyle \log_u a = \frac{\ln a}{\ln u}$, 
> 
> $$
> f'(x) = \lim_{\Delta x \to 0} \frac{\frac{\ln(x + \Delta x)}{\ln u} - \frac{\ln x}{\ln u}}{\Delta x} = \frac{1}{x \ln u} \cdot \lim_{\Delta x \to 0} \frac{\ln\left(1 + \frac{\Delta x}{x}\right)}{\frac{\Delta x}{x}}
> $$
> 
> 令 $\displaystyle h = \frac{\Delta x}{x}$，当 $\Delta x \to 0$ 时 $h \to 0$，则：
> $$
> f'(x) = \frac{1}{x \ln u} \cdot \lim_{h \to 0} \frac{\ln(1 + h)}{h} = \frac{1}{x \ln u}
> $$
>
> 注: 最后一步用到了上面的先导结论.
>
> 由此我们得到对数函数的导数为:
> 
> $$\boxed{
> (\log_u x)' = \frac{1}{x \ln u}.
> }
> $$

> [!warning]
>
> 特别的, 当 $u=e$ 时, $\log_u x = \ln x$, 此时 
> $$ \boxed{
> (\ln x)' = \frac{1}{x}.
> }
> $$

> [!important]
> 
>  ==指数函数的导数== 
> 
> **求指数函数 $f(x) = q^x$ 的导数，其中底数 $q$ 是大于 0 且不等于 1 的常数.**
> 
> 解：
> 
> $$
> f'(x) = \lim_{\Delta x \to 0} \frac{q^{x + \Delta x} - q^x}{\Delta x}= \lim_{\Delta x \to 0} \frac{q^x \cdot q^{\Delta x} - q^x}{\Delta x}= q^x \cdot \lim_{\Delta x \to 0} \frac{q^{\Delta x} - 1}{\Delta x}
> $$
>  
> 我们注意到当 $\Delta x\to 0$ 时, $q^{\Delta x} \to 1$, 而 $q^{\Delta x} -1 \to 0$, 于是我们把 $q^{\Delta x} -1$ 看作一个新的变量 $h$, 故此时有当 $\Delta x\to 0$ 时 $h \to 0$. 于是根据**极限运算的换元法**, 
> $$
> \lim_{\Delta x \to 0} \frac{q^{\Delta x} - 1}{\Delta x} = \lim_{h \to 0} \frac{h}{\log_q(1+h)} = \ln q.
> $$
>
> 上式中的最后一个等式用到了前面的先导结论.
> 
> 因此，
> $$\boxed{
> (q^x)' = q^x \ln q.
> }$$
> 
> 这就是指数函数的导数公式。

> [!warning]
> 
> 特别的, 当 $u = e$ 时，有
> $$\boxed{
> (e^x)' = e^x.
> }$$
> 
> 也就是说, 以欧拉数 $e$ 为底数的指数函数的导数正是**它自己**, 由此也可以看出 $e$ 在数学上的特殊性.

### 可导函数与连续函数

> [!caution]
> 
> ==连续与可导的关系==
>
> 处处可导的函数称为**可导函数**, 处处连续的函数称为**连续函数**. 函数在一点可导则在该点也必连续, 但函数在一点连续并不保证在该点可导. 
> 

> [!note]
> 
>  ==连续但不可导的反例1==
>  
>  **绝对值函数 $f(x) = |x|$ 在 0 点连续但不可导.**
> 
>  绝对值函数在 $x = 0$ 处是连续的. 在 $x=0$ 处, 
> $$
> \lim_{\Delta x \to 0} \frac{f(0+\Delta x)-f(0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{|\Delta x|}{\Delta x}
> $$
> 
> 当 $\Delta x < 0$ 时, $\displaystyle \frac{|\Delta x|}{\Delta x} = -1$; 
> 当 $\Delta x > 0$ 时, $\displaystyle \frac{|\Delta x|}{\Delta x} = 1$, 
> 左右极限不相等，故极限不存在, 因此，函数 $f(x) = |x|$ 在 $x=0$ 处不可导.

> 
>  ==连续但不可导的反例2==
>  
>  **函数 $f(x) = x^{\frac{1}{3}}$ 在 0 点处连续但不可导.**
> 
>  函数在 $x = 0$ 处连续. 下面我们来计算该函数在 $x=0$ 处的导数.
>
> - **方法一: 根据定义计算**
> 
> $$
> \frac{f(0+\Delta x)-f(0)}{\Delta x} = \frac{(0+\Delta x)^{\frac{1}{3}} - 0^{\frac{1}{3}}}{\Delta x} = (\Delta x)^{-\frac{2}{3}}.
> $$
> 当 $\Delta x \to 0$ 时，极限趋于无穷大，故函数在 $x = 0$ 处**不可导**.
>
> - **方法二: 对导函数取极限**
>
> 根据幂函数的求导公式可以得到
>
> $$
> f'(x) = \frac{1}{3}x^{-\frac{2}{3}}, \ x\ne 0.
> $$
>
> 当 $x \to 0$ 时, 导函数 $f'(x)$ 趋于无穷大, 提示 $f'(0)$ 可能不存在. 需要特别指出, 上述对导数取极限的做法主要提供一个感性认识(直觉), 要严格证明导数在 0 点不存在还是需要根据定义计算.
>
> **注意:** 
>
> 上述两种方法都涉及到极限, 但是取极限的对象不同, 方法一中是对 $\Delta x$ 取极限, 而方法二中是对 $x$ 取极限, 尽管都趋于无穷大(而且指数项都是 $-\frac{2}{3}$), 但两者的意义是不一样的, 请注意体会.
> 

### 单侧导数

> [!important]
> 
> ==单侧导数==
>
> 在计算绝对值函数在 0 点的导数时, 我们注意到 $f(x) = |x|$ 在 0 点左右两侧的切线斜率都存在, 为了更加细致的分析函数的行为, 我们可以引入**单侧导数**的概念. 
> 
> 我们定义函数 $f(x)$ 在 $x_0$ 处的**左导数**
> $$
> f'_-(x_0) = \lim_{\Delta x  \to 0^-} \frac{f(x_0 + \Delta x ) - f(x_0)}{\Delta x },
> $$
> 和**右导数**  
> $$
> f'_+(x_0) = \lim_{\Delta x  \to 0^+} \frac{f(x_0 + \Delta x ) - f(x_0)}{\Delta x }.
> $$
>
> 左导数和右导数统称为单侧导数, 函数 $ f(x) $ 在点 $ x_0 $ 处可导的条件是左导数和右导数都存在且相等.
>
> 对绝对值函数在 $x_0 = 0$ 点处而言, 其单侧导数都存在, 但是不相等, 因此在该点并不可导.
>



## 导数的计算

> [!tip]
>
> 求给定函数的导数的操作称为求导运算。本节将介绍常见函数的求导公式与导数的四则运算法则。熟练运用这些法则，将能显著简化求导过程，提高运算效率。

### 初等函数求导公式

> [!important]
> 
> ==常见初等函数的求导公式==
> 1. 幂函数
> - 如果 $f(x) = x^n$，则：
> $$\displaystyle f'(x) = n \cdot x^{n-1}$$
> 
> 2. 指数函数
> - 如果 $f(x) = e^x$，则：
> $$\displaystyle f'(x) = e^x$$
> 
> - 如果 $f(x) = a^x$，则：
> $$\displaystyle f'(x) = a^x \ln(a)$$
> 
> 3. 对数函数
> - 如果 $f(x) = \ln(x)$，则：
> $$\displaystyle f'(x) = \frac{1}{x}$$
> 
> - 如果 $f(x) = \log_a(x)$，则：
> $$\displaystyle f'(x) = \frac{1}{x \ln(a)}$$
> 
> 4. 三角函数
> - 如果 $f(x) = \sin(x)$，则：
> $$\displaystyle f'(x) = \cos(x)$$
> 
> - 如果 $f(x) = \cos(x)$，则：
> $$\displaystyle f'(x) = -\sin(x)$$
> 
> 5. 反三角函数 (不要求)
> - 如果 $f(x) = \arcsin(x)$，则：
> $$\displaystyle f'(x) = \frac{1}{\sqrt{1 - x^2}}$$
> 
> - 如果 $f(x) = \arccos(x)$，则：
> $$\displaystyle f'(x) = \frac{-1}{\sqrt{1 - x^2}}$$
> 
> - 如果 $f(x) = \arctan(x)$，则：
> $$\displaystyle f'(x) = \frac{1}{1 + x^2}$$

### 导数的四则运算

> [!tip]
> 
> 下面的导数四则法则都可以根据导数的定义加以证明.
> 

> [!important]
> 
> ==导数的四则运算法则==
> 
> - **加法**: 若函数 $f(x)$ 和 $g(x)$ 在点 $x$ 处可导，则：
>
> $$
> [f(x) + g(x)]' = f'(x) + g'(x)
> $$
>
> **证明**:
> 根据导数的定义：
> $$
> \begin{align*}
> [f(x) + g(x)]' &= \lim_{h \to 0} \frac{[f(x+h) + g(x+h)] - [f(x) + g(x)]}{h} \\
> & = \lim_{h \to 0} \left[ \frac{f(x+h) - f(x)}{h} + \frac{g(x+h) - g(x)}{h} \right] \\
> & = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} + \lim_{h \to 0} \frac{g(x+h) - g(x)}{h} \\ 
> & = f'(x) + g'(x)
> \end{align*}
> $$
>
> 
> - **减法**: 若函数 $f(x)$ 和 $g(x)$ 在点 $x$ 处可导，则：
>
> $$
> [f(x) - g(x)]' = f'(x) - g'(x)
> $$
>
> 该性质的证明跟导数的加法运算完全类似.
> 
> - **乘法**: 若函数 $f(x)$ 和 $g(x)$ 在点 $x$ 处可导，则：
> $$
> [f(x) \cdot g(x)]' = f'(x)g(x) + f(x)g'(x)
> $$
>
> **证明：**
> 根据导数的定义：
> $$
> \begin{align*}
> [f(x)g(x)]' &= \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x)g(x)}{h} \\
> &= \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x+h)g(x) + f(x+h)g(x) - f(x)g(x)}{h} \\
> &= \lim_{h \to 0} \left( f(x+h) \frac{g(x+h) - g(x)}{h} + g(x) \frac{f(x+h) - f(x)}{h} \right) \\
> &= \lim_{h \to 0} f(x+h) \cdot \lim_{h \to 0} \frac{g(x+h) - g(x)}{h} + g(x) \cdot \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \\
> &= f(x)g'(x) + g(x)f'(x)
> \end{align*}
> $$
>
> - **除法**
> 若函数 $f(x)$ 和 $g(x)$ 在点 $x$ 处可导，且 $g(x) \ne 0$，则：
>$$
> \displaystyle\left[ \frac{f(x)}{g(x)} \right]' = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
> $$
> 
>**证明：**
> 根据导数的定义：
> $$
> \begin{align*}
> \left[ \frac{f(x)}{g(x)} \right]' &= \lim_{h \to 0} \frac{\frac{f(x+h)}{g(x+h)} - \frac{f(x)}{g(x)}}{h} \\
> &= \lim_{h \to 0} \frac{f(x+h)g(x) - f(x)g(x+h)}{h \cdot g(x)g(x+h)} \\
> &= \lim_{h \to 0} \left( \frac{f(x+h) - f(x)}{h} \cdot \frac{g(x)}{g(x)g(x+h)} - \frac{g(x+h) - g(x)}{h} \cdot \frac{f(x)}{g(x)g(x+h)}\right) \\
> &= \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \cdot \lim_{h \to 0} \frac{g(x)}{g(x)g(x+h)} - \lim_{h \to 0} \frac{g(x+h) - g(x)}{h} \cdot\lim_{h \to 0} \frac{f(x)}{g(x)g(x+h)} \\
> &= f'(x) \cdot \frac{1}{g(x)} - g'(x) \cdot \frac{f(x)}{[g(x)]^2} \\
> &= \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
> \end{align*}
> $$

> [!note]
> 
> ==P86 例1== 
> 
> **求函数 $y = 3x^3 - 4x^2 + 5x - 9$ 的导数 $y'$.**
> 
> $\begin{aligned}
> 解：y' &= (3x^3 - 4x^2 + 5x - 9)' \\
> &= (3x^3)' - (4x^2)' + (5x)' - (9)' \quad  \\
> &= 3 \cdot 3x^{3-1} - 4 \cdot 2x^{2-1} + 5 \cdot 1x^{1-1}\\
> &= 9x^2 - 8x + 5 \quad 
> \end{aligned}$
> 
> 
> ==P86 例2==
> 
> **设 $y = 2e^{x}(\sin x + 2\cos x)$，求 $y'$**
> 
> $\begin{aligned}
> 解：y' &= (2e^{x})'(\sin x + 2\cos x) + 2e^{x}(\sin x + 2\cos x)' \\
> &= 2e^{x}(\sin x + 2\cos x) + 2e^{x}(\cos x - 2\sin x) \\
> &= 2e^{x}\sin x + 4e^{x}\cos x + 2e^{x}\cos x - 4e^{x}\sin x \\
> &= 6e^{x}\cos x - 2e^{x}\sin x \\
> &= 2e^{x}(3\cos x - \sin x)
> \end{aligned}$
>
> ==P86 例3==
> 
> **求函数 $f(x) = x^3 + 3\sin x + \frac{5}{2}$ 的导数 $f'(x)$ 及 $f'\left(\frac{\pi}{4}\right)$**
> 
> $\begin{aligned}
>    解：f'(x) &= \left( x^3 + 3\sin x + \frac{5}{2} \right)' \\
>    &= (x^3)' + (3\sin x)' + \left( \frac{5}{2} \right)' \quad \\
>    &= 3x^2 + 3\cos x + 0 \quad \\
>    &= 3x^2 + 3\cos x.
>    \end{aligned}$
> 
>  $\begin{aligned}\ \ \ \ \ \ \ 
>    f'\left( \frac{\pi}{4} \right) &= 3\left( \frac{\pi}{4} \right)^2 + 3\cos\left( \frac{\pi}{4} \right) \\
>    &= \frac{3\pi^2}{16} + \frac{3\sqrt{2}}{2}.
>    \end{aligned}$
>
>==P86 例4==
>
> **设 $y = \tan x$，求 $y$ 的导数 $y'$**
> 
> 解：
> $\displaystyle y' = (\tan x)' = \left( \frac{\sin x}{\cos x} \right)' = \frac{(\sin x)' \cos x - \sin x (\cos x)'}{\cos^2 x}$
> 
> $\displaystyle = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x$


### 高阶导数
> [!tip]
> 
> 导函数也是函数, 所以可以继续对导函数求导, 也就是二阶导数. 二阶导数反应了导函数的变化率. 依次可以继续到三阶导数, 四阶导数, ...
> 

> [!important]
> 
> ==二阶导数==
> 
> $f''(x) = (f'(x))'$
>
> ==高阶导数==
> 
> - $f'(x)$, $f''(x)$, $f'''(x)$, $f^{(n)}(x)$, $\cdots$.

> [!note]
> 
> ==P97 例1==
> 
> **设 $y = ax^2 + bx + c$，求 $y''$**
> 
> 解： 
> 
> 一阶导数 $y'$ ：
> $$
> y' = (ax^2)' + (bx)' + (c)' = 2ax + b 
> $$
> 
> 二阶导数 $y''$ ：
> $$
> y'' = (2ax)' + (b)' = 2a + 0 = 2a
> $$
>

> [!note]
> 
> ==P98 例7==
> 
> **求幂函数 $y = x^{a}$（$a$ 是任意常数）的 $n$ 阶导数**
> 
> 解： 
> $$
> y' = (x^{a})' = a x^{a-1}
> $$
> 
> $$
> y'' = \left( a x^{a-1} \right)' = a (a - 1) x^{a-2}
> $$
> 
> $$
> y''' = \left( a (a - 1) x^{a-2} \right)' = a (a - 1)(a - 2) x^{a-3}
> $$
> 
> $$\cdots $$
> 
> $$
> y^{(n)} = a (a - 1)(a - 2) \cdots (a - n + 1) x^{a-n}
> $$
>
> 特别的, 当 $a = n$ 为正整数时,
> $$
> (x^n)^{(n)} = n(n-1)(n-2) \cdot \cdots \cdot 3 \cdot 2 \cdot 1 = n!
> $$
> 
> $$
> (x^n)^{m} = 0 \quad m > n.
> $$
>

## 利用导数来研究函数的性质

> [!tip]
> 
> 导数可以用来研究**函数的变化率**, 仅仅这一条已经很强大了, 下面的应用都源自于导数的这一功能.

### 单调性

> [!caution]
> 
> - 导数>0, 单调递增
> - 导数<0, 单调递减
> - 导数=0, 无法判断
>

> [!note]
> 
> 
> 
>  ==P145 例1==
> 
> **判定函数 $\displaystyle y = x + \cos x$ 在 $[0, 2\pi]$ 上的单调性**
> 
> 解： 函数在 $[0, 2\pi]$ 上连续，在 $(0, 2\pi)$ 内可导。求导得：
> $\displaystyle y' = (x + \cos x)' = 1 - \sin x$
> 因为 $\sin x \in [-1, 1]$，
> 所以：$\displaystyle 1 - \sin x \geq 0 \quad (\forall x \in \mathbb{R})$
> 当 $\displaystyle x = \frac{\pi}{2}$ 时，$y' = 1 - 1 = 0$ 
> 
> 当 $\displaystyle x \neq \frac{\pi}{2}$ 时，$y' > 0$
> 导数非负且仅在离散点为零时函数单调递增
> 
> 故函数 $y = x + \cos x$ 在 $[0, 2\pi]$ 上严格单调递增
>

> [!note]
> 
>  ==P145 例2==
>  
> **讨论函数 $\displaystyle y = e^x - x + 3$ 的单调性**
> 
> 解： 函数在 $(-\infty, +\infty)$ 上可导，其导数为：
> $\displaystyle y' = (e^x - x + 3)' = e^x - 1$
> 
> 函数 $y = e^x - x - 1$ 的定义域为 $(-\infty, +\infty)$
> 
> - 在区间 $(-\infty, 0)$ 内：
> $\displaystyle y' = e^x - 1 < 0$
> 因此函数在 $(-\infty, 0]$ 上单调递减。
> 
> - 在区间 $(0, +\infty)$ 内：
> $\displaystyle y' = e^x - 1 > 0$
> 因此函数在 $[0, +\infty)$ 上单调递增。
> 
> 
### 极值

> [!caution]
> 
> - 导数=0, 二阶导数>0, 极小
> - 导数=0, 二阶导数<0, 极大
> - 导数=0, 二阶导数=0, 无法判断. 导数为0的点也称为**驻点**或**临界点**.
> 

> [!note]
> 
> ==P156 例2==
> 
> **求函数 $f(x) = x^4 - 4x^2$ 的极值**
> 
> 解：一阶导数为：
> $\displaystyle f'(x) = (x^4 - 4x^2)' = 4x^3 - 8x = 4x(x^2 - 2)$
> 
> 令 $f'(x) = 0$，解得：
> 
> $\displaystyle 4x(x^2 - 2) = 0 \quad \Rightarrow  x_1 = 0,\quad x_2 = \sqrt{2}, \quad x_3 = -\sqrt{2}$
> 
> 二阶导数为： 
> $\displaystyle f''(x) = (4x^3 - 8x)' = 12x^2 - 8$
> 
> 在 $x = 0$ 处：
> $\displaystyle f''(0) = 12 \cdot 0 - 8 = -8 < 0$ 因此 $x = 0$ 处为极大值，极大值为：
>    
> $\displaystyle f(0) = 0^4 - 4 \cdot 0^2 = 0$
> 
> 在 $x = \pm \sqrt{2}$ 处：
> 
> $\displaystyle f''(\pm \sqrt{2}) = 12 \cdot (\sqrt{2})^2 - 8 = 12 \cdot 2 - 8 = 16 > 0$
> 
> 因此 $x = \pm \sqrt{2}$ 处为极小值，极小值为：
> 
> $\displaystyle f(\pm \sqrt{2}) = (\sqrt{2})^4 - 4 \cdot (\sqrt{2})^2 = 4 - 8 = -4$

>
> [!caution]
> 
> ==极值和最值==
> 
>闭区间上连续函数最值的求解步骤
>设 $f(x)$ 在 $[a, b]$ 上连续，则其最大值和最小值可按以下步骤求解：
> 1. **确定临界点**：
> - 求 $f(x)$ 在 $(a, b)$ 内的 **驻点**（即 $f'(x) = 0$ 的解）；
> - 找出 $f(x)$ 的 **不可导点**（如分段点、尖点等）。
> 2. **计算候选值**：
> - 计算驻点、不可导点处的函数值 $f(x_i)$；
> - 计算端点值 $f(a)$ 和 $f(b)$。
> 3. **比较结果**：选出最大值和最小值


> [!warning]
> 
> ==光路最短原理==
>
> **问题：** 一束光线从空气中的点A出发，经过水面折射后到达水中的点B。已知光在空气中和水中的传播速度分别为 $v_1$ 和 $v_2$，试确定光线从点A到点B传播耗时最短的路径。
>
> **解：**
>
> 如图所示，我们建立一个直角坐标系，将光线传播路径与水面（$x$ 轴）的交点设为 $P$。
>
> * 点 $A$ 的坐标为 $(0, h_1)$。
> * 点 $B$ 的坐标为 $(l, -h_2)$。
> * 点 $P$ 的坐标为 $(x, 0)$。
>
> ![](../media/img/chap2_1.png)
>
>
> 光线从 $A$ 到 $P$ 在空气中传播的距离为 $S_1 = \sqrt{h_1^2 + x^2}$，从 $P$ 到 $B$ 在水中传播的距离为 $S_2 = \sqrt{h_2^2 + (l - x)^2}$。
>
> 根据**光路最短原理（费马原理）**，光线在两点之间传播时，所走的路径是耗时最短的路径。因此，光线从A到B的总传播时间 $T(x)$ 必须取最小值。
>
> $$T(x) = \frac{S_1}{v_1} + \frac{S_2}{v_2} = \frac{\sqrt{h_1^2 + x^2}}{v_1} + \frac{\sqrt{h_2^2 + (l - x)^2}}{v_2}, \ \ x \in [0, l]$$
>
> 为了找到使 $T(x)$ 最小的 $x$ 值，我们对函数 $T(x)$ 求导并令其等于零。
>
> $$T'(x) = \frac{1}{v_1} \cdot \frac{2x}{2\sqrt{h_1^2 + x^2}} + \frac{1}{v_2} \cdot \frac{2(l-x)(-1)}{2\sqrt{h_2^2 + (l - x)^2}}$$
>
> $$= \frac{1}{v_1} \cdot \frac{x}{\sqrt{h_1^2 + x^2}} - \frac{1}{v_2} \cdot \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}$$
>
> 令 $T'(x) = 0$，得到：
>
> $$\frac{1}{v_1} \cdot \frac{x}{\sqrt{h_1^2 + x^2}} = \frac{1}{v_2} \cdot \frac{l - x}{\sqrt{h_2^2 + (l - x)^2}}$$
>
> 观察几何关系，我们可以看到：
>
> * $\frac{x}{\sqrt{h_1^2 + x^2}} = \sin \theta_1$
> * $\frac{l - x}{\sqrt{h_2^2 + (l - x)^2}} = \sin \theta_2$
>
> 其中，$\theta_1$ 是入射光线与法线之间的夹角，$\theta_2$ 是折射光线与法线之间的夹角。将这两个关系代入上式，我们得到：
>
> $$\frac{\sin \theta_1}{v_1} = \frac{\sin \theta_2}{v_2}$$
>
> 这就是著名的**斯涅耳定律（Snell's Law）**。它精确地描述了光线在两种介质交界面上发生折射时的行为。
>
> **光路最短原理（费马原理，Fermat's Principle**是几何光学中最基本、最重要的原理之一，它指出光在两点之间传播时，所走的路径是光程最短的路径，而非距离最短的路径。这个例子很好地说明了如何利用微积分来证明费马原理与斯涅耳定律的等价性。

### 凸性

> [!important]
> 
> ==凸函数的定义==
>
> 设 $f(x)$ 是定义在实数集上的函数。如果对于定义域内任意的 $x_1, x_2$，都有：
> $$
> f\left(\frac{x_1 + x_2}{2}\right) \leq \frac{f(x_1) + f(x_2)}{2}
> $$
> 则称函数 $f(x)$ 是凸函数。
> 

> [!caution]
> 
> ==根据二阶导数判定函数的凸性==
> 
> 二阶导数<0, 凸函数
> 二阶导数>0, 凹函数
> 二阶导数=0, 可能是拐点
> 一般地，如果曲线在经过点 $(x_0, y_0)$时，曲线的凹凸性改变了，那么就称点 $(x_0, y_0)$ 为这曲线的**拐点**
> 


> [!note]
> 
> ==P148 例1==
> 
>  **判定曲线 $y = \sqrt{x}$ 的凹凸性**
> 
> 解： 一阶导数：
> $\displaystyle y' = (\sqrt{x})' = \frac{1}{2\sqrt{x}}$
> 二阶导数：$\displaystyle y'' = \left( \frac{1}{2\sqrt{x}} \right)' = -\frac{1}{4x^{3/2}}$
> 
> 在函数定义域 $(0, +\infty)$ 内：
> $\displaystyle x > 0 \quad \Rightarrow \quad x^{3/2} > 0 \quad \Rightarrow \quad y'' = -\frac{1}{4x^{3/2}} < 0$
> 
> 当 $y'' < 0$ 时，曲线为**凸的**，则曲线 $y = \sqrt{x}$ 在定义域 $(0, +\infty)$ 内始终为凸曲线


> [!note]
> 
> ==P149 例2==
> 
>  **判定曲线 $y = x^3 - 3x$ 的凹凸性**
> 
> 解： 一阶导数：$\displaystyle y' = 3x^2 - 3$
> 
> 二阶导数：  $\displaystyle y'' = 6x$
> 
>  - 当 $x < 0$：
>    $\displaystyle y'' = 6x < 0 \quad (\text{因为 } x < 0)$ 此时曲线为**凸的**
> 
>  - 当 $x > 0$：
>    $\displaystyle y'' = 6x > 0 \quad (\text{因为 } x > 0)$ 此时曲线为**凹的**

## 导数在人工智能中的应用: 梯度下降法

> [!important]
> 
> ==梯度下降法==
> 
> 想象你在调一台老式收音机，它只有一个旋钮 $ w $ 用来调频道。你转动旋钮时，耳朵会立刻听到声音的变化：有时候，往一个方向轻轻一转，会发现杂音立刻变小了，但也有时候，刚一转动旋钮，嗞嗞的噪声突然变大。整个过程就像是在黑暗中摸索，只能凭耳朵判断该往哪边走，一边转旋钮，一边听声音的变化，一步步靠近那个最清晰的频道。
> 你的目标：找到让声音最清晰的那个旋钮位置。
>
>损失函数：$ L(w) $ 表示：当旋钮在位置$ w $时，收音机的杂音强度是多少。
>- 杂音大 → $L(w)$ 大  
>- 杂音小 → $L(w)$ 小
>  
>我们的目标，就是找到让 $L(w)$ 最小的那个 $w$，也就是杂音最小、声音最清晰的旋钮位置。
>
>![收音机](../media/img/gd_1.png)
>
> **导数的含义**
> 
>如果$\displaystyle L'(w)>0$，说明 $L(w)$ 随 $w$ 增大而增大，所以我们要让 $w$ 变小  
>
>如果$\displaystyle L'(w)<0$，说明 $L(w)$ 随 $w$ 增大而减小，所以我们要让 $w$ 变大  
>
>导数的符号告诉我们当前这一刻旋钮往哪边调，杂音$($损失函数 $L(w))$会增加还是减少，而沿着负导数的方向调旋钮，就能让函数值 $L(w)$ 逐步减小。
>
> **学习率：控制 “转旋钮的幅度**
>
>数学上，用学习率控制幅度，公式是：$\displaystyle w \leftarrow w - \eta \cdot L'(w)$  
>
>- 如果 $\eta$ 太大 → 你猛地把旋钮转过头，直接跨过谷底，来回震荡，甚至跑到更高的山上  
>- 如果 $\eta$ 太小 → 你像用牙签拨旋钮，一次几乎没动，走到谷底需要很久  
>
>![学习率](../media/img/gd_2.png)
>
> **收敛**
>
>在迭代公式:
> $$
> w \leftarrow w - \eta \cdot L'(w)
> $$
>
>当导数很接近 $0$ 时，更新步长会非常小，参数 $w$ 变化几乎停下来，这时我们就找到了让 $L(w)$ 最小的 $w$，参数就收敛到了最优点。
>
> **梯度下降的过程**
>
>- 观察 $L(w)$ 数值变化（计算导数）  
>- 按合适的幅度调节 $w$  
>- 反复进行，直到导数接近 $0$，迭代结束
