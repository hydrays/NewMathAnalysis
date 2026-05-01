# 无穷级数

> [!tip: 章引言]
>
> 本章把"加法"从有限多项扩展到**无限**多项 —— 这就是**无穷级数**. 收敛性、绝对收敛、幂级数、傅里叶级数, 是这条路径上的关键里程碑.
>
> 一个核心张力贯穿全章: **无限多个数相加未必有意义**. 当它有意义时, 它常常是某个简单解析对象 ($e^x$, $\sin x$, 一段方波信号) 的精确数值表达. 用简单的多项式或三角函数无穷叠加去表示复杂函数, 既是分析学最有威力的思想之一, 也是现代数值计算与人工智能的基石.

## 13.1 常数项级数的概念和性质

> [!tip: 直觉 — 用部分和定义"无穷和"]
>
> "无限多个数的和"必须先严格化. 我们用**部分和**作桥梁: $S_n = a_1 + a_2 + \cdots + a_n$. 若 $\lim_{n\to\infty} S_n$ 存在 (有限), 这个极限就被定义为无穷和.

> [!important: 定义 — 无穷级数与收敛]
>
> 给定数列 $\{a_n\}_{n=1}^{\infty}$, 称形式上的"和" $\displaystyle\sum_{n=1}^{\infty} a_n$ 为**无穷级数**. 其前 $n$ 项和
> $$ S_n = \sum_{i=1}^{n} a_i $$
> 称为级数的**部分和** (Partial sum). 若 $\displaystyle\lim_{n\to\infty} S_n = S$ 存在 (是有限常数), 则称级数**收敛 (Convergent)**, $S$ 是它的**和**; 否则称**发散 (Divergent)**.

> [!important: 经典级数 — 几何、调和、裂项]
>
> 三个最常用作参照标准的级数:
>
> **(1) 几何级数 (等比级数)**: $\displaystyle \sum_{n=1}^{\infty} a q^{n-1}$ ($a \ne 0$).
> 部分和 $S_n = a \cdot \dfrac{1 - q^n}{1 - q}$ ($q \ne 1$). 因此
> - $|q| < 1$: 收敛, 和 $= \dfrac{a}{1-q}$;
> - $|q| \ge 1$: 发散.
>
> **(2) 调和级数**: $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots$
> 通项 $\frac{1}{n} \to 0$, 但级数**发散** —— 这是"通项趋零 ⇎ 收敛"最重要的反例.
>
> **(3) 裂项相消级数**: $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n(n+1)}$.
> $$
> S_n = \sum_{k=1}^{n}\!\left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} \xrightarrow{n\to\infty} 1.
> $$
> 收敛, 和 $= 1$.
>
> > <div id="chpt13-partial-sums" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt13-partial-sums.js?v=1"></script>
>
> 上图把上述三个级数 (再加交错调和) 的部分和 $S_n$ 画作 $n$ 的函数. 点击不同按钮切换级数; 拖动滑块, 黑点标记当前 $S_N$, 灰色虚线给出极限值 (若存在). **几何级数 (蓝)** 几步就锁定到 $\frac{a}{1-q}$; **调和级数 (橙)** 缓慢但坚定地往无穷里爬; **裂项相消 (绿)** 收敛得最快; **交错调和 (红)** 围绕 $\ln 2$ 振荡, 越来越窄.

> [!important: 性质 — 收敛级数的四条基本规则]
>
> 设 $\sum u_n = s$, $\sum v_n = \sigma$ 都收敛.
>
> 1. **数乘**: $\sum k u_n = k s$ ($k$ 为常数).
> 2. **线性组合**: $\sum (u_n \pm v_n) = s \pm \sigma$.
> 3. **去掉、增加或改变有限项**, 不改变级数的收敛性 (但和会改变).
> 4. **通项必要条件**: $\sum u_n$ 收敛 $\Rightarrow \displaystyle\lim_{n\to\infty} u_n = 0$.

> [!caution: 易错 — 通项趋零是必要而非充分条件]
>
> 性质 4 的逆命题不成立. 调和级数 $\sum \frac{1}{n}$ 即是反例: 通项趋于零, 级数仍发散. 实际使用要点:
>
> - 若发现 $\lim u_n \ne 0$, 级数**必发散**;
> - 若 $\lim u_n = 0$, 仍需借助审敛法判断.

::: {.exercise id="chpt13-ex-001"}
:::

::: {.exercise id="chpt13-ex-002"}
:::

