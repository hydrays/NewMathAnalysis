"""
chpt9_ex_figs.py
3D figures for chpt9 (向量与空间解析几何) exercises.
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


def _ax3d(figsize=(5.0, 4.6), elev=22, azim=-58):
    fig = plt.figure(figsize=figsize, dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); ax.set_zlabel("$z$")
    ax.tick_params(labelsize=8)
    ax.view_init(elev=elev, azim=azim)
    return fig, ax


def _plane(ax, normal, d, x_range, y_range, color, alpha=0.4, n=20):
    """Plot plane n·r + d = 0 over (x,y) grid; choose z = -(d + nx*x + ny*y)/nz."""
    nx, ny, nz = normal
    xs = np.linspace(*x_range, n)
    ys = np.linspace(*y_range, n)
    X, Y = np.meshgrid(xs, ys)
    if abs(nz) > 1e-6:
        Z = -(d + nx * X + ny * Y) / nz
        ax.plot_surface(X, Y, Z, color=color, alpha=alpha, linewidth=0)
    elif abs(ny) > 1e-6:
        # plane parallel to z; param via x,z
        zs = np.linspace(-2, 2, n)
        X, Z = np.meshgrid(xs, zs)
        Y = -(d + nx * X) / ny
        ax.plot_surface(X, Y, Z, color=color, alpha=alpha, linewidth=0)


# ──────────────────────────────────────────────────────────────────────────────
# ex001: line as intersection of two planes
#   x+y+z+1=0 and 2x-y+3z+4=0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex001():
    fig, ax = _ax3d()
    R = (-2, 2)
    _plane(ax, (1, 1, 1), 1, R, R, color=cm.Blues(0.55), alpha=0.35)
    _plane(ax, (2, -1, 3), 4, R, R, color=cm.Greens(0.55), alpha=0.35)
    # Direction vector of line: n1 × n2 = (1,1,1)×(2,-1,3) = (4, -1, -3)
    # Find a point: set z=0 → x+y=-1, 2x-y=-4 → 3x=-5, x=-5/3, y=2/3
    p0 = np.array([-5/3, 2/3, 0.0])
    d = np.array([4, -1, -3.0]); d /= np.linalg.norm(d)
    ts = np.linspace(-1.5, 1.5, 100)
    pts = p0[None, :] + ts[:, None] * d[None, :]
    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], "k-", lw=2.6)
    ax.scatter(*p0, color="#dc2626", s=40)
    ax.text(*(p0 + np.array([0.1, 0.1, 0.2])),
            "交线", fontsize=10, color="black")
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
    _save("chpt9_ex001")


# ──────────────────────────────────────────────────────────────────────────────
# ex002: angle between two lines
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex002():
    fig, ax = _ax3d()
    # L1: dir (1,-4,1), L2: dir (2,-2,-1) — common point at origin for clarity
    d1 = np.array([1, -4, 1.0]); d1 /= np.linalg.norm(d1)
    d2 = np.array([2, -2, -1.0]); d2 /= np.linalg.norm(d2)
    ts = np.linspace(-1.5, 1.5, 50)
    p1 = ts[:, None] * d1; p2 = ts[:, None] * d2
    ax.plot(p1[:, 0], p1[:, 1], p1[:, 2], color="#2563eb", lw=2.4, label="$L_1$")
    ax.plot(p2[:, 0], p2[:, 1], p2[:, 2], color="#dc2626", lw=2.4, label="$L_2$")
    ax.scatter(0, 0, 0, color="black", s=30)
    # angle arc — sample around the corner
    arc_t = np.linspace(0, 1, 30)
    arc = np.array([d1 * (1 - t) + d2 * t for t in arc_t]) * 0.5
    arc = arc / np.linalg.norm(arc, axis=1, keepdims=True) * 0.4
    ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color="#16a34a", lw=1.5)
    ax.text(*(arc[15] * 1.4), r"$\theta$", fontsize=12, color="#16a34a")
    ax.legend(loc="upper left", fontsize=10)
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    _save("chpt9_ex002")


# ──────────────────────────────────────────────────────────────────────────────
# ex003: line through point (1,-2,4) perpendicular to plane 2x-3y+z-4=0
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex003():
    fig, ax = _ax3d()
    R = (-3, 4)
    _plane(ax, (2, -3, 1), -4, R, R, color=cm.Blues(0.55), alpha=0.35)
    P0 = np.array([1, -2, 4.0])
    n = np.array([2, -3, 1.0]); n /= np.linalg.norm(n)
    ts = np.linspace(-3, 3, 60)
    pts = P0[None, :] + ts[:, None] * n[None, :]
    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], color="#dc2626", lw=2.4)
    ax.scatter(*P0, color="black", s=40)
    ax.text(*P0 + np.array([0.2, 0.2, 0.3]), "$P(1,-2,4)$", fontsize=10)
    # arrow head
    tip = P0 + 1.5 * n
    ax.quiver(*P0, *(1.4*n), color="#dc2626", arrow_length_ratio=0.2)
    ax.text(*(tip + np.array([0.1, 0.1, 0.1])), r"$\vec n=(2,-3,1)$",
            fontsize=10, color="#dc2626")
    ax.set_xlim(-3, 4); ax.set_ylim(-3, 4); ax.set_zlim(-1, 6)
    _save("chpt9_ex003")


# ──────────────────────────────────────────────────────────────────────────────
# ex004: line through (-3,2,5) parallel to intersection of two planes
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex004():
    fig, ax = _ax3d()
    R = (-5, 4)
    _plane(ax, (1, 0, -4), -3, R, R, color=cm.Blues(0.55), alpha=0.30)
    _plane(ax, (2, -1, -5), -1, R, R, color=cm.Greens(0.55), alpha=0.30)
    # direction of intersection: n1 × n2 = (1,0,-4)×(2,-1,-5) = (-4, -3, -1)
    d = np.array([-4, -3, -1.0]); d /= np.linalg.norm(d)
    P0 = np.array([-3, 2, 5.0])
    ts = np.linspace(-3, 3, 60)
    pts = P0[None, :] + ts[:, None] * d[None, :]
    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], color="#dc2626", lw=2.4,
            label="目标直线 (与交线平行, 过 $P$)")
    ax.scatter(*P0, color="black", s=40)
    ax.text(*P0 + np.array([0.2, 0.2, 0.3]), "$P$", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(-5, 4); ax.set_ylim(-5, 4); ax.set_zlim(0, 8)
    _save("chpt9_ex004")


# ──────────────────────────────────────────────────────────────────────────────
# ex005: line piercing plane at single point
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex005():
    fig, ax = _ax3d()
    R = (-1, 5)
    _plane(ax, (2, 1, 1), -6, R, R, color=cm.Blues(0.55), alpha=0.35)
    P0 = np.array([2, 3, 4.0])
    d = np.array([1, 1, 2.0]); d /= np.linalg.norm(d)
    # intersection: 2(2+t·dx)+(3+t·dy)+(4+t·dz)=6 → 4+2dx t + 3+dy t + 4+2dz t = 6
    # 11 + (2dx+dy+2dz)t = 6 → t = -5/(2dx+dy+2dz)
    coef = 2*d[0] + d[1] + 2*d[2]; tstar = -5 / coef
    Pstar = P0 + tstar * d
    ts = np.linspace(tstar - 2, tstar + 2, 60)
    pts = P0[None, :] + ts[:, None] * d[None, :]
    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], color="#dc2626", lw=2.4)
    ax.scatter(*Pstar, color="#16a34a", s=70, zorder=5)
    ax.text(*(Pstar + 0.3), "交点", fontsize=10, color="#16a34a")
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5); ax.set_zlim(-1, 6)
    _save("chpt9_ex005")


# ──────────────────────────────────────────────────────────────────────────────
# ex006: two perpendicular intersecting lines
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex006():
    fig, ax = _ax3d()
    P = np.array([2, 1, 3.0])
    L_dir = np.array([3, 2, -1.0]); L_dir /= np.linalg.norm(L_dir)
    # Original line passes through (-1, 1, 0)
    L_p0 = np.array([-1, 1, 0.0])
    # Foot of perpendicular from P to L:
    v = P - L_p0
    foot = L_p0 + np.dot(v, L_dir) * L_dir
    # Perpendicular direction:
    perp = (P - foot); perp /= np.linalg.norm(perp)

    ts1 = np.linspace(-1, 4, 60)
    pts1 = L_p0[None, :] + ts1[:, None] * L_dir[None, :]
    ax.plot(pts1[:, 0], pts1[:, 1], pts1[:, 2], color="#2563eb", lw=2.4,
            label="已知直线")
    ts2 = np.linspace(0, np.linalg.norm(P - foot), 30)
    pts2 = foot[None, :] + ts2[:, None] * perp[None, :]
    ax.plot(pts2[:, 0], pts2[:, 1], pts2[:, 2], color="#dc2626", lw=2.4,
            label="目标直线 (过 $P$, 垂直相交)")
    ax.scatter(*P, color="black", s=40)
    ax.text(*P + 0.2, "$P$", fontsize=11)
    ax.scatter(*foot, color="#16a34a", s=40)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(-1, 4); ax.set_ylim(0, 5); ax.set_zlim(0, 4)
    _save("chpt9_ex006")


# ──────────────────────────────────────────────────────────────────────────────
# ex007: paraboloid of revolution z = a(x^2 + y^2) (a=1)
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex007():
    fig, ax = _ax3d()
    th = np.linspace(0, 2*np.pi, 60)
    r = np.linspace(0, 1.4, 30)
    R, T = np.meshgrid(r, th)
    X = R*np.cos(T); Y = R*np.sin(T); Z = R**2
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.55, linewidth=0)
    # generating parabola z=x² in xz plane
    xs = np.linspace(-1.4, 1.4, 60)
    ax.plot(xs, np.zeros_like(xs), xs**2, color="black", lw=1.8)
    ax.text(1.5, 0, 1.4, r"$z = ax^2$", fontsize=10, color="black")
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(0, 2.0)
    _save("chpt9_ex007")


# ──────────────────────────────────────────────────────────────────────────────
# ex008: cone of revolution z = k|sqrt(x^2+y^2)|
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex008():
    fig, ax = _ax3d()
    th = np.linspace(0, 2*np.pi, 60)
    r = np.linspace(0, 1.5, 30)
    R, T = np.meshgrid(r, th)
    k = 1.2
    X = R*np.cos(T); Y = R*np.sin(T); Z = k*R
    ax.plot_surface(X, Y, Z, color=cm.viridis(0.55), alpha=0.55, linewidth=0)
    # generating line z=k x in xz plane
    xs = np.linspace(-1.5, 1.5, 50)
    ax.plot(xs, np.zeros_like(xs), k*np.abs(xs), color="black", lw=1.8)
    ax.text(1.6, 0, k*1.6, r"$z = kx$", fontsize=10, color="black")
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6); ax.set_zlim(0, k*1.8)
    _save("chpt9_ex008")


# ──────────────────────────────────────────────────────────────────────────────
# ex009: x²+y²=1 ∩ 2x+3z=6 — a tilted ellipse on the cylinder
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex009():
    fig, ax = _ax3d()
    th = np.linspace(0, 2*np.pi, 60)
    z = np.linspace(0, 3, 30)
    TH, Z = np.meshgrid(th, z)
    Xc = np.cos(TH); Yc = np.sin(TH)
    ax.plot_surface(Xc, Yc, Z, color=cm.Blues(0.55), alpha=0.32, linewidth=0)
    # Plane 2x+3z=6 → z=(6-2x)/3
    xs = np.linspace(-1.4, 1.4, 30); ys = np.linspace(-1.4, 1.4, 30)
    X, Y = np.meshgrid(xs, ys); Z2 = (6 - 2*X) / 3
    ax.plot_surface(X, Y, Z2, color=cm.Greens(0.55), alpha=0.32, linewidth=0)
    # intersection curve
    th2 = np.linspace(0, 2*np.pi, 200)
    cx = np.cos(th2); cy = np.sin(th2); cz = (6 - 2*cx) / 3
    ax.plot(cx, cy, cz, color="#dc2626", lw=2.6)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(0, 3)
    _save("chpt9_ex009")


# ──────────────────────────────────────────────────────────────────────────────
# ex010: Viviani's curve — sphere x²+y²+z²=a² ∩ cylinder (x-a/2)²+y²=(a/2)²
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex010():
    fig, ax = _ax3d()
    a = 1.0
    # sphere
    u = np.linspace(0, 2*np.pi, 60); v = np.linspace(0, np.pi, 30)
    Xs = a*np.outer(np.cos(u), np.sin(v))
    Ys = a*np.outer(np.sin(u), np.sin(v))
    Zs = a*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(Xs, Ys, Zs, color=cm.Blues(0.55), alpha=0.22, linewidth=0)
    # cylinder
    th = np.linspace(0, 2*np.pi, 60); zc = np.linspace(-1, 1, 30)
    TH, Zc = np.meshgrid(th, zc)
    Xc = a/2 + (a/2)*np.cos(TH); Yc = (a/2)*np.sin(TH)
    ax.plot_surface(Xc, Yc, Zc, color=cm.Greens(0.55), alpha=0.30, linewidth=0)
    # Viviani: parametrize cylinder, restrict to sphere top half
    t = np.linspace(0, 2*np.pi, 400)
    cx = a/2 + (a/2)*np.cos(t); cy = (a/2)*np.sin(t)
    cz = np.sqrt(np.clip(a**2 - cx**2 - cy**2, 0, None))
    ax.plot(cx, cy, cz, color="#dc2626", lw=2.6)
    ax.plot(cx, cy, -cz, color="#dc2626", lw=2.6)
    ax.set_xlim(-1, 1.2); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
    _save("chpt9_ex010")


# ──────────────────────────────────────────────────────────────────────────────
# ex011: two spheres' intersection projected to xOy
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex011():
    fig, ax = _ax3d(figsize=(5.2, 5.0))
    # Sphere 1: x²+y²+z²=1, centered at origin
    # Sphere 2: x²+(y-1)²+(z-1)²=1, centered at (0,1,1)
    u = np.linspace(0, 2*np.pi, 50); v = np.linspace(0, np.pi, 30)
    for cent, color in [((0, 0, 0), cm.Blues(0.55)), ((0, 1, 1), cm.Greens(0.55))]:
        Xs = cent[0] + np.outer(np.cos(u), np.sin(v))
        Ys = cent[1] + np.outer(np.sin(u), np.sin(v))
        Zs = cent[2] + np.outer(np.ones_like(u), np.cos(v))
        ax.plot_surface(Xs, Ys, Zs, color=color, alpha=0.25, linewidth=0)
    # Subtract: 0 = (y² - (y-1)²) + (z² - (z-1)²) = 2y - 1 + 2z - 1 → y+z=1
    # And x²+y²+z²=1. Parameterize: z=1-y, x²+y²+(1-y)²=1 → x²+2y²-2y=0 → x²=2y-2y²
    # So projection on xOy: x²+2y²-2y=0, i.e. x² + 2(y-1/2)² = 1/2 — an ellipse.
    th = np.linspace(0, 2*np.pi, 200)
    yp = 0.5 + np.cos(th)/2; xp = np.sin(th)/np.sqrt(2)
    # the ellipse on z=0 plane:
    ax.plot(xp, yp, np.zeros_like(xp), color="#dc2626", lw=2.4, label="$xOy$ 投影")
    # the actual 3D intersection circle (lift y+z=1 to spheres)
    z3 = 1 - yp
    ax.plot(xp, yp, z3, color="#16a34a", lw=2.0, ls="--", label="实际交线")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 2.2); ax.set_zlim(-1.2, 2.2)
    _save("chpt9_ex011")


# ──────────────────────────────────────────────────────────────────────────────
# ex012: hemisphere ∩ cone — projection on xOy
# ──────────────────────────────────────────────────────────────────────────────
def fig_ex012():
    fig, ax = _ax3d(figsize=(5.2, 5.0))
    # z=√(4-x²-y²), z=√(3(x²+y²)). Intersect: 4-r²=3r² → r²=1, z=√3.
    u = np.linspace(0, 2*np.pi, 50); v = np.linspace(0, np.pi/2, 30)
    Xs = 2*np.outer(np.cos(u), np.sin(v))
    Ys = 2*np.outer(np.sin(u), np.sin(v))
    Zs = 2*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(Xs, Ys, Zs, color=cm.Blues(0.55), alpha=0.30, linewidth=0)
    th = np.linspace(0, 2*np.pi, 60); rs = np.linspace(0, 1.3, 30)
    R, T = np.meshgrid(rs, th)
    Xc = R*np.cos(T); Yc = R*np.sin(T); Zc = np.sqrt(3)*R
    ax.plot_surface(Xc, Yc, Zc, color=cm.Greens(0.55), alpha=0.40, linewidth=0)
    # circle of intersection: r=1, z=√3
    th2 = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(th2), np.sin(th2), [np.sqrt(3)]*100, color="#dc2626", lw=2.4)
    # projection on xOy: unit disc
    ax.plot(np.cos(th2), np.sin(th2), np.zeros(100), color="#dc2626", lw=2.4, ls="--",
            label="$xOy$ 投影")
    # disc shading
    rs2 = np.linspace(0, 1, 12); pp = np.linspace(0, 2*np.pi, 36)
    Rg, Pg = np.meshgrid(rs2, pp)
    Xd = Rg*np.cos(Pg); Yd = Rg*np.sin(Pg)
    ax.plot_surface(Xd, Yd, np.zeros_like(Xd), color="#dc2626", alpha=0.18)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(0, 2.5)
    _save("chpt9_ex012")


if __name__ == "__main__":
    fig_ex001(); fig_ex002(); fig_ex003(); fig_ex004(); fig_ex005()
    fig_ex006(); fig_ex007(); fig_ex008(); fig_ex009(); fig_ex010()
    fig_ex011(); fig_ex012()
