---
title: 新工科数学分析(上)
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
---

[toc]

# 第1章 极限

> [!tip] 
>
> **微积分**是大学数学的核心内容, 是**人工智能**的基础之一, 学好它对我们以后的学习和成长有非常大的好处.
>
> 微积分的研究对象是**函数**. 我们中学已经学过函数的概念, 下面我们来复习和巩固一下.

## 1.1 集合与映射

### 1.1.1 集合

> [!TIP]
> 
> 集合是数学研究从具体到抽象的第一步. 当我们用**数学语言**来描述世界时, 首先要把我们**感兴趣的对象**给拿出来, 进行适当的抽象, 然后再研究它们的规律. **集合**就是数学中用来界定对象的一个概念.
> 

> [!Note]
> 
> ==集合举例==
>
> 1. *`自然数集`* --- $\mathbb{N} = \left\{0, 1, 2, 3, \cdots \right\}$
> 2. *`实数集`*  --- $\mathbb{R} = \left\{x: -\infty < x < \infty \right\}$
> 3. *`满足不等式 x-3<10 的所有实数 x`* --- $A=\left \{x < 7\right \}$

> [!Important]
>
> ==集合的概念==
> 
> 我们把所要研究的对象统称为**元素** (element), 这些元素所组成的总体叫做**集合** (set). 一般用大写字母如 $A, B, C$ 表示集合, 用小写字母如 $x$ 或 $a, b, c$ 来表示集合中的元素.
>
> - 如果 $x$ 是集合 $A$ 的元素, 就说 $x$ **属于** 集合 $A$ , 记作 $x\in A$ ; 
> - 如果 $x$ 不是集合 $A$ 中的元素, 就说 $x$ **不属于** 集合 $A$, 记作 $a \notin A$.
> - 不包含任何元素的集合叫做 **空集** (emptyset), 记为 $\phi $.

> [!caution]
>
> ==上机实验==
>
> 计算机图像处理中经常会用到**掩码** (mask) 的概念. 掩码本质上就是一个集合.
>
> - set_mask.ipynb: 图像掩码操作.
> 

> [!IMPORTANT]
>
> ==两个集合间的包含关系==
>
> 如果集合 $A$ 中**任意**_~Rd~_一个元素都是集合 $B$ 中的元素, 则称 $A$ **包含于** $B$ (或 $B$ **包含**$A$), 记作 $A\subseteq B$ 或 $B\supseteq A$, 此时称 $A$ 为 $B$ 的 **子集** (subset). 空集是任何集合的子集
> 
> - **集合相等**: 如果 $A\subseteq B$, 同时 $B\subseteq A$, 则集合 $A$, $B$ 中的元素是完全一样的, 此时我们说集合 $A$ 等于集合 $B$, 记作$A=B$.
> 

> [!Important]
> 
> ==集合之间的运算==
>
> **交集**
> 
> 所有既属于 $A$ 又属于 $B$ 的元素组成的集合称为 $A$ 与 $B$ 的 **交集** (intersection set), 记作 $A\cap B$ (读作“$A$ 交 $B$”), 即
> 
> $$
> A\cap B=\left \{ x: x\in A \ \mathrm{and} \ x\in B \right \}
> $$
> 
> 下图展示了交集运算: 
> 
> ![交集](../media/img/1.4.jpg)
>
> **并集**
>
> 所有属于集合 $A$ 或属于集合 $B$ 的元素组成的集合, 称为集合 $A$ 与 $B$ 的 **并集** (union set), 记作 $A\cup B$ (读作“ $A$ 并 $B$ ”), 即
> 
> $$
> A\cup B=\left \{ x: x\in A \ \mathrm{or} \ x\in B \right \}
> $$
> 
> 下图展示了并集运算: 
> 
> ![并集](../media/img/1.3.jpg)
> 
> **补集**
> 
> 如果集合 $A$ 是集合 $B$ 的子集, 则所有 $B$ 中不属于 $A$ 的所有元素构成的集合称为 $A$ 相对于 $B$ 的 **补集** (complementary set), 记作 $C_BA$ 或 $A^C$, 即
> 
> $$
> \bar{A} = C_B A = \{x \in B: \ x\notin A\}
> $$
> 
> 下图展示了补集运算: 
> 
> ![补集](../media/img/1.5.jpg)

> [!caution]
>
> ==上机实验==
>
> - set_iou.ipynb: **交并比**介绍. 

### 1.1.2 映射

> [!TIP]
>
> **集合**的概念是为了给**映射**做铺垫, 映射建立了**集合与集合之间的关联**. 
>

