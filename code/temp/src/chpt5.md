# 第五回: 投桃报李(下) --- 多元微分

# 向量与空间解析几何

> [!TIP]
>
> ==为什么要学习向量?==
>
> - 向量是一元变量的推广
>
> 例如我们在C++里可以进行运算 。
>
> ```
> a = 3，
> b = 2 
> c = a + b
> ```
> 得到 $c = 5$
>
> 而在 Python 中可以直接进行向量运算
> ```
> a = [1, 3]
> b = [2, 1]
> c = a + b
> ```
> 得到 $\mathbf{c} = [3, 4]$. 
>
> - 向量在很多实际问题需要用到
> 
> 向量是神经网络里的基本操作对象. 一张图片可以看成一个向量, 例如一个 28x28 分辨率的手写数字图片8, 可以看成是一个28x28=784维的向量. 一段文字也可以看成是一个向量, 把文字映射成向量也叫做**word embedding**, 这是一个非常有趣的问题.

## 向量

### 向量的概念

> [!important]
> 
> ==什么是向量?==
> 
> 向量可以从**数**和**形**两个方面去理解.
> 
> ---
> > ==向量的**数**属性==
> > 
> > 向量就是一串有序的数字 $\mathbf{x} = [x_1, x_2, \cdots, x_n]$. $n$ 称为向量的**维数**,  $x_i, i=1, \cdots, n$ 叫做向量 $\mathbf{x}$ 的**分量**. 分量 $x_i$ 可以属于实数集, 也可以属于复数集. 如不加说明, 本课程中所考虑的向量的分量均为实数, 所有的 $n$ 维实数向量构成的集合记作 $\mathbb{R}^n$. 
> 
> > ==向量的**形**属性==
> > 
> > 向量也可以看成是一个箭头, 既有长度, 又有方向. 例如 $\mathbb{R}^2$ 中的向量 $[2, 3]$ 可以看成是二维直角坐标系下从点 $(0, 0)$ 指向点 $(2, 3)$ 的一个箭头. 高维向量 $\mathbf{x} \in \mathbb{R}^n$ 也可以看作是一个箭头, 它是一个高维直角坐标系下中从坐标原点指向点 $[x_1, x_2, \cdots, x_n]$ 的箭头.
> 
> ![向量](media/img/vector.png#200pt)

> [!warning]
> ==向量相等==
> 两个向量相等当且仅当其**对应分量分别相等**.

### 向量与集合

> [!TIP]
> 
> **集合**是本课程所介绍的第一个概念. 将集合的观点运用到向量中既能帮助我们加深对集合的理解, 也能让我们更全面的认识向量.

> [!note]
>
> ==集合与映射的几个例子==
>
> - 闭区间 $[a, b]$ 上的所有连续函数构成一个集合, 记作 $C[a, b]$.
> - 闭区间 $[a, b]$ 上的所有可导的函数构成一个集合, 记作 $C^1[a, b]$.
> - 闭区间 $[a, b]$ 上的所有二阶可导的函数构成一个集合, 记作 $C^2[a, b]$.
> - $$C^2[a, b] \subset C^1[a, b] \subset C[a, b]$$
> - 求导是一个映射, 它把集合 $C^1[a, b]$ 中的元素 (例如 $f(x) = x^2$) 映射到  $C[a, b]$ 中的元素 (例如 $f(x) = 2x$ ). 
> - 关于函数求导, 大家可以再看看这个例子:
> $$
> f(x) = \left\{ \begin{matrix}
>   x^2, &  x<0& \\
>   0, &  x\ge0
>  \end{matrix}\right.
> $$
> 请问 $f(x)$, $f'(x)$, $f''(x)$ 分别属于哪个集合?
> - 积分是一个映射, 它把 $C[-\infty, \infty]$ 中的函数 $f(x)$ 映射到一个数 $\displaystyle \int_a^b f(x)dx$.
> - 不定积分**不是**一个映射, 因为它不满足唯一对映的性质 (一个原函数加上任何常数 C 还是原函数).
> - 变上限积分是一个映射, 在给定被积函数 $f(x)$ 后, 变上限积分把实数 $x$ 映到数 $\displaystyle F(x) = \int_a^x f(s)ds$, 所以变上限积分同时还是一个函数.
> - 微分方程的解构成一个集合, 称为该微分方程的**解集**, 这个集合中的元素为满足该方程的函数. 微分方程的解集可以是空集(方程无解), 包含一个元素(唯一解)或包含多个元素(多解). 例如满足微分方程 
> $$
> \frac{dy}{dx} = 2y
> $$
> 的解为
> $$
> f(x) = C\mathrm{e}^{2x}.
> $$
> $C$ 可以任意取值, 所以方程的解集包含无穷多个元素. 但是如果我们在原方程基础上加上**定解条件** $y(0) = 1$, 则可以确定 $C=1$, 从而方程的解集包含唯一一个元素 $f(x) = \mathrm{e}^{2x}$.

> [!important]
> 
> ==集合观点看向量==
> 
> 所有的  $n$ 维实数向量构成一个集合, 记作 $\mathbb{R}^n$. 通过刚才对向量数和形属性的介绍, 我们还知道所有的 $n$ 维实数向量都对映 $n$ 维直角坐标系下的一个点, 反过来,  $n$ 维直角坐标系下的任意一个点也都能对映到一个$n$ 维向量, 所以集合 $\mathbb{R}^n$ 与 $n$ 维直角坐标系所描述的空间(也叫做 $n$ 维**欧氏空间**, 常简称 $n$ 维空间) 之间存在一一对映的关系. 
> 
> 进一步, 如果我们把直角坐标系下的每个点 $A$ 对映到一个箭头, 这个箭头的起点是原点, 终点是点 $A$, 那么**所有的点所构成的集合**和**所有的从原点出发的箭头**所构成的集合是一一对映的, 从而每个向量都可以用(从原点出发的)箭头表示.
> 
> 需要注意, 如果箭头不是以原点为起点的, 我们总可以通过平移把这个箭头的起点挪到原点, 从这个意义上讲, 通过平移之后能够完全重合的两个箭头是彼此**等价**的, 对映**同一个向量**, 这就是物理中所谓的**向量的平移不变性**.


### 向量的运算

> [!TIP]
> 我们在研究集合的时候, 首先要搞清楚**集合内部元素的性质**. 所以我们先来看 $\mathbb{R}^n$ 内部元素的运算, 主要是**加法**和**数乘**两类运算.
>  

> [!warning]
> 
> 首先我们统一一下记号. 原则上, $\mathbb{R}^n$ 空间中的向量 $\mathbf{x}$ 可以横着写: 
> 
> $$
> \mathbf{x} = (x_1, x_2, \cdots, x_n)
> $$
> 也可以竖着写
> $$
> \mathbf{x} = \left(\begin{matrix}
> x_1 \\
> x_2 \\
> \vdots \\
> x_n \end{matrix}
> \right)
> $$
> 
> 一下我们规定所有的向量都采用竖着写的形式. 所以当我们说 $\mathbf{x}$ 时, 指的是 $\displaystyle \left(\begin{matrix} x_1 \\ x_2 \\ \vdots \\  x_n \end{matrix} \right)$, 为了节省空间, 我们可以把上述向量写成  $(x_1, x_2, \cdots, x_n)^T$, 这里的 T 不是躺平的躺的意思, 而是 **转置** (Transform).
> 
> 下面我们以二维平面 $\mathbb{R}^2$ 为例来介绍向量运算.
> 

> [!important]
>
> ==向量的加法==
>
> ---
> > ==数属性下的加法==
> > 向量 $\mathbf{u} = (2, 3)^T$ 与向量  $\mathbf{v} = (1, 4)^T$ 之间的加法定义为**对映分量元素之间的和**, 即
> > $$
> > \mathbf{u} + \mathbf{v} = (2+1, 3+4)^T = (3, 7)^T.
> > $$
>
> > ==形属性下的加法==
> > 向量 $\mathbf{u} = (2, 3)^T$ 与向量  $\mathbf{v} = (1, 4)^T$ 之间的加法还可以看成两个向量对映箭头首尾相接后形成的从起点到终点的新箭头.

> [!important]
>
> ==向量的数乘==
> 
> ---
> > ==数属性下的数乘==
> > 向量 $\mathbf{u} = (2, 3)^T$ 与实数  $k$ 之间的数乘定义为**$k$乘到向量$\mathbf{u}$的每一个分量上**, 即
> > $$
> > k\mathbf{u} = (2k, 3k)^T.
> > $$
> >
> > ==形属性下的数乘==
> > 向量 $\mathbf{u}$ 与实数  $k$ 之间的数乘可以看成保持向量 $\mathbf{u}$ 的方向不变, 将其长度变为原来的 $k$ 倍.

> [!warning]
> 向量的**减法**可以通过**加法**和**数乘**表示:
> $$
> \mathbf{u}-\mathbf{v}=\mathbf{u}+(-1)*\mathbf{v}
> $$
> 
> **向量没有除法!**

> [!note]
> 
> ==向量加法的性质==
>  
> 
> **交换律（Commutative Law）**
> 
> 对于任意向量 $\mathbf{a}$ 和 $\mathbf{b}$，有  
> $$
> \mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a}.  
> $$
> **几何解释**：  
> **平行四边形法则**：以 $\mathbf{a}$ 和 $\mathbf{b}$ 为邻边作平行四边形，对角线即为和向量。无论先画 $\mathbf{a}$ 还是 $\mathbf{b}$，对角线方向与长度均不变。  
>  
> **代数验证**（以二维向量为例）：  
> 设 $\mathbf{a} = (a_1, a_2)$，$\mathbf{b} = (b_1, b_2)$，则  
> $$
> \mathbf{a} + \mathbf{b} = (a_1 + b_1, a_2 + b_2) = (b_1 + a_1, b_2 + a_2) = \mathbf{b} + \mathbf{a}.  
> $$
>  
> **示例**：  
> 若 $\mathbf{a} = (2, 3)$，$\mathbf{b} = (-1, 4)$，则  
> $$
> \mathbf{a} + \mathbf{b} = (2 + (-1), 3 + 4) = (1, 7), \\  
> \mathbf{b} + \mathbf{a} = (-1 + 2, 4 + 3) = (1, 7).  
> $$
>  
> **结合律(Associative Law)**
> 
> 对于任意向量 $\mathbf{a}$、$\mathbf{b}$ 和 $\mathbf{c}$，有  
> $$
> (\mathbf{a} + \mathbf{b}) + \mathbf{c} = \mathbf{a} + (\mathbf{b} + \mathbf{c}).  
> $$
> **几何解释**：  
> 使用**三角形法则**或**多边形法则**时，无论先加前两个向量还是后两个向量，最终的和向量始终从第一个向量的起点指向最后一个向量的终点。  
> 例如，将 $\mathbf{a}$、$\mathbf{b}$、$\mathbf{c}$ 首尾相接，无论先组合 $\mathbf{a} + \mathbf{b}$ 还是 $\mathbf{b} + \mathbf{c}$，最终路径的起点和终点一致。  
>  
> **代数验证**（以三维向量为例）：  
> 设 $\mathbf{a} = (a_1, a_2, a_3)$，$\mathbf{b} = (b_1, b_2, b_3)$，$\mathbf{c} = (c_1, c_2, c_3)$，则  
> $$
> (\mathbf{a} + \mathbf{b}) + \mathbf{c} = (a_1 + b_1 + c_1, a_2 + b_2 + c_2, a_3 + b_3 + c_3), \\  
> \mathbf{a} + (\mathbf{b} + \mathbf{c}) = (a_1 + b_1 + c_1, a_2 + b_2 + c_2, a_3 + b_3 + c_3).  
> $$
> 两者结果相同。  
>  
> **示例**：  
> 若 $\mathbf{a} = (1, 0)$，$\mathbf{b} = (2, -1)$，$\mathbf{c} = (-3, 4)$，则  
> $$
> (\mathbf{a} + \mathbf{b}) + \mathbf{c} = (3, -1) + (-3, 4) = (0, 3), \\  
> \mathbf{a} + (\mathbf{b} + \mathbf{c}) = (1, 0) + (-1, 3) = (0, 3).
> $$
>

> [!note]
> 
> ==数乘运算的性质==
>  
> **结合律**
> 对任意标量 $\alpha, \beta$ 和向量 $\mathbf{v}$，有  
> $$
> (\alpha \beta) \mathbf{v} = \alpha (\beta \mathbf{v}).  
> $$
> **几何解释**：  
> 标量乘法表示向量的伸缩变换。先以 $\beta$ 缩放 $\mathbf{v}$，再以 $\alpha$ 缩放结果，等价于直接以 $\alpha \beta$ 缩放原向量 $\mathbf{v}$。  
>  
> **代数验证**（以三维向量为例）：  
> 设 $\mathbf{v} = (v_1, v_2, v_3)$，则  
> $$
> (\alpha \beta) \mathbf{v} = (\alpha \beta v_1, \alpha \beta v_2, \alpha \beta v_3) = \alpha (\beta v_1, \beta v_2, \beta v_3) = \alpha (\beta \mathbf{v}).  
> $$
>  
> **示例**：  
> 若 $\alpha = 2$，$\beta = 3$，$\mathbf{v} = (1, -1, 4)$，则  
> $$
> (2 \times 3) \mathbf{v} = 6 \times (1, -1, 4) = (6, -6, 24), \\  
> 2 \times (3 \mathbf{v}) = 2 \times (3, -3, 12) = (6, -6, 24).  
> $$
>  
> **分配律**
> 对任意标量 $\alpha$ 和向量 $\mathbf{u}, \mathbf{v}$，有  
> $$
> \alpha (\mathbf{u} + \mathbf{v}) = \alpha \mathbf{u} + \alpha \mathbf{v}.  
> $$
> **几何解释**：  
> - 若向量 $\mathbf{u}$ 和 $\mathbf{v}$ 构成三角形的两边，标量 $\alpha$ 缩放后的向量和仍保持三角形结构，但整体长度按 $\alpha$ 比例缩放。  
>  
> **代数验证**（以二维向量为例）：  
> 设 $\mathbf{u} = (u_1, u_2)$，$\mathbf{v} = (v_1, v_2)$，则  
> $$
> \alpha (\mathbf{u} + \mathbf{v}) = \alpha (u_1 + v_1, u_2 + v_2) = (\alpha u_1 + \alpha v_1, \alpha u_2 + \alpha v_2) = \alpha \mathbf{u} + \alpha \mathbf{v}.  
> $$
>  
> **示例**：  
> 若 $\alpha = 3$，$\mathbf{u} = (2, 1)$，$\mathbf{v} = (-1, 4)$，则  
> $$
> 3 \times \left( (2, 1) + (-1, 4) \right) = 3 \times (1, 5) = (3, 15), \\  
> 3 \times (2, 1) + 3 \times (-1, 4) = (6, 3) + (-3, 12) = (3, 15).
> $$
>

### 向量空间
> [!tip]
> 
> 数学里面有很多**空间**, 比如欧几里得空间, 希尔伯特空间(完备的线性赋范空间), 黎曼空间(具有黎曼度量的微分流形), 卡拉比-丘空间(紧致的复的凯勒的流形, 具有里奇平坦的度量)等等. 空间本质上其实就是一个**集合**, 但不是所有的集合都能叫做空间(不是所有的牛奶都叫特仑苏). 能够称之为空间的集合往往都有一些比较好的性质. $\mathbb{R}^n$ 中的所有向量所构成的集合是一个空间, 叫做**$n$ 维向量空间**, 也叫做欧几里得空间. 这个空间有很好的性质(想想<你的名字>里黄昏时的情景, 那个就不是一个好空间).

> [!Important]
> 
> ==向量空间==
> 
> $\mathbb{R}^n$ 中的所有向量所构成的集合是一个空间, 叫做**$n$ 维向量空间**, 也叫做欧几里得空间.
> 
> 这个空间最重要的性质是: **空间中的元素对加法和数乘封闭**. 也就是说, $\mathbb{R}^n$ 中两个向量的和还是 $\mathbb{R}^n$ 中的向量, 任意实数 $k$ 数乘一个向量也还在 $\mathbb{R}^n$ 中, 哪怕 $k=0$, 此时得到的是一个维数跟 $\mathbf{u}$ 相同的0向量(元素皆为0). 零向量不等于数字0.
> 
> 从计算机编程的角度看, **封闭性**的一个最大好处是不用每次执行运算后判断结果是不是还在这个空间里.
> 
> 向量空间的另一个重要性质是:  任给 $\mathbb{R}^n$ 中的两个向量 $\mathbf{u}$, $\mathbf{v}$,它们之间可以定义**距离**:
> $$
> d(\mathbf{u}, \mathbf{v}) = \sqrt{ (u_1 - v_1)^2 + (u_2 - v_2)^2 + \cdots + (u_n - v_n)^2}
> $$
> 
> 上述距离也称为**欧氏距离**, 正是在欧氏距离的规整下, 所有的向量构成了所谓的欧氏空间.

### 内积
> [!tip]
> 
> 两个向量除了可以计算距离外, 还可以计算角度, 进而能够刻画两个向量的平行与垂直(正交)关系, 让**向量空间**有了更好的性质.
> 

> [!important]
>
> ==向量的内积==
> 
> ---
> > ==数属性下的内积==
> > 向量 $\mathbf{u} = (u_1, u_2)^T$ 与向量  $\mathbf{v} = (v_1, v_2)^T$ 之间的内积定义为**对映分量乘积的和**, 即
> > $$
> > \mathbf{u} \cdot \mathbf{v} = u_1v_1+ u_2v_2.
> > $$
>
> > ==形属性下的内积==
> > 向量 $\mathbf{u}$ 与向量  $\mathbf{v}$ 的内积其中一个向量 $\mathbf{u}$ 在另一个向量 $\mathbf{v}$ 的方向上**投影**的长度(带符号)乘以向量 $\mathbf{v}$ 本身的长度. 也可以写成: 
> > $$
> > \mathbf{u} \cdot \mathbf{v} = |u| |v| \cos(\theta),
> > $$
> > 其中 $\theta$ 为 $\mathbf{u}$ 和  $\mathbf{v}$ 所对应的两个箭头之间的夹角.

> [!note]
> 
> 内积的概念非常重要, 下面我们通过几个例子来加深对内积的认识. 
>
> ---
> > $\mathbf{u} = (2, 3)^T$, $\mathbf{v} = (1, 4)^T$, 则 $\mathbf{u}\cdot \mathbf{v}=2*1 + 3*4=14$.
> 
> > $\mathbf{u} = (1, 2, -1)^T$, $\mathbf{v} = (-3, 2, 9)^T$, 则 $\mathbf{u}\cdot \mathbf{v}=1*(-3) + 2*2+(-1)*9=-8$.

> [!warning]
> 
> 注意, 两个向量的内积是一个实数, 因此内积运算在向量空间中不具有封闭性. **内积 (inner product)** 也叫做**点乘 (dot product)** 和**数量积 (scalar product)**. 

> [!important]
> 
> ==内积的性质==
> 
> > ==内积的交换律==
> > $$
> > \mathbf{u}\cdot \mathbf{v} = \mathbf{v}\cdot \mathbf{u}
> > $$
> > 
>
> > ==内积与向量加法的结合律==
> > $$
> > \mathbf{u}\cdot (k_1\mathbf{v}+k_2\mathbf{w}) = k1\mathbf{u}\cdot \mathbf{v}+k2\mathbf{u}\cdot \mathbf{w}
> > $$
> > 
>
> > ==内积与向量长度==
> > $$
> > \mathbf{u}\cdot \mathbf{u} = u_1^2+u^2=|u|^2.
> > $$
> > 
> > $|u|$ 也称为向量的**模**, 模长等于1的向量称为**单位向量**. 任给向量 $\mathbf{u}$, 新的向量 $\mathbf{u}/|u|$ 与原向量 $\mathbf{u}$ 方向相同, 模长为1, 这个过程称为向量的**归一化**.
>
> > ==内积与角度==
> > $$
> > \cos \theta=\frac{\mathbf{u}\cdot \mathbf{v}}{|u| |v|}.
> > $$
> > 
> 
> > ==内积与垂直==
> > 
> > 在上式中, 当 $\mathbf{u}\cdot \mathbf{v}$ 等于0时, $\cos\theta=0$, 表明两个向量**垂直**, 也叫做**正交**(orthogonal) 
> >
> > **定理**：若两个向量 $\mathbf{a}, \mathbf{b}$ 的内积为零，则这两个向量垂直. 即 $\mathbf{u } \perp  \mathbf{v} \iff \mathbf{u }  \cdot \mathbf{v} =0$.
> >
> > 我们以二维向量为例来说明这个定理的含义。如图所示，设向量 $\mathbf{a }=(a_{1} ,a_{2} )$，$\mathbf{b }=(b_{1} ,b_{2} )$, 向量 $\mathbf{c }=\mathbf{a }-\mathbf{b }=(a_{1}-b_{1} ,a_{2}- b_{2})$。根据向量模长的定义，
> > $$
> > \begin{align*}
> > \left | \mathbf{a}  \right |^{2}   &=a_{1}^{2}  +a_{2}^{2} \\
> > \left | \mathbf{b }  \right |^{2}  &=b_{1}^{2}  +b_{2}^{2}\\
> > \left | \mathbf{c}  \right |^{2}  &=(a_{1}-b_{1})^{2}  +(a_{2}-b_{2})^{2} \\
> > & = a_{1}^{2}  +a_{2}^{2} + b_{1}^{2}  +b_{2}^{2} - 2(a_1b_1 + a_2b_2)
> > \end{align*}
> > $$
> > 若 $\mathbf{a } \cdot \mathbf{b }=0$，即 $a_{1}b_{1}+ a_{2}b_{2}=0$, 则 
> > $$
> > \left | \mathbf{a }   \right | ^{2}+\left | \mathbf{b }   \right | ^{2}=\left | \mathbf{c }   \right | ^{2}
> > $$
> > 满足勾股定理，因此 $\mathbf{a }\perp  \mathbf{b}$。反过来，若向量 $\mathbf{a}\perp  \mathbf{b}$，则根据勾股定理公式（2）成立，此时 $a_{1}b_{1}+ a_{2}b_{2}=0$，因此这两个向量的内积为零。证毕。
> > 
> > **注意: 通过内积为0来判断两个向量正交的做法在高维情形同样适用.**
> 
> > ==内积与投影==
> > 
> > 内积与投影有着密切的联系. 
> > 
> > 一个向量  $\mathbf{u}$ 在另一个 $\mathbf{v}$ 所在方向上的投影还是一个向量, 该向量的模长等于 $\mathbf{u}$ 与单位向量 $\mathbf{v}/|v|$ 的内积, 方向与$\mathbf{v}$ 一致.
> > 
> > 投影的过程相当于将 $\mathbf{u}$ 分解成两部分的和, $\mathbf{u} = \mathbf{u}_1 + \mathbf{u}_2$. 其中 $\mathbf{u}_1$ 与 $\mathbf{v}$ 平行, $\mathbf{u}_2$ 与 $\mathbf{v}$ 垂直, 此时 $\mathbf{u}_2$ 的模长是所有分解中最小的. 
> > 
> > 向量在平面上的投影可以用类似的观点来理解.
> > 

> [!warning]
> 
> **内积**是向量空间中非常重要的一种运算, 在机器学习, 量子力学, 线性代数和泛函分析都有非常重要和广泛的应用. 


## 直线和平面

> [!tip]
> 
> 直线和平面可以看作是空间中一些特殊的点构成的集合. 在数学上可以用不同的方法来描述这些集合中的点. 向量语言是其中的一种方法.
> 

### 二维空间中的直线

> [!important]
> 
> 以二维平面上的直线为例, 我们知道所有满足方程 $y = kx + b$ 的点 $(x, y)$ 构成了一条直线, 这条直线的斜率为 $k$, 截距为 $b$, 反过来看, 给定了斜率 $k$ 和截距 $b$, 我们可以通过方程 $y = kx + b$ 来描述所有集合(直线)中的点.
> 
> 通过向量我们可以用另一种方式描述直线. 任意给定一个二维平面中的向量 $\mathbf{u}$, 所有满足 $\mathbf{v}\cdot \mathbf{u} = |u|^2$ 的向量 $\mathbf{v}$ 所对应的点都位于一条与向量 $\mathbf{u}$ 垂直, 且与原点的距离为 $\mathbf{u}$ 的直线上. 因此 $\mathbf{v}\cdot \mathbf{u} = |u|^2$ 也描述了一条直线, 这是通过向量运算给出直线方程的方法.
> 
> 反过来, 如果给定直线的**法向** $\mathbf{n}$, 其中$\mathbf{n}$ 为单位向量, 另外再给定有向距离 $b$ ($b$ 可以小于0), 则
> 
> $$
> \mathbf{v} \cdot \mathbf{n} = b
> $$
> 
> 描述了一条与 $\mathbf{n}$ 垂直, 且与原点的距离为 $b$ ($b<0$ 表示直线相对原点的位置与 $\mathbf{n}$ 的指向相反) 的直线.
> 
> 进一步, 假定 $\mathbf{v} = (x, y)^{T}$, 则在坐标形式下上式可以写为
> 
> $$
> n_1 x + n_2 y = b.
> $$
> 
> 而这正是一个直线方程.
> 

> [!note]
> 
> [直线的例子]

> [!tip]
> 
> 向量观点下的直线跟我们中学学过的坐标形式下的直线本质上是完全一样的, 只不过通过向量观点丰富了我们对直线的理解, 而且在一些问题中, 向量观点往往更加直观和简洁. 下面我们来看几个例子.
> 

> [!important]
> 
> ==直线方程的一般形式==
> 
> 我们中学学过, 二维平面中直线的一般形式可以写成 
> $$
> Ax + By + C = 0.
> $$
> 
> 在向量观点下, 我们可以把 $(A, B)^T$ 看成是一个向量, 将其归一化得到向量 $\mathbf{n} = \left( \frac{A}{\sqrt{A^2 + B^2}}, \frac{B}{\sqrt{A^2 + B^2}}\right)^T$, 同时定义 $b = -\frac{C}{\sqrt{A^2 + B^2}}$, 则该方程描述了一条与向量 $\mathbf{n}$ 垂直, 且距离原点的有向距离为 $b$ 的直线.
> 

> ==点到直线的距离==
> 
> 我们中学学过, 二维平面中任意一点 $(x_0,y_0)$ 到直线 $Ax + By + C = 0$ 的距离可以写成
> $$
> d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}
> $$
> 
> 这个结论如何证明呢?
> 
> 可以用传统的解析几何的方法, 先写出过点 $(x_0, y_0)$ 垂直于给定直线的直线方程, 然后求两条直线的交点, 最后求点 $(x_0, y_0)$ 到该交点的距离.
> 
> 在向量观点下, 我们可以计算向量 $\mathbf{v} = (x_0, y_0)^T$ 在单位向量 $\mathbf{n} = \left( \frac{A}{\sqrt{A^2 + B^2}}, \frac{B}{\sqrt{A^2 + B^2}}\right)^T$ 方向上的投影, 即 $p =  \frac{Ax_0}{\sqrt{A^2 + B^2}} + \frac{By_0}{\sqrt{A^2 + B^2}}$. $p$ 与 $b$ 的差的绝对值 $|p-b|$ 即为该点到直线的距离. 可以得到 
> $$
> |p-b| = | \frac{Ax_0 + By_0 + C}{\sqrt{A^2 + B^2}}|
> $$
> 与前面解方程得到的方法结果一样.
> 

