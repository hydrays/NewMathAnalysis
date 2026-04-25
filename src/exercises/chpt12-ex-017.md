---
id: chpt12-ex-017
chapter: 12
tags: [曲面积分, 高斯公式, 非封闭曲面, 补面法]
difficulty: hard
video:
---

## Problem

利用高斯公式计算曲面积分

$$
\iint_\Sigma (x^2\cos\alpha + y^2\cos\beta + z^2\cos\gamma)\,\mathrm{d}S,
$$

其中 $\Sigma$ 为锥面 $z^2 = x^2+y^2$ 介于平面 $z=0$，$z=h$（$h>0$）之间部分的下侧曲面，$(\cos\alpha, \cos\beta, \cos\gamma)$ 为法向量的方向余弦。

## Solution 1

### Hint

$\Sigma$ 是非封闭曲面，补充盖面 $\Sigma_1$（$z=h$，$x^2+y^2\leq h^2$ 的上侧）构成封闭曲面，用高斯公式算出整体，再减去 $\Sigma_1$ 上的积分。

### Answer

补充 $\Sigma_1: z = h$（$x^2+y^2\leq h^2$，上侧），设 $\Sigma+\Sigma_1$ 围成区域 $\Omega$。

$$
\oiint_{\Sigma+\Sigma_1}(x^2\cos\alpha+y^2\cos\beta+z^2\cos\gamma)\,\mathrm{d}S
= 2\iiint_\Omega(x+y+z)\,\mathrm{d}V.
$$

由对称性，$\iiint_\Omega(x+y)\,\mathrm{d}V = 0$，只剩 $z$ 项：

$$
= 2\iint_{D_{xy}}\mathrm{d}x\,\mathrm{d}y\int_{\sqrt{x^2+y^2}}^h z\,\mathrm{d}z = \iint_{D_{xy}}(h^2-x^2-y^2)\,\mathrm{d}x\,\mathrm{d}y = \frac{\pi h^4}{2}.
$$

在 $\Sigma_1$ 上（$z=h$，法向量向上，$\cos\gamma=1$，$\cos\alpha=\cos\beta=0$）：

$$
\iint_{\Sigma_1}z^2\,\mathrm{d}S = h^2\iint_{D_{xy}}\mathrm{d}x\,\mathrm{d}y = \pi h^4.
$$

故：

$$
\iint_\Sigma = \frac{\pi h^4}{2} - \pi h^4 = -\frac{\pi h^4}{2}.
$$
