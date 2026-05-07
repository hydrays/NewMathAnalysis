"""
chpt2_ex_figs.py
Static figures for chpt2 exercises where geometry adds insight.
Naming convention: chpt2_ex{NNN}.png matches the exercise file id.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Use a CJK-capable font so Chinese in legends/titles renders.
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "media/img"


def _save(name):
    out = f"{OUT}/{name}.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close()


def _axes(ax, xlim, ylim, xlabel="$x$", ylabel="$y$"):
    ax.axhline(0, color="#999", lw=0.6)
    ax.axvline(0, color="#999", lw=0.6)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(True, alpha=0.25)


# ──────────────────────────────────────────────────────────────────────────────
# ex002: f(x)=x^2, derivative at x=2 — tangent line
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex002():
    fig, ax = plt.subplots(figsize=(4.8, 4.0), dpi=150)
    x = np.linspace(-0.5, 3.5, 240)
    ax.plot(x, x**2, color="#2563eb", lw=2.4, label=r"$y=x^2$")
    # tangent at x=2: slope=4, y=4x-4
    xt = np.linspace(0.5, 3.5, 120)
    ax.plot(xt, 4*xt - 4, color="#dc2626", lw=2.0, ls="--",
            label=r"切线: $y=4x-4$, 斜率 $=4$")
    ax.scatter([2], [4], color="black", s=40, zorder=5)
    ax.annotate("$(2,\\,4)$", (2, 4), xytext=(2.1, 3.0),
                fontsize=11, color="black")
    _axes(ax, (-0.5, 3.5), (-2, 12))
    ax.legend(loc="upper left", fontsize=9.5)
    _save("chpt2_ex002")


# ──────────────────────────────────────────────────────────────────────────────
# ex003: f(x)=x^2 and its derivative f'(x)=2x — paired panels
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex003():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.8), dpi=150)
    x = np.linspace(-2.5, 2.5, 240)
    axes[0].plot(x, x**2, color="#2563eb", lw=2.4)
    axes[0].set_title(r"$y=x^2$", fontsize=12)
    _axes(axes[0], (-2.5, 2.5), (-1, 7))
    axes[1].plot(x, 2*x, color="#dc2626", lw=2.4)
    axes[1].set_title(r"$y'=2x$", fontsize=12)
    _axes(axes[1], (-2.5, 2.5), (-5.5, 5.5), ylabel="$y'$")
    _save("chpt2_ex003")


# ──────────────────────────────────────────────────────────────────────────────
# ex004: f(x)=cos x and f'(x)=-sin x
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex004():
    fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=150)
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    ax.plot(x, np.cos(x), color="#2563eb", lw=2.4, label=r"$y=\cos x$")
    ax.plot(x, -np.sin(x), color="#dc2626", lw=2.0, ls="--",
            label=r"$y'=-\sin x$")
    ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    _axes(ax, (-2*np.pi, 2*np.pi), (-1.4, 1.4))
    ax.legend(loc="upper right", fontsize=10)
    _save("chpt2_ex004")


# ──────────────────────────────────────────────────────────────────────────────
# ex009: y=tan x and y'=sec^2 x — show asymptotes
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex009():
    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=150)
    eps = 0.05
    for k in [-1, 0]:
        x = np.linspace(-np.pi/2 + eps + k*np.pi, np.pi/2 - eps + k*np.pi, 200)
        ax.plot(x, np.tan(x), color="#2563eb", lw=2.4)
        ax.plot(x, 1/np.cos(x)**2, color="#dc2626", lw=2.0, ls="--")
    # asymptote markers
    for v in [-np.pi/2, np.pi/2]:
        ax.axvline(v, color="#888", lw=0.8, ls=":")
    ax.plot([], [], color="#2563eb", lw=2.4, label=r"$y=\tan x$")
    ax.plot([], [], color="#dc2626", lw=2.0, ls="--", label=r"$y'=\sec^2 x$")
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    _axes(ax, (-np.pi - 0.1, np.pi + 0.1), (-6, 8))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt2_ex009")


# ──────────────────────────────────────────────────────────────────────────────
# ex012: y=x+cos x on [0,2π] — strictly increasing because y'=1-sin x ≥ 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex012():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8), dpi=150)
    x = np.linspace(0, 2*np.pi, 240)
    axes[0].plot(x, x + np.cos(x), color="#2563eb", lw=2.4)
    axes[0].set_title(r"$y=x+\cos x$", fontsize=12)
    _axes(axes[0], (0, 2*np.pi), (0, 2*np.pi + 1))
    axes[0].set_xticks([0, np.pi, 2*np.pi])
    axes[0].set_xticklabels(["0", r"$\pi$", r"$2\pi$"])
    axes[1].plot(x, 1 - np.sin(x), color="#dc2626", lw=2.4)
    axes[1].fill_between(x, 0, 1 - np.sin(x), alpha=0.15, color="#dc2626")
    axes[1].set_title(r"$y'=1-\sin x \geq 0$", fontsize=12)
    _axes(axes[1], (0, 2*np.pi), (-0.2, 2.3), ylabel="$y'$")
    axes[1].set_xticks([0, np.pi, 2*np.pi])
    axes[1].set_xticklabels(["0", r"$\pi$", r"$2\pi$"])
    _save("chpt2_ex012")


# ──────────────────────────────────────────────────────────────────────────────
# ex013: y=e^x - x + 3, minimum at x=0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex013():
    fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=150)
    x = np.linspace(-1.6, 1.8, 240)
    y = np.exp(x) - x + 3
    ax.plot(x, y, color="#2563eb", lw=2.4)
    ax.scatter([0], [4], color="#dc2626", s=70, zorder=5,
               label=r"最小值 $(0,\,4)$")
    # mark intervals
    ax.fill_between(x[x < 0], 3, y[x < 0], alpha=0.12, color="#dc2626")
    ax.fill_between(x[x >= 0], 3, y[x >= 0], alpha=0.12, color="#16a34a")
    ax.text(-0.8, 3.2, "递减\n($y'<0$)", ha="center", fontsize=10, color="#dc2626")
    ax.text(1.0, 3.2, "递增\n($y'>0$)", ha="center", fontsize=10, color="#16a34a")
    _axes(ax, (-1.6, 1.8), (3, 7))
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt2_ex013")


# ──────────────────────────────────────────────────────────────────────────────
# ex014: y=x^4 - 4x^2 — two local minima at ±√2, local max at 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex014():
    fig, ax = plt.subplots(figsize=(6.0, 4.4), dpi=150)
    x = np.linspace(-2.4, 2.4, 240)
    y = x**4 - 4*x**2
    ax.plot(x, y, color="#2563eb", lw=2.4)
    s2 = np.sqrt(2)
    ax.scatter([-s2, s2], [-4, -4], color="#dc2626", s=70, zorder=5,
               label=r"极小值 $(\pm\sqrt{2},\,-4)$")
    ax.scatter([0], [0], color="#16a34a", s=70, zorder=5,
               label=r"极大值 $(0,\,0)$")
    ax.axhline(-4, color="#dc2626", lw=0.7, ls=":", alpha=0.5)
    _axes(ax, (-2.4, 2.4), (-5.5, 4))
    ax.legend(loc="upper center", fontsize=10)
    _save("chpt2_ex014")


# ──────────────────────────────────────────────────────────────────────────────
# ex017: y=√x concave (上凸)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex017():
    fig, ax = plt.subplots(figsize=(5.0, 4.0), dpi=150)
    x = np.linspace(0, 4, 240)
    ax.plot(x, np.sqrt(x), color="#2563eb", lw=2.4, label=r"$y=\sqrt{x}$")
    # secant from (0.5, √0.5) to (3.5, √3.5) — lies BELOW the curve
    xa, xb = 0.5, 3.5
    ya, yb = np.sqrt(xa), np.sqrt(xb)
    ax.plot([xa, xb], [ya, yb], color="#dc2626", lw=2.0, ls="--",
            label="弦 (在曲线下方 → 凹/concave)")
    ax.scatter([xa, xb], [ya, yb], color="#dc2626", s=40, zorder=5)
    _axes(ax, (-0.2, 4.2), (-0.2, 2.3))
    ax.legend(loc="lower right", fontsize=9.5)
    _save("chpt2_ex017")


# ──────────────────────────────────────────────────────────────────────────────
# ex018: y=x^2 convex (下凸)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex018():
    fig, ax = plt.subplots(figsize=(5.0, 4.0), dpi=150)
    x = np.linspace(-2.5, 2.5, 240)
    ax.plot(x, x**2, color="#2563eb", lw=2.4, label=r"$y=x^2$")
    xa, xb = -1.5, 2.0
    ya, yb = xa**2, xb**2
    ax.plot([xa, xb], [ya, yb], color="#dc2626", lw=2.0, ls="--",
            label="弦 (在曲线上方 → 凸/convex)")
    ax.scatter([xa, xb], [ya, yb], color="#dc2626", s=40, zorder=5)
    _axes(ax, (-2.5, 2.5), (-0.5, 6.5))
    ax.legend(loc="upper left", fontsize=9.5)
    _save("chpt2_ex018")


# ──────────────────────────────────────────────────────────────────────────────
# ex019: y=ln x concave
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex019():
    fig, ax = plt.subplots(figsize=(5.0, 4.0), dpi=150)
    x = np.linspace(0.05, 5, 240)
    ax.plot(x, np.log(x), color="#2563eb", lw=2.4, label=r"$y=\ln x$")
    xa, xb = 0.5, 4.5
    ya, yb = np.log(xa), np.log(xb)
    ax.plot([xa, xb], [ya, yb], color="#dc2626", lw=2.0, ls="--",
            label="弦 (在曲线下方 → 凹/concave)")
    ax.scatter([xa, xb], [ya, yb], color="#dc2626", s=40, zorder=5)
    _axes(ax, (-0.2, 5.2), (-3.2, 2.0))
    ax.legend(loc="lower right", fontsize=9.5)
    _save("chpt2_ex019")


# ──────────────────────────────────────────────────────────────────────────────
# ex020: f(x)=x^2 凸 → k(x)=f(2x+1)=(2x+1)^2 也是凸
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex020():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8), dpi=150)
    x = np.linspace(-2.5, 2.5, 240)
    axes[0].plot(x, x**2, color="#2563eb", lw=2.4)
    axes[0].set_title(r"$f(x)=x^2$", fontsize=12)
    _axes(axes[0], (-2.5, 2.5), (-0.5, 7))
    xk = np.linspace(-2.5, 1.0, 240)
    axes[1].plot(xk, (2*xk + 1)**2, color="#dc2626", lw=2.4)
    axes[1].set_title(r"$k(x)=f(2x+1)=(2x+1)^2$", fontsize=12)
    _axes(axes[1], (-2.5, 1.0), (-0.5, 18))
    _save("chpt2_ex020")


if __name__ == "__main__":
    fig_ex002()
    fig_ex003()
    fig_ex004()
    fig_ex009()
    fig_ex012()
    fig_ex013()
    fig_ex014()
    fig_ex017()
    fig_ex018()
    fig_ex019()
    fig_ex020()