### 三维空间中的平面

> [!tip]
> 三维空间中的平面跟二维空间中的平面在数学地位上是对等的.
> 

> [!important]
>
> 类似于二维空间中直线的描述, 三维空间中, 给定**法向量** $\mathbf{n}$ 和有向距离 $b$, 所有在 $\mathbf{n}$ 上投影长度为 $b$ 的向量 $\mathbf{v}$ 构成一个平面.
> 
> 设 $\mathbf{v = (x, y, z)^T}$, $\mathbf{n} = (A, B, C)^T$, 则方程 $A x + B y + C z = b \sqrt{A^2 + B^2 + C^2}$ 成立. 再令 $D = -b \sqrt{A^2 + B^2 + C^2}$, 得到平面方程为:
> 
> $$
> A x + B y + C z + D =0.
> $$
> 
> 这正是三维空间中平面方程的标准形式. 从方程中我们也可以看出, 向量 $(A, B, C)^T$ 所在的方向就是平面的法方向.
> 

> [!note]
>
> ==点到平面的距离==
> 
> 三维空间中的点 $(x_0, y_0, z_0)$ 到平面 $A x + B y + C z + D =0$ 的距离的求法和二维平面中点到直线的距离求法类似. 最后可以得到:
> 
> $$
> d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}.
> $$
> 

