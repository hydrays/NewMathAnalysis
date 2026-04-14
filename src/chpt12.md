# 第十二章 曲线积分和曲面积分

> [!TIP]
>
> 本章我们将综合运用之前所学的多元函数微分和积分工具来解决来源于物理中的核心问题, 如做功和通量等物理量的数学定义和计算, 并揭示曲线和曲面积分之间的重要而深刻的联系. 
>

## 场的概念与例子

> [!important]
> 
> **场** (Field) 是物理中的重要概念, 简单说如果空间 (如 $\mathbb{R}^2$ 或 $\mathbb{R}^3$) 中的每个点都赋予一个量 (可以是标量, 向量等), 那么我们就得到了一个场. 根据赋予的量分类, 我们有
> 
> - **标量场(scalar field)**: 空间每个点对应一个标量.
> - **向量场(vector field)**: 空间每个点对应一个向量.
> 

> [!important: 判断下列场是标量场还是向量场]
> 
> - 引力场：向量场
> - 密度场：标量场
> - 温度场：标量场
> - 电磁场：向量场
> - 流场：向量场
> 

> [!important]
> 
> 
>  标量场可以用一个**多元函数** $f(\mathbf{x}), \mathbf{x} \in \mathbb{R}^n$ 表示. 如 
>  - 二维标量场: $f(x, y)$;
>  - 三维标量场: $f(x, y, z)$.
> 
>  向量场可以用一个**多元向量值函数** $\mathbf{F}(\mathbf{x}), \mathbf{x} \in \mathbb{R}^n$ 表示, 我们经常也把 $\mathbf{F}$ 写成如下的**分量形式**.
>  - 二维向量场: $\mathbf{F}(x, y) = P(x, y)\hat{\mathbf{i}} + Q(x, y)\hat{\mathbf{j}}$;
>  - 三维向量场: $\mathbf{F}(x, y, z) = P(x, y, z)\hat{\mathbf{i}} + Q(x, y, z)\hat{\mathbf{j}} + R(x, y, z)\hat{\mathbf{k}}$.
>  其中 $P, Q, R$ 为普通的多元函数, 表示向量在 $x, y, z$-轴上的分量.


