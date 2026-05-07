"""
chpt1_3_13_ex_figs.py — Round 7: figures for chpt1 (limits/continuity),
chpt3 (differentials/chain), chpt13 (series).
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


# ─── chpt1 ─────────────────────────────────────────────────────────────────────

# ex001: alternating sequence a_n = (-1)^(n+1)
def fig_chpt1_ex001():
    fig, ax = plt.subplots(figsize=(5.4, 3.4), dpi=150)
    n = np.arange(1, 16)
    a = (-1)**(n+1)
    ax.stem(n, a, basefmt=" ", linefmt="#2563eb", markerfmt="o")
    ax.axhline(1, color="#dc2626", lw=0.8, ls="--")
    ax.axhline(-1, color="#dc2626", lw=0.8, ls="--")
    ax.set_xlabel("$n$"); ax.set_ylabel("$a_n$")
    ax.set_xlim(0, 16); ax.set_ylim(-1.5, 1.5)
    ax.grid(True, alpha=0.25)
    ax.set_title(r"$a_n = (-1)^{n+1}$ — 在 $\pm 1$ 间永久跳跃, 不收敛", fontsize=10)
    _save("chpt1_ex001")


# ex014: |x| continuous, but corner at 0
def fig_chpt1_ex014():
    fig, ax = plt.subplots(figsize=(4.8, 3.6), dpi=150)
    x = np.linspace(-2, 2, 200)
    ax.plot(x, np.abs(x), color="#2563eb", lw=2.4)
    ax.scatter([0], [0], color="#dc2626", s=70, zorder=5)
    ax.text(0.1, -0.2, "尖点 (连续, 但不可导)", color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$|x|$")
    ax.set_xlim(-2, 2); ax.set_ylim(-0.5, 2.2); ax.grid(True, alpha=0.25)
    ax.set_title("$f(x) = |x|$ 在全实数轴连续", fontsize=10)
    _save("chpt1_ex014")


# ex015: 1/|x| — vertical asymptote at 0
def fig_chpt1_ex015():
    fig, ax = plt.subplots(figsize=(5.0, 3.6), dpi=150)
    x1 = np.linspace(-2, -0.05, 100); x2 = np.linspace(0.05, 2, 100)
    ax.plot(x1, 1/np.abs(x1), color="#2563eb", lw=2.4)
    ax.plot(x2, 1/np.abs(x2), color="#2563eb", lw=2.4)
    ax.axvline(0, color="#dc2626", lw=1.2, ls=":")
    ax.text(0.1, 18, r"$x=0$ 是无穷间断点", color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$1/|x|$")
    ax.set_xlim(-2, 2); ax.set_ylim(0, 22); ax.grid(True, alpha=0.25)
    _save("chpt1_ex015")


# ex016: sin(x)/x — removable discontinuity at 0
def fig_chpt1_ex016():
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=150)
    x = np.linspace(-3*np.pi, 3*np.pi, 400)
    y = np.where(np.abs(x) < 1e-8, 1.0, np.sin(x) / np.where(np.abs(x) < 1e-8, 1, x))
    ax.plot(x, y, color="#2563eb", lw=2.0)
    ax.scatter([0], [1], facecolor="white", edgecolor="#dc2626", s=80, lw=2, zorder=5)
    ax.text(0.5, 0.85, r"$x=0$ 处可去间断点 (补 $f(0)=1$ 即连续)",
            color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel(r"$\sin x/x$")
    ax.set_xticks([-3*np.pi, -np.pi, 0, np.pi, 3*np.pi])
    ax.set_xticklabels([r"$-3\pi$", r"$-\pi$", "0", r"$\pi$", r"$3\pi$"])
    ax.set_xlim(-3*np.pi, 3*np.pi); ax.set_ylim(-0.3, 1.2); ax.grid(True, alpha=0.25)
    _save("chpt1_ex016")


# ex017: sin(1/x) — essential discontinuity at 0
def fig_chpt1_ex017():
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=150)
    x = np.linspace(-1, 1, 4000)
    x = x[np.abs(x) > 1e-3]
    y = np.sin(1/x)
    ax.plot(x, y, color="#2563eb", lw=0.6)
    ax.axvline(0, color="#dc2626", lw=1.2, ls=":")
    ax.text(0.05, 1.15, r"$x \to 0$ 时无穷次振荡, 第二类间断", color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel(r"$\sin(1/x)$")
    ax.set_xlim(-1, 1); ax.set_ylim(-1.4, 1.4); ax.grid(True, alpha=0.25)
    _save("chpt1_ex017")


# ex019: sgn(x) — jump discontinuity
def fig_chpt1_ex019():
    fig, ax = plt.subplots(figsize=(5.0, 3.4), dpi=150)
    x_neg = np.linspace(-1.2, -0.001, 50); x_pos = np.linspace(0.001, 1.2, 50)
    ax.plot(x_neg, [-1]*len(x_neg), color="#2563eb", lw=2.4)
    ax.plot(x_pos, [1]*len(x_pos), color="#2563eb", lw=2.4)
    ax.scatter([0, 0, 0], [-1, 0, 1], facecolor=["white", "#dc2626", "white"],
               edgecolor=["#2563eb", "#dc2626", "#2563eb"], s=80, lw=2, zorder=5)
    ax.text(0.1, 0.0, r"$\mathrm{sgn}(0)=0$", color="#dc2626", fontsize=10)
    ax.text(-0.6, -0.85, r"左极限 $-1$", color="#2563eb", fontsize=9)
    ax.text(0.2, 1.05, r"右极限 $+1$", color="#2563eb", fontsize=9)
    ax.set_xlabel("$x$"); ax.set_ylabel(r"$\mathrm{sgn}(x)$")
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.4, 1.4); ax.grid(True, alpha=0.25)
    ax.set_title(r"符号函数 — $x=0$ 处跳跃间断, 维尔斯特拉斯定理不适用", fontsize=10)
    _save("chpt1_ex019")


# ex020: IVT for x³-4x²+1=0 on (0,1)
def fig_chpt1_ex020():
    fig, ax = plt.subplots(figsize=(5.4, 3.6), dpi=150)
    x = np.linspace(-0.2, 1.2, 240)
    f = x**3 - 4*x**2 + 1
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$f(x)=x^3-4x^2+1$")
    ax.axhline(0, color="black", lw=0.6)
    ax.scatter([0, 1], [1, -2], color="#dc2626", s=70, zorder=5)
    ax.text(0.02, 1.1, "$f(0)=1>0$", color="#dc2626", fontsize=10)
    ax.text(0.85, -1.85, "$f(1)=-2<0$", color="#dc2626", fontsize=10)
    # estimated root
    from scipy.optimize import brentq
    try:
        r = brentq(lambda t: t**3-4*t**2+1, 0, 1)
        ax.scatter([r], [0], color="#16a34a", s=70, zorder=5)
        ax.text(r-0.05, 0.4, fr"根 $\approx {r:.4f}$", color="#16a34a", fontsize=10)
    except Exception:
        pass
    ax.set_xlabel("$x$"); ax.set_ylabel("$f(x)$")
    ax.set_xlim(-0.2, 1.2); ax.set_ylim(-3, 1.5); ax.grid(True, alpha=0.25)
    ax.legend(loc="lower left", fontsize=10)
    ax.set_title("零点存在定理 — 连续函数变号必穿过零", fontsize=10)
    _save("chpt1_ex020")


# ex003: ε-N for 1/n → 0
def fig_chpt1_ex003():
    fig, ax = plt.subplots(figsize=(5.4, 3.4), dpi=150)
    n = np.arange(1, 50)
    a = 1/n
    ax.scatter(n, a, color="#2563eb", s=18)
    eps = 0.05
    ax.axhspan(-eps, eps, color="#dc2626", alpha=0.18, label=fr"$\varepsilon = {eps}$ 带")
    ax.axhline(0, color="black", lw=0.6)
    N = int(1/eps) + 1
    ax.axvline(N, color="#16a34a", lw=1.4, ls="--", label=fr"$N = {N}$")
    ax.set_xlabel("$n$"); ax.set_ylabel(r"$a_n = 1/n$")
    ax.set_xlim(0, 50); ax.set_ylim(-0.1, 1.1); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title(r"$\forall \varepsilon > 0,\; \exists N$ 使 $n>N \Rightarrow |a_n|<\varepsilon$", fontsize=10)
    _save("chpt1_ex003")


# ─── chpt3 ─────────────────────────────────────────────────────────────────────

# ex002: laser from origin to line y=b
def fig_chpt3_ex002():
    fig, ax = plt.subplots(figsize=(5.6, 3.6), dpi=150)
    b = 2.0; theta = np.deg2rad(35)
    x_int = b / np.tan(theta); l = b / np.sin(theta)
    ax.axhline(b, color="#dc2626", lw=1.5, ls="--", label=r"墙 $y=b$")
    ax.plot([0, x_int], [0, b], color="#2563eb", lw=2.4, label=r"激光 (长 $l$)")
    ax.scatter([x_int], [b], color="#16a34a", s=70, zorder=5,
               label=fr"交点 $x = b/\tan\theta$")
    # angle arc
    th_arc = np.linspace(0, np.pi/2 - theta, 30)
    ax.plot(0.6*np.sin(th_arc), 0.6*np.cos(th_arc), color="black", lw=1.2)
    ax.text(0.3, 0.8, r"$\theta$", fontsize=12)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-0.3, x_int + 1); ax.set_ylim(-0.3, b + 0.6)
    ax.set_aspect("equal"); ax.grid(True, alpha=0.25)
    ax.legend(loc="lower right", fontsize=9)
    _save("chpt3_ex002")


# ex012: hyperbola tangent at (3√2, 2)
def fig_chpt3_ex012():
    fig, ax = plt.subplots(figsize=(5.4, 4.2), dpi=150)
    x = np.linspace(-7, 7, 400)
    y_pos = np.sqrt(np.maximum(4*(x**2/9 - 1), 0))
    mask = x**2/9 - 1 >= 0
    ax.plot(x[mask & (x>0)], y_pos[mask & (x>0)], color="#2563eb", lw=2.0, label=r"$x^2/9 - y^2/4 = 1$")
    ax.plot(x[mask & (x>0)], -y_pos[mask & (x>0)], color="#2563eb", lw=2.0)
    ax.plot(x[mask & (x<0)], y_pos[mask & (x<0)], color="#2563eb", lw=2.0)
    ax.plot(x[mask & (x<0)], -y_pos[mask & (x<0)], color="#2563eb", lw=2.0)
    P = (3*np.sqrt(2), 2.0)
    # implicit derivative: 2x/9 - 2y y' /4 = 0 → y' = (4x)/(9y)
    slope = 4*P[0]/(9*P[1])
    xt = np.linspace(P[0]-3, P[0]+3, 50)
    ax.plot(xt, slope*(xt - P[0]) + P[1], color="#dc2626", lw=2.0,
            label=fr"切线 (斜率 $\approx {slope:.3f}$)")
    ax.scatter(*P, color="black", s=70, zorder=5)
    ax.text(P[0] + 0.3, P[1] + 0.2, fr"$(3\sqrt{{2}}, 2)$", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-7, 7); ax.set_ylim(-5, 5); ax.set_aspect("equal")
    ax.grid(True, alpha=0.25); ax.legend(loc="upper left", fontsize=9.5)
    _save("chpt3_ex012")


# ─── chpt13 ────────────────────────────────────────────────────────────────────

# ex001: "一尺之棰, 日取其半" — geometric series
def fig_chpt13_ex001():
    fig, ax = plt.subplots(figsize=(6.0, 3.4), dpi=150)
    bar_height = 0.7
    cum = 0
    colors = plt.cm.viridis(np.linspace(0.1, 0.85, 8))
    for i in range(8):
        seg_len = 0.5**(i+1)
        ax.barh(0, seg_len, left=cum, height=bar_height,
                color=colors[i], edgecolor="white", linewidth=1.2)
        if seg_len > 0.04:
            ax.text(cum + seg_len/2, 0, fr"$\frac{{1}}{{{2**(i+1)}}}$",
                    ha="center", va="center", fontsize=10)
        cum += seg_len
    # remaining
    ax.barh(0, 1 - cum, left=cum, height=bar_height,
            color="#cccccc", edgecolor="white", linewidth=1.2)
    ax.text(cum + (1-cum)/2, 0, "...", ha="center", va="center", fontsize=10)
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.6, 0.6); ax.set_yticks([])
    ax.set_xlabel(r"长度 $\to$ 1")
    ax.set_title(r"一尺之棰, 日取其半 — $S_n = \sum_{k=1}^n 1/2^k \to 1$", fontsize=11)
    _save("chpt13_ex001")


# ex002: inscribed n-gon area approaching circle
def fig_chpt13_ex002():
    fig, axes = plt.subplots(1, 4, figsize=(11, 3.0), dpi=150)
    th_circ = np.linspace(0, 2*np.pi, 200)
    for ax, n in zip(axes, [3, 6, 12, 24]):
        ax.plot(np.cos(th_circ), np.sin(th_circ), color="#dc2626", lw=1.6)
        th = np.linspace(0, 2*np.pi, n+1)
        x = np.cos(th); y = np.sin(th)
        ax.fill(x, y, color="#2563eb", alpha=0.30)
        ax.plot(x, y, color="#2563eb", lw=2.0)
        # area: (n/2) sin(2π/n)
        area = (n/2) * np.sin(2*np.pi/n)
        ax.set_title(fr"$n={n}$, 面积 $\approx {area:.4f}$", fontsize=10)
        ax.set_aspect("equal"); ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
        ax.axis("off")
    fig.suptitle(r"内接正 $n$ 边形面积 $\to \pi \approx 3.1416$", y=0.92, fontsize=11)
    _save("chpt13_ex002")


# ex006: alternating harmonic — partial sums oscillate to ln 2
def fig_chpt13_ex006():
    fig, ax = plt.subplots(figsize=(5.6, 3.4), dpi=150)
    N = 30
    n = np.arange(1, N + 1)
    terms = ((-1)**(n - 1)) / n
    partial = np.cumsum(terms)
    ax.plot(n, partial, color="#2563eb", marker="o", ms=4, lw=1.5)
    ax.axhline(np.log(2), color="#dc2626", lw=1.4, ls="--", label=r"$\ln 2 \approx 0.6931$")
    ax.set_xlabel("$n$"); ax.set_ylabel(r"前 $n$ 项和")
    ax.set_xlim(0, N); ax.set_ylim(0.4, 1.05); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title(r"交错调和级数 $\sum (-1)^{n-1}/n$ — 收敛到 $\ln 2$, 但绝对值不收敛", fontsize=10)
    _save("chpt13_ex006")


# ex007: power series convergence visualization
def fig_chpt13_ex007():
    fig, ax = plt.subplots(figsize=(5.4, 3.0), dpi=150)
    # Convergence on (1-2, 1+2)=(-1, 3); endpoint x=3 diverges, x=-1 converges (alternating)
    ax.plot([-1, 3], [0, 0], color="#16a34a", lw=4, solid_capstyle="butt", label="收敛区间")
    ax.scatter([-1], [0], color="#16a34a", s=80, zorder=5, label="$x=-1$ 收敛")
    ax.scatter([3], [0], facecolor="white", edgecolor="#dc2626", s=80, lw=2,
               zorder=5, label="$x=3$ 发散")
    ax.scatter([1], [0], color="black", s=60, zorder=5, label="中心 $x=1$, 半径 2")
    # mark with bracket
    ax.annotate("", xy=(-1.0, -0.3), xytext=(3.0, -0.3),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1.2))
    ax.text(1.0, -0.5, "收敛域 $[-1, 3)$", ha="center", fontsize=11)
    ax.set_xlim(-3, 5); ax.set_ylim(-0.8, 0.8); ax.set_yticks([])
    ax.set_xlabel("$x$"); ax.grid(True, alpha=0.25, axis="x")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title(r"幂级数 $\sum (x-1)^n/(2^n n)$ 的收敛域", fontsize=10)
    _save("chpt13_ex007")


if __name__ == "__main__":
    fig_chpt1_ex001(); fig_chpt1_ex003(); fig_chpt1_ex014()
    fig_chpt1_ex015(); fig_chpt1_ex016(); fig_chpt1_ex017()
    fig_chpt1_ex019(); fig_chpt1_ex020()
    fig_chpt3_ex002(); fig_chpt3_ex012()
    fig_chpt13_ex001(); fig_chpt13_ex002(); fig_chpt13_ex006(); fig_chpt13_ex007()