## 13.2 常数项级数的审敛法

> [!tip: 为何需要审敛法]
>
> 直接计算部分和 $S_n$ 的极限在大多数情况下不可能. 当我们只关心**是否收敛**而不求具体的和, 一组**判别法则**就成为必备工具. 接下来按"通项符号"的不同分类整理:**正项级数**、**交错级数**和**任意项级数**.

### 13.2.1 正项级数及其审敛法

> [!tip: 正项级数的关键事实]
>
> 若所有项 $u_n \ge 0$, 称 $\sum u_n$ 为**正项级数**. 此时部分和数列 $\{S_n\}$ **单调递增**, 因此其收敛性等价于"是否有界" —— 这是单调有界原理在无穷级数上的直接应用.

> [!important: 定理 — 单调有界原理 (正项级数版)]
>
> 正项级数 $\displaystyle\sum_{n=1}^{\infty} u_n$ 收敛 $\iff$ 部分和数列 $\{S_n\}$ 有界.

> [!important: 定理 — 比较审敛法]
>
> 设 $\sum u_n$, $\sum v_n$ 都是正项级数, 且自某项起 $u_n \le v_n$:
>
> - 若"大级数" $\sum v_n$ **收敛**, 则"小级数" $\sum u_n$ **收敛**;
> - 若"小级数" $\sum u_n$ **发散**, 则"大级数" $\sum v_n$ **发散**.

> [!important: 定理 — 极限比较审敛法]
>
> 设 $\sum u_n$, $\sum v_n$ 是正项级数. 若
> $$ \lim_{n\to\infty} \frac{u_n}{v_n} = l \in (0, +\infty), $$
> 则两级数**同收敛或同发散**.

> [!important: 定理 — 比值审敛法 (达朗贝尔)]
>
> 设 $\sum u_n$ 是正项级数. 若 $\displaystyle \lim_{n\to\infty} \frac{u_{n+1}}{u_n} = \rho$, 则:
>
> - $\rho < 1$: **收敛**;
> - $\rho > 1$ (或 $\rho = +\infty$): **发散**;
> - $\rho = 1$: **本法失效**, 需借助其他方法.
>
> 这是判定指数衰减/增长形级数最有力的工具.

::: {.exercise id="chpt13-ex-003"}
:::

::: {.exercise id="chpt13-ex-004"}
:::

::: {.exercise id="chpt13-ex-005"}
:::

### 13.2.2 交错级数与任意项级数

> [!important: 定理 — 莱布尼茨判别法 (交错级数)]
>
> 对交错级数 $\displaystyle\sum_{n=1}^{\infty} (-1)^{n-1} u_n$ ($u_n > 0$), 若同时满足:
>
> 1. $u_n \ge u_{n+1}$ (各项绝对值单调递减);
> 2. $\displaystyle\lim_{n\to\infty} u_n = 0$;
>
> 则级数**收敛**. 进一步有部分和误差估计 $|S - S_n| \le u_{n+1}$ —— 误差不超过被截断的下一项.

> [!important: 定义 — 绝对收敛与条件收敛]
>
> 对一般 (含正负项) 级数 $\sum u_n$:
>
> - 若 $\sum |u_n|$ 收敛, 称 $\sum u_n$ **绝对收敛**. 绝对收敛的级数必收敛, 且其重排不改变级数的和.
> - 若 $\sum u_n$ 收敛但 $\sum |u_n|$ 发散, 称 $\sum u_n$ **条件收敛**. 经典例子: 交错调和级数 $\sum (-1)^{n-1}/n$ 收敛 (莱布尼茨), 但加绝对值后是调和级数, 发散.

::: {.exercise id="chpt13-ex-006"}
:::

## 13.3 幂级数及其展开

> [!tip: 从常数项到函数项]
>
> 把级数中的常数 $a_n$ 换成函数, 就得到**函数项级数**. 其中最简单也最优美的一类形如代数多项式无限延伸 —— **幂级数**. 用幂级数逼近函数 (例如 $e^x = \sum x^n/n!$) 是泰勒展开的"无穷化"形态, 也是数值算法的基础.

> [!important: 定义 — 幂级数]
>
> 形如
> $$ \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n + \cdots $$
> 的级数称为 (中心在原点的) **幂级数**, 系数 $\{a_n\}$ 是给定常数. 一般地, 中心在 $x_0$ 处的幂级数写作 $\displaystyle\sum a_n (x - x_0)^n$.

