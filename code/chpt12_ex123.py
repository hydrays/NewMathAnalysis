"""
chpt12_ex123.py
Static figures for the first three first-kind line-integral examples in §12.2:

  ex023 — ∫_L (x²+y²) ds, L: unit circle x=cos t, y=sin t, t∈[0,2π]
          → 2D, f(x,y)=x²+y² as colormap, unit circle path in black

  ex001 — ∫_L √y ds, L: y=x², 0≤x≤1
          → 2D, f(x,y)=√y as colormap, parabolic path in black

  ex002 — ∫_Γ (x²+y²+z²) ds, helix x=a cos t, y=a sin t, z=k t
          → 3D, f shown on the y=0 slice plane as a colormap,
            helix path in black
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm

OUT_DIR = "media/img"


# ──────────────────────────────────────────────────────────────────────────────
# ex023: ∫_L (x²+y²) ds, L: unit circle
# ──────────────────────────────────────────────────────────────────────────────

def fig_ex023():
    fig, ax = plt.subplots(figsize=(5.0, 4.4), dpi=150)

    xs = np.linspace(-1.45, 1.45, 240)
    ys = np.linspace(-1.45, 1.45, 240)
    X, Y = np.meshgrid(xs, ys)
    F = X**2 + Y**2

    pcm = ax.pcolormesh(X, Y, F, cmap=cm.viridis, shading="auto")
    cbar = fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(r"$f(x,y)=x^2+y^2$", fontsize=10)

    # path: unit circle, traversed counter-clockwise
    t = np.linspace(0, 2 * np.pi, 400)
    px, py = np.cos(t), np.sin(t)
    ax.plot(px, py, color="black", linewidth=2.4, zorder=4)

    # direction arrow at t = π/4 (upper-right of the circle)
    i0 = 60
    ax.annotate(
        "", xy=(px[i0 + 6], py[i0 + 6]), xytext=(px[i0 - 6], py[i0 - 6]),
        arrowprops=dict(arrowstyle="-|>", color="black", lw=1.8, mutation_scale=14),
        zorder=5,
    )

    # start/end point at (1, 0)
    ax.scatter([1.0], [0.0], color="black", s=28, zorder=6)
    ax.text(1.05, 0.05, "$t=0$", fontsize=10, ha="left", va="bottom", color="black")

    ax.text(0.0, 0.05, "$L:\\;x^2+y^2=1$", fontsize=11, color="black", ha="center",
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.6, alpha=0.85))

    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.set_aspect("equal", adjustable="box")

    out = f"{OUT_DIR}/chpt12_ex023.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close(fig)


# ──────────────────────────────────────────────────────────────────────────────
# ex001: ∫_L √y ds, L: y=x², 0≤x≤1
# ──────────────────────────────────────────────────────────────────────────────

def fig_ex001():
    fig, ax = plt.subplots(figsize=(5.2, 4.4), dpi=150)

    xs = np.linspace(-0.05, 1.10, 240)
    ys = np.linspace(-0.05, 1.15, 240)
    X, Y = np.meshgrid(xs, ys)
    F = np.sqrt(np.clip(Y, 0, None))

    pcm = ax.pcolormesh(X, Y, F, cmap=cm.viridis, shading="auto")
    cbar = fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(r"$f(x,y)=\sqrt{y}$", fontsize=10)

    # path
    t = np.linspace(0, 1, 200)
    px, py = t, t**2
    ax.plot(px, py, color="black", linewidth=2.4, zorder=4)

    # direction arrow at midpoint
    mid = 120
    ax.annotate(
        "", xy=(px[mid + 8], py[mid + 8]), xytext=(px[mid - 8], py[mid - 8]),
        arrowprops=dict(arrowstyle="-|>", color="black", lw=1.8, mutation_scale=14),
        zorder=5,
    )

    # endpoints
    ax.scatter([0, 1], [0, 1], color="black", s=28, zorder=6)
    ax.text(-0.04, -0.02, "$O$", fontsize=12, ha="right", va="top", color="black")
    ax.text(1.03, 1.01, "$B$", fontsize=12, ha="left", va="bottom", color="black")

    # path label
    ax.text(0.42, 0.10, "$L:\\;y=x^2$", fontsize=11, color="black",
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="black", lw=0.6, alpha=0.85))

    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)
    ax.set_xlim(-0.05, 1.10)
    ax.set_ylim(-0.05, 1.15)
    ax.set_aspect("equal", adjustable="box")

    out = f"{OUT_DIR}/chpt12_ex001.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close(fig)


# ──────────────────────────────────────────────────────────────────────────────
# ex002: helix, ∫_Γ (x²+y²+z²) ds  with a=1, k=0.5
# ──────────────────────────────────────────────────────────────────────────────

def fig_ex002():
    a, k = 1.0, 0.5
    t = np.linspace(0, 2 * np.pi, 400)
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = k * t

    fig = plt.figure(figsize=(5.6, 5.0), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect([1, 1, 0.95])

    # field on y=0 slice plane (translucent so the full helix stays visible)
    nx, nz = 48, 48
    xs = np.linspace(-1.15, 1.15, nx)
    zs = np.linspace(0.0, 2 * np.pi * k, nz)
    Xp, Zp = np.meshgrid(xs, zs)
    Yp = np.zeros_like(Xp)
    Fp = Xp**2 + Yp**2 + Zp**2
    norm = plt.Normalize(vmin=Fp.min(), vmax=Fp.max())
    facecolors = cm.viridis(norm(Fp))
    facecolors[..., 3] = 0.6

    ax.plot_surface(
        Xp, Yp, Zp,
        facecolors=facecolors, rstride=1, cstride=1,
        shade=False, antialiased=True, linewidth=0,
    )

    # helix path
    ax.plot(x, y, z, color="black", linewidth=2.4)
    # endpoints
    ax.scatter([x[0], x[-1]], [y[0], y[-1]], [z[0], z[-1]],
               color="black", s=22, zorder=6)
    ax.text(x[0] + 0.05, y[0] - 0.05, z[0] - 0.10, "$t=0$",
            fontsize=10, color="black")
    ax.text(x[-1] + 0.05, y[-1] - 0.05, z[-1] + 0.10, "$t=2\\pi$",
            fontsize=10, color="black")

    # axes
    ax.set_xlabel("$x$", fontsize=10, labelpad=1)
    ax.set_ylabel("$y$", fontsize=10, labelpad=1)
    ax.set_zlabel("$z$", fontsize=10, labelpad=1)
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(0, 2 * np.pi * k)
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    ax.tick_params(labelsize=8)
    ax.view_init(elev=18, azim=-58)

    # colorbar (using scalar mappable since we drew with facecolors)
    sm = cm.ScalarMappable(norm=norm, cmap=cm.viridis)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, fraction=0.038, pad=0.10, shrink=0.75)
    cbar.set_label(r"$f=x^2+y^2+z^2$", fontsize=10)

    out = f"{OUT_DIR}/chpt12_ex002.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Saved → {out}")
    plt.close(fig)


if __name__ == "__main__":
    fig_ex023()
    fig_ex001()
    fig_ex002()
