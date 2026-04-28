# 多元函数的积分

> [!tip: 章引言]
>
> 单变量积分把一段曲线下的面积写成 $\int_a^b f(x)\,\mathrm{d}x$. 当被积对象从一段曲线变成一块薄片或一团立体, 当密度从均匀变成 $\rho(x,y)$ 或 $\rho(x,y,z)$, 我们需要新的积分: **二重积分**与**三重积分**. 本章贯穿一条物理主线 —— 不均匀薄片 / 立体的质量.
>
> 每一节都重复同样的四步: **分割 → 近似 → 求和 → 取极限**. 把这四步看清楚, 多元积分就只是单变量积分在更高维度上的自然延展.

## 物理动机: 不均匀薄片的质量

> [!tip: 动机 — 不均匀薄片的质量]
>
> 一块均匀薄片的质量 $M = \rho \cdot A$ —— 密度乘面积, 一步乘法搞定. 如果密度随位置变化, 写成 $\rho(x,y)$, 这种"乘法"还能用吗?
>
> **思路: 局部均匀, 整体求和.** 把薄片所占区域 $D$ 分成 $N$ 个互不重叠的小片, 第 $i$ 片面积记作 $\Delta A_i$. 当每片足够小时, 它内部的密度可以用一个代表点 $(x_i, y_i)$ 处的值 $\rho(x_i, y_i)$ 来近似. 因此:
> $$
> M \approx \sum_{i=1}^N \rho(x_i, y_i)\,\Delta A_i.
> $$
> 让分割越来越细 ($N\to\infty$, 且 $\max\Delta A_i \to 0$), 上面这个 Riemann 和如果有极限, 这个极限就是真正的质量.
>
> <div id="chpt11-mass-plate" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> <script type="module" src="threejs/chpt11-mass-plate.js?v=1"></script>
>
> 上图把这条思路可视化了: 颜色表示 $\rho(x,y) = 0.6 + 0.5\sin 2x\,\cos 1.5 y$ 在 $D = [0,\pi]^2$ 上的取值, 网格把 $D$ 切成 $N\times N$ 个小方块, 圆点是每块的代表点. 拖动滑块改变 $N$, 看 Riemann 和如何逐步逼近真实积分.

> [!note: 数值实验 — 收敛性]
>
> 把上图的滑块依次拨到 $N = 4, 16, 64$, 记下显示的 Riemann 和与真实积分的差距. 你会观察到: 误差大致以 $O(1/N)$ 的速度衰减 (粗网格时这条规律尤为清晰), 当 $N$ 足够大, 近似值与极限值的差小到任意指定阈值以下.
>
> 这正是"极限存在"的直观证据 —— 我们已经为非均匀薄片的"总质量"找到了精确定义. 把质量替换成"在 $D$ 上的总累积量", 把密度替换成任意函数 $f(x,y)$, 同样的步骤就给出了二重积分的一般概念.

## 把动机变成定义: 二重积分

> [!important: 定义 — 二重积分]
>
> 设 $f(x,y)$ 在有界闭区域 $D \subset \mathbb{R}^2$ 上有界. 把 $D$ 任意分割为 $N$ 个互不重叠的小区域 $\Delta D_1, \dots, \Delta D_N$, 它们的面积分别记作 $\Delta A_i$, 并在每个 $\Delta D_i$ 中任取一个代表点 $(\xi_i, \eta_i)$. 记 $\lambda = \max_i \mathrm{diam}(\Delta D_i)$ 为分割的细度. 若极限
> $$
> \lim_{\lambda\to 0}\sum_{i=1}^N f(\xi_i, \eta_i)\,\Delta A_i
> $$
> 存在且与分割方式、代表点选取无关, 则称该极限为 $f$ 在 $D$ 上的**二重积分**, 记作
> $$
> \iint_D f(x,y)\,\mathrm{d}A \quad\text{或}\quad \iint_D f(x,y)\,\mathrm{d}x\mathrm{d}y.
> $$
> 这里 $\mathrm{d}A$ 是面积元, 在直角坐标系中就是 $\mathrm{d}x\,\mathrm{d}y$.
>
> <div id="chpt11-double-integral" style="width:100%; height:440px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.2em 0;"></div>
> <script type="module" src="threejs/chpt11-double-integral.js?v=1"></script>
>
> 上图展示当 $f \ge 0$ 时的几何画面: Riemann 和是一族小柱体的体积之和, 极限值就是曲面 $z = f(x,y)$ 与底面 $D$ 之间所夹立体的体积.

