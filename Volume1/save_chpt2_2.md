
> [!tip]
> 
>==问题引入==
> 
>给定函数 $y = f(x)$, 确定一条直线, 使其在 $x=x_0$ 点**附近**能"最好"的近似 $f(x)$.

> [!important]
>
> 我们来回答上面的问题. 如图1, 假设待定的直线过点 $(x_0, z_0)$, 斜率为 $k$, 则直线方程为
> 
> $$
> z - z_0 = k(x - x_0).
> $$
> 
> 为了让这条直线在 $x_0$ 附近尽可能的接近 $f(x)$, 我们来分析 $z$ 与 $y = f(x)$ 的
> 
> 分成两步走:
>
> **Step 1**: 确定 $z_0$.
> 
> 直观上看, 这条直线必须经过点 $(x_0, f(x_0))$, 也就是说 $z_0 = f(x_0)$. 这是因为当 $x \to x_0$ 时, 
>
> $$
> \lim_{x \to x_0} z = \lim_{x \to x_0} [z_0 + k(x-x_0)] = z_0.
> $$
> 
> 而
>
> $$
> \lim_{x \to x_0} f(x) = f(x_0).
> $$
>
> 只有当 $z_0=f(x_0)$ 时才能保证上面的两个极限相等.
> 
> **Step 2**: 确定 $k$.
>
> 在 $z_0 = f(x_0)$ 的前提下, 
> 
> $$
> y - z = f(x_0 + \Delta x) - f(x_0) - k \Delta x
> $$
>
> $$
> y - z = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} - k 
> $$
>
> 记 $\Delta x = x- x_0$, $\Delta z = z - z_0$, 代入上式得
> 
> $$
> \Delta z = k \Delta x.
> $$
> 
> 
> 这正是我们在上一章给出的导数的定义. 此时令 $\Delta x \to 0$ 并引入微分记号, 把上式左边的 $\Delta y$ 和 $\Delta x$ 分别替换成 $dy$ 和 $dx$, 就得到
>
> $$\left.\frac{dy}{dx} \right|_{x_0} = f'(x_0).$$
>
> 由此我们得到, 在点 $x=x_0$ 处, $y$ 的微分与 $x$ 的微分的比值等于函数 $f(x)$ 在这一点的导数. 因此我们也经常用记号 $\displaystyle \frac{dy}{dx}$ 或 $\displaystyle \frac{df(x)}{dx}$ 来表示 $f(x)$ 的导数. 
>
> 在 $x_0$ 处, 对 $x_0$ 的值做一个微小的改变, 得到 $x_0 + \Delta x$. 相应的, $y$ 的改变量为
> $$ \Delta y = f(x_0 + \Delta x) - f(x_0).$$
>
> 我们关心的问题是, 在 $\Delta x$ 趋于 0 的过程中, $\Delta y$ 和 $\Delta x$ 之间有没有某种极限关系. 答案是有的, $\Delta y$ 与 $\Delta x$ 的比值的极限
>
> $$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = f'(x_0).$$ 
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
> **微分 (differential)** 的意思是 **无穷小的改变量 (infinitesimally small change)**，莱布尼茨为微分创立了其专属符号 "$d$", 例如 $dx$ 表示变量 $x$ 的微分, $dy$ 表示变量 $y$ 的微分. 与之对应的, 物理上经常用 $\Delta x$ 表示一个很小的改变量，比如一小段位移. 直观上看, $\Delta x$ 和 $dx$ 想传达的意思很相近, 都是**很小的量**, 但是在数学它们是有区别的. 
> 
> - $\Delta x$ 表示一个非常小但**固定的数**.
> 
> - $dx$ 则表示一个"无穷小量", 它不再是一个固定的数, 相当于蕴含了一个 $\Delta x \to 0$ 的**极限过程**.

> [!warning]
> 
> 在后面的学习中, $\Delta x$ 和 $d x$ 我们都会经常碰到, 前者是思维上的具象, 后者是数学上的严格, 双剑合璧, 才能在数学的道路上走得更远.
>


### 高阶无穷小
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