> [!important: 几个二维向量场的例子]
>
> 
>  ==例1==
>  
>  $$ \mathbf{F}(x, y) = 2\hat{\mathbf{i}} + 3\hat{\mathbf{j}}$$
> 
>  ![向量](media/img/fig2-4-1.png#200pt)
>
>  ==例2==
>  
>  $$ \mathbf{F}(x, y) = x\hat{\mathbf{i}}$$
>
>  ![向量](media/img/fig2-4-3.png#200pt)
>  
> 
>  ==例3==
>  
>  $$ \mathbf{F}(x, y) = x\hat{\mathbf{i}} + y\hat{\mathbf{j}}$$
>  
>  ![向量](media/img/fig2-4-2.png#200pt)
>  
> 
>  ==例4==
>  
>  $$ \mathbf{F}(x, y) = y\hat{\mathbf{i}} + x\hat{\mathbf{j}}$$
>
>  ![向量](media/img/fig2-4-4.png#200pt)
>  
>  



> [!note]
>
> **三维向量场**中每个点对应一个三维向量. 下面是两个典型例子，可拖动旋转查看.

<script type="importmap">
{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160/examples/jsm/"}}
</script>
<div style="display:flex;gap:10px;margin:1.2em 0 0.2em;">
<div id="vf3d-helix" style="flex:1;height:400px;min-width:0;position:relative;background:#04080f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
<div id="vf3d-dipole" style="flex:1;height:400px;min-width:0;position:relative;background:#06030f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
</div>
<script type="module" src="threejs/chapter12-vectorfield.js?v=20260414b"></script>


## 曲线积分

### 第一类曲线积分：标量场中的曲线积分

> [!TIP]
>
> 图
> $$
>\int_{L} f(x,y) \mathrm{d}x 
>$$
>$L$为平面曲线,$f(x,y)$是定义在$L$上的标量场，则积分可表示为极限形式：  
> $$
>\int_{L} f(x,y) \, \mathrm{d}x = \lim_{N \to \infty} \sum_{i=1}^{N} f(x_i, y_i)  \mathrm{d}s_i 
>$$
> 若曲线 $L$的参数方程为$x = x(t)$, $y = y(t)$，且$x(t),y(t)$在$[t_0,t_1]$上具有一阶连续导数，$x'^2(t)+y'^2(t)\neq 0$,则弧长
> $$
>\mathrm{d}s = \sqrt{[x'(t)]^2 + [y'(t)]^2} \, \mathrm{d}t
>$$
>
>此时曲线积分可转换为对参数 $ t $ 的定积分：
>
> $$
\int_{L} f(x,y) \, \mathrm{d}s = \int_{t_0}^{t_1} f(x(t), y(t)) \cdot \sqrt{[x'(t)]^2 + [y'(t)]^2} \, \mathrm{d}t
>$$
>
::: {.exercise id="chpt12-ex-001"}
:::

::: {.exercise id="chpt12-ex-002"}
:::


### 第二类曲线积分：二维向量场中的曲线积分

> [!TIP]
>
> 图
> 设向量场为  
> $$
> \vec{F}(x,y) = P(x,y)\hat{i} + Q(x,y)\hat{j},
> $$
> 力对质点沿曲线 $ L $ 所做的功 $ W $ 定义为：  
> $$
> W = \int_{L} \vec{F} \cdot \mathrm{d}\vec{r} = \lim_{N \to \infty} \sum_{i=1}^{N} \vec{F}_i \cdot \Delta \vec{r}_i,
> $$
> 将点积展开并分离坐标分量：  
> $$
> \begin{aligned}
> W &= \int_{L} \vec{F} \cdot \mathrm{d}\vec{r} = \sum_{i=1} \vec{F}_i \cdot \Delta \vec{r}_i 
> \end{aligned}
> $$
> 其中，$\mathrm{d}\vec{r}=(\mathrm{d}x,\mathrm{d}y)^T,\Delta\vec{r}=(\Delta x,\Delta y)^T$,从而
> $$
> \begin{aligned}
> W&= \sum_{i} \left( P \Delta x_i + Q \Delta y_i \right) \\
> &= \int_{L} P(x,y) \, \mathrm{d}x + Q(x,y) \, \mathrm{d}y.
> \end{aligned}
> $$
> 若曲线 $ L $ 由参数方程 $ x = x(t) $, $ y = y(t) $ 描述，且$x(t),y(t)$在$[t_1,t_2]$上具有一阶连续导数，$x'^2(t)+y'^2(t)\neq 0$  ，则
> $$
> \Delta \vec{r}_i = \left[ x'(t)\hat{i} + y'(t)\hat{j} \right] \mathrm{d}t.
> $$
> 且
> $$
> \begin{aligned}
> W &= \int_{t_1}^{t_2} \left[ P(x,y) x'(t) + Q(x,y) y'(t) \right] \mathrm{d}t \\
> &= \int_{t_1}^{t_2} \left[ P(x(t), y(t)) x'(t) + Q(x(t), y(t)) y'(t) \right] \mathrm{d}t.
> \end{aligned}
> $$
::: {.exercise id="chpt12-ex-003"}
:::

::: {.exercise id="chpt12-ex-004"}
:::

::: {.exercise id="chpt12-ex-005"}
:::

#### 封闭曲线上的第二类曲线积分

> [!TIP]
>
> 图
> $$
\vec{F}(x,y)=y\hat{i}+x\hat{j}
>$$
> $$
\oint_{C}\vec{F} \cdot \mathrm{d}\vec{r}=\int_{C_1}\vec{F} \cdot \mathrm{d}\vec{r}+\int_{C_2}\vec{F} \cdot \mathrm{d}\vec{r}+\int_{C_3}\vec{F} \cdot \mathrm{d}\vec{r}
>$$
> 其中，$$\int_{C_1}\vec{F} \cdot \mathrm{d}\vec{r}=0$$
> 对于$C_2$,其参数方程为
> $$
\begin{cases}
x=acos\theta \\
y=asin\theta
\end{cases},0\leq\theta\leq\frac{\pi}{4}
>$$
>从而
> $$
\begin{cases}
\mathrm{d}x=-asin\theta \mathrm{d}\theta \\
\mathrm{d}y=acos\theta \mathrm{d}\theta
\end{cases}
>$$
> 则
> $$
\begin{aligned}
\int_{C_2}\vec{F} \cdot \mathrm{d}\vec{r}
&= \int_0^{\frac{\pi}{4}}(-yasin\theta+xacos\theta)\mathrm{d}\theta \\
&=\int_0^{\frac{\pi}{4}}(-a^2sin^2\theta+a^2cos^2\theta)\mathrm{d}\theta \\
&= a^2\int_0^{\frac{\pi}{4}}\frac{1+cos2\theta-1+cos2\theta}{2}\mathrm{d}\theta \\
&=\frac{a^2}{2}\int_0^{\frac{\pi}{4}}cos2\theta\mathrm{d}\theta \\
&=\frac{a^2}{2}\left[sin2\theta\right]_0^{\frac{\pi}{4}} \\
&=\frac{a^2}{2}
\end{aligned}
>$$
> 对于$C_3$,其参数方程为
> $$
\begin{cases}
x=\frac{\sqrt{2}}{2}a-\frac{\sqrt{2}}{2}t \\
y=\frac{\sqrt{2}}{2}a-\frac{\sqrt{2}}{2}t
\end{cases},0 \leq t \leq a 
>$$
> 从而
> $$
> \begin{cases}
\mathrm{d}x=-\frac{\sqrt{2}}{2}\mathrm{d}t \\
\mathrm{d}y=-\frac{\sqrt{2}}{2}\mathrm{d}t
> \end{cases}
> $$
> 则
> $$
\begin{aligned}
\int_{C_3}y\mathrm{d}x+x\mathrm{d}y
&=-\frac{\sqrt{2}}{2}\int_{C_3}(\frac{\sqrt{2}}{2}a-\frac{\sqrt{2}}{2}t)\mathrm{d}t+(\frac{\sqrt{2}}{2}a-\frac{\sqrt{2}}{2}t)\mathrm{d}t\\
&=\int_0^a(t-a)\mathrm{d}t\\
&=\left[\frac{1}{2}t^2-at\right]_0^a\\
&=-\frac{a^2}{2}\\
\end{aligned}
>$$
> 综上，$$I=0+\frac{a^2}{2}-\frac{a^2}{2}=0$$


#### 两类曲线积分之间的关系

> [!TIP]
>
> 图
> $$
W=\int_L\vec{F}\cdot \mathrm{d}\vec{r}=\int_L\vec{F} \cdot \vec{\tau}\mathrm{d}s
>$$
::: {.exercise id="chpt12-ex-006"}
:::

::: {.exercise id="chpt12-ex-007"}
:::
> 
::: {.exercise id="chpt12-ex-008"}
:::


#### 特殊情况：梯度场

> [!TIP]
>
> 若$\exist f(x,y),s.t.$
> $$
\frac{\partial f}{\partial x}=P(x,y)，\frac{\partial f}{\partial y}=Q(x,y)
>$$
> 即
> $$
\mathrm{d}f=P\mathrm{d}x+Q\mathrm{d}y
>$$
> 则
> $$
\begin{aligned}
\int_LP(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y
&=\int_L \mathrm{d}f\\
&=f(x(t_2),y(t_2))-f(x(t_1),y(t_1))\\
&=f(终)-f(起)
\end{aligned}
>$$
> 在物理上，
> $$
W=f(终)-f(起)
>$$
> 若
> $$\vec{F}=(P,Q)=\nabla f=(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y})
>$$
> 则$\vec{F}$是$f$的梯度场
> **Note:并不是所有$\vec{F}$都是某函数的梯度场**

> - **Fundamental Thm of Line Integral**:
> $$
\int_LP(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y=f(x(t_2),y(t_2))-f(x(t_1),y(t_1))
>$$
> 类似于牛顿-莱布尼茨公式


> [!TIP]
>
> **假如$\vec{F}$是某函数$f$的梯度场**,会有什么结论？以**单连通区域**为前提
> - 积分与路径无关
> - $\vec{F}$是保守场，$\oint_L\vec{F} \cdot \mathrm{d}\vec{r}=0$（对所有封闭曲线$L$）
> 证明：
> 图
> $$\int_{C_1}\vec{F} \cdot \mathrm{d}\vec{r}+\int_{C_2}\vec{F} \cdot \mathrm{d}\vec{r}=\int_{C_1}\vec{F} \cdot \mathrm{d}\vec{r}-\int_{-C_2}\vec{F} \cdot \mathrm{d}\vec{r}=0$$

> [!TIP]
>
> **判定向量场 $\vec{F} = (P(x,y), Q(x,y))$ 是否为梯度场**
> 若存在函数 $f(x,y)$，使得 $\vec{F}$ 可以表示为该函数的梯度，即：
>$$
\nabla f = \frac{\partial f}{\partial x} \mathrm{d}x + \frac{\partial f}{\partial y} \mathrm{d}y,
>$$
> 则 $\vec{F}$ 是梯度场。此时，$\vec{F}$ 的分量满足：
>$$
P = \frac{\partial f}{\partial x}, \quad Q = \frac{\partial f}{\partial y}.
>$$
>由于函数 $f(x,y)$ 的二阶混合偏导数必须满足：
>$$
\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}.
>$$
>将 $\vec{F}$的分量代入，可得：
>$$
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) \implies \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}.
>$$
> 因此，**判定$\vec{F}$是梯度场的条件**为：
>$$
\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x},
>$$
::: {.exercise id="chpt12-ex-009"}
:::

> [!TIP]**有问题**
>
> **如何计算$f$**
> 图
> 已知$\vec{F}=(y,x),f(0,0)=c$
> $$
\begin{aligned}
f(x,y)&=\int_{C_1}P\mathrm{d}x+Q\mathrm{d}y+\int_{C_2}P\mathrm{d}x+Q\mathrm{d}y+f(0,0)\\
&=\int_0^x 0 \mathrm{d}x+\int_0^y
x\mathrm{d}y + c\\
&=xy+c
\end{aligned}
>$$
> 若
> $$
\vec{F}(x,y)=[(x^2+axy+3),(3y^2-2x^2)]
>$$
> $$
P_y=ax=Q_x=-4x
>$$
> 从而$a=-4$
> $$
\vec{F}(x,y)=[(x^2-4xy+3),(3y^2-2x^2)]
>$$


> [!TIP]
>
> **$curl$**
> 定义：
> $$
curl\vec{F}=Q_x-P_y=\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}
>$$
> - $$curl\vec{F}=0\Leftrightarrow 保守场（梯度场）$$
>  描述旋转
> (1)$\vec{F}=a\hat{i}+b\hat{j},curl\vec{F}=0$
> 图
> 
>  (2)$\vec{F}=x\hat{i}+y\hat{j}$
>  此时
>  $$
\frac{\partial x}{\partial y}=0,\frac{\partial y}{\partial x}=0
> $$
>  因此，
> $$
curl\vec{F}=\frac{\partial y}{\partial x}-\frac{\partial x}{\partial y}=0
> $$
>  图
> 
>  (3)$\vec{F}=-y\hat{i}+x\hat{j}$
>  此时
>  $$
curl\vec{F}=\frac{\partial x}{\partial x}-\frac{\partial (-y)}{\partial y}=1+1=2
> $$

> [!TIP]
>
> (以下文字由AI生成)
> 我们喜欢梯度场，因为它具有简洁的数学结构与明确的物理意义，其路径积分结果仅取决于起点和终点，这一特性在解决保守场相关问题时带来了极大便利。然而需要注意的是，$curl{\vec{F}}$是关键概念且它并非梯度场——梯度场的旋度恒为零，而$curl{\vec{F}}$的非零性恰恰刻画了向量场$\vec{F}$的"旋转"特性。对于一般的向量场$\vec{F}$，若想研究其曲线积分，抓住$curl{\vec{F}}$这一核心量是重要突破口：根据斯托克斯定理，向量场沿有向闭曲线的曲线积分等于其旋度通过以该曲线为边界的有向曲面的曲面积分，这一联系使得我们能够通过分析$curl{\vec{F}}$的分布与性质，更高效地求解复杂曲线积分问题，揭示向量场在空间中的动态特征。
> 图

> [!TIP]
>
> **格林公式(Green's theorem)**
> $$
\oint_C\vec{F} \mathrm{d}\vec{r}=\iint_R curl\vec{F}\mathrm{d}A
>$$
> $$
\oint_C P\mathrm{d}x+Q\mathrm{d}y = \iint_R (\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})\mathrm{d}A
>$$
> 其中
> - $C:$闭曲线，逆时针
> - $\vec{F}:$连续可微向量场
> **Note:闭曲线，逆时针，$\vec{F}$连续**


#### 格林公式

> [!TIP]
>
> **定理**：设闭区域$D$由分段光滑的曲线$L$围成，若函数$P(x,y)$及$Q(x,y)$在$D$上具有一阶连续偏导数，则有：
> **$$\oint_C P\mathrm{d}x+ Q\mathrm{d}y=\iint_R(Q_x-P_y)\mathrm{d}x\mathrm{d}y$$**
> 其中$L$是$D$的取正向的边界曲线.
> 上述公式称为**格林公式**.
> **证明**：
>  (1)special case:$Q=0$
>  $$
\int_C P \mathrm{d}x=\iint_R -P_y \mathrm{d}A
>  $$
>  同理，若$P=0$，则有
>  $$
\int_C Q \mathrm{d}y=\iint_R -Q_x \mathrm{d}A
>  $$
>  (2)简化区域
>  图
>  如图可得：
>  $$
\int_{C_1}P\mathrm{d}x=\iint_{R_1}-P_y\mathrm{d}A \\ \int_{C_2}P\mathrm{d}x=\iint_{R_2}-P_y\mathrm{d}A
> $$
>  由于
>  $$
\int_{C}P\mathrm{d}x=\int_{C_1}P\mathrm{d}x+\int_{C_2}P\mathrm{d}x \\ 
\iint_{R}-P_y\mathrm{d}A=\iint_{R_1}-P_y\mathrm{d}A+\iint_{R_2}-P_y\mathrm{d}A
> $$
>  因此，
>  $$
\int_{C}P\mathrm{d}x=\iint_{R}-P_y\mathrm{d}A
> $$
>  (3)主要部分
>  要证：
>  $$
\oint_C P\mathrm{d}x=\iint_R -P_y\mathrm{d}A
> $$
>  其中：
>  $C:simple$
>  $R:vert\ simple$
>  图
>  由图可得：
>  $$
> \oint_C P\mathrm{d}x=\int_{C_1}P\mathrm{d}x+\int_{C_2}P\mathrm{d}x+\int_{C_3}P\mathrm{d}x + \int_{C_4}P\mathrm{d}x
> $$
>  其中，
>  $$
\int_{C_1}P\mathrm{d}x=0 , \int_{C_3}P\mathrm{d}x=0 \\
\int_{C_2}P\mathrm{d}x=\int_a^bP(x,f_1(x))\mathrm{d}x \\ 
\int_{C_4}P\mathrm{d}x=\int_b^aP(x,f_2(x))\mathrm{d}x=-\int_a^bP(x,f_2(x))\mathrm{d}x
> $$
>  因此，
>  $$
\oint_C P\mathrm{d}x=-\int_a^b[P(x,f_2(x))-P(x,f_1(x))]\mathrm{d}x
> $$
>  又因为，
>  $$
\begin{aligned}
\iint_R-P_y \mathrm{d}x\mathrm{d}y&= -\int_a^b[\int_{f_1(x)}^{f_2(x)}\frac{\partial P}{\partial y}\mathrm{d}y]\mathrm{d}x\\
&=-\int_a^b[P(x,f_2(x))-P(x,f_1(x))]\mathrm{d}x
\end{aligned}
> $$
>  得证.
>
::: {.exercise id="chpt12-ex-010"}
:::

::: {.exercise id="chpt12-ex-011"}
:::

::: {.exercise id="chpt12-ex-012"}
:::

::: {.exercise id="chpt12-ex-013"}
:::

## 曲面积分

### 通量与曲面积分

> [!TIP]
>
> 图
> $$
\begin{aligned}
\int_C\vec{F}\cdot \vec{n}\mathrm{d}s&=\lim_{\Delta s \to 0}\sum_iF(x_i,y_i)\cdot \vec{n_i}\Delta s_i \\
&= \lim_{\Delta s \to 0}\sum_i[-Q_i\Delta x_i+P_i\Delta y_i]
\end{aligned}
>$$
> $$
Flux=\int_C-Q(x,y)\mathrm{d}x+P(x,y)\mathrm{d}y
>$$
> 又因为$\vec{F}=(P,Q)^T$,$\vec{F}^{\perp}=(-Q,P)$与$(P,Q)$垂直
> 从而，
> $$
Flux=\int_C\vec{F}^{\perp}\cdot \mathrm{d}\vec{r}
>$$
>
> **格林公式的flux表示**：
> 对
> $$
Flux =\oint_C-Q(x,y)\mathrm{d}x+P(x,y)\mathrm{d}y
>$$
> 应用格林公式，可得
> $$
\oint_C-Q(x,y)\mathrm{d}x+P(x,y)\mathrm{d}y=\iint_D(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y})\mathrm{d}x\mathrm{d}y
>$$
> 由散度定义：
> $$
div\vec{F}=(\frac{\partial}{\partial x},\frac{\partial}{\partial y})\cdot (P,Q)=\nabla \cdot \vec{F}
>$$
> 最终得到通量形式：
> $$
Flux =\iint_D\nabla \cdot \vec{F}\mathrm{d}A
>$$
::: {.exercise id="chpt12-ex-014"}
:::
>
> **3D情形**:$line \to surface$
>  **物理学家视角**：
> 图
>  $$
Flux=\iint_S\vec{F}\cdot \vec{n}\mathrm{d}s=\lim_{\Delta s \to 0}\sum_i\vec{F}(x_i,y_i,z_i)\cdot \vec{n_i}\Delta s_i
>  $$
>  $\mathrm{d}s \neq \mathrm{d}A=\mathrm{d}x\mathrm{d}y$
> 其中，$\vec{F}(x_i,y_i,z_i)\cdot \vec{n_i}$是高，$\Delta s_i$是底面积
> 
>  **数学家视角**:
>  先看一个简单的例子：
>  图
>  $$
\vec{F}=x\hat{i}+y\hat{j}+z\hat{k} \\ \vec{n}=\frac{1}{a}(x,y,z)^T
>  $$
> 可得
>  $$
\vec{F}\cdot \vec{n}=\left | F \right |=a
>  $$
>  因此，
>  $$
\iint_S\vec{F}\cdot \vec{n}\mathrm{d}S=a\iint_S\mathrm{d}S=4\pi a^3
>  $$
>  （特殊情形）
>  再来看一般情形：
>  图
>  $$
\vec{F}=P(x,y,z)\hat{i}+Q(x,y,z)\hat{j}+R(x,y,z)\hat{k} 
>  $$
>  $$
\iint_S\vec{F}\cdot \vec{n}\mathrm{d}S=\iint_SR(x,y,z)\mathrm{d}x\mathrm{d}y+Q(x,y,z)\mathrm{d}y\mathrm{d}z+P(x,y,z)\mathrm{d}z\mathrm{d}x
>  $$
> 其中，
>  $$
\iint_SR(x,y,z)\mathrm{d}x\mathrm{d}y=\iint_{D_xy}R(x,y,z(x,y))\mathrm{d}x\mathrm{d}y \\
\iint_SQ(x,y,z)\mathrm{d}y\mathrm{d}z=\iint_{D_xz}Q(x,y(x,z),z)\mathrm{d}x\mathrm{d}z \\
\iint_SP(x,y,z)\mathrm{d}z\mathrm{d}x=\iint_{D_yz}P(x(y,z),y,z)\mathrm{d}y\mathrm{d}z
>  $$
>  $$
\begin{aligned}
\iint_S\vec{F}\cdot \vec{n}\mathrm{d}S&=\iint_S(\vec{F_1}+\vec{F_2}+\vec{F_3})\cdot \vec{n}\mathrm{d}S\\
&=\iint_S\vec{F_1}\cdot \vec{n}\mathrm{d}S+\iint_S\vec{F_2}\cdot \vec{n}\mathrm{d}S+\iint_S\vec{F_3}\cdot \vec{n}\mathrm{d}S
\end{aligned}
>  $$
>  以$\vec{F_1}=(0,0,R(x,y,z))^T$为例，$\vec{v_1}=(\Delta x,0,\frac{\partial z}{\partial x}\Delta x),\vec{v_2}=(0,\Delta y,\frac{\partial z}{\partial y}\Delta y)$
>  则
>  $$
\begin{aligned}
\vec{n}\cdot \mathrm{d}S &= \vec{v_1}\times \vec{v_2}\\
&=
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\Delta x & 0 & \frac{\partial z}{\partial x}\Delta x \\
0 & \Delta y & \frac{\partial z}{\partial y}\Delta y
\end{vmatrix}\\
&=(-\frac{\partial z}{\partial x},-\frac{\partial z}{\partial y},1)\Delta x \Delta y
\end{aligned}
>  $$
>  从而
>  $$
\begin{aligned}
\iint_S(\vec{F_1})\cdot \vec{n}\mathrm{d}S
&=\iint_S R(x,y,z)\mathrm{d}x\mathrm{d}y\\
&=\iint_{D_{xy}}R(x,y,z)\mathrm{d}x\mathrm{d}y
\end{aligned}
>  $$
>$\vec{F_2}=(0,Q(x,y,z),0)^T$同理
>  要求：$S$的性质比较好，能同时被$(x,y),(y,z),(x,z)$参数化