> [!important]
> 
> ==三维空间中的直线==
> 
> 三维空间中的直线可以看成是两个平面的交集. 也就是说, 方程组
> 
> $$
> A_1x + B_1 y + C_1 z + D_1 = 0, \\
> A_1x + B_1 y + C_1 z + D_1 = 0.
> $$
>
> 联立得到的解就是一条直线.

### 高维空间中的平面

> [!tip]
> 
> $a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b$, 是不是看起来很熟悉?

### 向量的叉乘

> [!important]
> 
> 参见课本P17-19.

### 几道习题讲解

> [!Note]
> 
> 课本P30-34例1-例6 (例7原则上不做要求).


## 曲面
> [!tip]
> 
> 前面的向量空间为下一章的多元微积分搭建了舞台, 接下来我们在这个舞台上增加一些道具, 用以作为多元微积分的研究对象.
> 

> [!important]
> 
> 一般来说, 对于定义在 $\mathbb{R}^n$ 上的多元函数 $F(x_1, x_2, \cdots, x_n)$, 方程
> $$
> F(x_1, x_2, \cdots, x_n) = 0
> $$
> 
> 的解集对应着 $\mathbb{R}^n$ 空间中的一些点所构成的集合. 当 $F$ 具有某种**连续性**的时候 (注意多元函数的连续性我们现在还没有介绍), 这个点集也会具有某种连续性, 就像空间中的一块或多块布一样, 因此我们可以称其为**曲面**. 
> 
> 下面我们以二维和三维空间为例来介绍一些常用的曲面.
> 
> **一次曲面**
> 
> 前面我们讲了三维空间中的平面方程的一般形式为
> $$
> F(x, y, z) = Ax + By + Cz + D = 0
> $$
> 注意到函数 $F$ 关于所有变量 $x, y, z$ 最高都是一次的, 因此我们也把平面称为**一次曲面**, 在二维空间中它就是我们中学所熟知的**直线**.
> 
> **二次曲面**
> 
> 在中学我们还学过二维空间中的抛物线, 如 $y = x^2$, 它关于 $x$ 是二次的. 我们还学过抛物线和椭圆, 如 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, 它关于 $x, y$ 也是二次的. 在三维空间我们也类似有这样的二次曲面, 其一般形式为
> $$
> F(x, y, z) = Ax^2 + By^2 + Cz^2 + Dxy + Eyz + Fxz + Gx + Hy + Iz + J = 0
> $$
> $F$ 关于变量 $x, y, z$ 的最高阶都是二次的, 我们上述方程所对应的平面称为**二次曲面**.
> 