> [!Important]
> 
> ==映射的定义==
> 
> 映射 (map) 描述了从一个集合到另一个集合的某种对映关系. 设集合 $A$ 和 集合 $B$ 是两个集合, 如果存在一个对映关系 $f$, 使得集合 $A$ 中的每个元素都唯一的对映到 $B$ 中的一个元素, 则称 $f$ 为从 $A$ 到 $B$ 的映射, 记作
> $$
> f: A \rightarrow B
> $$
>
> 映射 $f$ 把集合 $A$ 中的元素 $a$ 对映到 $B$ 中的元素 $b$, 可记作
> $$
> f(a) = b
> $$
> 此时 $b$ 称为 $a$ 的**象**, $a$ 称为 $b$ 的**原象**.
>
> 映射可以通过下面的图像来理解: 
>
> ![映射](../media/img/Function_color_example_3.svg.png#200h)
> 
> 图中箭头表示了集合 $A$ 中元素与集合 $B$ 中元素的对映关系. 
> 
> 根据定义, 映射需要满足两个要求: **随处取值, 唯一对映**.
>
> - **随处取值**是指 $A$ 中的任何一个元素在 $B$ 中都有对映；
> - **唯一对映**是指 $f$ 可以把 $A$ 中的不同元素映射到 $B$ 中的同一个元素, 但不能把 $A$ 中的一个元素映射到 $B$ 中的多个元素.

> [!warning]
>
> ==映射的性质==
>
> 1. **单射**：如果 $A$ 中的每个元素都对映 $B$ 中的不同元素, 则称 $f$ 为单射.
> 2. **满射**：如果 $B$ 中的每个元素都有原象, 则称 $f$ 为满射.
> 3. **一一映射**：顾名思义, 一一映射就是集合 $A$ 中元素与集合 $B$ 中的元素一个对映一个.
> 可以证明, $f$ 是一一映射等价于 $f$ 既是单射又是满射.
>
> ==逆映射==
>
> 对于一一映射 $f: A \rightarrow B $, 把映射的象和原象反过来, 得到一个把集合 $B$ 映射到集合 $A$ 的新的映射, 称为逆映射, 记作 $f^{-1}: B\rightarrow A$.

> [!Note]
> 
> ==映射的例子==
> 
> 映射的例子在我们的生活中随处可见, 例如：
>
> 1. **名字**：集合 $A$ 是所有的人, 集合 $B$ 是所有的名字. 每个人都有一个名字, 我们允许重名, 但不允许一个人有2个名字.
> 2. **地图**：没错, map 本身就是一个 map！(我们希望)这是一个从地图到真实世界的一一映射.
> 3. **颜色**：为什么我们能看到不同的颜色？颜色是一个从光波长到我们主观感受的映射.
> 
> 从上面的例子可以感受到, 映射的作用在于把集合 $A$ 中的元素作为**输入信号**, 例如如不同的人、GPS坐标、光的波长等, 经过某种操作, 转换成我们关心的输出, 如名字、位置和颜色. 从这个意义上理解, 映射就是就是把输入 $x$ 转化成 $f(x)$ 的一个机器.
> 
> ![Function](../media/img/function.png#200w)

### 1.1.3 函数

> [!tip]
>
> ==映射与函数==
>
> 函数是一种特殊的映射: 从**数集** $A$ 到**数集** $B$ 的**映射** $f:A \rightarrow B$ 称为**函数** (function). 函数可写成 $y = f(x)$ 的形式, 其中 $x$ 称为**自变量**, $y$ 称为 $x$ 对映的**函数值**.
> 

> [!important]
> 
> ==数列==
> 
> **数列**是一类特殊的函数, 它把自然数集 $\mathbb{N}$ 映射到实数集 $\mathbb{R}$ 中, 这个函数可以记作 $a(n)$, 不过更多的时候我们会把 $n$ 作为下标, 以 $a_n$ 表示数列得第 $n$ 项, 并以 $\{ a_n \} $ 表示整个数列.
> 
> **等差数列**
> 
> - 首项为 $a_{1}$,  公差为 $d$ 的等差数列的**通项公式**为
>
> $$
> a_{n} =a_{1} +(n-1)d
> $$
>
> - 等差数列的**前 $n$ 项和**为
> $$
> \quad S_{n}=na_1+\frac{n(n-1)}{2}d
> $$
>
> **等比数列**
>
> - 首项为 $a_{1}$ , 公比为 $q$ 的等比数列的**通项公式**为
> $$
> a_{n}=a_{1} q^{n-1}
> $$
>
> - 等比数列的**前 $n$ 项和**为
> $$
> S_{n}=a_{1}\frac{1-q^n }{1-q} （q\ne 1)
> $$


> [!important]
> 
> ==初等函数==
> 
> 1. 幂函数: $y=x^{\alpha}$
> 2. 指数函数: $y=a^x$, 特别的有 $y=\mathrm{e}^x$, 后者在 python 中有专门的函数 $numpy.exp(x)$
> 3. 对数函数: $y=\mathrm{log}_a^{x}$, 特别的有 $y=\mathrm{ln}^{x}$, 后者在 python 中有专门的函数 $numpy.log(x)$
> 4. 三角函数: $y=\sin(x)$, $y=\cos(x)$, $y=\tan(x)$
> 5. 反三角函数: $y = \mathrm{arcsin}(x)$
> 
> ==其它常用函数==
>
> 1. 绝对值函数: $y=|x|$
> 2. 符号函数
> $$
> y=\mathrm{sgn}(x)=\left\{\begin{matrix}
>  1, &  x>0& \\
>  0, &  x=0& \\
>  -1, &  x<0&
> \end{matrix}\right.
> $$
> 
> 3. Sigmoid函数
> $$
> \sigma (x)=\frac{1}{1+e^{-x}}
> $$

> [!important]
>
> ==反函数== 
>
> **反函数**是**逆映射**的一个特例, 对于函数 $f: x \rightarrow y$ (也要求 $f$ 是一一映射), 其反函数为 $f^{-1}: y \rightarrow x$. 例如
> 
> - $y = 3x + 1$ 的反函数为 $y = (x-1)/3$
> - $y = \mathrm{e}^x$ 的反函数为 $y = \mathrm{ln}x$. 
>
> 反函数本质上是把 $x$ 和 $y$ 的顺序对调了一下, 因此不难发现原函数与反函数的图像是关于直线 $y = x$ 对称的.
> 
> ![反函数图形的对称性](../media/img/inverse_function.png#400w)

> [!important]
> 
> ==复合函数==
> 
> 对于函数 $f$ 和 $g$, 我们可以构造一个**新的函数** $y = f[g(x)]$, 它把自变量 $x$ 通过函数 $g$ 映射到 $u = g(x)$, 再把 $u$ 视作自变量 (也称为**中间变量**) 通过函数 $f$ 映射到 $y = y = f[g(x)]$. 这个过程可以表示为:
> 
> $$
> x \stackrel{g}{\longrightarrow} u \stackrel{f}{\longrightarrow} y.
> $$
> 
> 我们把这个新函数 $y = f[g(x)]$ 称为函数 $f$ 和 $g$ 的**复合函数**, 记作 $f \circ g$. 注意函数复合是讲顺序的, 一般来说 $f\circ g \ne g\circ f$.
> 

> [!note]
> 
> 假设 $f(x) = x + 2$, $g(x) = x^2$, 则
> 
> $$
> \begin{align}
> f\circ g &= g(x) + 2 = x^2 + 2, \\
> g\circ f &= [f(x)]^2 = (x+2)^2. 
> \end{align}
> $$

> [!Caution]
> 
> 计算机编程中的**函数**(function) 概念比数学中的函数要广, 它表示从输入 (可以是数、数组、函数等）到输出 (也可以是数、数组、函数等）的一系列操作. 
> 
> ==深度学习与复合函数==
>
> ![神经网络](../media/img/network.png#400w) 
>
> 人工智能中的核心技术为**深度学习**, 深度学习的背后其实就是有很多层 (从几十到几千层都有) 的**神经网络** (Neuron Network). 神经网络的本质正是复合函数. 对于图中所示的神经网络, 从最左端的**输入信号**开始, 之后每一层都是上一层信号的复合, 因此神经网络就是一个复合了很多次的函数, 这个函数把输入 (比如一张图片) 映射到我们关心的结果 (比如图像是猫还是狗的概率). 
>
> ==上机实验==
> 
> - set_mnist.ipynb: 手写数字识别演示.


## 1.2 极限

> [!TIP] 
> 
> 极限是微积分中的核心概念. 极限的出现代表了数学思想的一次转变, 而促成这一转变的动机来自于现实问题中对**曲线**相关问题的需求. 在初等数学中我们会计算矩形的周长和面积, 会计算三角形的周长和面积, 甚至是任意多边形的周长和面积, 但是, 这些都是由直线构成的结构, 而到了曲线大家就不会了. 曲线的长度怎么算? 由曲线构成区域的面积怎么算? 尽管我们初中就知道圆的周长是 $2\pi r$, 面积是 $\pi r^2$, 但是为什么是这样, 只有运用微积分才能给出严格的证明.
> 
> 极限的概念很直观, 但经过数学的严格化后会变得非常抽象. 可以说极限的公理化是一道门槛, 是我们从中学的初等数学迈向大学的高等数学的必经之路. 要学好极限并不容易, 这里面涉及从有限到无穷的观念转变. 我们会发现这条路一开始会辗转反复, 让人晕头转向, 但是当你学完这门课程再回头来看, 会发现这么做是值得的, 数学概念的严格化其实不是在追求外表的精美, 而是让我们的内心变得更加的强大, 使我们有力量走得更远. 那么, 我们深呼吸一下, 一起敲开通向高等数学的大门吧.

### 1.2.1 数列极限

> [!tip]
> 
> ==极限与圆的面积==
> 
> 圆的面积怎么算? 为了计算圆的面积, 我们构造了一**系列**圆的内接正多边形, 这些正多边形的面积是可以通过初等数学计算的, 我们把它们的面积记作 $A_n, n = 1, 2, \cdots$. 通过**直觉**我们能感受到, **当 $n$ 趋于无穷大时, $A_n$ 的面积会无限接近圆的面积**_~Rd~_. 接下来我们要做的就是**把这个直觉通过数学语言给严格化**. 


> [!caution]
>
> ==上机实验==
>
> - limit_array_circle.ipynb: 圆面积的极限.

> [!important]
> 
> 极限是一个**动中取静**_~Rd~_的过程. 
> 
> - 什么在动?
> 	数列 $\{ A_n \}$ 中的指标 $n$ 在**动**. 
> 
> - 什么是静?
> 	圆面积是静, $A_n$ 的取值会慢慢**趋于稳定**, 到最后**几乎不变**了, 数学上我们称这种行为叫**收敛**. 
> 


> [!Note]
>
> ==极限存在的例子==
>
> **一尺之捶，日取其半 (版本1)**
> 
> 站在棒子的角度, 这个过程可以用一个数列描述. $n$ 代表天数, $a_n$ 代表杠剩下的长度.
>
> $$
> \begin{align*}
> a_0 &= 1,  \\
> a_1 &= 1/2,  \\
> a_2 &= 1/4,  \\
> & \cdots \\
> a_n & = 1/2^n, \\
> & \cdots
> \end{align*}
> $$
> 
> 随着 $n$ 的增加 (**动**), $a_n$ 的值不断靠近0 (**静**), 直觉告诉我们当 $n$ 区域无穷大时 $a_n$ 的极限是0.
>
> **一尺之捶，日取其半 (版本2)**
> 
> 站在砍棒人的角度, 这个过程也可以用一个数列描述. $n$ 代表天数, $b_n$ 代表到第 $n$ 天为止所取的棒子的总数.
> 
> $$
> \begin{align*}
> b_0 &= 0,  \\
> b_1 &= 1/2,  \\
> b_2 &= 1/2 + 1/4 = 3/4,  \\
> & \cdots \\
> b_n & = 1/2 + 1/4 + \cdots + 1/2^n = 1 - \frac{1}{2^n}, \\
> & \cdots
> \end{align*}
> $$
>
> 随着 $n$ 的增加 (**动**), $b_n$ 的值不断靠近1 (**静**), 直觉告诉我们当 $n$ 区域无穷大时 $b_n$ 的极限是1.
> 
> **P21 例1**
> 
> $$
> a_n = \frac{n + (-1)^{n-1}}{n}
> $$
> 
> 随着 $n$ 的增加 (**动**), $a_n$ 的值不断靠近1 (**静**), 直觉告诉我们当 $n$ 区域无穷大时 $a_n$ 的极限是1.
>
> **P22 例2**
> 
> $$
> a_n = \frac{(-1)^{n}}{(n+1)^2}, \\
> $$
> 
> 随着 $n$ 的增加 (**动**), $a_n$ 的值不断靠近0 (**静**), 直觉告诉我们当 $n$ 区域无穷大时 $a_n$ 的极限是0.

> [!Note]
> 
> ==极限不存在的例子==
>
> **例3**
>  
> 数列 $\{ 1, -1, 1, -1, \cdots\}$ 不收敛, 因为直觉告诉我们这个数列**静**不下来.
>
> **例4**
>  
> 数列 $\{ 1, 2, 3, 4, \cdots\}$ 不收敛, 这个数列不断增长, 直觉告诉我们这个数列也**静**不下来.

> [!important]
> 
> ==数列极限的定义== (非常重要!!!)
> 
> 设 $\{a_n\}$ 为一数列, $A$ 为一常数, 如果**对于任意给定的正数 $\varepsilon$**, **总存在正整数 $N$**, 使得当 $n>N$ 时有
> $$
> |a_n - A| < \varepsilon,
> $$
> 则称 $A$ 为数列 $\{a_n\}$ 的**极限**, 记作
> $$
> \lim_{n\rightarrow \infty} a_n = A.
> $$
>
> **定义背后的数学直觉**_~Rd~_: 所以数列 $\{a_n\}$ 有极限就是, 当 $n$ 足够大时, $a_n$ 的值无限接近某个数 $A$. 上述定义把数列极限的直觉具象化了, 从而使得直觉变得可操作了. 根据定义, 我们现在可以严格的判断前面例子中数列的极限.

> [!Note]
>
> ==一尺之捶，日取其半 (版本1)==
> 
> **直觉**: $a_n  = 1/2^n$ 的极限为0.
> 
> **证明**: 对于任意给定的 $\varepsilon > 0$, 要找到 $N$ 使得 $|1/2^N - 0| = 1/2^N < \varepsilon$, 取 $N = \left[ -\mathrm{ln} \varepsilon / \mathrm{ln} 2 \right] + 1$, 可知当 $n > N$ 时, 总有 $|a_n - 0| < \varepsilon$. 因此 $\displaystyle \lim_{n \rightarrow \infty} a_n = 0$.
> 
> ==一尺之捶，日取其半 (版本2)==
> 
> **直觉**: $b_n  = 1 - \frac{1}{2^n}$ 的极限为1.
> 
> **证明**: 对于任意给定的 $\varepsilon > 0$, 要找到 $N$ 使得 $|1-1/2^N - 1| = 1/2^N< \varepsilon$, 取 $N = \left[ -\mathrm{ln} \varepsilon / \mathrm{ln} 2 \right] + 1$, 可知当 $n > N$ 时, 总有 $|b_n - 1| < \varepsilon$. 因此 $\displaystyle \lim_{n \rightarrow \infty} b_n = 1$.
>
>
> ==P21 例1==
> 
> **直觉**: $\displaystyle a_n  = \frac{n + (-1)^{n-1}}{n}$ 的极限为1.
> 
> **证明**: 对于任意给定的 $\varepsilon > 0$, 要找到 $N$ 使得 $\displaystyle \left|\frac{n + (-1)^{n-1}}{n} - 1\right| = \frac{1}{n}< \varepsilon$, 取 $N = \left[ 1/ \varepsilon\right] + 1$, 可知当 $n > N$ 时, 总有 $|a_n - 1| < \varepsilon$. 因此 $\displaystyle \lim_{n \rightarrow \infty} a_n = 1$.
>
> ==P22 例2==
> 
> **直觉**: $\displaystyle a_n  = \frac{(-1)^n}{(n+1)^2}$ 的极限为0.
> 
> **证明**: 对于任意给定的 $\varepsilon > 0$, 要找到 $N$ 使得 $\displaystyle \left| \frac{(-1)^n}{(n+1)^2} - 0\right| = \frac{1}{(n+1)^2}< \varepsilon$, 取 $N = \left[ \sqrt{1/ \varepsilon}\right]$, 可知当 $n > N$ 时, 总有 $|a_n - 0| < \varepsilon$. 因此 $\displaystyle \lim_{n \rightarrow \infty} a_n = 0$.

> [!warning]
> 
> ==数列极限的几条性质 (了解, 不需要证明)==
> 
> 1. 如果数列 $a_n$ 有极限, 那么它的极限唯一.
> 2. 如果数列 $a_n$ 有极限, 那么数列 $a_n$ 一定有界.
> 3. 如果 $\displaystyle \lim_{n\rightarrow \infty} a_n = A$, 且 $A > 0$, 那么存在正整数 $N$, 当 $n > N$ 时有 $x_n > 0$.
> 4. 如果 $\displaystyle \lim_{n\rightarrow \infty} a_n = A$, 那么 $a_n$ 的任一子数列的极限也是 $A$.
> 5. 任意改变数列的有限多项, 不影响极限的收敛.

### 1.2.2 函数极限

> [!tip]
> 
> 函数极限跟数列极限本质上都是极限, 都是**动中取静**, 只不过数列极限中动的是 $n$, 而函数极限中动的是自变量 $x$. 之前我们强调过**函数图像**的重要性, 函数的极限过程同样可以通过函数图像来理解. 下面这张图可以作为我们对函数极限的**直觉**, 图中展示了 $\displaystyle \lim_{x\rightarrow 2} f(x) = 4$, 请大家想想在这个极限过程中什么在**动**, 什么是**静**?
>
>  ![函数极限](../media/img/function_limit.png#400w)
>  

> [!caution]
>
> ==上机实验==
>
> 两个函数极限的例子:
> 
> - limit_fun_sin_over_x.ipynb
> - limit_fun_sin_1_x.ipynb 

> [!important]
> 
> ==函数极限的定义== (非常重要!!!)
> 
> 设函数 $\{f(x)\}$ 在点 $x_0$ 的某一去心领域内有定义 ( 为了让 $x$ 能够动起来), $A$ 为一常数. 如果**对于任意给定的正数 $\varepsilon$**, **总存在正数 $\delta$**, 使得当 $0 < |x-x_0| < \delta$ 时有
> $$
> |f(x) - A| < \varepsilon,
> $$
> 则称 $A$ 为函数 $\{f(x)\}$ 在 $x_0$ 的**极限**, 记作
> $$
> \lim_{x\rightarrow x_0} f(x) = A.
> $$
> 
> 上述定义可以通过下图来理解
> 
> ![函数极限](../media/img/function_limit_def.png#400w)
> 
> 所以函数 $\{f(x)\}$ 在 $x\rightarrow x_0$ 时有极限就是, 当 $x$ 足够接近 $x_0$ 时, $f(x)$ 的值无限接近某个数 $A$. 注意跟数列极限进行对比. 跟数列极限的定义一样, 上面关于函数极限的定义提供了一个**可操作的流程**, 能够将我们关于函数极限的直观**具象化**. 
>

> [!note]
> 
> **直觉**: $\displaystyle f(x)  = x^2 + 1$ 在 $x_0=2$ 的极限为5.
> 
> **证明**: 对于任意给定的 $\varepsilon > 0$, 要找到 $\delta$ 使得只要 $0 < |x-2|< \delta$, 总有 
> $$
> \begin{align*}
> \left|f(x) - 5\right| &= \left| x^2+1 - 5\right| \\
> & = \left| x^2 - 4\right| \\
> & = \left| x - 2\right| \left| x + 2\right|  \\
> & < 2.5|x-2| < \varepsilon
> \end{align*}
> $$
> 
> 取 $\displaystyle \delta = \frac{\varepsilon}{2.5}$, 可知当 $0< |x-2|<\delta$ 时, 总有 $|f(x) - 5| < \varepsilon$. 因此 $\displaystyle \lim_{x \rightarrow 2} f(x) = 5$.
> 

> [!warning]
> 
> ==函数极限的性质==
> 
> 1. 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x)$ 存在, 则极限唯一.
> 2. 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, 则 $f(x)$ 在 $x_0$ 周围有界, 即存在 $M >0$ 和 $\delta > 0$, 使得当 $0< |x-x_0|<\delta$ 时 $|f(x)| < M$ .
> 3. 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A > 0$, 则 $f(x)$ 在 $x_0$ 周围一定大于0, 即存在 $\delta > 0$, 使得当 $0< |x-x_0|<\delta$ 时 $f(x) > 0$.
>

> [!warning]
> 
> ==$\varepsilon-\delta$ 语言==
> 
> 本章的主要内容是*`数列极限`*和*`函数极限`*的**定义**, 在数学上我们也把这套定义极限的方法称为 $\varepsilon-N$ 语言 (数列) 或 $\varepsilon-\delta$ 语言 (函数). 这样的定义看似繁缛, 但只有这样才能把极限的本质说清楚. 初学者不要怕麻烦, 做题时应该一字一句的把极限的定义写清楚. 怕麻烦不想写字的同学, 在熟练掌握了极限的定义之后, 可以使用两个约定的缩写符号:
> 
> 1. $\forall$: **对于任意**_~Rd~_
> 2. $\exist$: **存在**_~Rd~_
> 
> 使用这两个符号, 数列极限和函数极限的定义可以写成下面的形式 (仅仅是少几个字而已).
> 
> ==数列极限的定义==
> 
> $\displaystyle \lim_{n\rightarrow \infty} a_n = A \iff  \forall \varepsilon > 0$, $\exist N$, s. t., $\ |a_n - A| < \varepsilon$ if $n > N$.
> 
> ==函数极限的定义==
> 
> $\displaystyle \lim_{x\rightarrow x_0} f(x) = A \iff \forall \varepsilon > 0$, $\exist \delta$, s. t., $|f(x) - A| < \varepsilon$ if $0 < |x-x_0| < \delta$.
> 

> [!warning]
> 
> ==对无穷大的描述==
> 
> 我们有时候会说一个数列或函数**趋于无穷大**, 也会写 $\displaystyle \lim_{n\rightarrow \infty} a_n = \infty$ 或 $\displaystyle \lim_{x\rightarrow x_0} f(x) = \infty$, 请注意, 这只是一种**习惯**上的说法, 并**不是**_~Rd~_真正意义上的 (有限的) 极限. 尽管如此, 我们可以借用类似 $\varepsilon-N$ 语言的做法来从数学上定义什么叫**趋于无穷大**, 例如:
> 
> 
> **数列趋于无穷大**
> 
> $\displaystyle \lim_{n\rightarrow \infty} a_n = \infty \iff  \forall M > 0$, $\exist N$, s. t., $|a_n| > M$ if $n > N$.
> 
>**函数趋于无穷大**
> 
> $\displaystyle \lim_{x\rightarrow x_0} f(x) = \infty \iff \forall M > 0$, $\exist \delta$, s. t., $|f(x)| > M$ if $0 < |x-x_0| < \delta$.
> 

### 1.2.3 极限的运算

> [!tip]
> 
> 这一讲我们主要关心如何计算极限.
> 
> - 对于一些简单的极限计算, 每次都用直觉和 $\varepsilon-\delta$ 语言来计算极限太繁琐, 也没有必要. 很多时候**极限的四则运算**能够帮上大忙.
> - 有一些困难的极限问题, 我们需要跟强大的数学结论和工具, 本讲介绍的**三明治定理**和**单调有界数列有极限**请收好.
>
> 注意, 本讲的性质和定理全部都建立在上一讲**极限定义**的基础之上, 其根本还是 $\varepsilon-\delta$ 语言.
> 

> [!caution]
>
> ==希尔伯特的旅店==
>
> 极限运算涉及到了**无限**_~Rd~_的概念, 对初学者来说这是一个之前从未踏足过的位置领域, 一些**有限世界中的直觉**将不再成立. **希尔伯特的旅店**是一个有趣的故事, 通过这个故事希望能让大家对**无限**_~Rd~_有一颗**敬畏之心**.
>
> <iframe src="https://player.bilibili.com/player.html?isOutside=true&aid=217018325&bvid=BV1Aa411N7Sg&cid=804913368&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

> [!important]
>
> ==数列极限四则运算==
> 
> - **加减法**: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n = A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 则 $\displaystyle \lim_{n\rightarrow \infty}[a_n \pm b_n]= A \pm B$.
> 
>  - **乘法**: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n = A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 则 $\displaystyle \lim_{n\rightarrow \infty}a_nb_n = AB$.
> 
>  - **除法**: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n= A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 且 $B \ne 0$, 则 $\displaystyle \lim_{n\rightarrow \infty}\frac{a_n}{b_n}= \frac{A}{B}$.
>
> 证明见教学视频或问DeepSeek.

> [!important]
>
> ==函数极限四则运算==
> 
>  - **加减法**: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 则 $\displaystyle \lim_{x\rightarrow x_0}[f(x) \pm g(x)]= A \pm B$.
>  
> - **乘法**: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 则 $\displaystyle \lim_{x\rightarrow x_0}f(x)g(x)= AB$.
> 
> - **除法**: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 且 $B \ne 0$, 则 $\displaystyle \lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}= \frac{A}{B}$.
>
> 证明见教学视频或问DeepSeek.

> [!note]
>
> **例1: 证明 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$**
> 
> **证明**: 对任意给定的 $\varepsilon > 0$，我们需要找到正整数 $N$，使得当 $n > N$ 时:
> 
>  $$
>  \left| \frac{1}{n} - 0 \right| = \frac{1}{n} < \varepsilon
>  $$
> 
>  解不等式 $\frac{1}{n} < \varepsilon$ 得 $n > \frac{1}{\varepsilon}$  
> 
>  取 $N = \left\lfloor \frac{1}{\varepsilon} \right\rfloor + 1$（即不小于 $\frac{1}{\varepsilon}$ 的最小整数）  
> 
>  则当 $n > N$ 时，必有 $\frac{1}{n} < \varepsilon$  
> 
>  故 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$.
>
> **例2: 计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{2n}$**
> 
> **解法1（直接法）**：  
> 由 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$ 可得：
> 
> $$
> \lim_{n\rightarrow \infty}\frac{1}{2n} = \frac{1}{2} \cdot \lim_{n\rightarrow \infty}\frac{1}{n} = 0
> $$
> 
> **解法2（$\varepsilon-N$ 定义证明）**：  
> 
> 对任意 $\varepsilon > 0$，需存在 $N$ 使得当 $n > N$ 时：
> 
> $$
> \left| \frac{1}{2n} - 0 \right| = \frac{1}{2n} < \varepsilon
> $$
> 
> 解不等式得 $n > \frac{1}{2\varepsilon}$, 取 $N = \left\lfloor \frac{1}{2\varepsilon} \right\rfloor + 1$  ，则当 $n > N$ 时必满足 $\frac{1}{2n} < \varepsilon$  ，故极限为 $0$
>
> **例3: 计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n^2}$**
>
> **解**：  
>
> 对任意 $\varepsilon > 0$，需存在 $N$ 使得当 $n > N$ 时：
> 
> $$
> \left| \frac{1}{n^2} - 0 \right| = \frac{1}{n^2} < \varepsilon
> $$
> 
> 解不等式得 $n > \frac{1}{\sqrt{\varepsilon}}$, 取 $N = \left\lfloor \frac{1}{\sqrt{\varepsilon}} \right\rfloor + 1$, 则当 $n > N$ 时必满足 $\frac{1}{n^2} < \varepsilon$, 故极限为 $0$.
>
> **例4: 计算 $\displaystyle \lim_{x\rightarrow 1}(2x-1)$**
> 
>**解法1（直接代入法）**：  
> 
> 由于 $f(x) = 2x - 1$ 在 $x=1$ 处连续，可直接代入：  
> $\lim_{x\rightarrow 1}(2x-1) = 2(1) - 1 = 1
> $
>
> **解法2（$\varepsilon-\delta$ 定义证明）**：  
> 
> 对任意 $\varepsilon > 0$，需找到 $\delta > 0$ 使得当 $0 < |x-1| < \delta$ 时：  
> $
> |(2x-1) - 1| = 2|x-1| < \varepsilon$ 
> 
> 取 $\delta = \frac{\varepsilon}{2}$，则当 $0 < |x-1| < \delta$ 时：  
> $
> 2|x-1| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon
> $ ，故极限为 $1$
>
> **例5: 计算 $\displaystyle \lim_{x\rightarrow 2}\frac{x^3-1}{x^2-5x+3}$**
>
> **解法**： 分子在 $x=2$ 处的值：$2^3 - 1 = 7$, 分母在 $x=2$ 处的值：$2^2 - 5(2) + 3 = -3$, 分母不为零，可直接代入：  
> 
> $$
> \lim_{x\rightarrow 2}\frac{x^3-1}{x^2-5x+3} = \frac{7}{-3} = -\frac{7}{3}
> $$
>
> **例6: 计算 $\displaystyle \lim_{x\rightarrow 3}\frac{x-3}{x^2-9}$**
>
> **解法**：识别不定式：直接代入得 $\frac{0}{0}$，需进一步处理, 因式分解分母：
> $
> x^2-9 = (x-3)(x+3)
> $
> 
> 约去公因式：
> $
> \frac{x-3}{x^2-9} = \frac{1}{x+3} \quad (x \neq 3)
> $
> 
> 计算简化后的极限：
> $
> \lim_{x\rightarrow 3}\frac{1}{x+3} = \frac{1}{6}
> $

### 1.2.4 两个重要的极限


> [!tip]
> 
> ==重要极限一==
> 
> 还记得"割圆法"求圆面积的例子吗? 圆的内接正 $n$ 边形的面积当 $n \rightarrow \infty$ 的极限的计算最后就会落到极限 $\displaystyle \lim_{x\rightarrow 0} \frac{\sin(x)}{x}$ 的计算, 这个极限与圆周率 $\pi$ (**阿基米德数**_~Rd~_)有着深刻的联系.

> [!important]
>
> ==三明治定理==
>
> **定理陈述**：  
> 设函数 $f(x), g(x), h(x)$ 在点 $x_0$ 的某去心邻域内满足：  
> 
> 1. $g(x) \leq f(x) \leq h(x)$  
> 2. $\displaystyle \lim_{x\to x_0} g(x) = \lim_{x\to x_0} h(x) = L$  
> 则 $\displaystyle \lim_{x\to x_0} f(x) = L$。  
>
> **数列版本**：  
> 若数列 $\{a_n\}, \{b_n\}, \{c_n\}$ 满足：  
> 1. $b_n \leq a_n \leq c_n$（对充分大的 $n$）  
> 2. $\displaystyle \lim_{n\to\infty} b_n = \lim_{n\to\infty} c_n = L$  
> 则 $\displaystyle \lim_{n\to\infty} a_n = L$。  
>

> [!warning]
>
> **证明** $\displaystyle \lim_{x\rightarrow 0} \frac{\sin(x)}{x} = 1$
> 
> 考虑单位圆（半径 \( r = 1 \)）中角度 $x \in \left(0, \frac{\pi}{2}\right)$:
>     -  $\sin x$  为对边长度
>     -  $x$  为圆弧长度（弧度制）
>     -  $\tan x$  为切线长度
> $\sin x < x < \tan x \implies 1 < \frac{x}{\sin x} < \frac{1}{\cos x}$, 取倒数得：$ \cos x < \frac{\sin x}{x} < 1$
> 
> 应用三明治定理:
>     $
>       \lim_{x \to 0} \cos x = 1 \quad \text{且} \quad \lim_{x \to 0} 1 = 1
>       $
>       故：
>       $
>       \lim_{x \to 0} \frac{\sin x}{x} = 1
>       $

> [!warning]
> 
> - \( x \) 必须使用弧度制
> - 对于 \( x < 0 \) 的情况，利用奇函数性质：
> $$
>  \frac{\sin(-x)}{-x} = \frac{\sin x}{x}
> $$


> [!tip]
>
> ==重要极限二==
>  
> 极限 $\displaystyle \lim_{n\rightarrow \infty} \left(1+\frac{1}{n}\right)^{n}$ 与无理数 $\mathrm{e}$ (**欧拉数**_~Rd~_)有密切的联系. Jacob Bernoulli 于1683年在研究**复利**的时候考虑过这个数列的极限.
> 
> ![Jakob Bernoulli](../media/img/Jakob_Bernoulli.jpg#400h)
> 
> **雅各布·伯努利与数e的发现**

> [!caution]
>
> ==上机实验==
>
> - limit_array_e.ipynb: 函数极限的例子.
> 

> [!important]
> 
> ==单调有界数列有极限==
>

> [!important]
> **证明** $\displaystyle \lim_{n\rightarrow \infty} \left(1+\frac{1}{n}\right)^{n} = \mathrm{e}$
>
> 证明见教学视频或问DeepSeek.

> [!warning]
>
> $\displaystyle \lim_{x\rightarrow 0} \left(1+x\right)^{\frac{1}{x}} = \mathrm{e}$

> [!caution]
>
> 可以证明 
>
> $$
> \mathrm{e} = 1 + \frac{1}{1!} + \frac{1}{2!} + \cdots + \frac{1}{n!} + \cdots
> $$
>
> 证明的方法也是用**单调有界数列有极限**.
>
> 中学学过**导数**的同学可以算一下展开式
>
> $$
> \mathrm{e}^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \cdots + \frac{x^n}{n!} + \cdots
> $$
> 
> 的导数, 看看会发现什么有趣的现象?

### 1.2.5 复合函数的极限

> [!tip] 
> 
> 下面的结论相当于极限运算中的换元法, 在计算极限的时候十分有用.
> 

> [!warning]
> 
> 假设 $y=f[g(x)]$,  $\displaystyle \lim_{x\rightarrow x_0}g(x) = u_0$, $\displaystyle \lim_{u\rightarrow u_0}f(x) = A$, 则 $\displaystyle \lim_{x\rightarrow x_0}f[g(x)] = A$.
> 
> 这个结论请自行根据直觉理解, 证明略.
>

> [!note]
>
> 综合运用*`极限的定义`*, *`极限的四则运算`*和*`复合函数的极限 (换元法)`*, 以及*`三明治定理`*和*`单调有界数列有极限`*等结论, 我们现在可以计算很多数列和函数的极限.
>
>
> **例1**
> 
> $\displaystyle \lim_{x\rightarrow 0}\frac{\tan(x)}{x}$ (P48: 例1)
> 
> 解：$$ \begin{aligned} \displaystyle &\lim_{x \rightarrow 0} \frac{\tan (x)}{x}= \lim_{x \rightarrow 0} \left( \frac{\sin (x)}{x} \cdot \frac{1}{\cos (x)} \right) \\= &\left( \lim_{x \rightarrow 0} \frac{\sin (x)}{x} \right) \cdot \left( \lim_{x \rightarrow 0} \frac{1}{\cos (x)} \right) =1 \end{aligned} $$.
>
> **例2**
> 
> $\displaystyle \lim_{x\rightarrow 0}\frac{1-\cos(x)}{x^2}$ (P48: 例2)
> 
> 解：
> $$ \begin{aligned}\displaystyle &\lim_{x \rightarrow 0} \frac{1 - \cos (x)}{x^{2}} \\= &\lim_{x \rightarrow 0} \left( \frac{\sin^{2}(x)}{x^{2}} \cdot \frac{1}{1 + \cos (x)} \right)\\= &\lim_{x \rightarrow 0} \left( \frac{\sin (x)}{x} \right)^{2} \cdot \lim_{x \rightarrow 0} \frac{1}{1 + \cos (x)} \\= &\frac{1}{2}\end{aligned} 
>$$.
>
>
> **例3**
> 
> $\displaystyle \lim_{x\rightarrow 0}\frac{\arcsin(x)}{x}$ (P48: 例3)
> 
> 解：$t = \arcsin (x)$，则 $x = \sin t$，当 $x \to 0$ 时，有 $t \to 0$.  于是由复合函数的极限运算法则得：$\displaystyle \lim_{x \to 0} \frac{\arcsin (x)}{x} = \lim_{t \to 0} \frac{t}{\sin (t)} = 1$.
>
> **例4**
> 
> $\displaystyle \lim_{x\rightarrow \infty}\left( 1-\frac{1}{x}\right)^{x}$ (P51: 例4)
> 
> 解：令 $t = -x$，则当 $x \to \infty$ 时，$t \to -\infty$.  
>于是 $$\begin{aligned}\displaystyle &\lim_{x \to \infty} \left( 1 - \frac{1}{x} \right)^{x} = \lim_{t \to -\infty} \left( 1 + \frac{1}{t} \right)^{-t} \\= &\lim_{t \to -\infty} \frac{1}{\left( 1 + \frac{1}{t} \right)^{t}} = \frac{1}{e} \end{aligned}$$.
>
> **例5**
> 
> $\displaystyle \lim_{x\rightarrow 0}\frac{\tan (2x)}{\sin (5x)}$ (P55: 例3)
> 
> 解：当 $ x \rightarrow 0 $ 时，$\tan (2)x \sim 2x$，$\sin (5x) \sim 5x$，所以  $\displaystyle \lim_{x \rightarrow 0} \frac{\tan (2x)}{\sin (5x)} = \lim_{x \rightarrow 0} \frac{2x}{5x} = \frac{2}{5}$.
>
> **例6**
> 
> $\displaystyle \lim_{n\rightarrow \infty}\frac{\sqrt{n^2 + a^2}}{n}$ (习题1-2: 5(3))
> 
> 解：约简分式为：$ \displaystyle \frac{\sqrt{n^{2} + a^{2}}}{n} = \sqrt{\frac{n^{2} + a^{2}}{n^{2}}} = \sqrt{1 + \frac{a^{2}}{n^{2}}} $
> 设两个基本函数：内层函数：$\displaystyle \ f(n) = 1 + \frac{a^{2}}{n^{2}}$ ，外层函数：$g(x) = \sqrt{x}$ 
> 原极限可表示为复合函数：$\displaystyle \lim_{n \to \infty} \frac{\sqrt{n^{2} + a^{2}}}{n} = \sqrt{\lim_{n \to \infty} \left(1 + \frac{a^{2}}{n^{2}}\right)}$
> 利用基本极限性质：$\displaystyle\lim_{n \to \infty} \frac{a^2}{n^2} = a^2 \cdot \lim_{n \to \infty} \frac{1}{n} \cdot \lim_{n \to \infty} \frac{1}{n} = 0$
因此：$\displaystyle\lim_{n \to \infty} f(n) = 1 + 0 = 1$
> 因外函数 $ g(x) = \sqrt{x} $ 在 $ x = 1 $ 处连续，满足：$\displaystyle\lim_{x \to L} g(x) = g(L)$
> 代入内部极限结果：$\displaystyle\lim_{n \to \infty} \sqrt{1 + \frac{a^2}{n^2}} = g(1) = \sqrt{1} = 1$
> 

## 1.3 连续函数

### 1.3.1 连续和间断

> [!tip]
> 
> 所谓**连续函数**, 直白的说就是能笔不离开纸面一气画出来的函数, 下面我们就来运用**极限**的概念把这个**连续的直观**_~Rd~_给**数学化**.

> [!important]
> 
>
> 
> ==函数在某一点的连续==
> 
> 若 $\displaystyle \lim_{x\rightarrow x_0}f(x) = f(x_0)$, 则称 $f(x)$ 在 $x_0$ 处连续.
>
> ==连续函数==
> 
> 如果函数在某个区域上**每一点都连续**, 则称 $f(x)$ 是该区域上的**连续函数**.
>

> [!note]
> 
> ==连续函数==
> 
>
>
> **例1 $f(x) = |x|$**
> 
>  $f(x)$ 在 $(-\infty, +\infty)$ 上连续.
> 
> ![绝对值函数](../media/img/chap1_5.1.1.png#200h)
> 
> **例2: $\displaystyle f(x) = \frac{1}{|x|}$**
> 
>  $f(x)$ 在 $(-\infty,0)\bigcup (0, +\infty)$ 上连续, 但是在 0 点处不连续.
> 
> ![绝对值的倒数](../media/img/chap1_5.1.2.png#200h)
> 

> [!warning]
> 
> ==间断函数==
> 
> 不连续的函数就是**间断函数**. 间断函数一定有某处是不连续的, 造成不连续的原因很多, 其中有些间断点还能够被挽救回来变成连续的 (**可去间断点**), 有些则挽救不回来. 


> [!note]
>
> ==间断函数的例子==
>
>
>
> **例3 $\displaystyle f(x) = \frac{\sin(x)}{x}$**
> 
> 这个函数在 $x=0$ 处不连续, 造成不连续的原因是 $f(0)$ 没有定义, 从而 $\displaystyle \lim_{x\rightarrow 0} f(x) = f(0)$ 无从说起. 幸运的是, $f(x)$ 在 $x=0$ 处的极限等于1, 只要令 $f(0) = 1$ 就可以让 $f(x)$ 在0点也连续了, 从而**改良**后的 $f(x)$ 对任意 $x \in (-\infty, \infty)$ 都连续.
>
> **例4: $f(x)=\displaystyle \sin\left(\frac{1}{x}\right)$**
> 
> $f(x)$ 在 $x=0$ 点处不连续. 造成不连续的原因跟*`例3`*一样也是 $f(0)$ 没有定义. 不幸的是,  $f(x)$ 在 $x=0$ 处无限震荡, 没有极限, 所以这个函数没法像*`例3`*一样简单的补上一个点就成为连续函数.
> 
> ![震荡函数](../media/img/chap1_5.1.3.png#200h)
>

> [!warning]
>
> ==单侧极限==
>
> - **左连续**(注意极限记号下方的 $-$ 号)
> 
> $\displaystyle \lim_{x\rightarrow x_0^-} f(x) = A \iff \forall \varepsilon > 0$, $\exist \delta>0$, s. t., $|f(x) - A| < \varepsilon$ if $-\delta < x-x_0 < 0$.
> 
> - **右连续**(注意极限记号下方的 $+$ 号)
>
> $\displaystyle \lim_{x\rightarrow x_0^+} f(x) = A \iff \forall \varepsilon > 0$, $\exist \delta>0$, s. t., $|f(x) - A| < \varepsilon$ if $0 < x-x_0 < \delta$.
>
> 造成函数 $f(x)$ 在 $x=x_0$ 处的极限不存在的一个常见原因是 $f(x)$ 的**左右极限不相等**.



> [!note]
> 
> ==符号函数 $\mathrm{sgn}(x)$==
> 
> $$
\mathrm{sgn}(x) = \begin{cases}
> 1,  & \text{if $x>0$}, \\
> 0, & \text{if $x=0$}, \\
> -1, & \text{if $x<0$}.
> \end{cases}
> $$
> 该函数在 $x_0=0$ 处不连续, 造成不连续的原因是函数在该点的左极限 ($x$ 从左往右趋于0) 等于 $-1$, 右极限 ($x$ 从右往左趋于0) 等于 $1$, 左右极限不相等. 这种情况也没有办法通过简单的修改 $f(0)$ 的值来让函数连续.
> 


> [!warning]
> 
> 函数的连续性是一个很**自然**的性质, 我们所感受到的世界就是连续的: 物体运动的轨迹, 温度的变化, 甚至计算机里的0-1也是用连续函数来近似的. 
> - 在做**目标追踪**问题的时候, 连续是一个很重要的**先验**; 
> - 在求解**物理方程**的时候, 解的连续性是一个很重要的**约束**;
> - 在人工智能里, 连续性是解决高维问题的一个**核心底层逻辑**.


### 1.3.2 闭区间上连续函数的性质

> [!tip]
> 
> 闭区间上的连续函数是函数中的**乖宝宝**_~Gn~_, 因为这类函数的值总是可以被**控制**住.
> 

> [!important]
> 
> ==闭区间上连续函数的定义==
> 
> 如果函数 $f(x)$ 在 $(a, b)$ 内连续, 在 $a$ 处右连续, 在 $b$ 处左连续, 则 $f(x)$ 是闭区间 $[a, b]$ 上的连续函数.
> 


> [!important]
>  
> ==维尔斯特拉斯 (Weierstrass) 极值定理/极大极小值定理==
> 
> 闭区间 $[a, b]$ 上的连续函数有界, 且至少有一点 $x_1 \in [a, b]$ 使得 $f(x_1)$ 是 $f(x)$ 在 $[a, b]$ 上的最大值, 也至少有一点 $x_2 \in [a, b]$ 使得 $f(x_2)$ 是 $f(x)$ 在 $[a, b]$ 上的最小值. 

> [!note]
>
> ==两个反例==
>
> **例1: $\displaystyle f(x) = \frac{1}{x}$ **
> 
> 在闭区间$[-1,1]$上, $f(x)$ 在 $x=0$ 处不连续, 因为 $f(0)$ 没有定义. 因此, $f(x)$ 在 $[-1,1]$ 上的连续性是不成立的. 违反维尔斯特拉斯极值定理，$f(x)$ 在闭区间$[-1,1]$上无界，当$x \to 0$ 时，$\displaystyle \lim_{x \to 0} |f(x)| \to +\infty$,不存在最大值和最小值.
>
> 
> **例2: 符号函数**
> 
> $$\mathrm{sgn}(x) = \begin{cases}
> 1,  & \text{if $x>0$}, \\
> 0, & \text{if $x=0$}, \\
> -1, & \text{if $x<0$}.
> \end{cases}$$
> 符号函数在闭区间$[-1, 1]$上不连续，因为在$x=0$处，符号函数的左右极限不相等。
> 

> [!important]
> 
> ==布尔查诺 (Bolzano) 定理/介值定理==
> 
> 设闭区间 $[a, b]$ 上的连续函数 $f(x)$ 在端点的值分别为 $f(a) < 0$, $f(b) > 0$, 则一定存在 $x_0 \in [a, b]$ 使得 $f(x_0) = 0$.
> 

> [!note]
>
> **例1：证明方程 $x^{3} - 4x^{2} + 1 = 0$ 在区间 $(0,\,1)$ 内至少有一个根**
> 
> 证明：函数 $f ( x ) = x ^ { 3 } - 4 x ^ { 2 } + 1$ 在闭区间 $[0，1]$上连续，又$f ( 0 ) = 1 >0$，$f ( 1 ) = - 2< 0$. 根据介值定理，区间 $[0，1]$ 内存在 $c$ 满足 $f(c) = 0$, 此即方程 $x ^ { 3 } - 4 x ^ { 2 } + 1 = 0$ 的一个根． 
>