### 高斯公式

> [!TIP]
>
> $$
\begin{alignat*}{3}
\text{Flux} &= \oiint _{\Sigma}P\mathrm{d}y\mathrm{d}z+Q\mathrm{d}z\mathrm{d}x+R\mathrm{d}x\mathrm{d}y &&= \iiint_D(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z})\mathrm{d}V  \\
            &= \oiint_{\Sigma}\vec{F}\cdot \vec{n}\mathrm{d}S &&= \iiint_Ddiv\vec{F}\mathrm{d}V=\iiint_D \nabla \cdot \vec{F}\mathrm{d}V \\
\end{alignat*}
>$$
::: {.exercise id="chpt12-ex-015"}
:::

::: {.exercise id="chpt12-ex-016"}
:::

::: {.exercise id="chpt12-ex-017"}
:::

::: {.exercise id="chpt12-ex-018"}
:::


### Stokes 公式

> [!TIP]
>
> - **三维空间中的曲线积分**
> 图
> $$
\vec{F}=P(x,y,z)\hat{i}+Q(x,y,z)\hat{j}+R(x,y,z)\hat{k} \\ \Delta \vec{r}=\Delta x\hat{i}+\Delta y\hat{j}+\Delta z\hat{k}
>$$
> 从而
> $$
\vec{F}\cdot\Delta \vec{r}=P\Delta x+Q\Delta y+R\Delta z \\ \int_C\vec{F}\cdot \mathrm{d}\vec{r}=\int_CP\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z
>$$
::: {.exercise id="chpt12-ex-021"}
:::
>
>
> - **曲线积分基本定理**
> 如果$f(x,y,z)$满足
> $$
\mathrm{d}f=P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z=\frac{\partial f}{\partial x}\mathrm{d}x+\frac{\partial f}{\partial y}\mathrm{d}y+\frac{\partial f}{\partial z}\mathrm{d}z
>$$
> 则
> $$
\int_CP\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z=\int_C\mathrm{d}f=f(B)-f(A)
>$$
> 保守场的条件为：
> $$
\begin{alignat*}{4}
 f(x,y,z) \,\Rightarrow \, \frac{\partial ^ 2f}{\partial x \partial y}&= \frac{\partial ^ 2f}{\partial y \partial x}\, \Rightarrow \, \frac{\partial}{\partial x}Q&&=\frac{\partial}{\partial y}P \, \Rightarrow \, Q_x &&&=P_y\\