> [!note]
> 
> 我们来看几个二次曲面的例子.
> 
> **1. 球面 (Sphere)**   
>   $$
>   (x-a)^2 + (y-b)^2 + (z-c)^2 = r^2  
>   $$
>
> **2. 椭球面 (Ellipsoid)**    
>   $$
>   \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
>   $$
>  
> - **3. 圆柱面 ( Cylinder)**：  
>   $$
>   x^2 + y^2 = r^2
>   $$
>  

> [!note]
> 
> ==旋转曲面==
> 
> 旋转曲面是由平面曲线绕某一固定轴旋转生成的曲面，具有轴对称性。其方程可通过原曲线方程的坐标变换推导：  
> - **生成方法**：若平面曲线在 $xz$ 平面上由方程 $f(x, z) = 0$ 定义，绕 $z$ 轴旋转时，将原方程中的 $x$ 替换为 $\sqrt{x^2 + y^2}$，得到旋转曲面方程：  
>   $$
>   f\left(\sqrt{x^2 + y^2}, z\right) = 0.  
>   $$
>  
> **例1：旋转抛物面**  
> - **原曲线**：抛物线 $z = ax^2$（在 $xz$ 平面内，开口向上）。  
> - **旋转轴**：绕 $z$ 轴旋转。  
> - **曲面方程**：  
>   $$
>   z = a(x^2 + y^2).  
>   $$
> - **图像特点**：碗状曲面，开口方向由系数 $a$ 的符号决定（$a > 0$ 时开口向上）。  
> - **应用**：卫星天线、太阳能聚光器（平行光线反射至焦点）。  
>  
> **例2：圆锥面**  
> - **原曲线**：直线 $z = kx$（在 $xz$ 平面内，过原点，斜率为 $k$）。  
> - **旋转轴**：绕 $z$ 轴旋转。  
> - **曲面方程**：  
>   $$
>   z^2 = k^2(x^2 + y^2).  
>   $$
> - **图像特点**：双锥面，顶点在原点，半顶角 $\theta$ 满足 $\tan\theta = k$。  
> - **应用**：锥形齿轮、光学棱镜、建筑尖顶。  

## 曲线
> [!tip]
> 
> 二维空间中的两条直线相交得到一个点, 三维空间中的两个平面相交得到一条直线, 这是曲线的两个简单实例.
> 

> [!note]
> 
> 三维空间中, 两个曲面的交集
> 
> $$
> F(x, y, z) = 0
> G(x, y, z) = 0
> $$
> 
> 长什么样呢?
> 
> **P46 例1**
> **P46 例2**

> [!important]
> 
> ==用参数方程描述曲线==
> 
> **二维空间中直线的参数方程**
> 
> **二维空间中圆的参数方程**
> 
> **三维空间中的螺旋线**

> [!important]
> 
> ==极坐标==
> 
> **二维空间的极坐标**
> 
> - 圆的极坐标方程 $r = a$
> - 椭圆的极坐标方程 $r = a(1+\mathrm{e} \cos\theta)$
> $$
> r(\theta) = \frac{ep}{1 + e\cos\theta},  
> $$
> 其中 $e$ 为离心率($0 < e < 1$), $d$ 为焦准距.
>  
> **三维空间的球极坐标**
>
> - **径向距离 $r$**：点到原点 $O$ 的距离，范围 $r \geq 0$。  
> - **极角 $\theta$**（天顶角, zenith）：点与正 $z$ 轴的夹角，范围 $0 \leq \theta \leq \pi$。  
> - **方位角 $\phi$**(azimuth)：点在 $xy$ 平面上的投影与正 $x$ 轴的夹角，范围 $0 \leq \phi < 2\pi$。  
>  
> **球坐标 → 直角坐标**：  
> $$
> \begin{cases}  
> x = r \sin\theta \cos\phi, \\  
> y = r \sin\theta \sin\phi, \\  
> z = r \cos\theta.  
> \end{cases}
> $$
>

> [!warning]
> 在大航海时代，航海家们需要精确地确定自己在海洋中的位置。天顶角和方位角的测量成为了关键技术。例如，著名航海家麦哲伦在其环球航行中，就利用了简单的天文仪器来测量天体的天顶角和方位角。通过测量北极星的天顶角，他可以估算出船只的纬度；而通过测量太阳或其他恒星的方位角，他能确定船只的航向。这在当时简陋的航海条件下，为航海家们开辟新航线、探索未知世界提供了重要的导航依据，对人类的航海事业和地理认知的拓展产生了深远影响 。

> [!important]
> 
> ==曲线的投影==
> 
> **P50 例4**
> **P50 例5**
> 
# 多元函数的微分

> [!tip]
> 
> 多元函数的微分是一元函数微分的推广, 它的一个非常重要的应用是求多元函数的极值. 例如 (P115例6) 有一块宽为 24cm 的方形铁板, 把它两边折起来做成一个断面为等腰梯形的水槽, 问怎样的折法才能使得截面面积最大? 设折出来的梯形底边长度为 $x$, 斜边的角度为 $\theta$, 则截面积可写成
> 
> $$
> S(x, \theta) = 24 x \sin\theta - 2x^2 \sin\theta + x^2 \sin\theta \cos\theta
> $$
> 
> 这是一个关于 $x, \theta$ 的二元函数, 如何求它的最大值呢?  我们可以带着这个问题开始本章的学习.

## 多元函数的连续性
> [!tip]
> 
> 在一元微积分中, 连续函数是我们的主要研究对象, 在多元微积分中同样也是这样. 下面我们先介绍一些准备知识作为铺垫, 然后给出多元函数极限和连续的定义.
> 

### 区域

> [!tip]
> 
> 在一元函数中, 我们经常**区间**的概念, 如开区间 $(a, b)$, 闭区间 $[a, b]$. **区域**是区间在高维空间中的推广. 下面我们以 $\mathbb{R}^2$ 为例进行介绍, 但所有的概念都可以推广到 $\mathbb{R}^n$ 中.
> 

