"""
chpt10_ex_figs.py — figures for chpt10 multivariate-differentiation exercises.
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
# ex001: f = (x²+y²) sin(1/(x²+y²)) — oscillates near origin but limit = 0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex001():
    fig = plt.figure(figsize=(5.4, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-0.5, 0.5, 200); y = np.linspace(-0.5, 0.5, 200)
    X, Y = np.meshgrid(x, y); R2 = X**2 + Y**2
    R2 = np.where(R2 < 1e-6, 1e-6, R2)
    Z = R2 * np.sin(1 / R2)
    ax.plot_surface(X, Y, Z, cmap=cm.RdBu_r, linewidth=0, alpha=0.95)
    # bounding cone ±r²
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=20, azim=-58)
    ax.set_title(r"$z = (x^2+y^2)\sin\frac{1}{x^2+y^2}$ — 在原点附近被 $\pm r^2$ 夹住", fontsize=10)
    _save("chpt10_ex001")


# ──────────────────────────────────────────────────────────────────────────────
# ex002: xy/(x²+y²) — limit at origin does not exist
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex002():
    fig = plt.figure(figsize=(5.4, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-1, 1, 80); y = np.linspace(-1, 1, 80)
    X, Y = np.meshgrid(x, y); R2 = X**2 + Y**2
    R2 = np.where(R2 < 1e-6, 1e-6, R2)
    Z = X * Y / R2
    ax.plot_surface(X, Y, Z, cmap=cm.RdBu_r, linewidth=0, alpha=0.92)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=20, azim=-58)
    ax.set_title(r"$z = xy/(x^2+y^2)$ — 沿 $y=kx$ 取值不同, 极限不存在", fontsize=10)
    _save("chpt10_ex002")


# ──────────────────────────────────────────────────────────────────────────────
# ex009: Trapezoidal cross-section channel
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex009():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    L = 24
    x = 6.0; theta = np.deg2rad(60)
    # bottom width = L - 2x; sides angle θ, length x; top width = bottom + 2x cosθ
    bw = L - 2*x
    h = x * np.sin(theta)
    top_extra = x * np.cos(theta)
    pts = [(-bw/2 - top_extra, h), (-bw/2, 0), (bw/2, 0), (bw/2 + top_extra, h)]
    xs, ys = zip(*pts)
    ax.fill(xs, ys, color="#bfdbfe", alpha=0.7)
    ax.plot(xs, ys, color="#1d4ed8", lw=2.4)
    # mark θ
    ax.annotate("", xy=(-bw/2 + 0.6, 0), xytext=(-bw/2 - 0.4, 0.6),
                arrowprops=dict(arrowstyle="-", color="black", lw=0.8))
    ax.text(-bw/2 + 0.6, 0.4, r"$\theta$", fontsize=12)
    ax.text(-bw/2 + bw/2*0.8 - 1.2, -0.7, r"底宽 $L-2x$", fontsize=10, ha="center")
    ax.text(-bw/2 - 1.5, h/2, r"$x$", fontsize=11)
    ax.text(0, h + 0.4, r"截面: $S = (L\!-\!2x)\,x\sin\theta + x^2\sin\theta\cos\theta$",
            ha="center", fontsize=10)
    ax.set_xlim(-L/2 - 1, L/2 + 1); ax.set_ylim(-1.5, h + 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    _save("chpt10_ex009")


# ──────────────────────────────────────────────────────────────────────────────
# ex010: gradient field of f = 1/(x²+y²)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex010():
    fig, ax = plt.subplots(figsize=(5.4, 4.4), dpi=150)
    x = np.linspace(-1.5, 1.5, 220); y = np.linspace(-1.5, 1.5, 220)
    X, Y = np.meshgrid(x, y); R2 = X**2 + Y**2
    R2c = np.where(R2 < 0.05, 0.05, R2)
    F = 1 / R2c
    pcm = ax.pcolormesh(X, Y, F, cmap=cm.viridis, shading="auto", vmin=0.5, vmax=8)
    fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04, label=r"$f = 1/(x^2+y^2)$")
    qx = np.linspace(-1.3, 1.3, 9); qy = np.linspace(-1.3, 1.3, 9)
    QX, QY = np.meshgrid(qx, qy); QR2 = QX**2 + QY**2
    mask = QR2 > 0.1
    # ∇f = -2(x,y)/r⁴
    U = -2*QX / np.where(QR2 < 0.05, 0.05, QR2)**2
    V = -2*QY / np.where(QR2 < 0.05, 0.05, QR2)**2
    ax.quiver(QX[mask], QY[mask], U[mask], V[mask], color="white",
              alpha=0.95, scale=120, width=0.005)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_title(r"$f=1/(x^2+y^2)$ — 等高线为同心圆, $\nabla f$ 指向原点", fontsize=10)
    _save("chpt10_ex010")


# ──────────────────────────────────────────────────────────────────────────────
# ex011: gradient at P₀ for f = x³ - xy² - z² (just show contours of restriction)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex011():
    fig, ax = plt.subplots(figsize=(5.4, 4.4), dpi=150)
    # restrict to z=0 slice — f(x,y,0) = x³ - xy²
    x = np.linspace(-1.5, 2.0, 220); y = np.linspace(-1.5, 1.5, 220)
    X, Y = np.meshgrid(x, y)
    F = X**3 - X*Y**2
    cs = ax.contour(X, Y, F, levels=14, cmap=cm.viridis)
    ax.clabel(cs, inline=True, fontsize=8, fmt="%.1f")
    # gradient at P0=(1,1) on z=0 slice: ∇f = (3x²-y², -2xy, -2z) = (2, -2, 0)
    ax.scatter([1], [1], color="#dc2626", s=70, zorder=5)
    ax.annotate("", xy=(1 + 0.4, 1 - 0.4), xytext=(1, 1),
                arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=2.2,
                                mutation_scale=14))
    ax.text(1.5, 0.45, r"$\nabla f = (2,-2,0)$ — 最快增长方向",
            color="#dc2626", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_title(r"$f$ 的 $z=0$ 截面等高线 ($P_0=(1,1,0)$)", fontsize=10)
    _save("chpt10_ex011")


# ──────────────────────────────────────────────────────────────────────────────
# ex012: tangent plane to x²+y²+z=9 at (1,2,4)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex012():
    fig = plt.figure(figsize=(5.4, 4.6), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-2, 4, 40); y = np.linspace(-1, 4, 40)
    X, Y = np.meshgrid(x, y); Z = 9 - X**2 - Y**2
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.5, linewidth=0)
    P = np.array([1, 2, 4])
    n = np.array([2, 4, 1])  # = (2x, 2y, 1) at P
    # tangent plane: 2(x-1) + 4(y-2) + (z-4) = 0 → z = 4 - 2(x-1) - 4(y-2) = 14 - 2x - 4y
    xs = np.linspace(-1, 3, 20); ys = np.linspace(0, 4, 20)
    Xt, Yt = np.meshgrid(xs, ys); Zt = 14 - 2*Xt - 4*Yt
    ax.plot_surface(Xt, Yt, Zt, color="#dc2626", alpha=0.4, linewidth=0)
    ax.scatter(*P, color="black", s=50)
    ax.quiver(*P, *n, length=0.18, color="black", arrow_length_ratio=0.3, lw=1.6)
    ax.text(*(P + np.array([0.4, 0.4, 0.6])), r"$\vec n=(2,4,1)$", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=22, azim=-50)
    ax.set_xlim(-1, 3); ax.set_ylim(0, 4); ax.set_zlim(-1, 9)
    _save("chpt10_ex012")


# ──────────────────────────────────────────────────────────────────────────────
# ex013: 长方形铁板折成等腰梯形水槽
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex013():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), dpi=150)
    # left: flat plate
    ax = axes[0]
    ax.add_patch(plt.Rectangle((-12, -1), 24, 2, color="#dbeafe", ec="#1d4ed8", lw=1.5))
    ax.axvline(-12 + 6, color="#dc2626", lw=1.2, ls="--")
    ax.axvline(12 - 6, color="#dc2626", lw=1.2, ls="--")
    ax.text(-9, 0, "$x$", fontsize=12, color="#dc2626")
    ax.text(9, 0, "$x$", fontsize=12, color="#dc2626")
    ax.text(0, -1.6, r"$L-2x$ (底)", ha="center", fontsize=10)
    ax.text(0, 1.8, "宽 $L=24$ 厘米的铁板", ha="center", fontsize=10)
    ax.set_xlim(-14, 14); ax.set_ylim(-3, 3); ax.set_aspect("equal"); ax.axis("off")
    # right: folded
    ax = axes[1]
    x_fold = 6.0; theta = np.deg2rad(60)
    bw = 24 - 2*x_fold
    h = x_fold * np.sin(theta); te = x_fold * np.cos(theta)
    pts = [(-bw/2 - te, h), (-bw/2, 0), (bw/2, 0), (bw/2 + te, h)]
    xs, ys = zip(*pts)
    ax.fill(xs, ys, color="#bfdbfe", alpha=0.6)
    ax.plot(xs, ys, color="#1d4ed8", lw=2.4)
    ax.text(-bw/2 - 1.2, h/2 + 0.3, r"$x$", fontsize=12, color="#dc2626")
    ax.text(0, -1.0, r"底宽 $L-2x$", ha="center", fontsize=10)
    ax.annotate("", xy=(-bw/2 + 0.6, 0), xytext=(-bw/2 - 0.4, 0.6),
                arrowprops=dict(arrowstyle="-", color="black", lw=0.8))
    ax.text(-bw/2 + 0.5, 0.5, r"$\theta$", fontsize=12)
    ax.set_xlim(-14, 14); ax.set_ylim(-2, h + 2); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("折出后的等腰梯形截面", fontsize=10, pad=8)
    axes[0].set_title("折之前", fontsize=10, pad=8)
    _save("chpt10_ex013")


# ──────────────────────────────────────────────────────────────────────────────
# ex014: optimal box dimensions
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex014():
    fig = plt.figure(figsize=(4.8, 4.4), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    a = 2 ** (1/3)  # cube root of 2
    # box [0,a]³
    pts = [(x, y, z) for x in (0, a) for y in (0, a) for z in (0, a)]
    edges = [(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]
    pts = np.array(pts)
    for i, j in edges:
        ax.plot(*zip(pts[i], pts[j]), color="#1d4ed8", lw=2.0)
    # face shading
    faces = [
        [pts[0], pts[1], pts[3], pts[2]],
        [pts[0], pts[1], pts[5], pts[4]],
        [pts[0], pts[2], pts[6], pts[4]],
    ]
    coll = Poly3DCollection(faces, alpha=0.18, facecolor="#bfdbfe", edgecolor="none")
    ax.add_collection3d(coll)
    ax.text(a/2, a/2, a + 0.1, r"$V = abc = 2\,\mathrm{m}^3$", fontsize=10, ha="center")
    ax.text(a + 0.1, a/2, 0, r"$a$", fontsize=11)
    ax.text(a/2, a + 0.1, 0, r"$b$", fontsize=11)
    ax.text(0, 0, a + 0.05, r"$c$", fontsize=11)
    ax.text(a/2, a/2, -0.4,
            r"用料最省: $a=b=c=\sqrt[3]{2}$ 米 (立方体)",
            ha="center", fontsize=10, color="#dc2626")
    ax.set_xlim(0, a + 0.5); ax.set_ylim(0, a + 0.5); ax.set_zlim(-0.5, a + 0.5)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.view_init(elev=22, azim=-50)
    _save("chpt10_ex014")


# ──────────────────────────────────────────────────────────────────────────────
# ex015: annulus 1 < x²+y² < 2
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex015():
    fig, ax = plt.subplots(figsize=(5.0, 4.6), dpi=150)
    th = np.linspace(0, 2*np.pi, 400)
    # annulus
    rs = np.linspace(1, np.sqrt(2), 30); pp = np.linspace(0, 2*np.pi, 60)
    R, P = np.meshgrid(rs, pp); X, Y = R*np.cos(P), R*np.sin(P)
    ax.scatter(X, Y, s=2, color="#bfdbfe")
    ax.plot(np.cos(th), np.sin(th), color="#dc2626", lw=2.0, ls="--",
            label=r"$x^2+y^2=1$ (边界, 不在 D 内)")
    ax.plot(np.sqrt(2)*np.cos(th), np.sqrt(2)*np.sin(th), color="#dc2626", lw=2.0, ls="--")
    # sample points
    ax.scatter([1.2], [0], color="#16a34a", s=70, zorder=5, label="内点")
    ax.scatter([0], [0], color="#f59e0b", s=70, zorder=5, label="外点 (在 D 之外)")
    ax.scatter([1, np.sqrt(2)], [0, 0], color="#dc2626", s=70, zorder=5,
               marker="x", label="边界点")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title(r"集合 $D = \{1 < x^2+y^2 < 2\}$ 的内点 / 外点 / 边界点", fontsize=10)
    _save("chpt10_ex015")


# ──────────────────────────────────────────────────────────────────────────────
# ex020: implicit dy/dx for x²+y²=1
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex020():
    fig, ax = plt.subplots(figsize=(5.0, 4.6), dpi=150)
    th = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="#2563eb", lw=2.4, label=r"$x^2+y^2=1$")
    P = np.array([np.cos(np.pi/3), np.sin(np.pi/3)])  # (1/2, √3/2)
    # dy/dx = -x/y = -1/√3
    slope = -P[0] / P[1]
    xt = np.linspace(P[0] - 0.6, P[0] + 0.6, 50)
    yt = slope * (xt - P[0]) + P[1]
    ax.plot(xt, yt, color="#dc2626", lw=2.0, label=r"切线 (斜率 $-x/y$)")
    ax.scatter(*P, color="black", s=60, zorder=5)
    ax.text(P[0] + 0.06, P[1] + 0.06, r"$(1/2, \sqrt{3}/2)$", fontsize=10)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_aspect("equal")
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
    ax.axhline(0, color="#999", lw=0.6); ax.axvline(0, color="#999", lw=0.6)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=10)
    _save("chpt10_ex020")


if __name__ == "__main__":
    fig_ex001(); fig_ex002(); fig_ex009(); fig_ex010()
    fig_ex011(); fig_ex012(); fig_ex013(); fig_ex014()
    fig_ex015(); fig_ex020()