<table>
  <tr>
    <th rowspan="2">Δt (s)</th>
    <th colspan="3">匀速运动 (m)</th>
    <th colspan="3">匀加速运动 (m)</th>
  </tr>
  <tr>
    <th>真实 Δs</th>
    <th>微分预测 v Δt</th>
    <th>差值</th>
    <th>真实 Δs</th>
    <th>微分预测 a Δt</th>
    <th>差值</th>
  </tr>
  <tr>
    <td>0.1</td>
    <td>0.2</td>
    <td>0.2</td>
    <td>0.0</td>
    <td>0.21</td>
    <td>0.2</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.01</td>
    <td>0.02</td>
    <td>0.02</td>
    <td>0.0</td>
    <td>0.0201</td>
    <td>0.02</td>
    <td>0.0001</td>
  </tr>
  <tr>
    <td>0.001</td>
    <td>0.002</td>
    <td>0.002</td>
    <td>0.0</td>
    <td>0.002001</td>
    <td>0.002</td>
    <td>0.000001</td>
  </tr>
  <tr>
    <td>0.0001</td>
    <td>0.0002</td>
    <td>0.0002</td>
    <td>0.0</td>
    <td>0.00020001</td>
    <td>0.0002</td>
    <td>0.00000001</td>
  </tr>
</table>


<table border="1" style="border-collapse: collapse; width: 100%;"> <tr> <th rowspan="2">Δθ (弧度)</th> <th colspan="3">横坐标 x 的变化</th> <th colspan="3">飞行距离 l 的变化</th> </tr> <tr> <th>真实 Δx (米)</th> <th>微分预测 dx (米)</th> <th>差值 (米)</th> <th>真实 Δl (米)</th> <th>微分预测 dl (米)</th> <th>差值 (米)</th> </tr> <tr> <td>0.1</td> <td>-0.234</td> <td>-0.200</td> <td>0.034</td> <td>-0.165</td> <td>-0.141</td> <td>0.024</td> </tr> <tr> <td>0.01</td> <td>-0.0201</td> <td>-0.0200</td> <td>0.0001</td> <td>-0.0142</td> <td>-0.0141</td> <td>0.0001</td> </tr> <tr> <td>0.001</td> <td>-0.002000</td> <td>-0.002000</td> <td>0.000000</td> <td>-0.001414</td> <td>-0.001414</td> <td>0.000000</td> </tr> <tr> <td>0.0001</td> <td>-0.000200</td> <td>-0.000200</td> <td>0.000000</td> <td>-0.000141</td> <td>-0.000141</td> <td>0.000000</td> </tr> </table>

<table border="1" style="border-collapse: collapse; width: 100%;"> <tr> <th rowspan="2">Δθ (弧度)</th> <th colspan="3">横坐标 x 的变化</th> <th colspan="3">飞行距离 l 的变化</th> </tr> <tr> <th>真实 Δx (米)</th> <th>微分预测 dx (米)</th> <th>差值 (米)</th> <th>真实 Δl (米)</th> <th>微分预测 dl (米)</th> <th>差值 (米)</th> </tr> <tr> <td>0.1</td> <td>-0.383</td> <td>-0.300</td> <td>0.083</td> <td>-0.200</td> <td>-0.173</td> <td>0.027</td> </tr> <tr> <td>0.01</td> <td>-0.0303</td> <td>-0.0300</td> <td>0.0003</td> <td>-0.0174</td> <td>-0.0173</td> <td>0.0001</td> </tr> <tr> <td>0.001</td> <td>-0.003003</td> <td>-0.003000</td> <td>0.000003</td> <td>-0.001732</td> <td>-0.001732</td> <td>0.000000</td> </tr> <tr> <td>0.0001</td> <td>-0.000300</td> <td>-0.000300</td> <td>0.000000</td> <td>-0.000173</td> <td>-0.000173</td> <td>0.000000</td> </tr> </table>


<table border="1" style="border-collapse: collapse; width: 100%;"> <tr> <th rowspan="2">Δθ (弧度)</th> <th colspan="3">横坐标 x 的变化</th> <th colspan="3">飞行距离 l 的变化</th> </tr> <tr> <th>真实 Δx (米)</th> <th>微分预测 dx (米)</th> <th>差值 (米)</th> <th>真实 Δl (米)</th> <th>微分预测 dl (米)</th> <th>差值 (米)</th> </tr> <tr> <td>0.1</td> <td>-0.383</td> <td>-0.300</td> <td>0.083</td> <td>-0.200</td> <td>-0.173</td> <td>0.027</td> </tr> <tr> <td>0.05</td> <td>-0.184</td> <td>-0.150</td> <td>0.034</td> <td>-0.098</td> <td>-0.087</td> <td>0.011</td> </tr> <tr> <td>0.01</td> <td>-0.0303</td> <td>-0.0300</td> <td>0.0003</td> <td>-0.0174</td> <td>-0.0173</td> <td>0.0001</td> </tr> <tr> <td>0.005</td> <td>-0.0151</td> <td>-0.0150</td> <td>0.0001</td> <td>-0.00867</td> <td>-0.00866</td> <td>0.00001</td> </tr> </table>