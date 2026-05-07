"""
chpt12_extra_figs.py
Static figures for chpt12 exercises (one per exercise where useful).
Companion to chpt12_ex123.py (which produced ex001 / ex002 / ex023).

Convention: viridis colormap for non-negative integrands or |F|; RdBu_r
for signed integrands. Integration path / region boundary in black with a
direction arrow. White quiver for vector fields.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

OUT = "media/img"


# ── shared helpers ───────────────────────────────────────────────────────────

def _save(name):
    out = f"{OUT}/{name}.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close()


def _arrow_on_path(ax, px, py, idx, span=6):
    ax.annotate(
        "",
        xy=(px[idx + span], py[idx + span]),
        xytext=(px[idx - span], py[idx - span]),
        arrowprops=dict(arrowstyle="-|>", color="black", lw=1.6, mutation_scale=13),
        zorder=6,
    )


def _common_2d(ax, xlim, ylim):
    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")


# =============================================================================
# §12.3 第二类曲线积分
# =============================================================================

# ex003 — F = (-y, x), path (t, t²), t ∈ [0,1]
def fig_ex003():
    fig, ax = plt.subplots(figsize=(5.2, 4.4), dpi=150)
    xs = np.linspace(-0.25, 1.25, 220)
    ys = np.linspace(-0.25, 1.25, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|=\sqrt{x^2+y^2}$")

    qx = np.linspace(-0.2, 1.2, 9); qy = np.linspace(-0.2, 1.2, 9)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, -QY, QX, color="white", scale=18, width=0.0045, alpha=0.95, zorder=3)

    t = np.linspace(0, 1, 200); px, py = t, t**2
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 120, 8)
    ax.scatter([0, 1], [0, 1], c="black", s=26, zorder=6)
    ax.text(-0.04, -0.04, "$t=0$", ha="right", va="top")
    ax.text(1.03, 1.02, "$t=1$", ha="left", va="bottom")
    _common_2d(ax, (-0.25, 1.25), (-0.25, 1.25))
    _save("chpt12_ex003")


# ex004 — ∫_L xy dx, L: x = y², y ∈ [-1, 1]
def fig_ex004():
    fig, ax = plt.subplots(figsize=(5.0, 4.6), dpi=150)
    xs = np.linspace(-0.15, 1.25, 220)
    ys = np.linspace(-1.25, 1.25, 220)
    X, Y = np.meshgrid(xs, ys)
    F = X * Y
    vmax = np.max(np.abs(F))
    pcm = ax.pcolormesh(X, Y, F, cmap=cm.RdBu_r, shading="auto", vmin=-vmax, vmax=vmax)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$f=xy$")

    yt = np.linspace(-1, 1, 200)
    px, py = yt**2, yt
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 120, 8)
    ax.scatter([1, 1], [-1, 1], c="black", s=26, zorder=6)
    ax.text(0.95, -0.95, "$A(1,-1)$", fontsize=10, ha="right", va="bottom")
    ax.text(0.95, 0.95, "$B(1,1)$", fontsize=10, ha="right", va="top")
    ax.text(0.05, 0.0, "$L:\\;x=y^2$", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.5, alpha=0.85))
    _common_2d(ax, (-0.15, 1.6), (-1.25, 1.25))
    _save("chpt12_ex004")


# ex005 — F = -k(x,y) on ellipse arc, A(a,0) → B(0,b) CCW
def fig_ex005():
    a, b = 2.0, 1.0
    fig, ax = plt.subplots(figsize=(5.2, 3.4), dpi=150)
    xs = np.linspace(-0.3, a + 0.3, 220)
    ys = np.linspace(-0.3, b + 0.3, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|=k\sqrt{x^2+y^2}$")

    qx = np.linspace(0.0, a + 0.1, 8); qy = np.linspace(0.0, b + 0.1, 5)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, -QX, -QY, color="white", scale=15, width=0.005, alpha=0.95, zorder=3)

    th = np.linspace(0, np.pi / 2, 200)
    px, py = a * np.cos(th), b * np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 120, 6)
    ax.scatter([a, 0], [0, b], c="black", s=26, zorder=6)
    ax.text(a + 0.06, 0.02, "$A(a,0)$", fontsize=10, ha="left", va="bottom")
    ax.text(-0.05, b + 0.06, "$B(0,b)$", fontsize=10, ha="right", va="bottom")
    _common_2d(ax, (-0.3, a + 0.3), (-0.3, b + 0.3))
    _save("chpt12_ex005")


# ex006 — F = (x,y), arbitrary closed curve (conservative ⇒ work = 0)
def fig_ex006():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    xs = np.linspace(-1.6, 1.6, 220)
    ys = np.linspace(-1.6, 1.6, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|=\sqrt{x^2+y^2}$")

    qx = np.linspace(-1.4, 1.4, 9); qy = np.linspace(-1.4, 1.4, 9)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, QX, QY, color="white", scale=22, width=0.0045, alpha=0.95, zorder=3)

    # bumpy closed curve r(θ) = 0.95 + 0.25 cos(3θ)
    th = np.linspace(0, 2 * np.pi, 400)
    r = 0.95 + 0.25 * np.cos(3 * th)
    px, py = r * np.cos(th), r * np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 80, 8)
    ax.text(0.0, 0.0, "$L$", ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="black", lw=0.5, alpha=0.9))
    _common_2d(ax, (-1.6, 1.6), (-1.6, 1.6))
    _save("chpt12_ex006")


# ex007 — y² dx, two paths from (1,0) to (-1,0)
def fig_ex007():
    a = 1.0
    fig, ax = plt.subplots(figsize=(5.4, 3.6), dpi=150)
    xs = np.linspace(-1.25, 1.25, 220)
    ys = np.linspace(-0.25, 1.25, 220)
    X, Y = np.meshgrid(xs, ys)
    F = Y**2
    pcm = ax.pcolormesh(X, Y, F, cmap=cm.viridis, shading="auto")
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$f=y^2$")

    th = np.linspace(0, np.pi, 200)
    cx, cy = a * np.cos(th), a * np.sin(th)
    ax.plot(cx, cy, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, cx, cy, 100, 6)
    lx = np.linspace(a, -a, 50)
    ax.plot(lx, np.zeros_like(lx), "k-", lw=2.4, zorder=4)
    ax.annotate("", xy=(-0.2, 0), xytext=(0.2, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.6, mutation_scale=13), zorder=6)

    ax.text(0.0, 1.05, "(1)", ha="center", va="bottom", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.5, alpha=0.85))
    ax.text(0.0, -0.18, "(2)", ha="center", va="top", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.5, alpha=0.85))
    ax.scatter([a, -a], [0, 0], c="black", s=26, zorder=6)
    ax.text(a + 0.05, 0.05, "$A$", fontsize=10)
    ax.text(-a - 0.05, 0.05, "$B$", fontsize=10, ha="right")
    _common_2d(ax, (-1.25, 1.25), (-0.25, 1.25))
    _save("chpt12_ex007")


# ex008 — 2xy dx + x² dy, three paths O→B(1,1); F = ∇(x²y), conservative
def fig_ex008():
    fig, ax = plt.subplots(figsize=(5.2, 4.4), dpi=150)
    xs = np.linspace(-0.05, 1.15, 220)
    ys = np.linspace(-0.05, 1.15, 220)
    X, Y = np.meshgrid(xs, ys)
    phi = X**2 * Y  # potential
    pcm = ax.pcolormesh(X, Y, phi, cmap=cm.viridis, shading="auto", alpha=0.6)
    cs = ax.contour(X, Y, phi, levels=8, colors="white", linewidths=0.6, alpha=0.7)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$\varphi=x^2 y$")

    t = np.linspace(0, 1, 200)
    # path 1: y = x²
    ax.plot(t, t**2, "k-", lw=2.2, zorder=4, label=r"$L_1:\,y=x^2$")
    # path 2: x = y²
    ax.plot(t**2, t, "k--", lw=2.2, zorder=4, label=r"$L_2:\,x=y^2$")
    # path 3: O→A(1,0)→B(1,1)
    ax.plot([0, 1, 1], [0, 0, 1], "k:", lw=2.4, zorder=4, label=r"$L_3:\,O\!\to\!A\!\to\!B$")

    ax.scatter([0, 1], [0, 1], c="black", s=26, zorder=6)
    ax.text(-0.03, -0.03, "$O$", ha="right", va="top", fontsize=10)
    ax.text(1.02, 1.02, "$B(1,1)$", ha="left", va="bottom", fontsize=10)
    ax.legend(loc="upper left", fontsize=8.5, framealpha=0.85)
    _common_2d(ax, (-0.05, 1.15), (-0.05, 1.15))
    _save("chpt12_ex008")


# =============================================================================
# §12.4 格林公式
# =============================================================================

# ex010 — F = (-y,x), generic D (illustrate with unit disc)
def fig_ex010():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    xs = np.linspace(-1.5, 1.5, 220)
    ys = np.linspace(-1.5, 1.5, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|=\sqrt{x^2+y^2}$")

    qx = np.linspace(-1.3, 1.3, 9); qy = np.linspace(-1.3, 1.3, 9)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, -QY, QX, color="white", scale=22, width=0.0045, alpha=0.95, zorder=3)

    th = np.linspace(0, 2 * np.pi, 300)
    px, py = np.cos(th), np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 40, 6)
    ax.fill(px, py, color="black", alpha=0.06, zorder=2)
    ax.text(0.0, 0.0, "$D$", ha="center", va="center", fontsize=12, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="black", lw=0.5, alpha=0.9))
    ax.text(0.95, 1.05, "$\\partial D$", fontsize=10)
    _common_2d(ax, (-1.5, 1.5), (-1.5, 1.5))
    _save("chpt12_ex010")


# ex011 — F = (x²y, -xy²) on x²+y²=a², a=1
def fig_ex011():
    a = 1.0
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    xs = np.linspace(-1.5, 1.5, 240)
    ys = np.linspace(-1.5, 1.5, 240)
    X, Y = np.meshgrid(xs, ys)
    P, Q = X**2 * Y, -X * Y**2
    M = np.sqrt(P**2 + Q**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|$")

    qx = np.linspace(-1.3, 1.3, 9); qy = np.linspace(-1.3, 1.3, 9)
    QX, QY = np.meshgrid(qx, qy)
    QP, QQ = QX**2 * QY, -QX * QY**2
    ax.quiver(QX, QY, QP, QQ, color="white", scale=2.5, width=0.0045, alpha=0.95, zorder=3)

    th = np.linspace(0, 2 * np.pi, 300)
    px, py = a * np.cos(th), a * np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 40, 6)
    ax.text(0.0, 0.0, "$L$", ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.5, alpha=0.9))
    _common_2d(ax, (-1.5, 1.5), (-1.5, 1.5))
    _save("chpt12_ex011")


# ex012 — F = (-y, x)/(x²+y²), two cases (encloses origin / not)
def fig_ex012():
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.0), dpi=150)
    for ax, encloses, title in zip(
        axes, [True, False], ["(1)", "(2)"]
    ):
        xs = np.linspace(-1.6, 1.6, 220)
        ys = np.linspace(-1.6, 1.6, 220)
        X, Y = np.meshgrid(xs, ys)
        with np.errstate(divide="ignore", invalid="ignore"):
            r2 = X**2 + Y**2
            M = np.where(r2 > 0.01, 1.0 / np.sqrt(r2), np.nan)
        pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.8,
                            vmin=0.5, vmax=4.0)

        qx = np.linspace(-1.3, 1.3, 7); qy = np.linspace(-1.3, 1.3, 7)
        QX, QY = np.meshgrid(qx, qy)
        with np.errstate(divide="ignore", invalid="ignore"):
            r2q = QX**2 + QY**2
            U = np.where(r2q > 0.01, -QY / r2q, 0)
            V = np.where(r2q > 0.01, QX / r2q, 0)
        ax.quiver(QX, QY, U, V, color="white", scale=18, width=0.005, alpha=0.95, zorder=3)

        th = np.linspace(0, 2 * np.pi, 300)
        if encloses:
            cx, cy = 1.0 * np.cos(th), 1.0 * np.sin(th)
        else:
            cx = 0.4 + 0.6 * np.cos(th)
            cy = 0.7 + 0.4 * np.sin(th)
        ax.plot(cx, cy, "k-", lw=2.4, zorder=4)
        _arrow_on_path(ax, cx, cy, 40, 5)
        ax.scatter([0], [0], c="red", s=30, zorder=6)
        ax.text(0.05, -0.18, "$O$", color="red", fontsize=10)
        ax.set_title(title, fontsize=10)
        _common_2d(ax, (-1.6, 1.6), (-1.6, 1.6))
    fig.colorbar(pcm, ax=axes, fraction=0.025, pad=0.03, label=r"$|\mathbf{F}|=1/r$")
    out = f"{OUT}/chpt12_ex012.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close()


# ex014 — F = (x,y), flux on D (illustrate with unit disc)
def fig_ex014():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    xs = np.linspace(-1.5, 1.5, 220)
    ys = np.linspace(-1.5, 1.5, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|=\sqrt{x^2+y^2}$")

    qx = np.linspace(-1.3, 1.3, 9); qy = np.linspace(-1.3, 1.3, 9)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, QX, QY, color="white", scale=22, width=0.0045, alpha=0.95, zorder=3)

    th = np.linspace(0, 2 * np.pi, 300)
    px, py = np.cos(th), np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    ax.fill(px, py, color="black", alpha=0.06, zorder=2)
    # outward-normal markers at four cardinals
    for ang in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        cx, cy = np.cos(ang), np.sin(ang)
        ax.annotate("", xy=(cx * 1.25, cy * 1.25), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=1.2,
                                    mutation_scale=10), zorder=5)
    ax.text(0.0, 0.0, "$D$", ha="center", va="center", fontsize=12, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="black", lw=0.5, alpha=0.9))
    ax.text(1.05, 1.18, "$\\vec n$", color="#dc2626", fontsize=11)
    _common_2d(ax, (-1.5, 1.5), (-1.5, 1.5))
    _save("chpt12_ex014")


# ex024 — ∫ y dx − x dy, upper semicircle from (1,0) to (-1,0)
def fig_ex024():
    fig, ax = plt.subplots(figsize=(5.4, 3.6), dpi=150)
    xs = np.linspace(-1.4, 1.4, 220)
    ys = np.linspace(-0.25, 1.25, 220)
    X, Y = np.meshgrid(xs, ys)
    M = np.sqrt(X**2 + Y**2)
    pcm = ax.pcolormesh(X, Y, M, cmap=cm.viridis, shading="auto", alpha=0.85)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$|\mathbf{F}|$")

    qx = np.linspace(-1.2, 1.2, 9); qy = np.linspace(-0.1, 1.1, 5)
    QX, QY = np.meshgrid(qx, qy)
    ax.quiver(QX, QY, QY, -QX, color="white", scale=18, width=0.005, alpha=0.95, zorder=3)

    th = np.linspace(0, np.pi, 200)
    px, py = np.cos(th), np.sin(th)
    ax.plot(px, py, "k-", lw=2.4, zorder=4)
    _arrow_on_path(ax, px, py, 100, 6)
    ax.scatter([1, -1], [0, 0], c="black", s=26, zorder=6)
    ax.text(1.05, 0.05, "$t=0$", fontsize=10)
    ax.text(-1.05, 0.05, "$t=\\pi$", fontsize=10, ha="right")
    _common_2d(ax, (-1.4, 1.4), (-0.25, 1.25))
    _save("chpt12_ex024")


# =============================================================================
# §12.5 曲面积分 / 高斯 / Stokes (3D figures)
# =============================================================================

def _setup_3d(fig, elev=22, azim=-55, box=(1, 1, 1)):
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect(box)
    ax.set_xlabel("$x$", fontsize=10, labelpad=1)
    ax.set_ylabel("$y$", fontsize=10, labelpad=1)
    ax.set_zlabel("$z$", fontsize=10, labelpad=1)
    ax.tick_params(labelsize=8)
    ax.view_init(elev=elev, azim=azim)
    return ax


# ex015 — F=(x,y,z) on sphere x²+y²+z²=a²
def fig_ex015():
    a = 1.0
    fig = plt.figure(figsize=(5.6, 4.8), dpi=150)
    ax = _setup_3d(fig, elev=22, azim=-50)

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 40)
    X = a * np.outer(np.cos(u), np.sin(v))
    Y = a * np.outer(np.sin(u), np.sin(v))
    Z = a * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.45,
                    linewidth=0, antialiased=True)

    # outward arrows F = (x,y,z) at sample points on sphere
    pts = []
    for ph in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        for th in [np.pi / 4, np.pi / 2, 3 * np.pi / 4]:
            pts.append((a * np.cos(ph) * np.sin(th),
                        a * np.sin(ph) * np.sin(th),
                        a * np.cos(th)))
    for x0, y0, z0 in pts:
        ax.quiver(x0, y0, z0, x0, y0, z0, length=0.35, color="black",
                  arrow_length_ratio=0.35, lw=1.0)

    ax.text(0, 0, a + 0.15, "$\\Sigma:\\,x^2+y^2+z^2=a^2$",
            fontsize=10, ha="center")
    lim = a * 1.4
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    _save("chpt12_ex015")


# ex016 — closed cylinder x²+y²≤1, 0≤z≤3
def fig_ex016():
    fig = plt.figure(figsize=(5.0, 5.4), dpi=150)
    ax = _setup_3d(fig, elev=20, azim=-58, box=(1, 1, 1.4))

    th = np.linspace(0, 2 * np.pi, 60)
    z = np.linspace(0, 3, 30)
    TH, Z = np.meshgrid(th, z)
    X = np.cos(TH); Y = np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.4, linewidth=0)

    # caps
    rr = np.linspace(0, 1, 20); pp = np.linspace(0, 2 * np.pi, 60)
    R, P = np.meshgrid(rr, pp)
    Xc, Yc = R * np.cos(P), R * np.sin(P)
    ax.plot_surface(Xc, Yc, np.zeros_like(Xc), color=cm.viridis(0.3), alpha=0.55)
    ax.plot_surface(Xc, Yc, np.full_like(Xc, 3.0), color=cm.viridis(0.75), alpha=0.55)

    # boundary edges
    ax.plot(np.cos(th), np.sin(th), np.zeros_like(th), "k-", lw=1.2)
    ax.plot(np.cos(th), np.sin(th), np.full_like(th, 3.0), "k-", lw=1.2)

    ax.text(0, 1.2, 3.2, "$z=3$", fontsize=10)
    ax.text(0, 1.2, 0.0, "$z=0$", fontsize=10)
    ax.text(1.15, 0, 1.5, "$x^2+y^2=1$", fontsize=10)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4); ax.set_zlim(0, 3.2)
    _save("chpt12_ex016")


# ex017 — cone z²=x²+y², 0≤z≤h (open at top)
def fig_ex017():
    h = 1.5
    fig = plt.figure(figsize=(5.0, 5.0), dpi=150)
    ax = _setup_3d(fig, elev=22, azim=-58, box=(1, 1, 1.0))

    th = np.linspace(0, 2 * np.pi, 60)
    z = np.linspace(0, h, 30)
    TH, Z = np.meshgrid(th, z)
    X, Y = Z * np.cos(TH), Z * np.sin(TH)
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.5, linewidth=0)

    # rim at z=h
    ax.plot(h * np.cos(th), h * np.sin(th), np.full_like(th, h), "k-", lw=1.2)
    # downward normals at sample points (cone outer normal points outward & down)
    for ph in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        zs = h * 0.6
        x0, y0 = zs * np.cos(ph), zs * np.sin(ph)
        # outward normal of z² = x²+y² (pointing away from axis): (x, y, -z)/√(2)·(1) — for downward (lower) side
        nx, ny, nz = np.cos(ph), np.sin(ph), -1.0
        n = np.sqrt(2)
        ax.quiver(x0, y0, zs, nx / n, ny / n, nz / n, length=0.35, color="#dc2626",
                  arrow_length_ratio=0.4, lw=1.0)

    ax.text(0, 0, h + 0.15, "$z=h$", fontsize=10, ha="center")
    ax.text(0.05, 0.05, 0.0, "$O$", fontsize=10)
    ax.text(h * 0.75, h * 0.75, h * 0.45, "$\\Sigma$", fontsize=11)
    ax.set_xlim(-h, h); ax.set_ylim(-h, h); ax.set_zlim(0, h + 0.2)
    _save("chpt12_ex017")


# ex019 — triangle x+y+z=1 in first octant
def fig_ex019():
    fig = plt.figure(figsize=(5.0, 4.6), dpi=150)
    ax = _setup_3d(fig, elev=24, azim=-50)

    verts = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    tri = Poly3DCollection([verts], alpha=0.45, facecolor=cm.viridis(0.55),
                            edgecolor="black", linewidth=2.0)
    ax.add_collection3d(tri)

    # axes-arrows along edges
    edges = [(verts[0], verts[1]), (verts[1], verts[2]), (verts[2], verts[0])]
    for a0, a1 in edges:
        mid = (a0 + a1) / 2
        d = (a1 - a0) * 0.25
        ax.quiver(mid[0] - d[0]/2, mid[1] - d[1]/2, mid[2] - d[2]/2,
                  d[0], d[1], d[2], color="black", arrow_length_ratio=0.5, lw=1.6)

    for v, lbl in zip(verts, ["$(1,0,0)$", "$(0,1,0)$", "$(0,0,1)$"]):
        ax.scatter(*v, color="black", s=18)
        ax.text(v[0] + 0.04, v[1] + 0.04, v[2] + 0.06, lbl, fontsize=9)

    # normal direction
    n_hat = np.array([1, 1, 1]) / np.sqrt(3)
    centroid = verts.mean(axis=0)
    ax.quiver(*centroid, *n_hat, length=0.35, color="#dc2626",
              arrow_length_ratio=0.4, lw=1.5)
    ax.text(centroid[0] + 0.25, centroid[1] + 0.18, centroid[2] + 0.30,
            "$\\vec n$", color="#dc2626", fontsize=11)
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.1); ax.set_zlim(0, 1.1)
    _save("chpt12_ex019")


# ex020 — hexagonal section of cube by x+y+z=3/2
def fig_ex020():
    fig = plt.figure(figsize=(5.4, 5.0), dpi=150)
    ax = _setup_3d(fig, elev=24, azim=-50)

    # cube wireframe
    cube_verts = np.array([(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)])
    edges = [(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]
    for i, j in edges:
        a, b = cube_verts[i], cube_verts[j]
        ax.plot(*zip(a, b), color="#666", lw=0.8)

    # hexagon vertices: intersection of x+y+z=3/2 with cube edges
    hex_v = np.array([
        (1, 0.5, 0), (0.5, 1, 0), (0, 1, 0.5),
        (0, 0.5, 1), (0.5, 0, 1), (1, 0, 0.5),
    ])
    poly = Poly3DCollection([hex_v], alpha=0.55, facecolor=cm.viridis(0.6),
                            edgecolor="black", linewidth=2.0)
    ax.add_collection3d(poly)

    # CCW direction arrow on hexagon (looking from +x)
    for i in [0, 2, 4]:
        a0, a1 = hex_v[i], hex_v[(i + 1) % 6]
        d = (a1 - a0) * 0.5
        mid = (a0 + a1) / 2
        ax.quiver(mid[0] - d[0]/2, mid[1] - d[1]/2, mid[2] - d[2]/2,
                  d[0], d[1], d[2], color="black", arrow_length_ratio=0.4, lw=1.5)

    ax.text(0.5, 0.5, 1.18, "$x+y+z=3/2$", fontsize=10, ha="center")
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.1); ax.set_zlim(0, 1.1)
    _save("chpt12_ex020")


# ex021 — curve (t³, t², t), 0≤t≤1
def fig_ex021():
    fig = plt.figure(figsize=(5.0, 4.4), dpi=150)
    ax = _setup_3d(fig, elev=20, azim=-55)

    t = np.linspace(0, 1, 200)
    x, y, z = t**3, t**2, t
    ax.plot(x, y, z, "k-", lw=2.4)
    ax.scatter([0, 1], [0, 1], [0, 1], color="black", s=22)
    ax.text(-0.05, -0.05, -0.05, "$t=0$", fontsize=10)
    ax.text(1.02, 1.02, 1.02, "$t=1$", fontsize=10)
    # direction arrow at t=0.6
    i0 = 120
    d = np.array([x[i0+5]-x[i0-5], y[i0+5]-y[i0-5], z[i0+5]-z[i0-5]])
    ax.quiver(x[i0]-d[0]/2, y[i0]-d[1]/2, z[i0]-d[2]/2, d[0], d[1], d[2],
              color="black", arrow_length_ratio=0.35, lw=1.6)

    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.1); ax.set_zlim(0, 1.1)
    _save("chpt12_ex021")


# ex026 — F = z·k̂ through upper hemisphere, z ≥ 0
def fig_ex026():
    a = 1.0
    fig = plt.figure(figsize=(5.0, 4.4), dpi=150)
    ax = _setup_3d(fig, elev=22, azim=-50)

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi / 2, 30)
    X = a * np.outer(np.cos(u), np.sin(v))
    Y = a * np.outer(np.sin(u), np.sin(v))
    Z = a * np.outer(np.ones_like(u), np.cos(v))
    norm = plt.Normalize(vmin=0, vmax=a)
    fc = cm.viridis(norm(Z))
    ax.plot_surface(X, Y, Z, facecolors=fc, alpha=0.7, linewidth=0,
                    antialiased=True, shade=False)

    # vertical field arrows F = z k̂ at sample points
    for ph in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        for r in [0.4, 0.85]:
            x0 = r * np.cos(ph); y0 = r * np.sin(ph)
            z0 = np.sqrt(max(a**2 - r**2, 0)) + 0.05
            ax.quiver(x0, y0, z0, 0, 0, 0.25, color="black",
                      arrow_length_ratio=0.4, lw=1.0)

    ax.text(0, 0, a + 0.15, "$\\Sigma:\\,z=\\sqrt{a^2-x^2-y^2}$",
            fontsize=9.5, ha="center")
    ax.set_xlim(-a, a); ax.set_ylim(-a, a); ax.set_zlim(0, a + 0.3)
    sm = cm.ScalarMappable(norm=norm, cmap=cm.viridis); sm.set_array([])
    fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.10, shrink=0.7,
                 label=r"$F\cdot\vec n=z$")
    _save("chpt12_ex026")


if __name__ == "__main__":
    fig_ex003()
    fig_ex004()
    fig_ex005()
    fig_ex006()
    fig_ex007()
    fig_ex008()
    fig_ex010()
    fig_ex011()
    fig_ex012()
    fig_ex014()
    fig_ex015()
    fig_ex016()
    fig_ex017()
    fig_ex019()
    fig_ex020()
    fig_ex021()
    fig_ex024()
    fig_ex026()