> [!important]
> 
> ==邻域==
> 
> 设 $P_0(x, y)$ 是 $\mathbb{R}^2$ 中的一点, 给定 $\delta > 0$,  $\mathbb{R}^2$ 中所有与点 $P_0$ 距离小于 $\delta$ 的点构成一个集合, 称为点 $P_0$ 的 **$\delta$-邻域**, 记作 $U(P_0, \delta)$, 即
>  $$
>   U(P_0, \delta) = \{ (x, y)| \sqrt{(x-x_0)^2+ (y-y_0)^2} < \delta\}.
> $$
> 
> $P_0$ 与其自己的距离为0, 所以根据上述定义, $P_0\in U(P_0, \delta)$. 但有时候我们希望排除掉 $P_0$ 这一点, 在集合 $U(P_0, \delta)$ 中把 $P_0$ 去掉, 由此得到的集合称为 $P_0$ 的 **$\delta$-去心邻域**, 记作 $\overset{\circ}{U}(P_0, \delta)$, 即
>  $$
>  \overset{\circ}{U}(P_0, \delta) = \{ (x, y)| 0 < \sqrt{(x-x_0)^2+ (y-y_0)^2} < \delta\}.
> $$
>
> 有时候我们不关心 $\delta$ 的具体取值 (比如接下来的问题中), 往往简单用 $U(P_0)$ 和  $\overset{\circ}{U}(P_0)$ 分别表示 $P_0$ 的**邻域**和**去心邻域**.
> 

> [!important]
> 
> ==内点==
> 
> 任意给定一个 $\mathbb{R}^2$ 中的集合 $D$, 任意一点 $P$ 与 $D$ 的关系比符合以下三种关系中的一种:
> 
> 1. **内点**: 存在点 $P$ 的某个邻域 $U(P)$, 使得  $U(P) \subset D$.
> 2. **外点**: 存在点 $P$ 的某个邻域 $U(P)$, 使得  $U(P) \cap D = \emptyset$.
> 3. **边界点**: 点 $P$ 的任一邻域内既有属于 $D$ 的点, 又有不属于  $D$ 的点.
> 
> 集合 $D$ 的全体**边界点**所构成的集合称为 $D$ 的**边界**, 记作 $\partial D$.
> 

> [!note]
> 
> >**例**
> >
> >判断 $1 < x^2 + y^2 < 2$ 的内点, 外点和边界点.


> [!important]
> 
> ==聚点==
> 
> 对于点 $P$ 和点集 $E$,若对任意 $\delta > 0$,去心邻域 $ U^\circ(P, \delta) $ 内总包含 $E$ 中的点,则称 $P$ 是 $E$ 的**聚点**,
> 
> **注意**： 聚点 $P$ 可以**属于** $E$,也可以**不属于** $E$,
>

> [!note]
> 
> >**例**
> >
> >点集：$ E = \{ (x,y) \mid 1 < x^2 + y^2 \leq 2 \} $
> >
> >1. 内点：满足 $1 < x^2 + y^2 < 2$ 的所有点
> >2. 边界点：
> >  - $x^2 + y^2 = 1$ 的点（不属于 $E$）
> >  - $x^2 + y^2 = 2$ 的点（属于 $E$）
> >3. 聚点：$E$ 及其边界 $\partial E$ 上的所有点

> [!warning]
> 
> - 内点一定是聚点
> - 边界点可能是聚点
> - 聚点构成导集 $E'$,且 $\overline{E} = E \cup E'$
>

> [!important]
>
> ==开集与闭集==
>
> **开集**: 集合中的所有点都是其内点
> **闭集**: 集合的边界属于该集合, $\partial D \in D$
>

> [!note]
> 
> >**例**
> >
> >集合 $1 < x^2 + y^2 < 2$ 为开集.
> >

> [!important]
> 
> ==连通集==
> 
> 顾名思义, 如果集合 $D$ 中的任意两点都可以用折线连接起来, 且该折线上的点都属于 $D$, 则称 $D$ 为**连通集**.

> [!important]
> 
> ==区域==
> 
> **连通开集**称为**区域**(或**开区域**); 开区域连同它的边界一起所构成的集合称为**闭区域**.
> 

> [!note]
> 
> ==例子== 
> 
> 集合 $\{(x,y) \mid 1 < x^2 + y^2 < 2\}$ 是区域,而集合 $\{(x,y) \mid 1 \leq x^2 + y^2 \leq 2\}$ 是闭区域.

> [!important]
> 
> ==有界集与无界集==
> 
> >**有界集**  ： 对于平面点集 $E$,如果存在正数 $r$,使得$E \subset U(O, r)$,其中 $O$ 为坐标原点,则称 $E$ 为有界集,
> >**无界集** : 如果一个集合不是有界集,则称其为无界集,

### 多元函数的极限
> [!tip]
> 
> 下面我们以含有两个自变量的函数, 即二元函数为例引入多元函数及其极限的概念. 相关概念可以很容易推广到含有三个或更多自变量的多元函数中去.

> [!important]
> 
> ==二元函数的定义==
> 
>设 $D$ 是 $\mathbb{R}^2$ 中的非空子集,称映射 $f: D \to \mathbb{R}$ 为定义在 $D$ 上的**二元函数**,记为 
>$$
>z = f(x, y), \quad (x, y) \in D
>$$
>
>其中 $D$ 称为函数的**定义域** ,$x$ 和 $y$ 称为**自变量**.

>[!important]
>
> ==二元函数的极限==
> 
> 设 $f(x,y)$ 的定义在 $D$ 上的二元函数,$P_0(x_0, y_0)$ 是 $D$ 的聚点,如果存在常数 $A$,对于任意给定的正数 $\varepsilon$,总存在正数 $\delta$,使得当 $(x,y) \in U(P_0, \delta)$ 时,有 $ |f(x, y) - A| < \varepsilon $,则称 $A$ 为函数 $f(x,y)$ 当 $(x,y)$ 趋于 $(x_0, y_0)$ 时的极限,记作 
> $$
> \displaystyle\lim_{(x,y) \to (x_0, y_0)} f(x,y) = A.
> $$
>

> [!warning]
> 
> 注意从 $(x, y)$ 趋于 $(x_0, y_0)$ 有无数条路径, 极限存在要求**任意一条路径都成立**, 不能仅仅验证从 $x$-轴趋近和从$y$-轴趋近就断言极限存在.

>[!note]
>
> >**例1: 设 $f(x,y) = (x^2 + y^2)  \displaystyle\sin \frac{1}{x^2 + y^2}$,求证：$ \displaystyle\lim_{(x,y) \to (0,0)} f(x,y) = 0.$**
> > 
> >**证:**  这里函数 $f(x,y)$ 的定义域为 $D = \mathbb{R}^2 \backslash \{(0,0)\}$,点 $O(0,0)$ 为 $D$ 的聚点,
> > 因为$|f(x,y) - 0| = \displaystyle\left| (x^2 + y^2) \sin \displaystyle\frac{1}{x^2 + y^2} - 0 \right| \leq x^2 + y^2,$
> > 可见,$\forall \varepsilon > 0$,取 $\delta = \sqrt{\varepsilon}$,则当$ 0 < \sqrt{(x-0)^2 + (y-0)^2} < \delta,$ 
> > 即 $P(x,y) \in D \cap U(0,\delta)$ 时,总有 $|f(x,y) - 0| < \varepsilon$ 成立,所以 $  \displaystyle\lim_{(x,y) \to (0,0)} f(x,y) = 0. $
>
> >**例2: 考察函数在 $(0, 0)$ 处的极限, $$ f(x,y) = \begin{cases} \displaystyle\frac{xy}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\0, & x^2 + y^2 = 0.\end{cases} $$.**
> > 
> >**解:** 首先, 我们看当点 $P(x,y)$ 沿 $x$ 轴趋于点 $(0,0)$ 时有,
> >$$
> >\lim_{x \to 0} f(x,0) = \lim_{x \to 0} 0 = 0
> >$$
> >又当点 $P(x,y)$ 沿 $y$ 轴趋于点 $(0,0)$ 时,
> >$$
> >\lim_{y \to 0} f(0,y) =  \lim_{y \to 0} 0 = 0.
> >$$
> >虽然以上述两种特殊方式（沿 $x$ 轴或沿 $y$ 轴）趋于原点时函数的极限存在且相等,但是不能以此断言该函数的极限存在. 例如, 当点 $P(x,y)$ 沿着直线 $y = kx$ 趋于点 $(0,0)$ 时,有
> >$$
> >\lim_{x \to 0} \frac{kx^2}{x^2 + k^2 x^2} = \frac{k}{1+k^2},
> >$$
> > $k$ 不同极限也不同, 由此可以断言函数在$(0, 0)$ 处的极限不存在.
> 
>
>>**例3: 求 $  \displaystyle\lim_{(x,y) \to (0,2)} \displaystyle\frac{\sin(xy)}{x} $.**
> >
> >**解:** 函数 $ \displaystyle\frac{\sin(xy)}{x} $ 的定义域为 $D = \{(x,y) | x \neq 0, y \in \mathbb{R}\}$,$P_0(0,2)$ 为 $D$ 的聚点,
> >$$
> >\displaystyle\lim_{(x,y) \to (0,2)} \displaystyle\frac{\sin(xy)}{x} =  \displaystyle\lim_{(x,y) \to (0,2)} \left[ \displaystyle\frac{\sin(xy)}{xy} \cdot y \right] =  \displaystyle\lim_{xy \to 0} \displaystyle\frac{\sin(xy)}{xy} \cdot \lim_{y \to 2} y = 1 \cdot 2=2
> >$$

### 多元函数的连续性
> [!tip]
> 
> 下面我们仍然以二元函数为例引入多元函数连续的概念. 相关概念可以很容易推广到含有三个或更多自变量的多元函数中去.
> 