> [!important: 定理 — Abel 收敛半径定理]
>
> 若幂级数 $\sum a_n x^n$ 在 $x = x_0 \ne 0$ 处收敛, 则对所有满足 $|x| < |x_0|$ 的 $x$, 它**绝对收敛**;
> 反之, 若在 $x = x_1$ 处发散, 则对所有 $|x| > |x_1|$ 的 $x$, 它**发散**.
>
> 推论: 幂级数的收敛域必是一个以原点为中心的对称区间.

> [!important: 定义 — 收敛半径与收敛域]
>
> Abel 定理保证存在唯一的 $R \in [0, +\infty]$, 使得
>
> - $|x| < R$ 时幂级数绝对收敛;
> - $|x| > R$ 时发散;
> - $|x| = R$ (端点 $x = \pm R$) 时收敛性需单独判定.
>
> 这个 $R$ 称为**收敛半径**. 收敛域是 $(-R, R)$ 加上端点收敛性后的具体集合.
>
> **收敛半径的求法 (比值法)**: 若 $\displaystyle \lim_{n\to\infty} \left|\frac{a_{n+1}}{a_n}\right| = \rho$, 则
> $$ R = \frac{1}{\rho} \quad (\rho = 0 \Rightarrow R = +\infty;\ \rho = +\infty \Rightarrow R = 0). $$

> [!important: 常用 — 五个麦克劳林展开]
>
> 这五个展开是数值计算与计算机算法中最常用的:
>
> 1. $\displaystyle e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \cdots \quad (x \in \mathbb{R})$
> 2. $\displaystyle \sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} \quad (x \in \mathbb{R})$
> 3. $\displaystyle \cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} \quad (x \in \mathbb{R})$
> 4. $\displaystyle \frac{1}{1-x} = \sum_{n=0}^{\infty} x^n \quad (-1 < x < 1)$
> 5. $\displaystyle \ln(1+x) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n} \quad (-1 < x \le 1)$
>
> > <div id="chpt13-taylor" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt13-taylor.js?v=1"></script>
>
> 上图直观展示了泰勒部分和 $T_N(x) = \sum_{k=0}^{N} \frac{f^{(k)}(0)}{k!}\,x^k$ (红线) 如何逐步逼近目标函数 (蓝线). 点击按钮切换 $f$, 拖动滑块改变阶数 $N$. 几个值得注意的现象: **sin/cos/exp** 在整条实轴上越走越准, $N$ 一旦大到把 $|x|$ 包住, 红蓝线几乎重合; 而 **ln(1+x)** 与 **1/(1−x)** 的级数有有限的收敛半径 ($R = 1$), 出了边界 (例如 $|x| > 1$) 红线立刻飞向无穷. 这正是 §13.3 强调"收敛半径"概念的关键原因.

::: {.exercise id="chpt13-ex-007"}
:::

## 13.4 傅里叶级数与傅里叶变换

> [!tip: 动机 — 周期信号需要不同的展开方式]
>
> 幂级数用 $x^n$ 在**某一点附近**作局部逼近, 适合"光滑函数"的局部分析. 但现实中大量信号 (声音、心电、图像纹理) 是**周期性**的, 用 $x^n$ 来逼近它们既低效又不自然.
>
> 19 世纪傅里叶提出了颠覆性的见解: **任何周期函数都可以展开为不同频率的正弦余弦波之叠加**. 这就是**傅里叶级数**, 它是现代信号处理、通信、AI 图像与音频处理的绝对基石.

### 13.4.1 三角级数与傅里叶展开

