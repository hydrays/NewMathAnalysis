---
title: 新工科数学分析
author: 胡煜成
description: 首都师范大学新工科数学分析
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,数学分析,讲义
vlook-chp-autonum: h1=off
vlook-query: vdl=on
vlook-query: ws=off..............
---

[toc]

# 第一章 极限

> [!tip] 
> 微积分是本课程的核心内容, 而极限则是微积分中的核心概念. 极限的概念很直观, 但经过数学的严格化后会变得非常抽象. 可以说极限的公理化是一道门槛, 是我们从中学的初等数学迈向大学的高等数学的必经之路. 要学好极限并不容易, 这里面涉及从有限到无穷的观念转变. 我们会发现这条路一开始会辗转反复, 让人晕头转向, 但是当你学完这门课程再回头来看, 会发现这么做是值得的, 数学概念的严格化其实不是在追求外表的精美, 而是让我们的内心变得更加的强大, 使我们有力量走得更远. 那么, 我们深呼吸一下, 一起敲开通向高等数学的大门吧.



## 1 集合与映射

> [!tip]
>
> ==集合与映射是数学研究从具体到抽象的第一步.==
>
> 举个例子, 比如我们上这门高数课, 最后需要给每个上课的学生一个成绩. 为了从数学上来更加严格的定义这个任务, 我们可以把所有选课的同学构放到一个**集合** $S$ 中, 同时把所有可能的成绩 (比如A, B, C, D四个档次) 放到另一个**集合** $G$ 中, 那么给学生成绩的这个任务在数学上就可以看成是**从集合 $S$ 到集合 $G$ 的一个映射**. 引入集合和映射的概念可以让一个问题变得更清晰, 更严格.
> 
> ![集合是数学抽象](../media/img/chpt1_set_final.svg)
>

### 1.1 集合
#### 集合的概念

> [!TIP]
> 
> 当我们用**数学语言**来描述世界时, 首先要把我们**感兴趣的对象**给拿出来, 进行适当的抽象, 然后再研究它们的规律. **集合**就是数学中用来界定对象的一个概念.
> 

> [!Note]
> 
> ==集合举例==
>
> 1. *`太阳系八大行星`* --- $\{水星, 金星, 地球, 火星, 木星, 土星, 天王星, 海王星\}$
> 2. *`10个阿拉伯数字`* --- $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
> 3. *`一个班所有男生的姓氏`* --- $\{李, 王, 张, 杨, 周, 诸葛, 徐, 孙, 胡\}$
> 4. *`1 ~ 10 之间的所有偶数`* $A=\left \{  2,4,6,8,10\right \} $
> 6. *`自然数集`* --- $\mathbb{N} = \left\{0, 1, 2, 3, \cdots \right\}$
> 7. *`整数集`* --- $\mathbb{Z} = \left\{0, \pm 1, \pm 2, \pm 3, \cdots \right\}$
> 8. *`实数集`*  --- $\mathbb{R} = \left\{x: -\infty < x < \infty \right\}$
> 9. *`满足不等式 x-3<10 的所有实数 x`* --- $A=\left \{x < 7\right \} $

> [!Important]
>
> 我们把所要研究的对象统称为**元素** (element), 这些元素所组成的总体叫做**集合** (set). 
>
> 描述集合的方式既可以通过文字叙述, 也可以把所有的元素写在 $\{\}$ 里面, 不管用那种方式, 一定要让人能够判断某个对象是不是在这个集合里.
>
> 集合需要满足下面两个性质: 
>
> 1. ###### **互异性**: 集合中的任何两个元素都是不同的. 比如在集合3的例子中, 即使这个班里有3个同学姓“王”, 在集合3中“王”姓也只出现一次, 重复的不算.
>
> 2. **无序性**: 集合中的元素没有顺序之分. 所以集合 $\{水星, 金星, 地球\}$ 与集合 $\{地球, 水星, 金星\}$ 是没有区别的.
>

> [!Caution]
>
> 一般用大写字母如 $A, B, C$ 表示集合, 用小写字母如 $x$ 或 $a, b, c$ 来表示集合中的元素.
>
> 我们说一个对象**在**或**不在**一个集合中, 用数学术语就是**属于**或**不属于**: 
>
> - 如果 $x$ 是集合 $A$ 的元素, 就说 $x$ **属于** 集合 $A$ , 记作 $x\in A$ ; 
> - 如果 $x$ 不是集合 $A$ 中的元素, 就说 $x$ **不属于** 集合 $A$, 记作 $a \notin A$.

> [!Warning]
> 
> ==图像掩码 (mask)==
> 
> **图像掩码**是计算机视觉中的重要概念. 掩码 (mask) 通常是一个二值 (0或1) 图像, 像素值为0表示不关心的区域, 1表示感兴趣的区域. 因此**所有像素值为1的像素点构成的集合**就是我们感兴趣的区域 (ROI, Region of Interest). 比如下图中, 左侧是我们拿到的一张图片 , 我们只关心图片中狗的区域, 因此对应的掩码就是中间的一个二值图像 (黑色区域的像素值为0, 白色区域的像素值为1), 将这个掩码逐像素的跟原图相乘, 得到的结果就是右边的这张只有狗的图 (狗所在部分的值跟原图一样, 之外部分的值都等于0).
>
> ![图像掩码](../media/img/mask.png)
> 

#### 集合的性质

> [!TIP]
> 
> 集合是一个包罗万象的容器, 不同的集合可能包含截然不同对象, 我们在研究集合的时候, 首先要搞清楚**集合内部元素的性质**.
> 

> [!important]
>
> ==有序性==
>
> 如果一个集合中的元素可以排序, 那么这个集合就是**有序集**, 否则就是**无序集**. 
>
> 注意这个并不是一个严格的数学定义, 即使在实际操作中也是模糊的, 比如集合 $\{红, 绿, 蓝\}$, 理解成三个汉字的话可能无法排序, 但理解成颜色所对应的波长则可以间接的通过波长大小进行排序. 所以关键的问题是, 你在建立这个集合时所关心的**具体问题**是什么. 我们在使用集合这个工具的时候一定要先想清楚这一点, 这很重要, 尤其是对于学习**编程**_~Rd~_的同学！例如, 在程序里, 有序集通常可以使用**array**数据结构, 其中的元素可以通过指标很方便的访问；而无序集则往往使用**set**数据结构, 其中的元素需要一个一个去比较.
>

> [!Note]
>
> ==有序性和无序集==
> 
> 下面的集合中的元素之间通常是可以比较大小, 如: 
>
> - 实数集 $\mathbb{R}$
> - 音阶集 $\{ 哆, 来, 咪, 发, 嗦, 啦, 西\}$
> 
> 下面的集合中的元素之间通常无法比较大小(至少没有显而易见的比较大小的规则), 如: 
>
> - 天气集 $\{ 天晴, 多云, 下雨, 雾霾\}$ 
> - 动物集 $\{ 猫, 狗, 牛, 马\}$
> 

