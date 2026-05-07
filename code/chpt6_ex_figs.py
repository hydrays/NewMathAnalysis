"""
chpt6_ex_figs.py
Figures for chpt6 (积分应用) exercises where geometry adds insight.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "media/img"


def _save(name):
    out = f"{OUT}/{name}.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close()


# ──────────────────────────────────────────────────────────────────────────────
# ex002: Cone volume — show cone with radius R, height h, sample disc dh
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex002():
    fig = plt.figure(figsize=(5.0, 5.0), dpi=150)
    ax = fig.add_subplot(111, projection="3d")

    R, H = 1.0, 2.0
    th = np.linspace(0, 2 * np.pi, 50)
    z = np.linspace(0, H, 30)
    TH, Z = np.meshgrid(th, z)
    X = (R * (1 - Z / H)) * np.cos(TH)
    Y = (R * (1 - Z / H)) * np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.5, linewidth=0)

    # base circle
    ax.plot(R * np.cos(th), R * np.sin(th), 0, "k-", lw=1.0)

    # one slice disc at z = 1.0
    z0 = 1.0
    r0 = R * (1 - z0 / H)
    ax.plot(r0 * np.cos(th), r0 * np.sin(th), z0, color="#dc2626", lw=1.6)
    ax.text(r0 + 0.1, 0, z0, r"$r(z)=R(1-z/h)$", fontsize=10, color="#dc2626")

    # axis arrow
    ax.plot([0, 0], [0, 0], [0, H + 0.2], "k--", lw=0.8)
    ax.text(0.05, 0.05, H + 0.18, "$h$", fontsize=12)
    ax.text(R + 0.1, 0, -0.05, "$R$", fontsize=12)

    ax.set_xlim(-R - 0.2, R + 0.2)
    ax.set_ylim(-R - 0.2, R + 0.2)
    ax.set_zlim(0, H + 0.3)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=18, azim=-55)
    _save("chpt6_ex002")


# ──────────────────────────────────────────────────────────────────────────────
# ex003: Revolution of y=√x about x-axis on [0,1]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex003():
    fig = plt.figure(figsize=(5.4, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(0, 1, 50)
    th = np.linspace(0, 2 * np.pi, 60)
    X, TH = np.meshgrid(x, th)
    R = np.sqrt(X)
    Y = R * np.cos(TH)
    Z = R * np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.55, linewidth=0)

    # silhouette (the curve y=√x on the plane z=0)
    ax.plot(x, np.sqrt(x), 0, "k-", lw=2.0)
    ax.plot(x, -np.sqrt(x), 0, "k-", lw=2.0)
    ax.plot([0, 1], [0, 0], [0, 0], "k--", lw=0.8)

    # one slice disc at x=0.6
    x0 = 0.6
    r0 = np.sqrt(x0)
    ax.plot([x0]*60, r0*np.cos(th), r0*np.sin(th), color="#dc2626", lw=1.6)
    ax.text(x0 + 0.05, 0, r0 + 0.1, r"半径 $\sqrt{x}$", fontsize=10, color="#dc2626")

    ax.set_xlim(0, 1.1); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=15, azim=-60)
    _save("chpt6_ex003")


# ──────────────────────────────────────────────────────────────────────────────
# ex004: Revolution of y=x about y-axis on [0,1]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex004():
    fig = plt.figure(figsize=(5.0, 5.0), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    # The line y=x rotated around y-axis gives a cone with apex at origin,
    # opening upward; at height y the radius is y.
    y = np.linspace(0, 1, 40)
    th = np.linspace(0, 2 * np.pi, 60)
    Y, TH = np.meshgrid(y, th)
    X = Y * np.cos(TH)
    Z = Y * np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.55, linewidth=0)

    # silhouette
    ax.plot([0, 1], [0, 1], [0, 0], "k-", lw=2.0)
    ax.plot([0, -1], [0, 1], [0, 0], "k-", lw=2.0)

    # slice ring at y=0.6
    y0 = 0.6
    ax.plot(y0*np.cos(th), [y0]*60, y0*np.sin(th), color="#dc2626", lw=1.6)
    ax.text(y0 + 0.05, y0 + 0.05, 0, r"半径 $=y$", fontsize=10, color="#dc2626")

    ax.set_xlim(-1.1, 1.1); ax.set_ylim(0, 1.2); ax.set_zlim(-1.1, 1.1)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=14, azim=-58)
    _save("chpt6_ex004")


# ──────────────────────────────────────────────────────────────────────────────
# ex005: Arc length of y = x^(3/2), 0..1
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex005():
    fig, ax = plt.subplots(figsize=(5.0, 4.0), dpi=150)
    x = np.linspace(0, 1, 200)
    y = x ** 1.5
    ax.plot(x, y, color="#2563eb", lw=2.4, label=r"$y=x^{3/2}$")
    # tiny ds element annotation around x=0.5
    x0 = 0.5
    y0 = x0 ** 1.5
    dx = 0.06
    dy = 1.5 * np.sqrt(x0) * dx
    ax.plot([x0, x0 + dx], [y0, y0 + dy], color="#dc2626", lw=3.0)
    ax.annotate("", xy=(x0 + dx, y0 + dy), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color="#dc2626"))
    ax.text(x0 + 0.03, y0 - 0.05, r"$ds = \sqrt{1+(y')^2}\,dx$",
            fontsize=10, color="#dc2626")
    ax.scatter([0, 1], [0, 1], c="black", s=30, zorder=5)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-0.05, 1.1); ax.set_ylim(-0.05, 1.15)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt6_ex005")


# ──────────────────────────────────────────────────────────────────────────────
# ex007: Cardioid r = a(1+cosθ)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex007():
    fig, ax = plt.subplots(figsize=(5.0, 5.0), dpi=150,
                            subplot_kw={"projection": "polar"})
    th = np.linspace(0, 2 * np.pi, 400)
    a = 1.0
    r = a * (1 + np.cos(th))
    ax.plot(th, r, color="#dc2626", lw=2.4)
    ax.fill(th, r, color="#dc2626", alpha=0.12)
    ax.set_title(r"心形线 $r = a(1+\cos\theta)$", fontsize=12, pad=14)
    ax.set_rticks([0.5, 1.0, 1.5, 2.0])
    _save("chpt6_ex007")


# ──────────────────────────────────────────────────────────────────────────────
# ex009: Pumping water out of cylindrical tank
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex009():
    fig = plt.figure(figsize=(5.0, 5.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    R, H = 1.0, 2.0
    th = np.linspace(0, 2 * np.pi, 50)
    z = np.linspace(0, H, 30)
    TH, Z = np.meshgrid(th, z)
    X = R * np.cos(TH); Y = R * np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.Blues(0.55), alpha=0.42, linewidth=0)

    # top and bottom circles
    ax.plot(R * np.cos(th), R * np.sin(th), 0, "k-", lw=1.0)
    ax.plot(R * np.cos(th), R * np.sin(th), H, "k-", lw=1.0)

    # one thin slab dz at height z0
    z0 = 1.2
    dz = 0.10
    rr = np.linspace(0, R, 12)
    pp = np.linspace(0, 2*np.pi, 36)
    Rg, Pg = np.meshgrid(rr, pp)
    Xs = Rg * np.cos(Pg); Ys = Rg * np.sin(Pg)
    ax.plot_surface(Xs, Ys, np.full_like(Xs, z0), color="#dc2626", alpha=0.55)

    ax.text(R + 0.1, 0, z0, r"切片厚 $dz$", fontsize=10, color="#dc2626")
    ax.text(R + 0.1, 0, H, "顶面", fontsize=10)
    # Distance arrow from z0 to H
    ax.plot([R + 0.05, R + 0.05], [0, 0], [z0, H], color="#16a34a", lw=1.4)
    ax.text(R + 0.18, 0, (z0 + H) / 2, r"$H-z$", fontsize=10, color="#16a34a")

    ax.set_xlim(-R - 0.2, R + 0.4); ax.set_ylim(-R - 0.2, R + 0.2); ax.set_zlim(0, H + 0.2)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=15, azim=-60)
    _save("chpt6_ex009")


# ──────────────────────────────────────────────────────────────────────────────
# ex010: Gravitational work — F=GMm/r^2 with shaded area to infinity
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex010():
    fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=150)
    r = np.linspace(0.6, 6, 240)
    F = 1 / r ** 2
    ax.plot(r, F, color="#2563eb", lw=2.4, label=r"$F(r) = \dfrac{GMm}{r^2}$")
    r_start = 1.0
    rfill = r[r >= r_start]
    Ffill = 1 / rfill ** 2
    ax.fill_between(rfill, 0, Ffill, color="#dc2626", alpha=0.22,
                    label=r"$W = \int_r^\infty F\,dr$")
    ax.axvline(r_start, color="#dc2626", lw=0.8, ls="--")
    ax.text(r_start - 0.05, 1.7, "$r$", fontsize=12, ha="right", color="#dc2626")
    ax.set_xlabel("距离 $r$"); ax.set_ylabel("引力大小 $F$")
    ax.set_xlim(0.5, 6); ax.set_ylim(0, 2.5)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    _save("chpt6_ex010")


# ──────────────────────────────────────────────────────────────────────────────
# ex011: ∫_0^1 1/√x dx — improper integral with singularity at 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex011():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0.01, 1.2, 240)
    y = 1 / np.sqrt(x)
    ax.plot(x, y, color="#2563eb", lw=2.4, label=r"$y = 1/\sqrt{x}$")
    xfill = x[x <= 1.0]
    yfill = 1 / np.sqrt(xfill)
    ax.fill_between(xfill, 0, yfill, color="#dc2626", alpha=0.18,
                    label=r"$\int_0^1 \frac{1}{\sqrt{x}}\,dx = 2$ (收敛)")
    ax.axvline(0, color="#888", lw=0.7, ls=":")
    ax.text(0.02, 8.5, "瑕点 $x=0$", fontsize=10, color="#888")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-0.05, 1.2); ax.set_ylim(0, 11)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    _save("chpt6_ex011")


# ──────────────────────────────────────────────────────────────────────────────
# ex012: PDF triangle f(x) = 2x on [0,1]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex012():
    fig, ax = plt.subplots(figsize=(5.0, 3.8), dpi=150)
    x = np.linspace(-0.3, 1.3, 200)
    y = np.where((x >= 0) & (x <= 1), 2 * x, 0)
    ax.plot(x, y, color="#2563eb", lw=2.4)
    xf = np.linspace(0, 1, 200)
    ax.fill_between(xf, 0, 2*xf, color="#dc2626", alpha=0.22,
                    label=r"$\int_0^1 2x\,dx = 1$")
    ax.set_xlabel("$x$"); ax.set_ylabel("$f(x)$")
    ax.set_xlim(-0.3, 1.3); ax.set_ylim(-0.1, 2.4)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.25)
    _save("chpt6_ex012")


# ──────────────────────────────────────────────────────────────────────────────
# ex014: Exponential decay + tail probability P(X>1000)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex014():
    fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=150)
    lam = 0.001
    x = np.linspace(0, 4000, 240)
    f = lam * np.exp(-lam * x)
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$f(x)=\lambda e^{-\lambda x}$")
    xt = x[x >= 1000]
    ft = lam * np.exp(-lam * xt)
    ax.fill_between(xt, 0, ft, color="#dc2626", alpha=0.25,
                    label=r"$P(X>1000)=e^{-1}\approx 0.368$")
    ax.axvline(1000, color="#dc2626", lw=0.8, ls="--")
    ax.set_xlabel(r"寿命 $x$ (小时)"); ax.set_ylabel("$f(x)$")
    ax.set_xlim(0, 4000); ax.set_ylim(0, lam * 1.05)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    _save("chpt6_ex014")


# ──────────────────────────────────────────────────────────────────────────────
# ex015: Convergence of ∫_1^∞ 1/x^p dx for various p
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex015():
    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
    x = np.linspace(1, 8, 300)
    for p, color, label in [
        (0.5, "#dc2626", r"$p=0.5$ (发散)"),
        (1.0, "#f59e0b", r"$p=1$ (临界, 发散)"),
        (1.5, "#16a34a", r"$p=1.5$ (收敛)"),
        (2.0, "#2563eb", r"$p=2$ (收敛)"),
    ]:
        ax.plot(x, 1 / x ** p, color=color, lw=2.0, label=label)
    ax.set_xlabel("$x$"); ax.set_ylabel("$1/x^p$")
    ax.set_xlim(0.9, 8); ax.set_ylim(0, 1.1)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    ax.set_title(r"$\int_1^\infty \frac{1}{x^p}\,dx$ — $p>1$ 收敛", fontsize=11)
    _save("chpt6_ex015")


# ──────────────────────────────────────────────────────────────────────────────
# ex016: Convergence of ∫_0^1 1/x^p (singularity at 0) — opposite story
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex016():
    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
    x = np.linspace(0.02, 1, 300)
    for p, color, label in [
        (0.5, "#16a34a", r"$p=0.5$ (收敛)"),
        (1.0, "#f59e0b", r"$p=1$ (临界, 发散)"),
        (1.5, "#dc2626", r"$p=1.5$ (发散)"),
        (2.0, "#2563eb", r"$p=2$ (发散)"),
    ]:
        ax.plot(x, 1 / x ** p, color=color, lw=2.0, label=label)
    ax.set_xlabel("$x$"); ax.set_ylabel("$1/x^p$")
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 25)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    ax.set_title(r"$\int_0^1 \frac{1}{x^p}\,dx$ — $p<1$ 收敛", fontsize=11)
    _save("chpt6_ex016")


# ──────────────────────────────────────────────────────────────────────────────
# ex017: Generic area under f(x) from a to b
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex017():
    fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=150)
    x = np.linspace(0, 4, 300)
    f = 1.5 + 0.8 * np.sin(0.9 * x) + 0.4 * x - 0.05 * x**2
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$y=f(x)$")
    a, b = 0.7, 3.2
    xf = x[(x >= a) & (x <= b)]
    ff = 1.5 + 0.8 * np.sin(0.9 * xf) + 0.4 * xf - 0.05 * xf**2
    ax.fill_between(xf, 0, ff, color="#dc2626", alpha=0.22,
                    label=r"$\int_a^b f(x)\,dx$")
    ax.axvline(a, color="#dc2626", lw=0.8, ls="--")
    ax.axvline(b, color="#dc2626", lw=0.8, ls="--")
    ax.text(a, -0.3, "$a$", color="#dc2626", ha="center", fontsize=11)
    ax.text(b, -0.3, "$b$", color="#dc2626", ha="center", fontsize=11)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-0.1, 4.1); ax.set_ylim(-0.6, 3.5)
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(True, alpha=0.25)
    _save("chpt6_ex017")


if __name__ == "__main__":
    fig_ex002()
    fig_ex003()
    fig_ex004()
    fig_ex005()
    fig_ex007()
    fig_ex009()
    fig_ex010()
    fig_ex011()
    fig_ex012()
    fig_ex014()
    fig_ex015()
    fig_ex016()
    fig_ex017()
