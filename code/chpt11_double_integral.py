"""
chpt11_double_integral.py
Generates a 3D illustration of the double integral as a Riemann sum:
  z = f(x,y) = 1 - 0.5*(x^2 + y^2)  over  D = [0,1]x[0,1]
Shows the surface and N×N rectangular pillars approximating the volume.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ── function ──────────────────────────────────────────────────────────────────

def f(x, y):
    return 1.2 - 0.5 * (x**2 + y**2)

# ── figure setup ──────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(7, 5.5), dpi=150)
ax = fig.add_subplot(111, projection="3d")
ax.set_box_aspect([1, 1, 0.75])

# ── smooth surface ────────────────────────────────────────────────────────────

xs = np.linspace(0, 1, 60)
ys = np.linspace(0, 1, 60)
X, Y = np.meshgrid(xs, ys)
Z = f(X, Y)

surf = ax.plot_surface(
    X, Y, Z,
    cmap=cm.YlOrRd,
    alpha=0.60,
    linewidth=0,
    antialiased=True,
    zorder=3,
)

# ── Riemann pillars ───────────────────────────────────────────────────────────

N = 4  # N×N grid of pillars
xi = np.linspace(0, 1, N + 1)
yi = np.linspace(0, 1, N + 1)
dx = xi[1] - xi[0]
dy = yi[1] - yi[0]

pillar_color = "#93c5fd"   # light blue
pillar_edge  = "#1e40af"   # dark blue

for i in range(N):
    for j in range(N):
        x0, x1 = xi[i], xi[i + 1]
        y0, y1 = yi[j], yi[j + 1]
        # sample at centre
        xc = 0.5 * (x0 + x1)
        yc = 0.5 * (y0 + y1)
        zc = f(xc, yc)

        # 6 faces of the rectangular pillar
        verts = [
            # bottom
            [(x0,y0,0),(x1,y0,0),(x1,y1,0),(x0,y1,0)],
            # top
            [(x0,y0,zc),(x1,y0,zc),(x1,y1,zc),(x0,y1,zc)],
            # front (y=y0)
            [(x0,y0,0),(x1,y0,0),(x1,y0,zc),(x0,y0,zc)],
            # back (y=y1)
            [(x0,y1,0),(x1,y1,0),(x1,y1,zc),(x0,y1,zc)],
            # left (x=x0)
            [(x0,y0,0),(x0,y1,0),(x0,y1,zc),(x0,y0,zc)],
            # right (x=x1)
            [(x1,y0,0),(x1,y1,0),(x1,y1,zc),(x1,y0,zc)],
        ]
        poly = Poly3DCollection(
            verts,
            alpha=0.40,
            facecolor=pillar_color,
            edgecolor=pillar_edge,
            linewidth=0.6,
            zorder=2,
        )
        ax.add_collection3d(poly)

        # dot at (xc, yc, zc)
        ax.scatter([xc], [yc], [zc], color=pillar_edge, s=10, zorder=5)

# ── region D outline on z=0 ───────────────────────────────────────────────────

rect_x = [0, 1, 1, 0, 0]
rect_y = [0, 0, 1, 1, 0]
rect_z = [0, 0, 0, 0, 0]
ax.plot(rect_x, rect_y, rect_z, color="#374151", linewidth=1.2, zorder=4)
ax.text(0.5, -0.12, 0, "$D$", fontsize=13, ha="center", color="#374151")

# ── annotation: ΔA and f(xi,yi) ──────────────────────────────────────────────

# pick one pillar to annotate
i0, j0 = 1, 2
x0, x1 = xi[i0], xi[i0 + 1]
y0, y1 = yi[j0], yi[j0 + 1]
xc, yc = 0.5*(x0+x1), 0.5*(y0+y1)
zc = f(xc, yc)

# vertical dashed line from top of pillar to surface label
ax.plot([xc, xc], [yc, yc], [0, zc],
        color=pillar_edge, linewidth=0.8, linestyle="--", zorder=6)

ax.text(xc + 0.06, yc - 0.08, zc + 0.06,
        "$f(x_i,y_i)$", fontsize=10, color="#b91c1c",
        fontweight="bold", zorder=7)
ax.text(xc - 0.03, yc + 0.03, -0.10,
        "$\\Delta A$", fontsize=10, color="#374151",
        fontweight="bold", zorder=7)

# ── axes ──────────────────────────────────────────────────────────────────────

ax.set_xlabel("$x$", fontsize=11, labelpad=2)
ax.set_ylabel("$y$", fontsize=11, labelpad=2)
ax.set_zlabel("$z$", fontsize=11, labelpad=2)
ax.set_xlim(0, 1);  ax.set_ylim(0, 1);  ax.set_zlim(0, 1.4)
ax.set_xticks([0, 0.5, 1])
ax.set_yticks([0, 0.5, 1])
ax.set_zticks([0, 0.5, 1])
ax.tick_params(labelsize=8)

# title
ax.set_title(
    "$V \\approx \\sum_{i=1}^{N} f(x_i,y_i)\\,\\Delta A$",
    fontsize=12, pad=8, color="#1e3a8a",
)

ax.view_init(elev=22, azim=-55)

out = "media/img/chpt11_double_integral.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved → {out}")
plt.close()