> [!important]
> 
> ==二元函数连续性==
> 
> 设 $f(x, y)$ 为定义在 $D$ 上的二元函数,$P_0 (x_0, y_0)$ 为 $D$ 的聚点,且 $P_0 \in D$,如果 $ \displaystyle\lim_{(x,y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$, 则称函数 $f(x, y)$ 在点 $P_0 (x_0, y_0)$ 连续,  
> 进一步, 如果函数 $f(x, y)$ 在 $D$ 内**每一点都连续**,则称函数 $f(x, y)$ 为 $D$ 上的**连续函数**,
> 
> ==间断点==
> 设函数 $f(x,y)$ 的定义域为 $D$,$P_0(x_0, y_0)$ 是 $D$ 的聚点,如果函数 $f(x,y)$ 在点 $P_0(x_0, y_0)$ **不连续**,那么称 $P_0(x_0, y_0)$ 为函数 $f(x,y)$ 的**间断点**,

> [!important]
>
> ==连续函数的性质==
>  
> 与**闭区间**上一元连续函数的性质相类似,在**有界闭区域**上连续的多元函数具有如下性质:
>
> - **性质1: 最大值与最小值**  
> 有界闭区域 $D$ 上的多元连续函数必定在 $D$ 上有界,且能取到它的最大值和最小值,
>
> - **性质2: 介值定理**  
> 有界闭区域 $D$ 上的多元连续函数能取到介于最大值和最小值之间的任何值,
>

## 偏导数
> [!tip]
> 固定其它变量, 看一个变量变化对函数值的影响.


> [!important]
> ==偏导数==
> 设函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 的某一邻域内有定义,固定 $y=y_0$ 让 $x$ 在 $x_0$ 附近变化, 若极限  
> $$
> \displaystyle\lim_{\Delta x \to 0} \displaystyle\frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x} \tag{2-1} 
> $$
> 存在, 则称此极限为函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处对 $x$ 的**偏导数**,记作：  
> $$
> \left. \displaystyle\frac{\partial z}{\partial x} \right|_{x=x_0}, \quad \left. \displaystyle\frac{\partial f}{\partial x} \right|_{x=x_0}, \quad z_x \bigg|_{x=x_0} \text{ 或 } f_x(x_0, y_0)
> $$
> 
> 类似地, 函数 $z=f(x,y)$ 对 $y$ 的偏导数为：  
> $$
> \displaystyle\lim_{\Delta y \to 0} \displaystyle\frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y} 
> $$
> 记作：  
> $$
> \displaystyle\left. \displaystyle\frac{\partial z}{\partial y} \right|_{y=y_0}, \quad \left. \displaystyle\frac{\partial f}{\partial y} \right|_{y=y_0}, \quad z_y \bigg|_{y=y_0} \text{ 或 } f_y(x_0, y_0)
> $$
> 

> [!warning]
> ==偏导函数== 
> 若 $z=f(x,y)$ 在区域 $D$ 内每一点 $(x,y)$ 处对 $x$ 的偏导数存在, 则由此构成的函数称为**偏导函数**,记作：  
>$$
>\displaystyle\frac{\partial z}{\partial x}, \quad \displaystyle\frac{\partial f}{\partial x}, \quad z_x \text{ 或 } f_x(x, y)
>$$
> 对 $y$ 的偏导函数记为：  
> $$
> \displaystyle\frac{\partial z}{\partial y}, \quad \displaystyle\frac{\partial f}{\partial y}, \quad z_y \text{ 或 } f_y(x, y)
> $$

>[!note]
>
> >**例1:求分段函 $
> >z = f(x, y) = 
> >\displaystyle\begin{cases} 
> >\displaystyle\frac{xy}{x^2 + y^2}, & x^2 + y^2 \neq 0 \\
> >0, & x^2 + y^2 = 0 
> >\end{cases}$ 在点 (0,0) 处的偏导数.**
> >
> >**解:**
> >
> > - 计算 $f_x(0, 0)$  
> > 
> > $f_x(0, 0) =  \displaystyle\lim_{\Delta x \to 0} \displaystyle\frac{f(0+\Delta x, 0) - f(0, 0)}{\Delta x} =  \displaystyle\lim_{\Delta x \to 0} \displaystyle\frac{0 - 0}{\Delta x} = 0$
> > 
> > - 计算 $f_y(0, 0)$  
> >
> > $f_y(0, 0) =  \displaystyle\lim_{\Delta y \to 0} \displaystyle\frac{f(0, 0+\Delta y) - f(0, 0)}{\Delta y} =  \displaystyle\lim_{\Delta y \to 0} \displaystyle\frac{0 - 0}{\Delta y} = 0$


>[!important]
>
>==高阶偏导数==
>
> 对偏导函数再求偏导数称为**二阶偏导数**, 以此类推还有三阶偏导数和更高阶的偏导数.
>

> [!warning]
> 
> ==二阶偏导数的四种形式==
>
>1. 对 $x$ 的二阶偏导：
>$$ \displaystyle\displaystyle\frac{\partial}{\partial x} \left( \displaystyle\frac{\partial z}{\partial x} \right) = \displaystyle\frac{\partial^2 z}{\partial x^2} = f_{xx}(x, y) $$
>
>2. 先对 $x$ 后对 $y$ 的混合偏导：
>$$ \displaystyle\frac{\partial}{\partial y} \left( \displaystyle\frac{\partial z}{\partial x} \right) = \displaystyle\frac{\partial^2 z}{\partial x \partial y} = f_{xy}(x, y) $$
>
>3. 先对 $y$ 后对 $x$ 的混合偏导：
>$$ \displaystyle\frac{\partial}{\partial x} \left( \displaystyle\frac{\partial z}{\partial y} \right) = \displaystyle\frac{\partial^2 z}{\partial y \partial x} = f_{yx}(x, y) $$
>
>4. 对 $y$ 的二阶偏导：
>$$ \displaystyle\frac{\partial}{\partial y} \left( \displaystyle\frac{\partial z}{\partial y} \right) = \displaystyle\frac{\partial^2 z}{\partial y^2} = f_{yy}(x, y) $$

>[!note]
>
> >**例：设函数 $z = x^3 y^2 - 3xy^3 - xy + 1$,求下列高阶偏导数：
> >$$ \displaystyle\frac{\partial^2 z}{\partial x^2},\ \displaystyle\frac{\partial^2 z}{\partial y \partial x},\ \displaystyle\frac{\partial^2 z}{\partial x \partial y},\ \displaystyle\frac{\partial^2 z}{\partial y^2} \ \text{及}\ \displaystyle\frac{\partial^3 z}{\partial x^3} .$$**
> >
> >**解:**  
> >先求一阶偏导数:
> >$ \displaystyle\frac{\partial z}{\partial x} = 3x^2 y^2 - 3y^3 - y $
> >$ \displaystyle\frac{\partial z}{\partial y} = 2x^3 y - 9xy^2 - x $
> >然后求二阶偏导数：
> >$ \displaystyle\frac{\partial^2 z}{\partial x^2} = \displaystyle\frac{\partial}{\partial x}(3x^2 y^2 - 3y^3 - y) = 6xy^2 $
> >$ \displaystyle\frac{\partial^2 z}{\partial y \partial x} = \displaystyle\frac{\partial}{\partial y}(3x^2 y^2 - 3y^3 - y) = 6x^2 y - 9y^2 - 1 $
> >$ \displaystyle\frac{\partial^2 z}{\partial x \partial y} = \displaystyle\frac{\partial}{\partial x}(2x^3 y - 9xy^2 - x) = 6x^2 y - 9y^2 - 1 $
> >$ \displaystyle\frac{\partial^2 z}{\partial y^2} = \displaystyle\frac{\partial}{\partial y}(2x^3 y - 9xy^2 - x) = 2x^3 - 18xy $
> >最后求三阶偏导数
> >$ \displaystyle\frac{\partial^3 z}{\partial x^3} = \displaystyle\frac{\partial}{\partial x}(6xy^2) = 6y^2 $

>[!important]
>
>==二阶混合偏导数定理==
>
> 如果函数 $z = f(x, y)$ 的二阶混合偏导数  $ \displaystyle\frac{\partial^2 z}{\partial y \partial x} \quad \text{和} \quad \displaystyle\frac{\partial^2 z}{\partial x \partial y} $  在区域 $D$ 内连续,那么在该区域内必有： 
> $$
> \displaystyle\frac{\partial^2 z}{\partial y \partial x} = \displaystyle\frac{\partial^2 z}{\partial x \partial y}
> $$
> 
> 即：**二阶混合偏导数在连续条件下与求导次序无关**,  