> [!tip: 几何意义 — 带符号体积 vs. 纯体积]
>
> > <div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.0em 0;">
> >  <div id="chpt11-example1" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> >  <div id="chpt11-example2" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> > </div>
> > <script type="module" src="threejs/chpt11-example1.js?v=1"></script>
> > <script type="module" src="threejs/chpt11-example2.js?v=1"></script>
>
> 两图对应同一个被积函数 $z = 1 - x^2 - y^2$, 区别只在积分区域:
>
> - **左图** $D = [0,1]^2$ 包含 $z<0$ 的角落区域 (<span style="color:#b91c1c">红色</span>): 红色体积按负值计入, 绿色按正值计入, 二重积分 $\iint_D (1-x^2-y^2)\,\mathrm{d}A = \tfrac{1}{3}$ 是这两块体积的**代数和**, 即"带符号体积".
> - **右图** $D = \{(x,y): x^2+y^2\le 1, x,y\ge 0\}$ 恰好取 $z \ge 0$ 的最大区域: 此时 $\iint_D (1-x^2-y^2)\,\mathrm{d}A = \tfrac{\pi}{8}$ 等于以四分之一圆盘为底、抛物面为顶的立体的纯体积.
>
> 同一个被积函数, 选择不同的 $D$, 几何含义随之改变 —— 这正是后面"何时换坐标"问题背后的几何动机.

> [!important: 性质 — 线性 / 区域可加性 / 单调性 / 平均值]
>
> 设 $f, g$ 在 $D$ 上可积, $D = D_1 \cup D_2$ 且 $D_1, D_2$ 仅在边界相交.
>
> **(1) 线性.** 对任意常数 $\alpha, \beta$,
> $$\iint_D (\alpha f + \beta g)\,\mathrm{d}A = \alpha\iint_D f\,\mathrm{d}A + \beta\iint_D g\,\mathrm{d}A.$$
> **(2) 区域可加性.** $\iint_D f\,\mathrm{d}A = \iint_{D_1} f\,\mathrm{d}A + \iint_{D_2} f\,\mathrm{d}A.$
>
> **(3) 单调性.** 若在 $D$ 上 $f \le g$, 则 $\iint_D f\,\mathrm{d}A \le \iint_D g\,\mathrm{d}A.$ 特别地, $|\iint_D f\,\mathrm{d}A| \le \iint_D |f|\,\mathrm{d}A.$
>
> **(4) 平均值.** 设 $A = \iint_D \mathrm{d}A$ 为 $D$ 的面积, 则 $f$ 在 $D$ 上的平均值为 $\bar f = \dfrac{1}{A}\iint_D f\,\mathrm{d}A.$ 若 $f$ 连续, 存在 $(x^*, y^*) \in D$ 使 $f(x^*, y^*) = \bar f$ (二维积分中值定理).

> [!extension: 拓展 — 可积性的充分条件]
>
> 一个常用结论: 若 $f$ 在有界闭区域 $D$ 上**连续**, 则 $f$ 在 $D$ 上可积. 更一般地, 若 $f$ 在 $D$ 上有界且仅在测度为零的子集 (例如有限条曲线) 上不连续, 则 $f$ 仍然可积. 严格证明属于实分析内容, 此处仅作了解.

## 通过累次积分求解 (Fubini)

> [!tip: 直觉 — 切片求和]
>
> 计算曲面下立体的体积有一个朴素的办法: **切片**. 沿 $x$ 方向把立体切成无穷多个薄片, 每片在 $x = x_0$ 处的截面是一个二维图形, 其面积记作 $A(x_0)$; 把所有片的"面积 × 厚度"加起来, 体积 $V = \int_a^b A(x_0)\,\mathrm{d}x_0$. 而每片的截面面积 $A(x_0) = \int f(x_0, y)\,\mathrm{d}y$, 又是一个一维积分. 这样, 二重积分就被拆成了**两次一维积分**.
>
> > <div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.0em 0;">
> >  <div id="chpt11-iterated-x" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> >  <div id="chpt11-iterated-y" style="flex:1 1 320px; min-width:300px; height:380px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> > </div>
> > <script type="module" src="threejs/chpt11-iterated.js?v=1"></script>
>
> 左图沿 $x$ 切, 右图沿 $y$ 切. 拖动滑块, 高亮的截面随之扫过整个立体. 两种切法对应两种"先内后外"的累次积分顺序, 而它们都应该得到同一个体积 —— 这正是下面 Fubini 定理要保证的事.

> [!important: 定理 — Fubini (矩形区域)]
>
> 设 $f(x,y)$ 在矩形 $D = [a,b]\times[c,d]$ 上连续, 则
> $$
> \iint_D f(x,y)\,\mathrm{d}A
> = \int_a^b\!\left(\int_c^d f(x,y)\,\mathrm{d}y\right)\mathrm{d}x
> = \int_c^d\!\left(\int_a^b f(x,y)\,\mathrm{d}x\right)\mathrm{d}y.
> $$
> 即: 二重积分等于两次累次积分, 且两种顺序结果相同.
>
> ::: {.fold label="证明"}
> 把 $[a,b]$ 等分为 $m$ 段, $[c,d]$ 等分为 $n$ 段, 形成 $m\times n$ 个小矩形 $\Delta D_{ij}$, 面积 $\Delta x\,\Delta y$. 取代表点 $(x_i, y_j)$, Riemann 和为
> $$
> S_{m,n} = \sum_{i=1}^m\sum_{j=1}^n f(x_i, y_j)\,\Delta x\,\Delta y
> = \sum_{i=1}^m \left(\sum_{j=1}^n f(x_i, y_j)\,\Delta y\right)\Delta x.
> $$
> 由 $f$ 在闭矩形上一致连续, 当 $n\to\infty$ 时内层和一致地收敛到 $\int_c^d f(x_i, y)\,\mathrm{d}y$. 记此一维积分为 $A(x_i)$, 它仍是 $x$ 的连续函数. 再令 $m\to\infty$, 外层 Riemann 和收敛到 $\int_a^b A(x)\,\mathrm{d}x$. 因此
> $$
> \iint_D f\,\mathrm{d}A = \lim_{m,n\to\infty} S_{m,n} = \int_a^b\!\int_c^d f\,\mathrm{d}y\,\mathrm{d}x.
> $$
> 把内外层互换重复以上推理, 得到对偶的累次顺序. $\blacksquare$
> :::