> [!Important]
> 
> ==等价关系==
> 
> 如果我们能够在一个集合上定义某种**等价关系**, 那么凡是“等价”的元素都可以划分到一个子集中, 而这些子集也被称为**等价类**. **等价关系**是集合元素间的一种二元关系, 以符号 $\sim$ 表示, 它满足以下三个条件: 
>
> 1. **自反性**: 对于所有 $a \in A$, 有 $a \sim a$.
> 2. **对称性**: 对于所有 $a, b \in A$, 如果 $a \sim b$, 则 $b \sim a$.
> 3. **传递性**: 对于所有 $a, b, c \in A$, 如果 $a \sim b$ 且 $b \sim c$, 则 $a \sim c$.

> [!Note]
>
> ==等价关系==
>
> - 整数集 $ℤ$ 模 2 的等价关系: 如果 $a, b$ 除 2 的余数相等则 $a$ 和 $b$ 等价. 在该等价关系下, 所有偶数 (除2余0) 构成了一个等价类, 所有奇数 (除2余1) 构成了另一个等价类.
> - 记某个班全体同学构成的集合为 $A$, 按照座位我们规定, 如果 $a, b$ 两位同学坐在同一列则 $a$ 和 $b$ 等价. 在该等价关系下, 每一列的同学构成一个等价类. 老师就经常利用上述等价关系对同学进行分组或收发作业.

> [!Important]
> 
> ==一些常用的集合性质==
> 
> - 有限集 (有穷集) : 含有有限个元素的集合, 如 $\{ 2, 4, 5, 8\}$.
> - 无限集 (无穷集) : 含有无穷多个元素的集合, 如自然数集 $\mathbb{N}$.
> 
> **数集**中常用的性质还有
> 
> - 有界集: 集合中的所有元素 $x$ 的绝对值都小于 $M$, 如开区间 $(0, 1)$.
> - 无界集: 如 $(0, +\infty)$.

#### 集合之间的关系

> [!TIP]
> 
> 集合 $A$ 和 $B$ 之间能不能进行比较?有没有大小关系? 例如, 如何通过数学的语言来描述一个班全体男生构成的集合 $A$, 全体女生构成的集合 $B$, 以及全班所有同学构成的集合 $C$ 之间的关系呢?

> [!IMPORTANT]
>
> ==两个集合间的包含关系==
>
> 如果集合 $A$ 中**任意**_~Rd~_一个元素都是集合 $B$ 中的元素, 则称 $A$ **包含于** $B$ (或 $B$ **包含**$A$), 记作 $A\subseteq B$ 或 $B\supseteq A$, 此时称 $A$ 为 $B$ 的 **子集** (subset). 
> 
> 基于集合的包含关系我们再引入两个概念: 
> 1. **空集**: 不包含任何元素的集合叫做 **空集** (emptyset), 记为 $\phi $, 空集是任何集合的子集.
> 2. **集合相等**: 如果 $A\subseteq B$, 同时 $B\subseteq A$, 则集合 $A$, $B$ 中的元素是完全一样的, 此时我们说集合 $A$ 等于集合 $B$, 记作$A=B$.
> 
> 在上面的例子中, 全体男生构成的集合 $A$ 包含于全班同学构成的集合 $C$, 全体女生构成的集合 $B$ 也包含于集合 $C$, 但是 $A, B$ 之间没有包含与被包含的关系.

> [!Caution] 
> ==借助图像表示集合间的包含关系==
> 
> 集合 $A$ 包含于集合 $B$ 可以用下图表示
> 
> ![集合的包含关系](../media/img/1.2.jpg) 

> [!Note]
> 
> 下面例子中的 $A$ 和 $B$ 存在包含关系:
> 
> 1. $A=\left\{ 1,2,3 \right\},$  $B=\left\{1,2,3,4,5\right\}.$
> 2. $A$ 为所有等腰三角形, $B$ 为所有三角形.
> 
> 下面例子中的 $A$ 和 $B$ 不存在包含关系 (找反例: 是否能找到 $A$ 中的一个元素, 使其不在 $B$ 中):
> 
> 1. $A=\left\{ 1,2,6 \right\}$, $B=\left\{1,2,3,4,5\right\}$.
> 2. $A$ 为所有等腰三角形, $B$ 为锐角三角形.
> 

#### 集合之间的运算

> [!TIP]
> 
> 集合 $A$ 和 $B$ 之间能不能做运算? *`加`* *`减`*法是没有的, 但是有*`交`* *`并`* *`补`*运算. 

> [!Important]
> 
> ==交集==
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

> [!Note]
> 1. $A=\left\{2, 4, 6, 8, 10 \right\}$, $B=\left\{ 3, 5, 8, 12 \right\}$,  则 $ A \cap B =\left\{ 8 \right\}$. 
> 2. $A=\left \{全校女同学 \right \} $, $B=\left \{所有高一级同学 \right \} $,  $A \cap B = \left \{ 高一级全体女同学 \right \}$.

> [!important]
> 
> ==并集==
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

> [!Note]
> 
> 1. $A=\left \{ 1,3,5 \right \} $, $B=\left \{ 2,4,6 \right \} $, $A \cup B=\left \{ 1,2,3,4,5,6 \right \} $；
> 2. $A=\left \{有理数 \right \} $, $B=\left \{无理数 \right \} $, $A \cup B=\left \{实数 \right \} $.

> [!Important]
> 
> ==补集==
> 
> 如果集合 $A$ 是集合 $B$ 的子集, 则所有 $B$ 中不属于 $A$ 的所有元素构成的集合称为 $A$ 相对于 $B$ 的 **补集** (complementary set), 记作 $C_BA$ 或 $A^C$, 即
> 
> $$
> \bar{A} = C_B A = \{x \in B: \ x\notin A\}
> $$
> 
> 下图展示了补集运算: 
> 
> ![补集](../media/img/image.png)

> [!Note]
> 
> 1. $A=\left \{ 1,3,5 \right \} $, $B=\left \{ 1,2,3,4,5,6 \right \} $, $C_BA = \{ 2, 4, 6\}$.
> 2. $A=\left \{有理数 \right \} $, $B=\left \{ 实数 \right \} $, $C_BA = \{无理数\}$.

