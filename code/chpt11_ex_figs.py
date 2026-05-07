"""
chpt11_ex_figs.py — figures for chpt11 multiple-integral exercises.
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
# ex001: f = 1 - x² - y² over D = [0,1]×[0,1]
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex001():
    fig = plt.figure(figsize=(5.4, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(0, 1, 30); y = np.linspace(0, 1, 30)
    X, Y = np.meshgrid(x, y); Z = 1 - X**2 - Y**2
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.6, linewidth=0)
    # base square
    sq = [(0,0,0),(1,0,0),(1,1,0),(0,1,0)]
    ax.add_collection3d(Poly3DCollection([sq], color="#dc2626", alpha=0.18))
    for a, b in [(0,1), (1,2), (2,3), (3,0)]:
        ax.plot(*zip(sq[a], sq[b]), color="#dc2626", lw=1.5)
    ax.text(0.5, 0.5, -0.15, "$D=[0,1]^2$", ha="center", color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=22, azim=-58)
    _save("chpt11_ex001")


# ──────────────────────────────────────────────────────────────────────────────
# ex002: quarter unit disc, integrand 1-x²-y²
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex002():
    fig, ax = plt.subplots(figsize=(4.6, 4.6), dpi=150)
    th = np.linspace(0, np.pi/2, 100)
    cx = np.cos(th); cy = np.sin(th)
    region = np.concatenate([[0], cx, [0]])
    region_y = np.concatenate([[0], cy, [0]])
    ax.fill(region, region_y, color="#bfdbfe", alpha=0.6, label=r"$D$")
    ax.plot(cx, cy, color="#dc2626", lw=2.0)
    ax.plot([0, 1, 0], [0, 0, 0], color="#dc2626", lw=2.0)
    ax.plot([0, 0], [0, 1], color="#dc2626", lw=2.0)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-0.1, 1.2); ax.set_ylim(-0.1, 1.2)
    ax.grid(True, alpha=0.25)
    ax.set_title(r"$D = \{x^2+y^2 \leq 1, x\geq 0, y\geq 0\}$ — 第一象限的 1/4 圆盘", fontsize=10)
    _save("chpt11_ex002")


# ──────────────────────────────────────────────────────────────────────────────
# ex003: triangle bounded by y=1, x=2, y=x
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex003():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    pts = [(1, 1), (2, 1), (2, 2)]
    xs, ys = zip(*(pts + [pts[0]]))
    ax.fill(xs, ys, color="#bfdbfe", alpha=0.65)
    ax.plot(xs, ys, color="#dc2626", lw=2.0)
    # boundary line annotations
    ax.axhline(1, color="#888", lw=0.8, ls=":")
    ax.axvline(2, color="#888", lw=0.8, ls=":")
    xs2 = np.linspace(0, 3, 50)
    ax.plot(xs2, xs2, color="#888", lw=0.8, ls=":")
    ax.text(1.4, 0.85, "$y=1$", color="#dc2626", fontsize=11)
    ax.text(2.05, 1.5, "$x=2$", color="#dc2626", fontsize=11)
    ax.text(1.0, 1.3, "$y=x$", color="#dc2626", fontsize=11)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.grid(True, alpha=0.25)
    _save("chpt11_ex003")


# ──────────────────────────────────────────────────────────────────────────────
# ex004: triangle bounded by y=x, x=-1, y=1
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex004():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)
    pts = [(-1, -1), (1, 1), (-1, 1)]
    xs, ys = zip(*(pts + [pts[0]]))
    ax.fill(xs, ys, color="#bfdbfe", alpha=0.65)
    ax.plot(xs, ys, color="#dc2626", lw=2.0)
    ax.axhline(1, color="#888", lw=0.8, ls=":")
    ax.axvline(-1, color="#888", lw=0.8, ls=":")
    xs2 = np.linspace(-2, 2, 50)
    ax.plot(xs2, xs2, color="#888", lw=0.8, ls=":")
    ax.text(0, 0.7, "$y=x$", color="#dc2626", fontsize=11)
    ax.text(-1.15, 0.5, "$x=-1$", color="#dc2626", fontsize=11)
    ax.text(-0.4, 1.05, "$y=1$", color="#dc2626", fontsize=11)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.grid(True, alpha=0.25)
    _save("chpt11_ex004")


# ──────────────────────────────────────────────────────────────────────────────
# ex005: polar curve ρ = 2 cos θ — circle of radius 1 centered at (1, 0)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex005():
    fig, ax = plt.subplots(figsize=(5.0, 4.6), dpi=150)
    th = np.linspace(-np.pi/2, np.pi/2, 200)
    rho = 2 * np.cos(th)
    x = rho * np.cos(th); y = rho * np.sin(th)
    ax.fill(x, y, color="#bfdbfe", alpha=0.65)
    ax.plot(x, y, color="#dc2626", lw=2.0, label=r"$\rho = 2\cos\theta$")
    ax.scatter([1], [0], color="black", s=30, zorder=5)
    ax.text(1.05, -0.1, "圆心 $(1,0)$", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color="#888", lw=0.6); ax.axvline(0, color="#888", lw=0.6)
    ax.grid(True, alpha=0.25); ax.legend(loc="upper right", fontsize=10)
    ax.set_title(r"$D$: 极坐标圆 $\rho = 2\cos\theta$ — 半径 1, 圆心在 $(1,0)$", fontsize=10)
    _save("chpt11_ex005")


# ──────────────────────────────────────────────────────────────────────────────
# ex007: sphere x²+y²+z² ≤ 4a² ∩ cylinder x²+y² ≤ 2ax
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex007():
    fig = plt.figure(figsize=(5.4, 4.6), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    a = 1.0
    # sphere
    u = np.linspace(0, 2*np.pi, 50); v = np.linspace(0, np.pi, 30)
    Xs = 2*a*np.outer(np.cos(u), np.sin(v))
    Ys = 2*a*np.outer(np.sin(u), np.sin(v))
    Zs = 2*a*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(Xs, Ys, Zs, color=cm.Blues(0.55), alpha=0.18, linewidth=0)
    # cylinder x²+y²=2ax  →  (x-a)²+y² = a²
    th = np.linspace(0, 2*np.pi, 60); zc = np.linspace(-2*a, 2*a, 30)
    TH, Zc = np.meshgrid(th, zc)
    Xc = a + a*np.cos(TH); Yc = a*np.sin(TH)
    # restrict to inside sphere
    mask = Xc**2 + Yc**2 + Zc**2 <= 4*a**2
    Xc_m = np.where(mask, Xc, np.nan)
    Yc_m = np.where(mask, Yc, np.nan)
    Zc_m = np.where(mask, Zc, np.nan)
    ax.plot_surface(Xc_m, Yc_m, Zc_m, color=cm.Greens(0.55), alpha=0.45, linewidth=0)
    ax.set_xlim(-2.2*a, 2.2*a); ax.set_ylim(-2.2*a, 2.2*a); ax.set_zlim(-2.2*a, 2.2*a)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=18, azim=-58)
    ax.set_title("球 (蓝, 透明) ∩ 圆柱 (绿) — 求圆柱内部分体积", fontsize=10)
    _save("chpt11_ex007")


# ──────────────────────────────────────────────────────────────────────────────
# ex008: ellipse area
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex008():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    a, b = 2.0, 1.2
    th = np.linspace(0, 2*np.pi, 200)
    x = a*np.cos(th); y = b*np.sin(th)
    ax.fill(x, y, color="#bfdbfe", alpha=0.65)
    ax.plot(x, y, color="#dc2626", lw=2.0, label=r"$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$")
    ax.plot([-a, a], [0, 0], color="#888", lw=0.8, ls=":")
    ax.plot([0, 0], [-b, b], color="#888", lw=0.8, ls=":")
    ax.text(a/2, 0.08, "$a$", color="black", fontsize=11)
    ax.text(0.08, b/2, "$b$", color="black", fontsize=11)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-a-0.3, a+0.3); ax.set_ylim(-b-0.3, b+0.3)
    ax.grid(True, alpha=0.25); ax.legend(loc="upper right", fontsize=10)
    ax.set_title(r"椭圆 — 面积 $= \pi ab$ (用变量替换 $x=ar\cos\theta, y=br\sin\theta$)", fontsize=10)
    _save("chpt11_ex008")


# ──────────────────────────────────────────────────────────────────────────────
# ex010: tetrahedron x+2y+z ≤ 1, x,y,z ≥ 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex010():
    fig = plt.figure(figsize=(5.0, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    verts = np.array([[0,0,0],[1,0,0],[0,0.5,0],[0,0,1]])
    faces = [
        [verts[0], verts[1], verts[2]],
        [verts[0], verts[1], verts[3]],
        [verts[0], verts[2], verts[3]],
        [verts[1], verts[2], verts[3]],
    ]
    for face in faces:
        coll = Poly3DCollection([face], alpha=0.45, facecolor=cm.viridis(0.55),
                                edgecolor="#1d4ed8", linewidth=1.5)
        ax.add_collection3d(coll)
    for v, lbl in zip(verts, ["$O$", "$(1,0,0)$", "$(0,1/2,0)$", "$(0,0,1)$"]):
        ax.scatter(*v, color="black", s=20)
        ax.text(v[0]+0.04, v[1]+0.04, v[2]+0.04, lbl, fontsize=9)
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 0.6); ax.set_zlim(0, 1.1)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=22, azim=-50)
    ax.set_title(r"$\Omega$: $x+2y+z \leq 1$, $x,y,z\geq 0$ 围成的四面体", fontsize=10)
    _save("chpt11_ex010")


# ──────────────────────────────────────────────────────────────────────────────
# ex011: paraboloid z = x²+y² capped at z = 4
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex011():
    fig = plt.figure(figsize=(5.2, 4.6), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    th = np.linspace(0, 2*np.pi, 60); r = np.linspace(0, 2, 30)
    R, T = np.meshgrid(r, th)
    X = R*np.cos(T); Y = R*np.sin(T); Z = R**2
    ax.plot_surface(X, Y, Z, color=cm.Blues(0.55), alpha=0.45, linewidth=0)
    # cap z=4
    ax.plot_surface(X, Y, np.full_like(X, 4), color=cm.Greens(0.55), alpha=0.4, linewidth=0)
    # boundary
    ax.plot(2*np.cos(th), 2*np.sin(th), [4]*60, color="#dc2626", lw=2.0)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.3, 2.3); ax.set_zlim(0, 4.3)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=18, azim=-58)
    ax.set_title(r"$\Omega$: 抛物面 $z=x^2+y^2$ (蓝) 与平面 $z=4$ (绿) 之间", fontsize=10)
    _save("chpt11_ex011")


# ──────────────────────────────────────────────────────────────────────────────
# ex013: Gaussian integral — bell curve with integral = √π
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex013():
    fig, ax = plt.subplots(figsize=(5.6, 3.6), dpi=150)
    x = np.linspace(-3.5, 3.5, 240)
    f = np.exp(-x**2)
    ax.plot(x, f, color="#2563eb", lw=2.4, label=r"$y = e^{-x^2}$")
    ax.fill_between(x, 0, f, color="#dc2626", alpha=0.22,
                    label=r"$\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-3.5, 3.5); ax.set_ylim(0, 1.1)
    ax.grid(True, alpha=0.25); ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Gauss 积分 — 用极坐标做平方再开方求得", fontsize=10)
    _save("chpt11_ex013")


if __name__ == "__main__":
    fig_ex001(); fig_ex002(); fig_ex003(); fig_ex004(); fig_ex005()
    fig_ex007(); fig_ex008(); fig_ex010(); fig_ex011(); fig_ex013()