> [!important: 定理 — 一般区域上的累次积分 (X-型 / Y-型)]
>
> 把 $D$ 按"沿哪一个方向是单调的纵向条带"分类:
>
> - **X-型区域**: $D = \{(x,y): a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$, 其中 $g_1, g_2$ 在 $[a,b]$ 上连续. 则
> $$
> \iint_D f\,\mathrm{d}A = \int_a^b\!\int_{g_1(x)}^{g_2(x)} f(x,y)\,\mathrm{d}y\,\mathrm{d}x.
> $$
>
> - **Y-型区域**: $D = \{(x,y): c\le y\le d,\ h_1(y)\le x\le h_2(y)\}$. 则
> $$
> \iint_D f\,\mathrm{d}A = \int_c^d\!\int_{h_1(y)}^{h_2(y)} f(x,y)\,\mathrm{d}x\,\mathrm{d}y.
> $$
>
> 同一个 $D$ 可能同时是 X-型与 Y-型, 此时两种顺序均可, 通常选**内层积分更易算**的那一种.
>
> > ![X-型 与 Y-型 区域](../media/img/chpt11-region-types.svg#560w)

> [!note: 例 1 — 矩形区域上的二重积分]
>
> 计算 $\displaystyle\iint_D (x+y)\,\mathrm{d}A$, 其中 $D = [0,1]\times[0,2]$.
>
> ::: {.fold label="详细计算"}
> 选择"先 $y$ 后 $x$"的顺序:
> $$
> \iint_D (x+y)\,\mathrm{d}A
> = \int_0^1\!\int_0^2 (x+y)\,\mathrm{d}y\,\mathrm{d}x
> = \int_0^1 \left[xy + \tfrac{y^2}{2}\right]_{y=0}^{y=2}\mathrm{d}x
> = \int_0^1 (2x + 2)\,\mathrm{d}x = 1 + 2 = 3.
> $$
> 反过来"先 $x$ 后 $y$"也得 3, 验证 Fubini.
> :::

> [!note: 例 2 — X-型区域]
>
> 设 $D$ 为曲线 $y = x$ 与 $y = x^2$ 在第一象限围成的区域. 求 $\displaystyle\iint_D xy\,\mathrm{d}A$.
>
> ::: {.fold label="详细计算"}
> 两曲线交于 $(0,0)$ 与 $(1,1)$. 在 $0\le x\le 1$ 上, $x^2 \le y \le x$, 因此 $D$ 是 X-型. 于是
> $$
> \iint_D xy\,\mathrm{d}A
> = \int_0^1\!\int_{x^2}^{x} xy\,\mathrm{d}y\,\mathrm{d}x
> = \int_0^1 x \cdot \tfrac{1}{2}(x^2 - x^4)\,\mathrm{d}x
> = \tfrac{1}{2}\int_0^1 (x^3 - x^5)\,\mathrm{d}x = \tfrac{1}{2}\left(\tfrac{1}{4} - \tfrac{1}{6}\right) = \tfrac{1}{24}.
> $$
> :::

> [!tip: 何时换序? — 简化计算]
>
> 当内层积分**没有初等原函数**时, 调换累次顺序常能救场. 经典例子:
> $$
> I = \int_0^1\!\int_x^1 e^{y^2}\,\mathrm{d}y\,\mathrm{d}x.
> $$
> 内层 $\int e^{y^2}\,\mathrm{d}y$ 没有初等表达, 直接算无从下手. 把积分区域 $\{0\le x\le 1,\ x\le y\le 1\}$ 重新看作 Y-型 $\{0\le y\le 1,\ 0\le x\le y\}$, 换序得
> $$
> I = \int_0^1\!\int_0^y e^{y^2}\,\mathrm{d}x\,\mathrm{d}y
> = \int_0^1 y\,e^{y^2}\,\mathrm{d}y
> = \tfrac{1}{2}(e - 1).
> $$
> 一次换序, 一个无初等原函数的难题立刻可算 —— 这正是累次积分的灵活之处.

> [!caution: 易错 — 上下限的依赖关系]
>
> 在累次积分中, **内层积分的上下限只能依赖外层变量, 反过来不行**. 比如写 $\int_a^b\!\int_{g_1(y)}^{g_2(y)} f\,\mathrm{d}y\,\mathrm{d}x$ 是错的: 内层是对 $y$ 积分, 上下限里却又出现了 $y$, 积完之后表达式仍含 $y$, 无法继续对 $x$ 积. 写累次积分时检查: 最外层积分的上下限必须是常数, 中间各层的上下限只能含**外侧**变量.

::: {.exercise id="chpt11-ex-001"}
:::

::: {.exercise id="chpt11-ex-002"}
:::

::: {.exercise id="chpt11-ex-003"}
:::

::: {.exercise id="chpt11-ex-004"}
:::

::: {.exercise id="chpt11-ex-012"}
:::

## 坐标变换

> [!tip: 直觉 — 面积元在变换下放缩多少?]
>
> 一个变换 $\varphi: (u,v) \mapsto (x,y)$ 把 $(u,v)$ 平面的一个小矩形 $\mathrm{d}u\,\mathrm{d}v$ 送到 $(x,y)$ 平面的一个**小平行四边形**. 这个平行四边形的面积一般不再等于 $\mathrm{d}u\,\mathrm{d}v$, 而是放大了某个倍数. 这个倍数就是变换的**雅可比行列式**的绝对值.
>
> > <div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.0em 0;">
> >  <div id="chpt11-jacobian-uv" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
> >  <div id="chpt11-jacobian-xy" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
> > </div>
> > <script type="module" src="threejs/chpt11-jacobian.js?v=1"></script>
>
> 上图展示线性变换 $\varphi(u,v) = (1.2u + 0.6v,\ 0.4u + 1.3v)$. 左侧 $(u,v)$ 平面上的单位正方格被均匀映成右侧 $(x,y)$ 平面上的平行四边形格. 每个小格的面积放大了 $|J| = 1.2\cdot 1.3 - 0.6\cdot 0.4 = 1.32$ 倍. 两根彩色向量正是 $\partial\varphi/\partial u, \partial\varphi/\partial v$, 它们是平行四边形的两条边.

> [!important: 定义 — 雅可比行列式]
>
> 设 $C^1$ 变换 $\varphi: (u,v) \mapsto (x,y)$, 即 $x = x(u,v),\ y = y(u,v)$. 它的**雅可比矩阵**与**雅可比行列式**分别为
> $$
> \frac{\partial(x,y)}{\partial(u,v)}
> = \begin{pmatrix}
> \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2pt]
> \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}
> \end{pmatrix},
> \quad
> J = \det\frac{\partial(x,y)}{\partial(u,v)}
> = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}.
> $$
>
> ::: {.fold label="为什么是这个公式"}
> 全微分给出
> $$
> \mathrm{d}x = \frac{\partial x}{\partial u}\,\mathrm{d}u + \frac{\partial x}{\partial v}\,\mathrm{d}v,
> \quad
> \mathrm{d}y = \frac{\partial y}{\partial u}\,\mathrm{d}u + \frac{\partial y}{\partial v}\,\mathrm{d}v.
> $$
> 把 $\mathrm{d}u, \mathrm{d}v$ 看作 $(u,v)$ 平面上沿坐标轴的两个无穷小向量, 则它们在 $(x,y)$ 平面上的像分别是行向量
> $$
> \vec a = \left(\tfrac{\partial x}{\partial u},\ \tfrac{\partial y}{\partial u}\right)\mathrm{d}u,
> \quad
> \vec b = \left(\tfrac{\partial x}{\partial v},\ \tfrac{\partial y}{\partial v}\right)\mathrm{d}v.
> $$
> 二维空间中以 $\vec a, \vec b$ 为邻边的平行四边形的有向面积等于行列式 $\det(\vec a, \vec b)$, 取绝对值即面积. 化简后:
> $$
> \mathrm{d}x\,\mathrm{d}y = |J|\,\mathrm{d}u\,\mathrm{d}v.
> $$
>
> **互逆性.** 由反函数定理, 若 $J\ne 0$, 反向变换的雅可比行列式与原方向**互为倒数**:
> $$
> \det\frac{\partial(u,v)}{\partial(x,y)} = \left[\det\frac{\partial(x,y)}{\partial(u,v)}\right]^{-1}.
> $$
> 这保证了 $\mathrm{d}u\,\mathrm{d}v$ 与 $\mathrm{d}x\,\mathrm{d}y$ 之间的双向换算前后一致.
> :::