> [!Warning]
>
> ==图像掩码与集合的交集==
>
> 假设在一个图像里面我们有两个感兴趣的区域集合 $A$ 和集合 $B$, 分别对应掩码 $M_A$ 和 $M_B$, 则集合 $A \cap B$ 对应的掩码可以通过逐像素相乘运算得到, 即 $ M_{A \cap B} = M_A * M_B$, 其中 $*$ 表示每个对应位置的像素分别相乘.
>
> *==掩码的交集==*
> |![alt text](../media/img/mask_a.png)|![alt text](../media/img/mask_b.png)|![alt text](../media/img/intersection_mask.png)|
> |:-:|:-:|:-:|
> |$M_A$|$M_B$| $M_{A \cap B}$|
>
> ==图像掩码中的集合并运算==
>
> 假设在一个图像里面我们有两个感兴趣的区域集合 $A$ 和集合 $B$, 分别对应掩码 $M_A$ 和 $M_B$, 则集合 $A \cup B$ 对应的掩码可以通过逐像素作“或”运算得到.“或”运算的符号为 $ \lor$, 运算规则为 
>
> $$
> 1 \lor 1 = 1, \ 1\lor 0 = 0 \lor 1 = 1, \ 0 \lor 0 = 0.
> $$
>
> 我们有 $ M_{A \cup B} = M_A \lor M_B$.
>
> *==掩码的并集==*
>
> |![image\label{testlab1}](../media/img/mask_a.png)| ![alt text](../media/img/mask_b.png)| ![alt text](../media/img/union_mask.png)|
> |:-:    |:-:    |:-:            |
> |$M_A$|$M_B$| set $M_{A \cup B}$|
>
> ==图像掩码与集合的补集==
>
> 如下图, 假设在一个图像里面我们有一个感兴趣的区域集合 $A$, 对应掩码 $M_A$, 则图像中我们不感兴趣的区域可以看成是集合 $A$ 在以整个图像为全集的补集 $C_{M}A $,  $C_{M}A $ 可以通过取反运算得到, 即 $ M_{C_{M}A} = \mathrm{NOT}(M_A)$, 其中 $\mathrm{NOT}$ 表示每个对应位置的像素分别取反运算($\mathrm{NOT}(0) = 1, \mathrm{NOT}(1) = 0$).
>
> *==掩码的补集==*
> |![alt text](../media/img/mask_a.png)|![alt text](../media/img/comp_mask.png)|
> |:-:|:-:|
> |$M_A$|$M_{C_{M}A}$|



> [!Warning]
> 
> ==训练集和测试集==
> 
> **训练集和测试集**是机器学习中常见的两个集合. 假设我们手中有一个包含1000张图像的数据集, 我们通常会将这些图像分成两个不相交的部分: 一部分用来训练模型 (称为训练集), 另一部分用来评估模型性能 (称为测试集). **训练集是图像全集的一个子集**, 同样, 测试集也是全集的一个子集, 但它们**没有交集**——也就是说, 一个图像不能同时出现在训练集和测试集中. 这种划分就是集合的一个典型应用: 给定全集 $A$, 我们从中选出两个不相交的子集 $B$ 和 $C$, 满足 $A = B \cup C$ 且 $B \cap C = \emptyset$. 在实际应用中, 我们通常用70%的图像作为训练集, 30%的图像作为测试集, 也就是说我们从集合的角度划分数据, 保证模型的训练与测试在**不同的样本**上进行, 从而更好地评估模型的泛化能力.


### 1.2 映射

> [!TIP]
>
> 前面所讲的**集合**的概念是为了给**映射**做铺垫. 映射是集合与集合之间的关联, 集合对数学就好像计算机中的**键盘**, 无非就是100多个键; 而映射对数学就好像计算机中的**程序**, 变幻无穷. 
>
> 回到我们之前给学生打分的例子, 为了更加合理的给学生打分, 我们可以把学生努力的程度转化成数值, 然后把分数对应成绩点, 从而把打分的问题变成了一个从数到数的映射, 也就是**函数**. 可以看到函数是用来解决具体问题的一个很方便的工具.
>
> ![图片](../media/img/chpt1_function_final.svg)
>

#### 映射的概念

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
> ![映射](../media/img/image-2.png)
> 
> 图中箭头表示了集合 $A$ 中元素与集合 $B$ 中元素的对映关系. 
> 
> 根据定义, 映射需要满足两个要求: **随处取值, 唯一对映**.
>
> - **随处取值**是指 $A$ 中的任何一个元素在 $B$ 中都有对映；
> - **唯一对映**是指 $f$ 可以把 $A$ 中的不同元素映射到 $B$ 中的同一个元素, 但不能把 $A$ 中的一个元素映射到 $B$ 中的多个元素.

> [!Caution]
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
> ![Function](../media/img/function.png)