\frac{\partial ^ 2f}{\partial y \partial z}&= \frac{\partial ^ 2f}{\partial z \partial y}\, \Rightarrow \, \frac{\partial}{\partial y}R&&=\frac{\partial}{\partial z}Q \, \Rightarrow \, R_y &&&=Q_z\\
\frac{\partial ^ 2f}{\partial x \partial z}&= \frac{\partial ^ 2f}{\partial z \partial x}\, \Rightarrow \, \frac{\partial}{\partial x}R&&=\frac{\partial}{\partial z}P \, \Rightarrow \, R_x &&&=P_z
\end{alignat*}(*)
>$$
>$f(x,y,z)$的梯度是$\vec{F}=\nabla f$
>
>
> - **定义(3D)：$curl\vec{F}=(R_y-Q_z)\hat{i}+(P_z-R_x)\hat{j}+(Q_x-P_y)\hat{k}$**
> $$
\nabla \times \vec{F}=
\begin{vmatrix}
  \hat{i} & \hat{j} & \hat{k} \\
  \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
  P & Q & R
\end{vmatrix}
= (R_y-Q_z)\hat{i}+(P_z-R_x)\hat{j}+(Q_x-P_y)\hat{k}
>$$
> **以下条件等价**
>  - $curl\vec{F}=0$
>  - 梯度场
>  - 条件(*)
>  - 路径无关
>  - 环路为零
>
::: {.exercise id="chpt12-ex-022"}
:::
>
> **$curl \vec{F}$的意义**
> 图
> $$
\vec{F}=(-y,x,0)
>$$
> $$
curl \vec{F}=\nabla \times \vec{F}=
\begin{vmatrix}
  \hat{i} & \hat{j} & \hat{k} \\
  \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
  -y & x & 0