> [!note]
>
> >**例1:验证函数 $z = \ln \sqrt{x^2 + y^2}$ 满足拉普拉斯方程 $$ \displaystyle\frac{\partial^2 z}{\partial x^2} + \displaystyle\frac{\partial^2 z}{\partial y^2} = 0 .$$**
> >
> >**证明:**   
> >首先将函数化简为：
> >$$ z = \displaystyle\frac{1}{2} \ln(x^2 + y^2) $$  
> >$$ \displaystyle\frac{\partial z}{\partial x} = \displaystyle\frac{x}{x^2 + y^2} $$
> >$$ \displaystyle\frac{\partial z}{\partial y} = \displaystyle\frac{y}{x^2 + y^2} $$
> >$$ \displaystyle\frac{\partial^2 z}{\partial x^2} = \displaystyle\frac{y^2 - x^2}{(x^2 + y^2)^2} $$
> >$$ \displaystyle\frac{\partial^2 z}{\partial y^2} = \displaystyle\frac{x^2 - y^2}{(x^2 + y^2)^2} $$
> >验证方程 
> >将二阶偏导数相加：
> >$$ \displaystyle\frac{\partial^2 z}{\partial x^2} + \displaystyle\frac{\partial^2 z}{\partial y^2} = \displaystyle\frac{y^2 - x^2 + x^2 - y^2}{(x^2 + y^2)^2} = 0 $$
>
>
> >**例2:证明函数 $u = \dfrac{1}{r}$ 满足拉普拉斯方程$$ \displaystyle\frac{\partial^2 u}{\partial x^2} + \displaystyle\frac{\partial^2 u}{\partial y^2} + \displaystyle\frac{\partial^2 u}{\partial z^2} = 0 $$,其中 $r = \sqrt{x^2 + y^2 + z^2}$.**
> >
> >**证明:**
> > $$ \displaystyle\frac{\partial u}{\partial x} = -\displaystyle\frac{1}{r^2} \cdot \displaystyle\frac{\partial r}{\partial x} = -\displaystyle\frac{x}{r^3} $$
> > $$ \displaystyle\frac{\partial^2 u}{\partial x^2} = -\displaystyle\frac{1}{r^3} + \displaystyle\frac{3x^2}{r^5} $$
> >  由对称性可得：
> >  $$ \displaystyle\frac{\partial^2 u}{\partial y^2} = -\displaystyle\frac{1}{r^3} + \displaystyle\frac{3y^2}{r^5}, \quad \displaystyle\frac{\partial^2 u}{\partial z^2} = -\displaystyle\frac{1}{r^3} + \displaystyle\frac{3z^2}{r^5} $$
> >验证方程  
> >  $$ \begin{aligned}
> >  \displaystyle\frac{\partial^2 u}{\partial x^2} + \displaystyle\frac{\partial^2 u}{\partial y^2} + \displaystyle\frac{\partial^2 u}{\partial z^2} 
> >  &= -\displaystyle\frac{3}{r^3} + \displaystyle\frac{3(x^2 + y^2 + z^2)}{r^5} \\&= -\displaystyle\frac{3}{r^3} + \displaystyle\frac{3r^2}{r^5} \\ &= 0 \end{aligned} $$

## 全微分

> [!tip]
> 
> 在学习全微分的知识之前, 我们来回顾一下**一元函数微分**, 对于函数 $y=f(x)$, 其增量可表示为 
> 
> $$
> df = f'(x)dx
> $$
> 
> 接下来我们要把上述关系推广多元函数, 从而将函数值的变化于自变量的变化联系起来.
> 

> [!important]
> 
> ==全微分公式==
> 
> $$
> dz = \displaystyle\frac{\partial z}{\partial x}dx + \displaystyle\frac{\partial z}{\partial y}dy 
> $$
> 

> [!warning]
>
> ==全微分的几何理解==
> 
> ![全微分几何图示](media/img/Total_differential.jpg#200pt)
> 

>[!note]
>
> >**例1:$ z(x,y) = x + y $.**
> >
> >**解:**
> >变量变化：$x \to x + \Delta x, \quad y \to y + \Delta y$
> >函数增量计算： $z(x + \Delta x, y + \Delta y) = (x + \Delta x) + (y + \Delta y)$
> >增量分解： $\Delta z = z(x + \Delta x, y + \Delta y) - z(x, y) = \Delta x + \Delta y$
> >偏导数表示：  $\displaystyle\frac{\partial z}{\partial x} = 1, \quad \displaystyle\frac{\partial z}{\partial y} = 1$
> >全微分公式：  $dz = dx + dy$
> 
>
> >**例2:函数 $z(x,y) = x^2 + 2y^3$.**
> >
> >**解:** 
> >考虑自变量的微小变化：
> >$
> >\begin{cases}
> >x \rightarrow x + dx \\ 
> >y \rightarrow y + dy
> >\end{cases}
> >$
> >函数增量计算： $\begin{aligned}
> >z(x+dx,y+dy) &= (x+dx)^2 + 2(y+dy)^3 \\
> >&= x^2 + 2xdx + dx^2 + 2(y^3 + 3y^2dy + 3ydy^2 + dy^3) \\
> >&= x^2 + 2y^3 + 2xdx + 6y^2dy + \underbrace{dx^2 + 6ydy^2 + 2dy^3}_{\text{高阶无穷小项}}
> >\end{aligned} $
> >线性主部提取： 保留一阶增量项
> >$
> >\Delta z \approx 2xdx + 6y^2dy
> >$
> >偏导数计算：
> >$
> >\displaystyle\frac{\partial z}{\partial x} = 2x \quad \text{和} \quad \displaystyle\frac{\partial z}{\partial y} = 6y^2
> >$
> >全微分公式：$
> >dz = \displaystyle\frac{\partial z}{\partial x}dx + \displaystyle\frac{\partial z}{\partial y}dy = 2xdx + 6y^2dy$
>
>
> >**例3:$ S = \displaystyle\frac{1}{2} \left( L - 2x + L - 2x + 2x \cos \theta \right) x \sin \theta $.**
> >
> >**解:**
> >化简：$ S(x, \theta) = L x \sin \theta - 2x^2 \sin \theta + x^2 \sin \theta \cos \theta $
> >变量代换过程：$ x \to x + \Delta x, \quad \theta \to \theta + \Delta \theta $
> >函数增量展开：
> >$ 
> >\begin{aligned}
> S(x+\Delta x, \theta+\Delta \theta) &= L (x+\Delta x) \sin(\theta+\Delta \theta) \\
> &\quad -2(x+\Delta x)^2 \sin(\theta+\Delta \theta) \\
> &\quad + (x+\Delta x)^2 \sin(\theta+\Delta \theta)\cos(\theta+\Delta \theta)
> \end{aligned}
> >$
> >线性近似处理（保留一阶项）：
> >$
> >\begin{aligned}
> >\Delta S &\approx (L \sin \theta - 4x \sin \theta + 2x \sin \theta \cos \theta)\Delta x \\
> >&\quad + (L x \cos \theta - 2x^2 \cos \theta - x^2 \sin^2 \theta + x^2 \cos^2 \theta)\Delta \theta
> >\end{aligned}$
> >偏导数提取：
> >$
> >\begin{cases}
> >\displaystyle\frac{\partial S}{\partial x} = L \sin \theta - 4x \sin \theta + x \sin \theta \cos \theta \\
> >\displaystyle\frac{\partial S}{\partial \theta} = L x \cos \theta - 2x^2 \cos \theta + x^2 (\cos^2 \theta - \sin^2 \theta)
> >\end{cases}$
> >全微分公式：$dS = \displaystyle\frac{\partial S}{\partial x}dx + \displaystyle\frac{\partial S}{\partial \theta}d\theta$
> >最终结果：$dS = \sin\theta (L - 4x + 2x \cos\theta)dx + [x \cos\theta (L - 2x) + x^2 \cos 2\theta]d\theta$


### 链式法则

## 隐函数求导

## 梯度与方向导数

### 梯度

>[!important]
>
>==梯度的定义==
>设二元函数$f(x,y) $ 在区域$D$ 内具有一阶连续偏导数,则对于任意点 $ P_0(x_0,y_0) \in D $,其梯度定义为：
>$$\text{grad}\, f(x_0,y_0) = \nabla f(x_0,y_0) = f_x(x_0,y_0)\,\mathbf{i} + f_y(x_0,y_0)\,\mathbf{j}$$
>其中微分算子$  \nabla = \dfrac{\partial}{\partial x}\mathbf{i} + \dfrac{\partial}{\partial y}\mathbf{j} ,$

> [!warning]
> 
> ==梯度方向是函数值增长最快的方向==

>[!note]
>
> >**例3:求 $\mathrm{grad}\ \dfrac{1}{x^2 + y^2}$.**
> >
> >**解:**这里 $f(x, y) = \dfrac{1}{x^2 + y^2}$,因为 
> >$$\displaystyle\frac{\partial f}{\partial x} = -\displaystyle\frac{2x}{(x^2 + y^2)^2}, \quad  \displaystyle\frac{\partial f}{\partial y} = -\displaystyle\frac{2y}{(x^2 + y^2)^2}, $$
> >所以  
> >$$\mathrm{grad}\ \dfrac{1}{x^2 + y^2} = -\displaystyle\frac{2x}{(x^2 + y^2)^2} \mathbf{i} - \displaystyle\frac{2y}{(x^2 + y^2)^2} \mathbf{j}.$$
> >
>
>
>
> >**例5:设 $f(x, y, z) = x^3 - x y^2 - z^2,\ P_0(1,1,0)$,问 $f(x,y,z)$ 在 $P_0$ 处沿什么方向变化最快,  在这个方向的变化率是多少?**
> >
> >**解:** $\nabla f = \dfrac{\partial f}{\partial x}\mathbf{i} + \dfrac{\partial f}{\partial y}\mathbf{j} + \dfrac{\partial f}{\partial z}\mathbf{k} = (3x^2 - y^2)\mathbf{i} - 2xy\mathbf{j} - 2z\mathbf{k},\ 
> > \nabla f(1,1,0) = 2\mathbf{i} - 2\mathbf{j} - \mathbf{k}$.  
> > $f(x,y,z)$ 在 $P_0$ 处沿 $\nabla f(1,1,0)$ 的方向增加最快,沿 $-\nabla f(1,1,0)$ 的方向减少最快,在这两个方向的变化率分别是  
> > $$|\nabla f(1,1,0)| = \sqrt{2^2 + (-2)^2 + 1^2} = 3, \quad -|\nabla f(1,1,0)| = -3.$$
>
>
> >**例6:求曲面 $x^2 + y^2 + z = 9$ 在点 $P_0(1,2,4)$ 的切平面和法线方程.**
> >
> >**解:** 设 $f(x, y, z) = x^2 + y^2 + z$,由梯度与等值面的关系可知,梯度  
> >$$\nabla f \Big|_{P_0} = (2x\mathbf{i} + 2y\mathbf{j} + \mathbf{k})\Big|_{(1,2,4)} = 2\mathbf{i} + 4\mathbf{j} + \mathbf{k}
> >$$的方向是等值面 $f(x,y,z)=9$ 在点 $P_0$ 的法线方向,因此切平面方程是  $$
> >2(x - 1) + 4(y - 2) + (z - 4) = 0,$$
> >即  
> >$$2x + 4y + z = 14,$$
> >曲面在 $P_0$ 处的法线方程是  
> >$$x = 1 + 2t,\ y = 2 + 4t,\ z = 4 + t \quad (t\ \text{为任意常数}).$$

>[!important]
>
> ==三元函数的梯度定义与性质==
>设三元函数 \( f(x,y,z) \) 在空间区域 \( G \) 内具有一阶连续偏导数,则对于点 $ P_0(x_0,y_ 0,z_0)$ $in G$ \),其梯度为：
>
>>$$\text{grad}\, f(x_0,y_0,z_0) = \nabla f(x_0,y_0,z_0) = f_x\,\mathbf{i} + f_y\,\mathbf{j} + f_z\,\mathbf{k}$$
>>其中三维Nabla算子：
>>$$ \nabla = \dfrac{\partial}{\partial x}\mathbf{i} + \dfrac{\partial}{\partial y}\mathbf{j} + \dfrac{\partial}{\partial z}\mathbf{k} $$
>