> [!Caution]
>
> ==映射与函数==
>
> 映射的概念如此重要, 以至于在不同的场合映射还有不同的专业名称. 在计算机编程中, **函数**(function) 就是映射, 是一个从输入 (可以是数、数组、函数等）到输出 (也可以是数、数组、函数等）的一系列操作. 在数学里, 当集合 $A$ 和 $B$ 都是数集的时候, 映射也叫做**函数 **(function), 如函数 $f(x) = 2x+3$ 是一个从实数集到实数集的一个映射. 函数是高等数学上册的主要研究对象, 而多元函数 (从 $n$ 维实数空间到实数空间的映射, $n>2$ )则是高等数学下册的主要研究对象 (前面的给学生打分的例子可以进一步细化成一个多元函数, 也就是把平时, 期中, 期末和其它因素的成绩统一考虑, 然后映射到一个分数上).
>
> ![图片](../media/img/chpt1_mvfunction_final.svg)

#### 数列

> [!TIP]
> 
> **数列**是一类特殊的映射, 它把自然数集 $\mathbb{N}$ 映射到实数集 $\mathbb{R}$ 中, 进一步, 这还是一个数到数的映射, 因此同时也是一个函数, 这个函数可以记作 $a(n)$, 不过更多的时候我们会把 $n$ 作为下标, 以 $a_n$ 表示数列得第 $n$ 项, 并以 $\{ a_n \} $ 表示整个数列.

---

> [!Note]
> ==等差数列==
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

> [!Note]
> ==等比数列==
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

#### 函数

> [!TIP]
>
> 函数是用数学解决实际问题的重要**工具**, 函数之于数学就像**程序**之于计算机. 
> 
> 学习函数的时候不要去跟冰冷的公式硬刚, 而应该把函数的图像放在心里, 产生画面感, 把公式具象化, 成为直觉的一部分. 因此, **函数的图像非常重要!**_~Rd~_

> [!important]
> 
> ==函数的定义==
>
> 从**数集** $A$ 到**数集** $B$ 的映射 $f:A \rightarrow B$ 称为**函数** (function). 可以把函数写成 $y = f(x)$ 的形式, 并把 $x$ 称为**自变量**, $y$ 称为 $x$ 对映的**函数值**.
> 

> [!note]
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

> [!Note]
> 
> ==函数的性质==
>
> - 单调性
> - 奇偶性
> - 周期性
> 

> [!Caution]
>
> ==反函数== 
>
> **反函数**是**逆映射**的一个特例, 对于函数 $f: x \rightarrow y$ (也要求 $f$ 是一一映射), 其反函数为 $f^{-1}: y \rightarrow x$.
>
> [!Note]
> - $y = 3x + 1$ 的反函数为 $y = (x-1)/3$
> - $y = \mathrm{e}^x$ 的反函数为 $y = \mathrm{ln}x$. 
>
> 反函数本质上是把 $x$ 和 $y$ 的顺序对调了一下, 因此不难发现原函数与反函数的图像是关于直线 $y = x$ 对称的.
> 
> ![反函数图形的对称性](../media/img/inverse_function.png#400w)

> [!Caution]
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

> [!Warning]
>
> ==深度学习与复合函数==
>
> ![神经网络](../media/img/network.png#400w) 
> 
> 人工智能中的核心技术为**深度学习**, 深度学习的背后其实就是有很多层 (从几十到几千层都有) 的**神经网络** (Neuron Network). 神经网络的本质正是复合函数. 对于图中所示的神经网络, 从最左端的**输入信号**开始, 之后每一层都是上一层信号的复合, 因此神经网络就是一个复合了很多次的函数, 这个函数把输入 (比如一张图片) 映射到我们关心的结果 (比如图像有猫还是狗的概率). 


## 2. 极限

> [!TIP] 
> 
> **极限**是高等数学有别于初等数学的核心概念. 极限的出现代表了数学思想的一次转变, 而促成这一转变的动机来自于现实问题中对**曲线**相关问题的需求. 在初等数学中我们会计算矩形的周长和面积, 会计算三角形的周长和面积, 甚至是任意多边形的周长和面积, 但是, 这些都是由直线构成的结构, 而到了曲线大家就不会了. 曲线的长度怎么算? 由曲线构成区域的面积怎么算? 尽管我们初中就知道圆的周长是 $2\pi r$, 面积是 $\pi r^2$, 但是为什么是这样, 只有运用微积分才能给出严格的证明.
> 
> 如果我们拿西游记作为类比, 那初等数学就是**小乘佛法**, 可以修身养性, 而微积分则是**大乘佛法**, 可以普度众生. 数学史上, 微积分的确立历经了千难万险, 九九八十一难, 要说这里面的**孙悟空**之名, 我认为当属**牛顿**: 牛顿的时代还没有微积分, 正是他开创性的运用我们今天微积分中的各种思想和方法, 成功的解决了**天体运行理论** (注意天体运行的轨迹就是**曲线**), 开启了人类理性思潮的革命.
> 
> 今天, 我们将追随西天取经的足迹, 开启一场精神朝圣之旅. 一路上我们会经历重重磨难, 但最终我们会穿上牛顿的衣钵, 运用我们所学的微积分, 来推导**天体运行理论**, 揭示宇宙运行的奥义. 而**极限**_~Rd~_是我们西行路上的第一难, 这个**观念上的转变**是重要的, 我们一开始慢慢来, 好好的理解, 这个转变做得**越深刻越彻底**, 对以后的学习就越有帮助.

### 2.1 数列极限

> [!tip]
> 
> ==极限与圆的面积==
> 
> 圆的面积怎么算? 我们来看教材 P18 的例子. 这个例子体现了极限中从有限到无限再到极限的思想: 为了计算圆的面积, 我们构造了一**系列**圆的内接正多边形, 这些正多边形的面积是可以通过初等数学计算的, 我们把它们的面积记作 $A_n, n = 1, 2, \cdots$. 通过**直觉**我们能感受到, **当 $n$ 趋于无穷大时, $A_n$ 的面积会无限接近圆的面积**_~Rd~_. 接下来我们要做的就是**把这个直觉通过数学语言给严格化**. 
> 
>
> 
> 极限是一个**动中取静**_~Rd~_的过程. 
> 
> - 什么在动?
> 	在上面的例子中, 我们构造了一个数列 $\{ A_n \}$, 前面说过数列是个从自然数集 $\mathbb{N}$ 到实数集 $\mathbb{R}$ 的映射. 我们说的**动**发生在集合 $\mathbb{N}$ 中, 指标 $n$ 从 1, 2 直到 1千, 一万 ..., 这是**数列极限**概念中**动**的部分. 
> 
> - 什么是静?
> 	**数列极限**概念中**静**的部分来自于集合 $\mathbb{R}$ 中, 它表示 $A_n$ 的取值会慢慢**趋于稳定**, 到最后**几乎不变**了, 数学上我们称这种行为叫**收敛**. 
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

>**直觉**_~Rd~_: 所以数列 $\{a_n\}$ 有极限就是, 当 $n$ 足够大时, $a_n$ 的值无限接近某个数 $A$.

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

> [!Note]
> 
> 上述定义把数列极限的直觉具象化了, 从而使得直觉变得可操作了. 根据定义, 我们现在可以严格的判断前面例子中数列的极限.
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
> 在极限的概念里, **有限**和**无限**, **动**和**静**交汇到了一起.
> 
> - 任意改变数列的有限多项, 不影响极限的收敛.

> [!caution]
> 
> ==数列极限的几条性质 (了解, 不需要证明)==
> 
> 1. 如果数列 $a_n$ 有极限, 那么它的极限唯一.
> 2. 如果数列 $a_n$ 有极限, 那么数列 $a_n$ 一定有界.
> 3. 如果 $\displaystyle \lim_{n\rightarrow \infty} a_n = A$, 且 $A > 0$, 那么存在正整数 $N$, 当 $n > N$ 时有 $x_n > 0$.
> 4. 如果 $\displaystyle \lim_{n\rightarrow \infty} a_n = A$, 那么 $a_n$ 的任一子数列的极限也是 $A$.

### 2.2 函数极限

> [!tip]
> 
> 函数极限跟数列极限本质上都是极限, 都是**动中取静**, 只不过数列极限中动的是 $n$, 而函数极限中动的是自变量 $x$. 之前我们强调过**函数图像**的重要性, 函数的极限过程同样可以通过函数图像来理解. 下面这张图可以作为我们对函数极限的**直觉**, 图中展示了 $\displaystyle \lim_{x\rightarrow 2} f(x) = 4$, 请大家想想在这个极限过程中什么在**动**, 什么是**静**?
>
>  ![函数极限](../media/img/function_limit.png)
>  

> [!note]
> 
> 考虑函数 $\displaystyle f(x) = \frac{\sin(x)}{x}$ 在 $x \rightarrow 0$ 时的极限. 从下面的表格和图像中我们**感觉**_~Gn~_这个极限等于1. 
> 
> *==函数极限举例==*
> | $x$ | $\displaystyle \frac{\sin(x)}{x}$|
> |:--:|:--:|
> |1|0.841471...|
> |0.1|0.998334...|
> |0.01|0.999983...|
> 
> ![函数图像](../media/img/sinx_over_x.png#200h)
> 

> [!warning]
>  
> **直觉**_~Rd~_: 所以函数 $\{f(x)\}$ 在 $x\rightarrow x_0$ 时有极限就是, 当 $x$ 足够接近 $x_0$ 时, $f(x)$ 的值无限接近某个数 $A$.
>
> 注意跟数列极限进行对比:
> 数列 $\{a_n\}$ 有极限就是, 当 $n$ 足够大时, $a_n$ 的值无限接近某个数 $A$.

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
> ![函数极限](../media/img/function_limit_def.jpg)

> [!note]
> 跟数列极限的定义一样, 上面关于函数极限的定义提供了一个**可操作的流程**, 能够将我们关于函数极限的直观**具象化**. 
> 
> 
> ==例1==
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
> ![函数极限例1](../media/img/function_limit_of_xsquare.png#400h)
>
> ==例2==
> 
> **直觉**: $\displaystyle \frac{\sin(x)}{x}$ 的极限为1.
> 
> **证明**: 根据定义来证明这个极限比较困难, 后面我们会介绍更加强大的方法.
> 
> ![一个重要的函数极限](../media/img/sinx_over_x_full.png#400h)
> 

> [!caution]
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

### 2.3. 极限的运算

> [!tip]
> 
> 这一讲我们主要关心如何计算极限.
> 
> - 对于一些简单的极限计算, 每次都用直觉和 $\varepsilon-\delta$ 语言来计算极限太繁琐, 也没有必要. 很多时候**极限的四则运算**能够帮上大忙.
> - 有一些困难的极限问题, 我们需要跟强大的数学结论和工具, 本讲介绍的**三明治定理**和**单调有界数列有极限**请收好.
>
> 注意, 本讲的性质和定理全部都建立在上一讲**极限定义**的基础之上, 其根本还是 $\varepsilon-\delta$ 语言.
> 

> [!warning]
>
> ==希尔伯特的旅店==
>
> 极限运算涉及到了**无限**_~Rd~_的概念, 对初学者来说这是一个之前从未踏足过的位置领域, 一些**有限世界中的直觉**将不再成立. **希尔伯特的旅店**是一个有趣的故事, 通过这个故事希望能让大家对**无限**_~Rd~_有一颗**敬畏之心**.
>
> [待补充]

> [!important]
>
> **数列极限四则运算**
> 
>  *`加减法`*: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n = A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 则 $\displaystyle \lim_{n\rightarrow \infty}[a_n \pm b_n]= A \pm B$.
>  **证明**:  
>  对任意 $\varepsilon > 0$，存在 $N_1$ 使当 $n > N_1$ 时 $|a_n - A| < \frac{\varepsilon}{2}$，  
>  存在 $N_2$ 使当 $n > N_2$ 时 $|b_n - B|$ < $\frac{\varepsilon}{2}$。  
>  取 
> 
>  $|(a_n \pm b_n)$ - $(A \pm B)$| $\leq |a_n - A|$ + $|b_n - B|$ < $\varepsilon$.
>  
> 
>  *`乘法`*: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n = A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 则 $\displaystyle \lim_{n\rightarrow \infty}a_nb_n = AB$.
>  **证明**:  
>  关键分解：\|$a_nb_n - AB$|$ = $|$a_nb_n - Ab_n + Ab_n - AB|$ $\leq $|$b_n||a_n - A| + |A||b_n - B$|  
>  因\{$b_n\}$收敛，故存在M>0使|$b_n|\leq M$  
>  对$\varepsilon > 0$，取$N_1$使当$n>N_1$时$|a_n-A|<\frac{\varepsilon}{2M}$  
>  取$N_2$使当$n>N_2$时$|b_n-B|<\frac{\varepsilon}{2|A|+1}$  
>  取$N=\max\{N_1,N_2\}$，则当$n>N$时：  
>  $|a_nb_n - AB| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$
> 
>  *`除法`*: 如果 $\displaystyle \lim_{n\rightarrow \infty}a_n= A$, $\displaystyle \lim_{n\rightarrow \infty}b_n = B$, 且 $B \ne 0$, 则 $\displaystyle \lim_{n\rightarrow \infty}\frac{a_n}{b_n}= \frac{A}{B}$.
>  **证明**:  
>  先证$\varepsilon > 0，取$$N_2$使当$n>N_2$时$|b_n-B|<\frac{\varepsilon B^2}{2}$  
>  则当$n>\max\{N_1,N_2\}$时：  
>  $\left|\frac{1}{b_n} - \frac{1}{B}\right| = \frac{|b_n - B|}{|b_nB|} < \frac{2}{|B|^2} \cdot \frac{\varepsilon B^2}{2} = \varepsilon$ 
>  再结合乘法法则即得结论。

> [!important]
>
> **函数极限四则运算**
> 
>  *`加减法`*: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 则 $\displaystyle \lim_{x\rightarrow x_0}[f(x) \pm g(x)]= A \pm B$.
>  **证明**：
> 
>  对任意$\varepsilon > 0$，由 $lim_{x \to x_0} f(x) = A$，存在 $\delta_1$ > 0，  
>  使得当 $0 < |x - x_0| < \delta_1$ 时，$|f(x) - A| < \frac{\varepsilon}{2}$  
> 
>  由 $\lim_{x \to x_0} g(x) = B$，存在 $\delta_2 > 0$，  
>  使得当 $0 < |x - x_0| < \delta_2$ 时，$|g(x) - B| < \frac{\varepsilon}{2}$  
> 
>  取 $\delta = \min\{\delta_1, \delta_2\}$，则当 $0 < |x - x_0| < \delta$ 时：  
>  $
>  |[f(x) \pm g(x)] - [A \pm B]| \leq |f(x) - A| + |g(x) - B| < \varepsilon
>  $

> [!important]
> 
>  *`乘法`*: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 则 $\displaystyle \lim_{x\rightarrow x_0}f(x)g(x)= AB$.
>  **证明**：
> 
>  对任意$\varepsilon > 0$，由 $\lim_{x \to x_0} f(x) = A$，存在 $\delta_1 > 0$，  
>  使得当 $0 < |x - x_0| < \delta_1$ 时，$|f(x) - A| < \frac{\varepsilon}{2}$  
> 
>  由 $\lim_{x \to x_0} g(x) = B，存在 \delta_2 > 0$，  
>  使得当 $0 < |x - x_0| < \delta_2$时，$|g(x) - B| < \frac{\varepsilon}{2}$  
> 
>  取 $\delta = \min\{\delta_1, \delta_2\}，则当 0 < |x - x_0| < \delta$ 时：  
>  $|[f(x) \pm g(x)] - [A \pm B]| \leq |f(x) - A| + |g(x) - B| < \varepsilon
>  $

> [!important]
> 
>  *`除法`*: 如果 $\displaystyle \lim_{x\rightarrow x_0}f(x) = A$, $\displaystyle \lim_{x\rightarrow x_0}g(x) = B$, 且 $B \ne 0$, 则 $\displaystyle \lim_{x\rightarrow x_0}\frac{f(x)}{g(x)}= \frac{A}{B}$.
> 
>  **证明**：
> 
>  先证 $\lim_{x \to x_0} \frac{1}{g(x)} = \frac{1}{B}$：  
> 
>  由 $\lim_{x \to x_0} g(x) = B \neq 0，存在 \delta_1 > 0使当 0 < |x - x_0| < \delta_1时，|g(x)| > \frac{|B|}{2}$  
> 
>  - 对任意$\varepsilon > 0$，取 $\delta_2 > 0 使当 0 < |x - x_0| < \delta_2$ 时：  
>    $
>    |g(x) - B| < \frac{\varepsilon B^2}{2}
>    $ 
>  - 取 $\delta = \min\{\delta_1, \delta_2\}$，则当 $0 < |x - x_0| < \delta$ 时：  
>    $
>    \left| \frac{1}{g(x)} - \frac{1}{B} \right| = \frac{|g(x) - B|}{|g(x)B|} < \frac{2}{|B|^2} \cdot \frac{\varepsilon B^2}{2} = \varepsilon
>    $
> 
>  2. 再结合乘法法则即得：  
>  $
>     \lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \left( f(x) \cdot \frac{1}{g(x)} \right) = A \cdot \frac{1}{B} = \frac{A}{B}
>     $
> 

> [!note]
>
> ==极限四则运算的例子==
>
>
>
> **例1**
> 
> 证明 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$
> 
> **证明**：  
> 
>  对任意给定的 $\varepsilon > 0$，我们需要找到正整数 $N$，使得当 $n > N$ 时：  
>  $
>  \left| \frac{1}{n} - 0 \right| = \frac{1}{n} < \varepsilon
>  $ 
> 
>  解不等式 $\frac{1}{n} < \varepsilon$ 得 $n > \frac{1}{\varepsilon}$  
> 
>  取 $N = \left\lfloor \frac{1}{\varepsilon} \right\rfloor + 1$（即不小于 $\frac{1}{\varepsilon}$ 的最小整数）  
> 
>  则当 $n > N$ 时，必有 $\frac{1}{n} < \varepsilon$  
> 
>  由极限定义，$\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$ 得证  
>  **几何解释**：  
>  当 $n$ 趋近无穷大时，$\frac{1}{n}$ 无限接近于 $0$，如图像 $y=\frac{1}{x}$ 在 $x\to\infty$ 时的渐近线为 $y=0$。
> 
>
> **例2**
> 
> 计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{2n}$
> **解法1（直接法）**：  
> 由 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n}=0$ 可得：  
> $
> \lim_{n\rightarrow \infty}\frac{1}{2n} = \frac{1}{2} \cdot \lim_{n\rightarrow \infty}\frac{1}{n} = \frac{1}{2} \times 0 = 0
> $
> **解法2（$\varepsilon-N$ 定义证明）**：  
> 
> 对任意 $\varepsilon > 0$，需存在 $N$ 使得当 $n > N$ 时：  
> $\left| \frac{1}{2n} - 0 \right| = \frac{1}{2n} < \varepsilon
> $ 
> 
> 解不等式得 $n > \frac{1}{2\varepsilon}$  
> 
> 取 $N = \left\lfloor \frac{1}{2\varepsilon} \right\rfloor + 1$  ，则当 $n > N$ 时必满足 $\frac{1}{2n} < \varepsilon$  ，故极限为 $0$
>
> **几何解释**：  
> 数列 $\frac{1}{2n}$ 的收敛速度是 $\frac{1}{n}$ 的一半，但最终都趋于 $0$。
>
> **推广结论**：  
> 对任意常数 $c \neq 0$，有：  
> $
> \lim_{n\rightarrow \infty}\frac{c}{n} = 0
> $
>
> [注] 两种解法分别展示了：  
> （1）利用已知极限的性质  
> （2）严格的 $\varepsilon-N$ 语言验证
>
>
> **例3**
>>
> 计算 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n^2}$
>>
> **解法1（夹逼定理法）**：  
> 
> 注意到当 $n \geq 1$ 时：  
> $
> 0 < \frac{1}{n^2} \leq \frac{1}{n}
> $ 
> 
> 已知 $\displaystyle \lim_{n\rightarrow \infty}\frac{1}{n} = 0$  
> 
> 由夹逼定理可得：  
> $
> \lim_{n\rightarrow \infty}\frac{1}{n^2} = 0
> $
> 
> **解法2（$\varepsilon-N$ 定义证明）**：  
>
> 对任意 $\varepsilon > 0$，需存在 $N$ 使得当 $n > N$ 时：  
> $
> \left| \frac{1}{n^2} - 0 \right| = \frac{1}{n^2} < \varepsilon
> $ 
> 
> 解不等式得 $n > \frac{1}{\sqrt{\varepsilon}}$  
> 
> 取 $N = \left\lfloor \frac{1}{\sqrt{\varepsilon}} \right\rfloor + 1$  
> 
> 则当 $n > N$ 时必满足 $\frac{1}{n^2} < \varepsilon$  
> 
> 故极限为 $0$.
>
> **例4**
> 
> 计算 $\displaystyle \lim_{x\rightarrow 1}(2x-1)$
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
> **几何解释**：
> 函数 $y=2x-1$ 是斜率为 $2$ 的直线，在 $x=1$ 处函数值自然趋近于 $1$。
>
> 
> **例5**
> 
> 计算 $\displaystyle \lim_{x\rightarrow 2}\frac{x^3-1}{x^2-5x+3}$
>
> **解法1（直接代入法）**：  
> 
> 分子在 $x=2$ 处的值：$2^3 - 1 = 7$  
> 
> 分母在 $x=2$ 处的值：$2^2 - 5(2) + 3 = -3$  
> 
> 分母不为零，可直接代入：  
> $
> \lim_{x\rightarrow 2}\frac{x^3-1}{x^2-5x+3} = \frac{7}{-3} = -\frac{7}{3}
> $
>
> **解法2（因式分解验证）**：  
> 
> 检查分子分母在 $x=2$ 时是否有公因式：  
> - 分子：$x^3-1 = (x-1)(x^2+x+1)$  
> - 分母：$x^2-5x+3$ 在 $x=2$ 处不为零  
> 
> 确认无零因子相消，直接代入有效
>
> **$\varepsilon-\delta$ 证明思路**：  
> 对于任意 $\varepsilon > 0$，存在 $\delta > 0$ 使得当 $0 < |x-2| < \delta$ 时：  
> $
> \left| \frac{x^3-1}{x^2-5x+3} - \left(-\frac{7}{3}\right) \right| < \varepsilon
> $  
> 可通过控制 $x$ 在 $2$ 附近的范围（如 $\delta < 0.5$）保证分母不为零，再构造不等式。
> 
> **例6**
>
> 计算 $\displaystyle \lim_{x\rightarrow 3}\frac{x-3}{x^2-9}$
>
> **解法1（因式分解法）**：
>
> 识别不定式：直接代入得 $\frac{0}{0}$，需进一步处理
> 
> 因式分解分母：
> $x^2-9 = (x-3)(x+3)
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

### 2.4 两个重要的极限

#### 重要极限一
> [!tip]
> 还记得"割圆法"求圆面积的例子吗? 圆的内接正 $n$ 边形的面积当 $n \rightarrow \infty$ 的极限的计算最后就会落到极限 $\displaystyle \lim_{x\rightarrow 0} \frac{\sin(x)}{x}$ 的计算, 这个极限与圆周率 $\pi$ (**阿基米德数**_~Rd~_)有着深刻的联系.

> [!warning]
> 
> ==圆内接正多边形的面积==

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
> **示例**：  
> 证明 $\displaystyle \lim_{x\to 0} x^2 \sin\left(\frac{1}{x}\right) = 0$  
> 
> - 因 $-1 \leq \sin\left(\frac{1}{x}\right) \leq 1$，故 $-x^2 \leq x^2 \sin\left(\frac{1}{x}\right) \leq x^2$  
>- 由 $\displaystyle \lim_{x\to 0} -x^2 = \lim_{x\to 0} x^2 = 0$ 得证  
> 

> [!caution]
>
> **证明** $\displaystyle \lim_{x\rightarrow 0} \frac{\sin(x)}{x} = 1$
> 
> ![一个重要的函数极限](../media/img/sinx_over_x_full.png#400h)
> 
> ##### 几何法证明
> 1. **单位圆构造**：
>   - 考虑单位圆（半径 \( r = 1 \)）中角度 \( x \in (0, \frac{\pi}{2}) \)   - 定义：
>     - \( \sin x \) 为对边长度
>     - \( x \) 为圆弧长度（弧度制）
>     - \( \tan x \) 为切线长度
> 2. **面积比较**：
>    $ \text{面积} \triangle OAP < \text{扇形面积} OAP < \text{面积} \triangle OAT$
>    即：$ \frac{1}{2} \sin x < \frac{1}{2} x < \frac{1}{2} \tan x $
> 3. **化简不等式**：
> $\sin x < x < \tan x \implies 1 < \frac{x}{\sin x} < \frac{1}{\cos x}$
> 取倒数得：$ \cos x < \frac{\sin x}{x} < 1$
> 
> 4. **应用夹逼定理**：
>     $
      \lim_{x \to 0} \cos x = 1 \quad \text{且} \quad \lim_{x \to 0} 1 = 1
      $
      故：
      $
      \lim_{x \to 0} \frac{\sin x}{x} = 1
      $

> [!warning]
> 
> ==注意事项==
> 
> 1. 角度 \( x \) 必须使用弧度制
> 2. 对于 \( x < 0 \) 的情况，利用奇函数性质：
> $
>  \frac{\sin(-x)}{-x} = \frac{\sin x}{x}
>  $
> 3. 该极限是推导三角函数导数的基础

#### 重要极限二
> [!tip]
> 
> 极限 $\displaystyle \lim_{n\rightarrow \infty} \left(1+\frac{1}{n}\right)^{n}$ 与无理数 $\mathrm{e}$ (**欧拉数**_~Rd~_)有密切的联系. Jacob Bernoulli 于1683年在研究**复利**的时候考虑过这个数列的极限.
> 
> ==复利与无理数 $\mathrm{e}$==
> 
> ![Jakob Bernoulli](../media/img/Jakob_Bernoulli.jpg#400h)
> 
> **雅各布·伯努利与数e的发现**
>
> **雅各布·伯努利**（Jacob Bernoulli，1654-1705）在研究**复利计算**时发现, 
> - 年复利 → 2.00美元  
> - 半年复利 → 2.25美元  
> - 日复利 → ≈2.7146美元  
> 最终确定极限值 ≈ 2.7182818
> 发现常数**e**：  
> $$
> e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
> $$
> ![数列的值](../media/img/limit_to_e.png#400h)

> [!important]
> 
> ==单调有界数列有极限==
>

> [!note]
> **证明** $\displaystyle \lim_{n\rightarrow \infty} \left(1+\frac{1}{n}\right)^{n} = \mathrm{e}$
>
> 1. **单调性证明**：
>    - 使用二项式定理展开：
>    $
>    \left(1+\frac{1}{n}\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k}
>    $
>    - 通过比较相邻项证明数列单调递增
>
> 2. **有界性证明**：
>    - 证明展开式小于3：
>    $
>    \left(1+\frac{1}{n}\right)^n < 1 + 1 + \frac{1}{2!} + \cdots + \frac{1}{n!} < 3
>    $
>
> 3. **极限存在性**：
>    - 由单调有界定理，极限存在
>    - 定义该极限为e

> [!note]
>
> **证明** $\displaystyle \lim_{x\rightarrow 0} \left(1+x\right)^{\frac{1}{x}} = \mathrm{e}$
>
>    对任意小的\( x \)，取整数\( n \)使得：
>    $\frac{1}{n+1} \leq x \leq \frac{1}{n}
>    $
>    - 建立不等式：
>       $
>       \left(1+\frac{1}{n+1}\right)^n \leq (1+x)^{1/x} \leq \left(1+\frac{1}{n}\right)^{n+1}
>       $
>    - 当$ x \to 0 $时$ n \to \infty $，两边极限均为$e$. 

> [!warning]
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

### 2.5 复合函数的极限

> [!tip] 
> 
> 下面的结论相当于极限运算中的换元法, 在计算极限的时候十分有用.
> 

> [!caution]
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
> 解：$\displaystyle \lim_{x \rightarrow 0} \frac{\tan (x)}{x}= \lim_{x \rightarrow 0} \left( \frac{\sin (x)}{x} \cdot \frac{1}{\cos (x)} \right) = \left( \lim_{x \rightarrow 0} \frac{\sin (x)}{x} \right) \cdot \left( \lim_{x \rightarrow 0} \frac{1}{\cos (x)} \right)=1$.
>
> **例2**
> 
> $\displaystyle \lim_{x\rightarrow 0}\frac{1-\cos(x)}{x^2}$ (P48: 例2)
> 
> 解：$\displaystyle \lim_{x \rightarrow 0} \frac{1 - \cos (x)}{x^{2}} = \lim_{x \rightarrow 0} \left( \frac{\sin^{2}(x)}{x^{2}} \cdot \frac{1}{1 + \cos (x)} \right)= \lim_{x \rightarrow 0} \left( \frac{\sin (x)}{x} \right)^{2} \cdot \lim_{x \rightarrow 0} \frac{1}{1 + \cos (x)} = \frac{1}{2}$.
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
> 解：令 $t = -x$，则当 $x \to \infty$ 时，$t \to -\infty$.  于是
> $\displaystyle \lim_{x \to \infty} \left( 1 - \frac{1}{x} \right)^{x} = \lim_{t \to -\infty} \left( 1 + \frac{1}{t} \right)^{-t} = \lim_{t \to -\infty} \frac{1}{\left( 1 + \frac{1}{t} \right)^{t}} = \frac{1}{e}$.
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
> - 方法一: 用定义证明.
> 解：当 $ a = 0 $ 时，所给数列为常数列，显然有此结论.以下设 $a ≠ 0$.
> 由不等式变形：
> $$\begin{aligned}\left| \frac{\sqrt{n^2 + a^2}}{n} - 1 \right|&= \frac{\sqrt{n^2 + a^2} - n}{n} \\&= \frac{a^2}{n(\sqrt{n^2 + a^2} + n)} \\&< \frac{a^2}{2n^2}\end{aligned}$$
> 要使 $\displaystyle \left| \frac{\sqrt{n^2 + a^2}}{n} - 1 \right| < \varepsilon $，只需满足：$\displaystyle \frac{a^2}{2n^2} < \varepsilon \quad \Rightarrow \quad n > \frac{|a|}{\sqrt{2\varepsilon}}$.
> 取 $ \displaystyle \ N = \left\lceil \frac{|a|}{\sqrt{2\varepsilon}} \right\rceil $，则当 $ n > N $ 时，有：$\displaystyle \lim_{n \to \infty} \frac{\sqrt{n^2 + a^2}}{n} = 1$
> 
> - 方法二: 用极限运算和复合函数的极限证明.
> 解：约简分式为：$ \displaystyle \frac{\sqrt{n^{2} + a^{2}}}{n} = \sqrt{\frac{n^{2} + a^{2}}{n^{2}}} = \sqrt{1 + \frac{a^{2}}{n^{2}}} $
> 设两个基本函数：内层函数：$\displaystyle \ f(n) = 1 + \frac{a^{2}}{n^{2}}$ ，外层函数：$g(x) = \sqrt{x}$ 
> 原极限可表示为复合函数：$\displaystyle \lim_{n \to \infty} \frac{\sqrt{n^{2} + a^{2}}}{n} = \sqrt{\lim_{n \to \infty} \left(1 + \frac{a^{2}}{n^{2}}\right)}$
> 利用基本极限性质：$\displaystyle\lim_{n \to \infty} \frac{a^2}{n^2} = a^2 \cdot \lim_{n \to \infty} \frac{1}{n} \cdot \lim_{n \to \infty} \frac{1}{n} = 0$
因此：$\displaystyle\lim_{n \to \infty} f(n) = 1 + 0 = 1$
> 因外函数 $ g(x) = \sqrt{x} $ 在 $ x = 1 $ 处连续，满足：$\displaystyle\lim_{x \to L} g(x) = g(L)$
> 代入内部极限结果：$\displaystyle\lim_{n \to \infty} \sqrt{1 + \frac{a^2}{n^2}} = g(1) = \sqrt{1} = 1$
> 

## 3 连续函数

> [!tip]
> 
> 我们研究**极限**的一个出发点是为了研究*`函数的极大值极小值`*或*`曲线包含区域的面积`*, 要实现这一目的我们还需要引入*`微分`*和*`积分`*等数学工具, 这是后面几章的内容, 所以我们离这个目标还有一定的距离. 但是, 仅用极限的概念, 我们也能初步刻画曲线 (或函数) 本身的一些基本性质, 比如这一讲要讲的**连续性**_~Rd~_.

### 3.1 连续和间断

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

> [!caution]
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

> [!caution]
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
> ==更多间断函数的例子==
> 
>
> 
> **例5: 符号函数 $\mathrm{sgn}(x)$**
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
> **例6: $\displaystyle f(x) = \frac{1}{|x|}$**
> 
>  $f(x)$ 在 $x=0$ 点处不连续, 造成不连续的原因是 $f(0)$ 没有定义, 而且 $f(x)$ 在 $x=0$ 左右极限都趋于无穷大, 没有 (有限的) 极限. 这种情况也没有办法通过简单的修改 $f(0)$ 的值来让函数连续.
> 

> [!warning]
> 
> 函数的连续性是一个很**自然**的性质, 我们所感受到的世界就是连续的: 物体运动的轨迹, 温度的变化, 甚至计算机里的0-1也是用连续函数来近似的. 
> - 在做**目标追踪**问题的时候, 连续是一个很重要的**先验**; 
> - 在求解**物理方程**的时候, 解的连续性是一个很重要的**约束**;
> - 在人工智能里, 连续性是解决高维问题的一个**核心底层逻辑**.


### 3.2 闭区间上连续函数的性质

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
> **维尔斯特拉斯 (Weierstrass) 极值定理/极大极小值定理**
> 
> 闭区间 $[a, b]$ 上的连续函数有界, 且至少有一点 $x_1 \in [a, b]$ 使得 $f(x_1)$ 是 $f(x)$ 在 $[a, b]$ 上的最大值, 也至少有一点 $x_2 \in [a, b]$ 使得 $f(x_2)$ 是 $f(x)$ 在 $[a, b]$ 上的最小值. 

> [!warning]
>
> ==Karl Weierstrass==
>
> ![Karl Weierstrass](../media/img/karl_weierstrass.jpeg#400h) 
>

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
> **布尔查诺 (Bolzano) 定理/介值定理**
> 
> 设闭区间 $[a, b]$ 上的连续函数 $f(x)$ 在端点的值分别为 $f(a) < 0$, $f(b) > 0$, 则一定存在 $x_0 \in [a, b]$ 使得 $f(x_0) = 0$.
> 

> [!warning]
>
> ==Bernard Bolzano==
> 
> ![Bernard Bolzano](../media/img/bernard_bolzano.jpeg#400h)
> 

> [!note]
>
> **例1：证明方程 $x^{3} - 4x^{2} + 1 = 0$ 在区间 $(0,\,1)$ 内至少有一个根**
> 
> 证明：函数 $f ( x ) = x ^ { 3 } - 4 x ^ { 2 } + 1$ 在闭区间 $[0，1]$上连续，又$f ( 0 ) = 1 >0$，$f ( 1 ) = - 2< 0$.
> 根据介值定理，在 $(0，1)$内至少有一点 $ξ$，使得 $f ( η ) = 0$.
即 $ ξ ^{3 }- 4 ξ ^{ 2 } + 1 = 0$ $\quad$ $(0<ξ<1)$.
这等式说明方程 $x ^ { 3 } - 4 x ^ { 2 } + 1 = 0$ 在区间(0，1)内至少有一个根是 $ξ$． 
>
> **习题1:  设函数$f ( x )$ 在闭区间 $[ a，b ]$ 上连续，且满足$a ≤ f ( x ) ≤ b$ 对所有$x \in [ a,b ]$ 成立. 证明：存在 $c \in [ a,b ]$，使得$f ( c ) = c$**
> 
> 借助**介值定理**可以很容易证明上述定理, 其中的 $c$ 也称为函数 $f(x)$ 的不动点.


---
title: 高等数学讲义
author: 胡煜成
description: 首都师范大学高等数学A
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,讲义
vlook-chp-autonum: h1=off
vlook-query: vdl=on, ws=off
---


[toc]

# 第二章 导数

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
