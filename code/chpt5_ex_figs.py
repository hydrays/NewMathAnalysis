"""
chpt5_ex_figs.py
Figures for chpt5 (中值定理 + 泰勒展开 + 应用) exercises.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "media/img"


def _save(name):
    out = f"{OUT}/{name}.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close()


def _ax(ax, xlim, ylim, xlabel="$x$", ylabel="$y$"):
    ax.axhline(0, color="#999", lw=0.6)
    ax.axvline(0, color="#999", lw=0.6)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.grid(True, alpha=0.25)


# ──────────────────────────────────────────────────────────────────────────────
# ex003: MVT for f(x)=x^2 — find c on [x1, x2]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex003():
    fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=150)
    x = np.linspace(-0.3, 4.3, 240)
    ax.plot(x, x**2, color="#2563eb", lw=2.4, label=r"$f(x)=x^2$")
    x1, x2 = 1.0, 3.5
    y1, y2 = x1**2, x2**2
    # secant
    sec = lambda x: (y2 - y1)/(x2 - x1) * (x - x1) + y1
    ax.plot([x1, x2], [y1, y2], color="#dc2626", lw=2.0, ls="--", label="割线")
    ax.scatter([x1, x2], [y1, y2], color="#dc2626", s=45, zorder=5)
    # MVT: c = (x1+x2)/2 for x²
    c = (x1 + x2) / 2
    fc = c**2; slope = 2*c
    xt = np.linspace(c - 1.0, c + 1.0, 100)
    ax.plot(xt, slope*(xt - c) + fc, color="#16a34a", lw=2.0,
            label=r"$x=c$ 处的切线 (斜率 $=$ 割线斜率)")
    ax.scatter([c], [fc], color="#16a34a", s=70, zorder=6)
    ax.text(c, fc - 1.3, f"$c={c}$", color="#16a34a", ha="center", fontsize=11)
    _ax(ax, (-0.3, 4.3), (-1.5, 16))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt5_ex003")


# ──────────────────────────────────────────────────────────────────────────────
# ex004: MVT for f(x)=x^3 on [0,1]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex004():
    fig, ax = plt.subplots(figsize=(5.0, 4.0), dpi=150)
    x = np.linspace(-0.1, 1.2, 200)
    ax.plot(x, x**3, color="#2563eb", lw=2.4, label=r"$f(x)=x^3$")
    ax.plot([0, 1], [0, 1], color="#dc2626", lw=2.0, ls="--", label="割线 (斜率 $=1$)")
    ax.scatter([0, 1], [0, 1], color="#dc2626", s=45, zorder=5)
    c = 1/np.sqrt(3); fc = c**3
    xt = np.linspace(c - 0.4, c + 0.4, 50)
    ax.plot(xt, 3*c**2*(xt - c) + fc, color="#16a34a", lw=2.0,
            label=r"$x=c=1/\sqrt{3}$ 处切线")
    ax.scatter([c], [fc], color="#16a34a", s=70, zorder=6)
    _ax(ax, (-0.1, 1.2), (-0.1, 1.3))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt5_ex004")


# ──────────────────────────────────────────────────────────────────────────────
# ex006: integral MVT — ∫_0^2 x² dx = 8/3 = f(c)·2 ⇒ c = 2/√3
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex006():
    fig, ax = plt.subplots(figsize=(5.4, 4.0), dpi=150)
    x = np.linspace(-0.2, 2.4, 240)
    ax.plot(x, x**2, color="#2563eb", lw=2.4, label=r"$f(x)=x^2$")
    xf = np.linspace(0, 2, 100)
    ax.fill_between(xf, 0, xf**2, color="#dc2626", alpha=0.18,
                    label=r"$\int_0^2 x^2\,dx = 8/3$")
    c = 2/np.sqrt(3); fc = c**2  # 4/3
    ax.fill_between([0, 2], 0, fc, color="#16a34a", alpha=0.22)
    ax.axhline(fc, xmin=0.07, xmax=0.83, color="#16a34a", lw=2.0,
               label=fr"等高矩形: 高 $=f(c)=4/3$")
    ax.scatter([c], [fc], color="#16a34a", s=70, zorder=5)
    ax.text(c, fc + 0.3, f"$c=2/\\sqrt{{3}}$", color="#16a34a", ha="center", fontsize=11)
    _ax(ax, (-0.2, 2.4), (-0.5, 5.5))
    ax.legend(loc="upper left", fontsize=9.5)
    _save("chpt5_ex006")


# ──────────────────────────────────────────────────────────────────────────────
# ex007: continuous f with ∫=0 has a zero
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex007():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, np.pi, 240)
    f = np.sin(2*x)  # ∫_0^π sin(2x) dx = 0
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$f(x)$ 连续, $\int_a^b f\,dx=0$")
    pos = f > 0; neg = f < 0
    ax.fill_between(x[pos], 0, f[pos], color="#16a34a", alpha=0.22, label="正面积")
    ax.fill_between(x[neg], 0, f[neg], color="#dc2626", alpha=0.22, label="负面积 (大小相同)")
    ax.scatter([np.pi/2], [0], color="black", s=70, zorder=5,
               label=r"$\exists c$ 使 $f(c)=0$")
    _ax(ax, (-0.1, np.pi + 0.1), (-1.3, 1.3))
    ax.legend(loc="upper right", fontsize=9.5)
    _save("chpt5_ex007")


# ──────────────────────────────────────────────────────────────────────────────
# ex008: ∫_0^1 e^(-x²) dx — bound between two rectangles
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex008():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 240)
    f = np.exp(-x**2)
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$y = e^{-x^2}$")
    ax.fill_between(x, 0, f, color="#2563eb", alpha=0.18,
                    label=r"$\int_0^1 e^{-x^2}\,dx \approx 0.7468$")
    # bounds: min on [0,1] is e^(-1), max is 1
    ax.axhline(np.exp(-1), color="#dc2626", lw=1.8, ls="--",
               label=r"下界 $e^{-1}\approx 0.368$")
    ax.axhline(1, color="#16a34a", lw=1.8, ls="--", label="上界 $1$")
    _ax(ax, (-0.05, 1.05), (0, 1.15))
    ax.legend(loc="lower left", fontsize=9.5)
    _save("chpt5_ex008")


# ──────────────────────────────────────────────────────────────────────────────
# ex009: e^x Taylor approximations of orders 1, 2, 3
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex009():
    fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=150)
    x = np.linspace(-1.5, 2.0, 240)
    ax.plot(x, np.exp(x), color="black", lw=2.4, label=r"$e^x$")
    p1 = 1 + x
    p2 = 1 + x + x**2/2
    p3 = 1 + x + x**2/2 + x**3/6
    ax.plot(x, p1, color="#2563eb", lw=1.8, ls="--", label=r"1 阶: $1+x$")
    ax.plot(x, p2, color="#dc2626", lw=1.8, ls="--", label=r"2 阶: $+\,x^2/2$")
    ax.plot(x, p3, color="#16a34a", lw=1.8, ls="--", label=r"3 阶: $+\,x^3/6$")
    _ax(ax, (-1.5, 2.0), (-1, 8))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt5_ex009")


# ──────────────────────────────────────────────────────────────────────────────
# ex010: sin x Taylor approximations of orders 1, 3, 5
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex010():
    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    ax.plot(x, np.sin(x), color="black", lw=2.4, label=r"$\sin x$")
    p1 = x
    p3 = x - x**3/6
    p5 = p3 + x**5/120
    ax.plot(x, p1, color="#2563eb", lw=1.6, ls="--", label=r"1 阶: $x$")
    ax.plot(x, p3, color="#dc2626", lw=1.6, ls="--", label=r"3 阶: $-\,x^3/6$")
    ax.plot(x, p5, color="#16a34a", lw=1.6, ls="--", label=r"5 阶: $+\,x^5/120$")
    ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    _ax(ax, (-2*np.pi, 2*np.pi), (-3, 3))
    ax.legend(loc="upper right", fontsize=10)
    _save("chpt5_ex010")


# ──────────────────────────────────────────────────────────────────────────────
# ex014: e^x > 1 + x + x²/2 for x > 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex014():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 2.0, 240)
    e = np.exp(x); q = 1 + x + x**2/2
    ax.plot(x, e, color="#2563eb", lw=2.4, label=r"$e^x$")
    ax.plot(x, q, color="#dc2626", lw=2.0, ls="--", label=r"$1+x+x^2/2$")
    ax.fill_between(x, q, e, color="#16a34a", alpha=0.22, label=r"差 $>0$ (即 $e^x$ 更大)")
    _ax(ax, (-0.1, 2.0), (0, 8.5))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt5_ex014")


# ──────────────────────────────────────────────────────────────────────────────
# ex015: sin x > x - x³/6 for 0 < x < π/2
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex015():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, np.pi/2, 240)
    ax.plot(x, np.sin(x), color="#2563eb", lw=2.4, label=r"$\sin x$")
    ax.plot(x, x - x**3/6, color="#dc2626", lw=2.0, ls="--",
            label=r"$x - x^3/6$ (3 阶 Taylor)")
    ax.fill_between(x, x - x**3/6, np.sin(x), color="#16a34a", alpha=0.22,
                    label=r"差 $>0$")
    ax.set_xticks([0, np.pi/4, np.pi/2])
    ax.set_xticklabels(["0", r"$\pi/4$", r"$\pi/2$"])
    _ax(ax, (-0.05, np.pi/2 + 0.05), (-0.05, 1.1))
    ax.legend(loc="lower right", fontsize=10)
    _save("chpt5_ex015")


# ──────────────────────────────────────────────────────────────────────────────
# ex017: trapezoidal vs Simpson — same function, two error pictures
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex017():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), dpi=150)
    f = lambda x: np.sin(x) + 0.4*x
    a, b = 0.0, np.pi
    x = np.linspace(a, b, 240); fx = f(x)
    # Trapezoidal with 4 subintervals
    n = 4
    xs = np.linspace(a, b, n + 1)
    fs = f(xs)
    axes[0].plot(x, fx, color="#2563eb", lw=2.0)
    for i in range(n):
        axes[0].fill_between([xs[i], xs[i+1]], 0, [fs[i], fs[i+1]],
                             color="#dc2626", alpha=0.22)
        axes[0].plot([xs[i], xs[i+1]], [fs[i], fs[i+1]], color="#dc2626", lw=1.5)
    axes[0].set_title("梯形公式 — 误差 $O(h^2)$", fontsize=11)
    _ax(axes[0], (a, b), (0, max(fx)*1.15))
    # Simpson — fit parabola through (xs[0],fs[0]),(xs[1],fs[1]),(xs[2],fs[2]) etc per pair
    axes[1].plot(x, fx, color="#2563eb", lw=2.0)
    for i in range(0, n, 2):
        xpair = np.linspace(xs[i], xs[i+2], 30)
        # parabola through (xs[i], fs[i]), (xs[i+1], fs[i+1]), (xs[i+2], fs[i+2])
        from numpy.polynomial.polynomial import polyfit, polyval
        cf = np.polyfit([xs[i], xs[i+1], xs[i+2]],
                        [fs[i], fs[i+1], fs[i+2]], 2)
        yp = np.polyval(cf, xpair)
        axes[1].fill_between(xpair, 0, yp, color="#16a34a", alpha=0.22)
        axes[1].plot(xpair, yp, color="#16a34a", lw=1.5)
    axes[1].set_title("辛普森公式 — 误差 $O(h^4)$", fontsize=11)
    _ax(axes[1], (a, b), (0, max(fx)*1.15))
    _save("chpt5_ex017")


# ──────────────────────────────────────────────────────────────────────────────
# ex018: little-o / asymptotic equivalence — three relations near 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex018():
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4), dpi=150)
    # (1) x² = o(x)
    x = np.linspace(-1, 1, 240)
    axes[0].plot(x, x, color="#2563eb", lw=2.0, label=r"$x$")
    axes[0].plot(x, x**2, color="#dc2626", lw=2.0, label=r"$x^2$")
    axes[0].set_title(r"$x^2 = o(x)$ 当 $x\to 0$", fontsize=11)
    _ax(axes[0], (-1, 1), (-1.1, 1.1))
    axes[0].legend(loc="upper left", fontsize=9)
    # (2) sin x ~ x
    x2 = np.linspace(-1.5, 1.5, 240)
    axes[1].plot(x2, np.sin(x2), color="#2563eb", lw=2.0, label=r"$\sin x$")
    axes[1].plot(x2, x2, color="#dc2626", lw=1.6, ls="--", label=r"$x$")
    axes[1].set_title(r"$\sin x \sim x$ 当 $x\to 0$", fontsize=11)
    _ax(axes[1], (-1.5, 1.5), (-1.5, 1.5))
    axes[1].legend(loc="upper left", fontsize=9)
    # (3) 1 - cos x ~ x²/2
    x3 = np.linspace(-1.5, 1.5, 240)
    axes[2].plot(x3, 1 - np.cos(x3), color="#2563eb", lw=2.0, label=r"$1-\cos x$")
    axes[2].plot(x3, x3**2/2, color="#dc2626", lw=1.6, ls="--", label=r"$x^2/2$")
    axes[2].set_title(r"$1-\cos x \sim \frac{1}{2}x^2$", fontsize=11)
    _ax(axes[2], (-1.5, 1.5), (-0.1, 1.2))
    axes[2].legend(loc="upper left", fontsize=9)
    _save("chpt5_ex018")


# ──────────────────────────────────────────────────────────────────────────────
# ex020: Leibniz π series partial sums vs true π
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex020():
    fig, ax = plt.subplots(figsize=(6.0, 3.8), dpi=150)
    N = 80
    n = np.arange(1, N + 1)
    # Leibniz: π/4 = 1 - 1/3 + 1/5 - ...
    terms = ((-1)**(n - 1)) / (2*n - 1)
    partial = 4 * np.cumsum(terms)
    ax.plot(n, partial, color="#2563eb", lw=2.0, label=r"前 $n$ 项和 $\times 4$")
    ax.axhline(np.pi, color="#dc2626", lw=1.8, ls="--", label=r"$\pi \approx 3.1415927$")
    ax.set_xlabel("项数 $n$"); ax.set_ylabel(r"近似 $\pi$")
    ax.set_xlim(0, N); ax.set_ylim(2.5, 3.7)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="lower right", fontsize=10)
    ax.set_title(r"Leibniz 级数 $\pi = 4\sum (-1)^{n-1}/(2n-1)$ 收敛极慢", fontsize=11)
    _save("chpt5_ex020")


if __name__ == "__main__":
    fig_ex003(); fig_ex004(); fig_ex006(); fig_ex007()
    fig_ex008(); fig_ex009(); fig_ex010()
    fig_ex014(); fig_ex015(); fig_ex017(); fig_ex018(); fig_ex020()