>[!note]
>
> >**例:对 $f(x,y,z) = x^2 + yz $在点 $ (1,2,3) $ 的梯度.**
> >  
> >$ \nabla f = (2x, z, y) \big|_{(1,2,3)} = (2,3,2) $


### 方向导数

>[!important]
>
>==方向导数的定义==
>设函数 $f(x,y,z)$ 在点 $P_0(x_0,y_0,z_0)$ 的某邻域内有定义,$\mathbf{l}$ 为从 $P_0$ 出发的给定方向向量,$P(x,y,z)$ 为 $\mathbf{l}$ 上邻近 $P_0$ 的点,若极限  
>$$
> \displaystyle\lim_{\rho \to 0^+} \frac{f(P) - f(P_0)}{\rho} = \left. \frac{\partial f}{\partial l} \right|_{P_0}
>$$
>存在,则称此极限为 $f$ 在 $P_0$ 点沿方向 $\mathbf{l}$ 的**方向导数**,其中 $\rho = |PP_0|$.

>[!warning]
>==方向导数与梯度的关系==
>
> 方向导数等于梯度在该方向上的投影.

## 多元函数的极值

>[!note]
> >**例1:有一宽为24 cm的长方形铁板,把它两边折起来做成一断面为等腰梯形的水槽,问怎样折法才能使断面的面积最大？**
> >
> >**解:** 设折起来的边长为$x$ cm,倾角为$\alpha$(如图),则梯形断面的下底长为$(24 - 2x)$ cm,上底长为$(24 - 2x + 2x \cos \alpha)$ cm,高为$(x \sin \alpha)$ cm,所以断面面积
> > $$A = \displaystyle\frac{1}{2} [ (24 - 2x + 2x \cos \alpha) + (24 - 2x) ] \cdot x \sin \alpha$$
> > 即
> > $$A = (24x \sin \alpha - 2x^2 \sin \alpha + x^2 \sin \alpha \cos \alpha) \quad (0 < x < 12, 0 < \alpha \leq \displaystyle\frac{\pi}{2})$$
> > 可见断面面积$A = A(x, \alpha)$,这就是目标函数,下面求使该函数取得最大值的点$(x, \alpha)$,令$
> > \begin{cases}
> > A_x = 24 \sin \alpha - 4x \sin \alpha + 2x \sin \alpha \cos \alpha = 0 \\
> > A_\alpha = 24x \cos \alpha - 2x^2 \cos \alpha + x^2 (\cos^2 \alpha - \sin^2 \alpha) = 0
> > \end{cases}
> > $
> > 由于$\sin \alpha \neq 0$,$x \neq 0$,上述方程组可化为$
> > \begin{cases}
> > 12 - 2x + x \cos \alpha = 0 \\
> > 24 \cos \alpha - 2x \cos \alpha + x (\cos^2 \alpha - \sin^2 \alpha) = 0
> > \end{cases}
> > $
> > 解这方程组,得$\alpha = \displaystyle\frac{\pi}{3} = 60^\circ, \quad x = 8$
> > 根据题意可知断面面积的最大值一定存在,并且在$D = \{(x, \alpha) | 0 < x < 12, 0 < \alpha \leq \displaystyle\frac{\pi}{2}\}$内取得,通过计算得知$\alpha = \displaystyle\frac{\pi}{2}$时的函数值比$\alpha = 60^\circ, x = 8$时的函数值小,又函数在D内只有一个驻点,因此可以断定,当$x = 8$, $\alpha = 60^\circ$时,就能使断面的面积最大.
> 
>
> >**例2:某厂要用铁板做成一个体积为2 m³的有盖长方体水箱,问当长、宽和高各取怎样的尺寸时,才能使用料最省?**
> >
> >**解:**  设水箱的长为 $x$ m, 宽为 $y$ m, 则其高应为 $\displaystyle\frac{2}{xy}$ m. 此水箱所用材料的面积为 $A = 2 \left( xy + y \cdot \displaystyle\frac{2}{xy} + x \cdot \displaystyle\frac{2}{xy} \right)$, 即$A = 2 \left( xy + \displaystyle\frac{2}{x} + \displaystyle\frac{2}{y} \right) \quad (x > 0, y > 0).$
> > 可见材料面积 $A = A(x, y)$ 是 $x$ 和 $y$ 的二元函数, 这就是目标函数, 下面求使该函数取得最小值的点 $(x, y)$,
> > 令$A_x = 2 \left( y - \displaystyle\frac{2}{x^2} \right) = 0, \quad A_y = 2 \left( x - \displaystyle\frac{2}{y^2} \right) = 0.$
> > 解这方程组, 得$x = \sqrt[3]{2}, \quad y = \sqrt[3]{2}.$
> > 根据题意可以知道, 水箱所用材料面积的最小值一定存在, 并在开区域 $D = \{(x, y) | x > 0, y > 0\}$ 内取得,又函数在 $D$ 内只有唯一的驻点 $(\sqrt[3]{2}, \sqrt[3]{2})$, 因此可断定当 $x = \sqrt[3]{2}, y = \sqrt[3]{2}$ 时, $A$ 取得最小值,就是说, 当水箱的长为 $\sqrt[3]{2}$ m, 宽为 $\sqrt[3]{2}$ m, 高为 $\displaystyle\frac{2}{\sqrt[3]{2} \cdot \sqrt[3]{2}} = \sqrt[3]{2}$ m 时, 水箱所用的材料最省.
> > 从这个例子还可看出, 在体积一定的长方体中, 以立方体的表面积为最小,

### 条件极值

>[!important]
> **条件极值** 是指函数 $f(x, y, \dots)$ 在满足约束条件 $g(x, y, \dots) = 0$ 的前提下取得的极大值或极小值.
> **拉格朗日乘数法** 是用于求**带有约束条件的极值问题**的一种重要方法,  假设要求函数 $f(x, y)$ 在约束条件 $g(x, y) = 0$ 下的极值, 
> **方法**  
> 1. 构造拉格朗日函数  
> $$ L(x, y, \lambda) = f(x, y) + \lambda g(x, y) $$
> 2. 求偏导并列方程组  
> $$\displaystyle\frac{\partial L}{\partial x} = 0,\quad \displaystyle\frac{\partial L}{\partial y} = 0,\quad \displaystyle\frac{\partial L}{\partial \lambda} = 0 $$
> 3. 解这个方程组,得到可疑点；
> 4. 将这些点代入 $f(x, y)$,比较函数值,判断极值,

>[!note]
>
> >**例:求函数$ u = xyz $ 在附加条件 $\displaystyle\frac{1}{x} + \displaystyle\frac{1}{y} + \displaystyle\frac{1}{z} = \displaystyle\frac{1}{a} $$(x,y,z,a > 0$)下的极值.**
> >
> >**解:**构造拉格朗日函数：$$ L(x,y,z) = xyz + \lambda \left( \displaystyle\frac{1}{x} + \displaystyle\frac{1}{y} + \displaystyle\frac{1}{z} - \displaystyle\frac{1}{a} \right) $$
> >求偏导并令其为零：
> >$$ \begin{cases}
> >L_x = yz - \displaystyle\frac{\lambda}{x^2} = 0 \\
> >L_y = xz - \displaystyle\frac{\lambda}{y^2} = 0 \\
> >L_z = xy - \displaystyle\frac{\lambda}{z^2} = 0
> >\end{cases}$$
> >将各方程乘以对应变量后相加,代入原条件得：
> >$$ xyz = \displaystyle\frac{\lambda}{3a} $$
> >回代解得唯一驻点：
> >$$ x = y = z = 3a $$
> >**结论**  
> >函数在点 \((3a,3a,3a)\) 处取得极小值：
> >$$ u_{\text{极小}} = 27a^3 $$
