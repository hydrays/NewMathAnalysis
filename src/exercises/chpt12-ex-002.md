---
id: chpt12-ex-002
chapter: 12
tags: [曲线积分, 第一类曲线积分, 空间曲线, 螺旋线]
difficulty: medium
video:
---

## Problem

计算曲线积分 $\displaystyle\int_\Gamma (x^2+y^2+z^2)\,\mathrm{d}s$，其中 $\Gamma$ 为螺旋线 $x = a\cos t$，$y = a\sin t$，$z = kt$，$t$ 从 $0$ 到 $2\pi$ 的一段弧。

## Solution 1

### Hint

将参数代入并计算弧长元素 $\mathrm{d}s = \sqrt{x'^2+y'^2+z'^2}\,\mathrm{d}t = \sqrt{a^2+k^2}\,\mathrm{d}t$，注意 $x^2+y^2+z^2 = a^2+k^2t^2$。

### Answer

弧长元素：

$$
\mathrm{d}s = \sqrt{(-a\sin t)^2 + (a\cos t)^2 + k^2}\,\mathrm{d}t = \sqrt{a^2+k^2}\,\mathrm{d}t.
$$

被积函数：$x^2+y^2+z^2 = a^2\cos^2 t + a^2\sin^2 t + k^2 t^2 = a^2 + k^2 t^2$。

$$
\int_\Gamma (x^2+y^2+z^2)\,\mathrm{d}s
= \sqrt{a^2+k^2}\int_0^{2\pi}(a^2+k^2t^2)\,\mathrm{d}t
= \sqrt{a^2+k^2}\left[a^2 t + \frac{k^2 t^3}{3}\right]_0^{2\pi}
= \frac{2\pi\sqrt{a^2+k^2}}{3}(3a^2 + 4\pi^2 k^2).
$$