\end{vmatrix}
= 0\cdot \hat{i}+0\cdot \hat{j}+2\cdot \hat{k}
>$$

## 总结与联系

> [!TIP]
>
>$$\nabla : (del,nabla)=(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z})^T$$
>
|  | 3D | 2D |
|:------|:------|:------|
|grad|$\nabla f=(f_x,f_y,f_z)^T$|$\nabla f=(f_x,f_y,)^T$|
|div|$\nabla \cdot \vec{F}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$|$\nabla \cdot \vec{F}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}$|
|curl|$\nabla \times \vec{F}= \begin{matrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\P & Q & R \end{matrix} $|$\nabla \times \vec{F}= \begin{matrix} \frac{\partial}{\partial x} & \frac{\partial}{\partial y} \\ P & Q \end{matrix} $|
|$\iiint_Df(x,y,z)\mathrm{d}v$|$\iint_S\vec{F}\cdot \vec{n}\mathrm{d}S$|$\int_C\vec{F}\cdot \mathrm{d}\vec{r}$|
|体积|flux|work|
|多重积分|$\iint_SP\mathrm{d}x\mathrm{d}y+Q\mathrm{d}y\mathrm{d}z+R\mathrm{d}y\mathrm{d}x$|$\int_CP\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z$|
>
> - 3D:Gauss公式
> $$
\iiint_{D}div\vec{F}\mathrm{d}v=\oiint_S \vec{F} \ cdot \vec{n}\mathrm{d}S
>$$
> - 3D:Green公式
> $$
\iint_D curl\vec{F}\mathrm{d}A=\oint_C \vec{F}\cdot \mathrm{d}\vec{r}
>$$
> - 3D:Stokes公式
> $$
work=\oint_C P\mathrm{d}x+Q\mathrm{d}y+R\mathrm{d}z=\oint_C\vec{F}\cdot \mathrm{d}\vec{r}=\iint_S(curl\vec{F})\vec{n}\mathrm{d}S=\iint_S\nabla \times \vec{F}\cdot \vec{n}\mathrm{d}S
>$$
::: {.exercise id="chpt12-ex-019"}
:::

::: {.exercise id="chpt12-ex-020"}
:::
