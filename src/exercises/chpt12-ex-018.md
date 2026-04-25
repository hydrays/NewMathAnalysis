---
id: chpt12-ex-018
chapter: 12
tags: [曲面积分, 高斯公式, 格林公式, 证明]
difficulty: hard
video:
---

## Problem

设函数 $u(x,y,z)$ 和 $v(x,y,z)$ 在闭区域 $\Omega$ 上具有一阶及二阶连续偏导数，证明**格林第一公式**：

$$
\iiint_\Omega u\Delta v\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z
= \oiint_\Sigma u\frac{\partial v}{\partial n}\,\mathrm{d}S
- \iiint_\Omega\left(\frac{\partial u}{\partial x}\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y}\frac{\partial v}{\partial y}+\frac{\partial u}{\partial z}\frac{\partial v}{\partial z}\right)\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z,
$$

其中 $\Sigma$ 是 $\Omega$ 的整个边界曲面，$\frac{\partial v}{\partial n}$ 为 $v$ 沿 $\Sigma$ 外法线方向的方向导数。

## Solution 1

### Hint

利用方向导数展开 $\frac{\partial v}{\partial n}$，将曲面积分转化为形如 $\oiint_\Sigma (u v_x\cos\alpha + u v_y\cos\beta + u v_z\cos\gamma)\,\mathrm{d}S$，对向量场 $\vec{G} = (uv_x, uv_y, uv_z)$ 用高斯公式，展开散度后分离即得。

### Answer

方向导数展开（$\cos\alpha$，$\cos\beta$，$\cos\gamma$ 为外法向方向余弦）：

$$
\frac{\partial v}{\partial n} = v_x\cos\alpha + v_y\cos\beta + v_z\cos\gamma.
$$

曲面积分：

$$
\oiint_\Sigma u\frac{\partial v}{\partial n}\,\mathrm{d}S
= \oiint_\Sigma (u v_x\cos\alpha + u v_y\cos\beta + u v_z\cos\gamma)\,\mathrm{d}S.
$$

对向量场 $\vec{G} = (uv_x,\, uv_y,\, uv_z)$ 用高斯公式：

$$
= \iiint_\Omega \left[\frac{\partial(u v_x)}{\partial x} + \frac{\partial(u v_y)}{\partial y} + \frac{\partial(u v_z)}{\partial z}\right]\mathrm{d}V.
$$

展开散度（用乘积法则）：

$$
= \iiint_\Omega u\Delta v\,\mathrm{d}V + \iiint_\Omega\left(u_x v_x + u_y v_y + u_z v_z\right)\mathrm{d}V.
$$

移项即得所证公式。$\square$