> [!important: 定理 — 二重积分换元公式]
>
> 设 $\varphi: D' \to D$ 是 $C^1$ 双射, 在 $D'$ 内部 $J = \det\dfrac{\partial(x,y)}{\partial(u,v)} \ne 0$, 函数 $f$ 在 $D$ 上连续. 则
> $$
> \iint_D f(x,y)\,\mathrm{d}x\,\mathrm{d}y
> = \iint_{D'} f\bigl(x(u,v), y(u,v)\bigr)\,|J|\,\mathrm{d}u\,\mathrm{d}v.
> $$
>
> ::: {.fold label="证明思路"}
> 把 $D'$ 划分为若干小矩形 $\Delta_k$, 每个 $\Delta_k$ 经 $\varphi$ 映成 $D$ 中的一片"小弯曲四边形" $\varphi(\Delta_k)$. 由前面的几何论证, 当 $\Delta_k$ 足够小时, $\varphi(\Delta_k)$ 的面积近似为 $|J(u_k^*, v_k^*)|\cdot \mathrm{Area}(\Delta_k)$, 其中 $(u_k^*, v_k^*)$ 是 $\Delta_k$ 中的代表点. 于是
> $$
> \sum_k f\bigl(\varphi(u_k^*, v_k^*)\bigr)\,\mathrm{Area}(\varphi(\Delta_k))
> \approx \sum_k f\bigl(\varphi(u_k^*, v_k^*)\bigr)\,|J(u_k^*, v_k^*)|\,\mathrm{Area}(\Delta_k).
> $$
> 左侧极限是 $\iint_D f\,\mathrm{d}x\mathrm{d}y$, 右侧极限是 $\iint_{D'} f(\varphi)\,|J|\,\mathrm{d}u\mathrm{d}v$. 把误差严格控制需要 $\varphi$ 的 $C^1$ 性质保证 $J$ 在闭包上一致连续, 细节留给实分析教材. $\blacksquare$
> :::

> [!note: 例 3 — 极坐标作为重要特例]
>
> 极坐标变换 $x = r\cos\theta,\ y = r\sin\theta$ 的雅可比行列式为
> $$
> J = \begin{vmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{vmatrix} = r.
> $$
> 因此 $\mathrm{d}x\,\mathrm{d}y = r\,\mathrm{d}r\,\mathrm{d}\theta$. 这是后面所有"圆形区域"积分的工作原理.
>
> > <div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.0em 0;">
> >  <div id="chpt11-polar-rtheta" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
> >  <div id="chpt11-polar-xy" style="flex:1 1 280px; min-width:260px; height:320px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; background: #fff;"></div>
> > </div>
> > <script type="module" src="threejs/chpt11-polar-change.js?v=1"></script>
>
> 左侧 $(r,\theta)$-矩形 $[0,1]\times[0,\pi/2]$ 被等分成 $5\times 6$ 个等大小矩形, 右侧映射成四分之一圆盘的极坐标网格. 靠近 $r=0$ 的格子被压得很小, 靠近 $r=1$ 的最大 —— 这正是 $|J| = r$ 的几何含义.

> [!note: 例 4 — 用极坐标计算抛物面下的体积]
>
> 计算 $\displaystyle V = \iint_D (1 - x^2 - y^2)\,\mathrm{d}A$, 其中 $D = \{(x,y): x^2 + y^2 \le 1\}$ 是单位圆盘.
>
> ::: {.fold label="详细计算"}
> 直接用直角坐标: $D$ 在 $-\sqrt{1-x^2}\le y\le \sqrt{1-x^2}$, 内层积分能算但形状不"自然". 换极坐标: $D' = \{(r,\theta): 0\le r\le 1,\ 0\le \theta\le 2\pi\}$, 被积函数 $1 - r^2$, $\mathrm{d}A = r\,\mathrm{d}r\,\mathrm{d}\theta$. 因此
> $$
> V = \int_0^{2\pi}\!\int_0^1 (1-r^2)\,r\,\mathrm{d}r\,\mathrm{d}\theta
> = 2\pi \int_0^1 (r - r^3)\,\mathrm{d}r
> = 2\pi \left(\tfrac{1}{2} - \tfrac{1}{4}\right) = \tfrac{\pi}{2}.
> $$
> :::

> [!tip: 何时换坐标?]
>
> 几个经验法则:
>
> - 圆形 / 扇形 / 环形区域 → **极坐标** $x = r\cos\theta,\ y = r\sin\theta$.
> - 椭圆区域 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2}\le 1$ → 仿射变换 $x = au,\ y = bv$.
> - 平行四边形或线性条带 → 一般**线性变换**, 直接读出 $|J| = |\det A|$.
> - 双曲线型边界 ($xy = c$ 之类) → 取 $u = xy,\ v = x/y$ 或类似的非线性组合.
>
> 总原则: 让积分区域在新坐标下变成最简单的"标准形" (矩形 / 长方体), 哪怕被积函数稍变复杂也值得.

> [!caution: 易错 — 雅可比行列式的绝对值]
>
> 换元公式里出现的是 $|J|$, 不是 $J$. 当 $J$ 可能取负 (例如反射型变换或参数化方向反了), 漏写绝对值会让积分莫名变号. 任何"面积或体积应当为正"的情景中, $|J|$ 才是物理上正确的放缩因子.

::: {.exercise id="chpt11-ex-013"}
:::

## 推广到三维: 三重积分

> [!tip: 动机 — 不均匀立体]
>
> 把 §11.1 的薄片换成立体: 占据 $\mathbb{R}^3$ 中区域 $V$ 的物体, 密度 $\rho(x,y,z)$ 随位置变化. 同样的四步 (分割 → 近似 → 求和 → 取极限) 给出总质量
> $$
> M = \iiint_V \rho(x,y,z)\,\mathrm{d}V.
> $$
>
> > <div id="chpt11-mass-solid" style="width:100%; height:460px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.0em 0;"></div>
> > <script type="module" src="threejs/chpt11-mass-solid.js?v=1"></script>
>
> 上图把单位圆柱体上的密度 $\rho(x,y,z) = 0.5 + 0.4 z + 0.3(x^2+y^2)$ 用颜色画出来; 拖动滑块看一片片水平截面如何揭示密度的空间变化.

> [!important: 定义 — 三重积分]
>
> 设 $f(x,y,z)$ 在有界闭体 $V \subset \mathbb{R}^3$ 上有界. 把 $V$ 分割为 $\Delta V_1, \dots, \Delta V_N$, 体积分别为 $\Delta V_i$, 取代表点 $(\xi_i, \eta_i, \zeta_i) \in \Delta V_i$, 记 $\lambda = \max_i \mathrm{diam}(\Delta V_i)$. 若极限
> $$
> \lim_{\lambda\to 0}\sum_{i=1}^N f(\xi_i, \eta_i, \zeta_i)\,\Delta V_i
> $$
> 存在且与分割、代表点选取无关, 则称之为 $f$ 在 $V$ 上的**三重积分**, 记作
> $$
> \iiint_V f(x,y,z)\,\mathrm{d}V \quad\text{或}\quad \iiint_V f\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z.
> $$

> [!important: 定理 — 三维 Fubini (投影到底面)]
>
> 设 $V = \{(x,y,z): (x,y) \in D_{xy},\ z_1(x,y)\le z\le z_2(x,y)\}$, 其中 $D_{xy}$ 是 $V$ 在 $xy$-平面的投影, $z_1, z_2$ 在 $D_{xy}$ 上连续, $f$ 在 $V$ 上连续. 则
> $$
> \iiint_V f\,\mathrm{d}V
> = \iint_{D_{xy}}\!\left(\int_{z_1(x,y)}^{z_2(x,y)} f(x,y,z)\,\mathrm{d}z\right)\mathrm{d}A.
> $$
> 类似地可投影到 $xz$-平面或 $yz$-平面. 三种顺序得到相同的值, 选择何种投影由 $V$ 的几何形状决定.
>
> ::: {.fold label="证明要点"}
> 与二维 Fubini 平行: 把 $V$ 切成柱状的小条 (底为 $D_{xy}$ 中的小区域 $\Delta D$, 顶底由 $z_2, z_1$ 限定), 每条体积为 $\int_{z_1}^{z_2}\mathrm{d}z\cdot \Delta A$. 内层积分给出 $z$ 方向的"线密度", 外层是该线密度在 $D_{xy}$ 上的二重积分. 一致连续性保证内外极限可交换. $\blacksquare$
> :::

> [!note: 例 5 — 直接累次积分]
>
> 计算 $\displaystyle \iiint_{[0,1]^3} xyz\,\mathrm{d}V$.
>
> ::: {.fold label="详细计算"}
> 三个变量分离, 一次累次积分即可:
> $$
> \iiint_{[0,1]^3} xyz\,\mathrm{d}V
> = \int_0^1 x\,\mathrm{d}x \cdot \int_0^1 y\,\mathrm{d}y \cdot \int_0^1 z\,\mathrm{d}z
> = \tfrac{1}{2}\cdot \tfrac{1}{2}\cdot \tfrac{1}{2} = \tfrac{1}{8}.
> $$
> :::

> [!important: 坐标变换 — 柱面坐标]
>
> 柱面坐标 $(\rho, \theta, z)$ 与直角坐标的关系:
> $$
> x = \rho\cos\theta,\quad y = \rho\sin\theta,\quad z = z, \qquad \rho\ge 0,\ \theta\in [0, 2\pi).
> $$
> 雅可比行列式 $|J| = \rho$, 因此体积元
> $$
> \mathrm{d}V = \rho\,\mathrm{d}\rho\,\mathrm{d}\theta\,\mathrm{d}z.
> $$
> 几何上: 体积元是一根高 $\mathrm{d}z$、底面是半径 $\rho$ 处宽 $\mathrm{d}\rho$、弧长 $\rho\,\mathrm{d}\theta$ 的小薄片.
>
> > <div id="chpt11-cylindrical" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.0em 0;"></div>
> > <script type="module" src="threejs/chpt11-cylindrical.js?v=1"></script>

> [!important: 坐标变换 — 球面坐标]
>
> 球面坐标 $(\rho, \varphi, \theta)$ 的约定 ($\rho$ 是到原点距离, $\varphi$ 是与 $z$-轴正向夹角, $\theta$ 是在 $xy$ 平面的方位角):
> $$
> x = \rho\sin\varphi\cos\theta,\quad y = \rho\sin\varphi\sin\theta,\quad z = \rho\cos\varphi,
> $$
> 其中 $\rho\ge 0,\ \varphi\in[0,\pi],\ \theta\in[0, 2\pi)$. 雅可比行列式
> $$
> |J| = \rho^2\sin\varphi,
> \qquad
> \mathrm{d}V = \rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta.
> $$
>
> > <div id="chpt11-spherical" style="width:100%; height:480px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden; margin:1.0em 0;"></div>
> > <script type="module" src="threejs/chpt11-spherical.js?v=1"></script>
>
> ::: {.fold label="为什么是 ρ²sin φ"}
> 球坐标体积元可以由几何分解直接读出: 给三个变量分别一个微小增量, 立方体边长依次为
>
> - 沿 $\rho$ 方向: $\mathrm{d}\rho$;
> - 沿 $\varphi$ 方向 (以原点为圆心、半径 $\rho$ 的子午圆): $\rho\,\mathrm{d}\varphi$;
> - 沿 $\theta$ 方向 (以 $z$-轴为轴、半径 $\rho\sin\varphi$ 的纬度圆): $\rho\sin\varphi\,\mathrm{d}\theta$.
>
> 三者两两正交, 所以体积元 $= \mathrm{d}\rho \cdot \rho\,\mathrm{d}\varphi \cdot \rho\sin\varphi\,\mathrm{d}\theta = \rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta.$ 形式化的 $|J|$ 计算可作为练习, 结果一致.
> :::

> [!note: 例 6 — 球的体积, 算两遍]
>
> 半径 $R$ 的球 $V = \{x^2+y^2+z^2\le R^2\}$ 的体积 $V = \iiint_V \mathrm{d}V$, 分别在球坐标和柱坐标下计算, 互相验证.
>
> > <div style="display: flex; gap:10px; flex-wrap: wrap; margin:1.2em 0;">
> >  <div id="chpt11-example12" style="flex:1 1 320px; min-width:300px; height:400px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> >  <div id="chpt11-example13" style="flex:1 1 320px; min-width:300px; height:400px; position: relative; border:1px solid #e5e7eb; border-radius:8px; overflow: hidden;"></div>
> > </div>
> > <script type="module" src="threejs/chpt11-example12.js?v=2"></script>
> > <script type="module" src="threejs/chpt11-example13.js?v=2"></script>
>
> ::: {.fold label="详细计算 (球坐标 / 柱坐标)"}
> **球坐标.** $V = \{0\le \rho\le R,\ 0\le \varphi\le \pi,\ 0\le\theta\le 2\pi\}$:
> $$
> V = \int_0^{2\pi}\!\int_0^\pi\!\int_0^R \rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta
> = 2\pi \cdot 2 \cdot \tfrac{R^3}{3} = \tfrac{4\pi R^3}{3}.
> $$
>
> **柱坐标.** 在柱坐标下, 球内 $z$ 介于 $\pm\sqrt{R^2 - \rho^2}$ 之间, $\rho \in [0, R],\ \theta\in[0,2\pi)$:
> $$
> V = \int_0^{2\pi}\!\int_0^R\!\int_{-\sqrt{R^2-\rho^2}}^{\sqrt{R^2-\rho^2}} \rho\,\mathrm{d}z\,\mathrm{d}\rho\,\mathrm{d}\theta
> = 2\pi \int_0^R 2\rho\sqrt{R^2-\rho^2}\,\mathrm{d}\rho
> = 2\pi \cdot \tfrac{2R^3}{3} = \tfrac{4\pi R^3}{3}.
> $$
> 两种坐标给出同一答案. $\blacksquare$
> :::

> [!tip: 何时用哪种坐标?]
>
> - 圆柱形 / 含轴对称的立体 → **柱坐标**.
> - 球状 / 锥状 / 含中心对称 → **球坐标**.
> - 长方体 / 平面边界 → 直角坐标累次积分.
> - 一般原则: 让积分区域成为新坐标网格的"自然形状", 即让 $V$ 在新坐标下变成简单的矩形盒.

::: {.exercise id="chpt11-ex-010"}
:::

::: {.exercise id="chpt11-ex-011"}
:::

## 更多应用

> [!important: 应用 — 质量与质心]
>
> 设密度函数为 $\mu(x,y)$ (二维) 或 $\mu(x,y,z)$ (三维). 总质量
> $$
> M = \iint_D \mu(x,y)\,\mathrm{d}A, \qquad
> M = \iiint_V \mu(x,y,z)\,\mathrm{d}V.
> $$
> **质心**是质量分布的加权平均位置. 二维情形:
> $$
> \bar x = \frac{1}{M}\iint_D x\,\mu\,\mathrm{d}A,\quad
> \bar y = \frac{1}{M}\iint_D y\,\mu\,\mathrm{d}A.
> $$
> 三维情形把每个公式各换为 $\iiint_V$ 即可, 再增加一条 $\bar z$. 当 $\mu$ 为常数时质心退化为**几何形心**. 当 $D$ 关于某条直线对称且 $\mu$ 也对称, 质心必落在对称轴上 —— 这条对称性常常省去一半计算.

> [!note: 例 7 — 半圆盘的质心]
>
> 取 $D = \{(x,y): x^2 + y^2\le R^2,\ y \ge 0\}$ (上半圆盘), 密度均匀 $\mu \equiv 1$. 求质心 $(\bar x, \bar y)$.
>
> ::: {.fold label="详细计算"}
> 总质量 (即面积) $M = \tfrac{1}{2}\pi R^2$.
>
> $D$ 关于 $y$-轴对称, $\mu$ 也对称, 因此 $\bar x = 0$. 计算 $\bar y$, 用极坐标 $0\le r\le R,\ 0\le\theta\le \pi$:
> $$
> \iint_D y\,\mathrm{d}A
> = \int_0^\pi\!\int_0^R (r\sin\theta)\,r\,\mathrm{d}r\,\mathrm{d}\theta
> = \int_0^\pi \sin\theta\,\mathrm{d}\theta \cdot \int_0^R r^2\,\mathrm{d}r
> = 2\cdot \tfrac{R^3}{3} = \tfrac{2R^3}{3}.
> $$
> 因此 $\bar y = \dfrac{2R^3/3}{\pi R^2/2} = \dfrac{4R}{3\pi}.$
> :::

> [!extension: 拓展 — 转动惯量]
>
> 二维区域 $D$ 上密度为 $\mu$ 的质量分布, 关于某点 $(x_0, y_0)$ 的转动惯量
> $$
> I(x_0, y_0) = \iint_D \mu\bigl[(x-x_0)^2 + (y-y_0)^2\bigr]\,\mathrm{d}A.
> $$
> 它衡量物体绕该点转动时的"惯性大小": 同等角加速度所需的力矩与 $I$ 成正比.
>
> ::: {.fold label="为什么质心使 I 最小"}
> 把 $I$ 看作 $(x_0, y_0)$ 的函数. 求驻点:
> $$
> \tfrac{\partial I}{\partial x_0} = -2\iint_D \mu(x - x_0)\,\mathrm{d}A = 0
> \;\Longrightarrow\;
> x_0 = \tfrac{1}{M}\iint_D \mu x\,\mathrm{d}A = \bar x,
> $$
> 同理 $y_0 = \bar y$. 二阶项 $\partial^2 I/\partial x_0^2 = 2M > 0$ 给出极小. 因此**质心是使转动惯量最小的位置**, 这给出了"最易转动"的轴.
> :::

> [!extension: 拓展 — 平行轴定理]
>
> 设质心为 $C = (\bar x, \bar y)$, 绕过质心的 (垂直于 $D$ 的) 转动惯量记作 $I_C$. 则绕另一点 $(x_0, y_0)$ 的转动惯量为
> $$
> I(x_0, y_0) = I_C + M\,r^2,
> $$
> 其中 $r = \sqrt{(\bar x - x_0)^2 + (\bar y - y_0)^2}$ 是两轴之间的距离, $M$ 是总质量.
>
> ::: {.fold label="证明"}
> 把 $(x - x_0)^2 + (y - y_0)^2$ 改写为 $\bigl((x - \bar x) + (\bar x - x_0)\bigr)^2 + \bigl((y-\bar y) + (\bar y - y_0)\bigr)^2$, 展开:
> $$
> I = \underbrace{\iint_D \mu\bigl[(x-\bar x)^2 + (y-\bar y)^2\bigr]\,\mathrm{d}A}_{I_C}
> + \underbrace{\bigl[(\bar x - x_0)^2 + (\bar y - y_0)^2\bigr]\iint_D \mu\,\mathrm{d}A}_{M r^2}
> + 2(\bar x - x_0)\underbrace{\iint_D \mu(x - \bar x)\,\mathrm{d}A}_{=\,0}
> + 2(\bar y - y_0)\underbrace{\iint_D \mu(y - \bar y)\,\mathrm{d}A}_{=\,0}.
> $$
> 末两项的积分由质心定义恒为零, 故 $I = I_C + Mr^2.$ $\blacksquare$
>
> 推论: 在所有平行于过质心的轴中, 过质心那条转动惯量最小; 远离质心 $r$ 单位, 惯量增加 $Mr^2$.
> :::

> [!tip: 速查 — 体积 / 表面积 / 流量]
>
> - **平面区域面积**: $A = \iint_D \mathrm{d}A.$
> - **曲面 $z = f(x,y)$ 下方体积** ($f\ge 0$): $V = \iint_D f\,\mathrm{d}A.$
> - **三维区域体积**: $V = \iiint_V \mathrm{d}V.$
> - **流量、第一/第二型曲面积分、引力**: 留待第 12 章 (向量场与曲线/曲面积分) 系统处理.

::: {.exercise id="chpt11-ex-005"}
:::

::: {.exercise id="chpt11-ex-006"}
:::

::: {.exercise id="chpt11-ex-007"}
:::

::: {.exercise id="chpt11-ex-008"}
:::

::: {.exercise id="chpt11-ex-009"}
:::