> [!important: 定义 — 傅里叶级数]
>
> 设 $f(x)$ 以 $2\pi$ 为周期 (在适当条件下), 则它可展开为**三角级数**:
> $$ f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \bigl[a_n \cos(nx) + b_n \sin(nx)\bigr]. $$
>
> **傅里叶系数**通过下列积分给出:
> $$
> a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\, dx, \quad
> a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx)\, dx, \quad
> b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx)\, dx.
> $$
>
> $a_0/2$ 是信号的"直流分量" (平均值); $a_n, b_n$ 描述各频率成分的振幅与相位.
>
> > <div id="chpt13-fourier" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> > <script type="module" src="threejs/chpt13-fourier.js?v=1"></script>
>
> 上图展示傅里叶部分和 $F_N(x) = \frac{a_0}{2} + \sum_{n=1}^{N} (a_n \cos nx + b_n \sin nx)$ (红) 逼近周期目标 (蓝) 的过程. 切换**方波**, **锯齿波**, **三角波**三种典型信号, 拖动滑块增加 $N$:
>
> - **三角波**最"光滑", 收敛速度最快 (系数衰减 $\sim 1/n^2$).
> - **锯齿波**与**方波**都有跳跃, 在跳跃点处即使 $N$ 取得很大也总有 $\sim 9\%$ 的"过冲" —— 这就是著名的 **Gibbs 现象**, 它是傅里叶级数处理不连续信号的固有特征, 反映了"逐点收敛"与"一致收敛"的差异.
>
> ::: {.fold label="为什么是这些积分公式"}
> 三角函数族 $\{1,\, \cos x,\, \sin x,\, \cos 2x,\, \sin 2x,\, \dots\}$ 在 $[-\pi, \pi]$ 上构成**正交基**: 任意两个不同函数的乘积积分为零. 假设
> $$ f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \bigl[a_n \cos(nx) + b_n \sin(nx)\bigr], $$
> 两边乘以 $\cos(kx)$ 并在 $[-\pi, \pi]$ 上积分, 利用正交性把求和号"打开", 仅保留 $k$-项, 即得 $a_k$ 的公式; 对 $\sin(kx)$ 同理得 $b_k$. 这正是"用正交基分解函数"的最早范式, 后来抽象为内积空间中的 Fourier 展开. $\blacksquare$
> :::

### 13.4.2 引入欧拉公式与复数形式

> [!tip: 简化 — 把 sin/cos 合二为一]
>
> 同时写出 $\cos$ 和 $\sin$ 累人. 欧拉公式 $e^{ix} = \cos x + i \sin x$ 提供一把统一两者的钥匙, 使傅里叶级数可以写成更简洁的指数形式.

> [!important: 欧拉公式]
>
> $$ e^{ix} = \cos x + i \sin x. $$
>
> 推论: 当 $x = \pi$ 时得到数学上最优雅的恒等式
> $$ e^{i\pi} + 1 = 0, $$
> 它把数学中最重要的五个常数 $0, 1, i, \pi, e$ 融为一体.
>
> 反解出三角函数:
> $$ \cos(nx) = \frac{e^{inx} + e^{-inx}}{2}, \qquad \sin(nx) = \frac{e^{inx} - e^{-inx}}{2i}. $$

> [!important: 定义 — 傅里叶级数的复数形式]
>
> 把欧拉公式代入实数形式并合并整理, 三项 (常数项、$a_n$ 项、$b_n$ 项) 被压缩成一个统一公式:
> $$ f(x) = \sum_{n=-\infty}^{\infty} c_n\, e^{inx}, \qquad c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x)\, e^{-inx}\, dx. $$
>
> 这里 $n$ 取遍正负整数与零, 代表信号离散的**频率**成分; $|c_n|$ 是该频率成分的**振幅**, $\arg c_n$ 是其**相位**.

### 13.4.3 从傅里叶级数走向傅里叶变换

> [!extension: 拓展 — 傅里叶变换]
>
> 傅里叶级数完美但有一个限制: **只能处理周期函数**. 若现实中只有一段语音、一张有限尺寸的图像 (它们并非周期信号), 还能用傅里叶分析吗? 微积分的极限思想再次发挥作用 —— 把**非周期信号**看成"**周期 $T \to \infty$ 的周期信号**".
>
> - 周期 $T$ 有限时, 频率取值离散 ($n = 0, \pm 1, \pm 2, \dots$), 频谱是分立的柱子.
> - 当 $T \to \infty$, 相邻频率间隔 $\Delta\omega \to 0$, 离散求和 $\sum$ 变成连续积分 $\int$.
>
> 由此得到工程界最重要的公式之一 —— **连续傅里叶变换**:
>
> **正变换 (时域 → 频域)**:
> $$ F(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-i\omega t}\, dt. $$
>
> **逆变换 (频域 → 时域)**:
> $$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega)\, e^{i\omega t}\, d\omega. $$
>
> **AI 与工程中的角色**: 计算机视觉中的图像滤波 (例如边缘提取), 语音识别中先把信号转为声谱图 (Spectrogram), 都需要先做傅里叶变换. 离散形式 (DFT 与 FFT) 是这条管线的算法核心. 严格的存在性条件、收敛性 (Dini, Dirichlet 等) 留给后续课程.
