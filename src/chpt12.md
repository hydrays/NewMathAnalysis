# 第十二章 曲线积分和曲面积分

> [!tip]
>
> 本章综合运用多元函数微积分，解决物理中的核心问题：力沿路径做的功、流体穿过曲面的通量，以及将它们联系起来的三大积分定理（格林、高斯、斯托克斯）。每一个定理都是微积分基本定理在更高维度的推广。

## 12.1 场与向量场

自然界中许多物理量随空间位置变化：温度在房间各处不同，风速在每个地点有大小和方向，引力场在不同位置指向不同的方向。数学上，我们用**场**来描述这类"空间中每个点都对应一个量"的结构。

> [!important: 定义：标量场与向量场]
>
> 设 $D \subset \mathbb{R}^n$ 为一区域。
>
> - **标量场（scalar field）**：$D$ 上的实值函数 $f: D \to \mathbb{R}$，每个点对应一个数。例：温度场、密度场、电势场。
> - **向量场（vector field）**：$D$ 上的向量值函数 $\mathbf{F}: D \to \mathbb{R}^n$，每个点对应一个向量。例：引力场、流速场、电场。

向量场的**分量形式**：

$$
\mathbf{F}(x,y) = P(x,y)\,\hat{\mathbf{i}} + Q(x,y)\,\hat{\mathbf{j}} \qquad \text{（二维）}
$$

$$
\mathbf{F}(x,y,z) = P(x,y,z)\,\hat{\mathbf{i}} + Q(x,y,z)\,\hat{\mathbf{j}} + R(x,y,z)\,\hat{\mathbf{k}} \qquad \text{（三维）}
$$

其中 $P, Q, R$ 是普通的多元函数，分别表示向量在 $x, y, z$ 方向的分量。

> [!important: 几个二维向量场的例子]
>
> ==例 1==　$\mathbf{F}(x,y) = 2\hat{\mathbf{i}} + 3\hat{\mathbf{j}}$　— 均匀场，每处方向和大小相同。
>
> ![均匀向量场](media/img/fig2-4-1.png#200pt)
>
> ==例 2==　$\mathbf{F}(x,y) = x\hat{\mathbf{i}}$　— 水平分量随 $x$ 增大，无竖直分量。
>
> ![水平向量场](media/img/fig2-4-3.png#200pt)
>
> ==例 3==　$\mathbf{F}(x,y) = x\hat{\mathbf{i}} + y\hat{\mathbf{j}}$　— 从原点向外辐射的源场。
>
> ![辐射向量场](media/img/fig2-4-2.png#200pt)
>
> ==例 4==　$\mathbf{F}(x,y) = y\hat{\mathbf{i}} + x\hat{\mathbf{j}}$　— 场线呈双曲线形。
>
> ![双曲向量场](media/img/fig2-4-4.png#200pt)

> [!note]
>
> **三维向量场**的结构更为丰富。下面是两个典型例子，可拖动旋转查看：左图为螺旋场 $\mathbf{F}=(-z,\tfrac{1}{2},x)$，右图为磁偶极子场。

<div style="display:flex;gap:10px;margin:1.2em 0 0.2em;">
<div id="vf3d-helix" style="flex:1;height:400px;min-width:0;position:relative;background:#04080f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
<div id="vf3d-dipole" style="flex:1;height:400px;min-width:0;position:relative;background:#06030f;border-radius:8px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,0.5);"></div>
</div>
<script type="module" src="threejs/chapter12-vectorfield.js?v=20260414b"></script>

本章的核心问题是：**如何在向量场中进行积分？**

## 12.2 第一类曲线积分

## 12.3 第二类曲线积分

## 12.4 格林公式与保守场

### 12.4.1 格林公式

### 12.4.2 保守场与曲线积分基本定理

## 12.5 曲面积分

## 12.6 高斯公式与斯托克斯公式

### 12.6.1 高斯公式

### 12.6.2 斯托克斯公式

## 12.7 统一视角：广义牛顿-莱布尼茨公式
