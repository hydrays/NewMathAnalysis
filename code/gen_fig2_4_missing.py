"""
Generate fig2-4-3.png and fig2-4-4.png for Chapter 12 vector field examples.

例2: F(x,y) = x î
例4: F(x,y) = y î + x ĵ

Style matches fig2-4-1.png and fig2-4-2.png.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../media/img")

# ── shared style parameters (reverse-engineered from existing figs) ──────────
GRID_N     = 11          # number of grid points per axis
X_RANGE    = (-2.5, 2.5)
Y_RANGE    = (-2.5, 2.5)
FIG_SIZE   = (4.5, 4.5)  # inches – matches ~480×480 px @ ~107 dpi
ARROW_COLOR = "#3A6EA5"  # dark steel-blue matching existing figs
ARROW_SCALE = 0.38 * 2.5  # fraction of grid spacing for normalised arrows
AXIS_COLOR  = "black"
AXIS_LW     = 1.2
GRID_COLOR  = "#cccccc"
GRID_LS     = "--"
TITLE_FS    = 11
TITLE_FONT  = "DejaVu Sans"


def make_grid():
    x = np.linspace(X_RANGE[0], X_RANGE[1], GRID_N)
    y = np.linspace(Y_RANGE[0], Y_RANGE[1], GRID_N)
    return np.meshgrid(x, y)


def plot_vector_field(ax, X, Y, U, V, title_latex):
    """Draw normalised vector field on ax, matching existing figure style."""
    # normalise each arrow to equal length (but show zero vectors as nothing)
    mag = np.sqrt(U**2 + V**2)
    mag_safe = np.where(mag == 0, np.nan, mag)
    dx = X_RANGE[1] - X_RANGE[0]
    step = dx / (GRID_N - 1)
    length = step * ARROW_SCALE

    Un = U / mag_safe * length
    Vn = V / mag_safe * length

    # offset tail so arrow is centred on grid point
    Xs = X - Un / 2
    Ys = Y - Vn / 2

    ax.quiver(
        Xs, Ys, Un, Vn,
        color=ARROW_COLOR,
        angles="xy", scale_units="xy", scale=1,
        width=0.002,
        headwidth=4, headlength=4, headaxislength=3.5,
        linewidth=0.5,
        pivot="tail",
        zorder=3,
    )

    # Extend the displayed range slightly so the y arrow/label are inside axes
    XPAD = 0.35   # room for x arrow + label on the right
    YPAD = 0.38   # room for y arrow + label on the top
    ax.set_xlim(X_RANGE[0], X_RANGE[1] + XPAD)
    ax.set_ylim(Y_RANGE[0], Y_RANGE[1] + YPAD)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # dashed plot border (at the actual data range)
    border_x = [X_RANGE[0], X_RANGE[1], X_RANGE[1], X_RANGE[0], X_RANGE[0]]
    border_y = [Y_RANGE[0], Y_RANGE[0], Y_RANGE[1], Y_RANGE[1], Y_RANGE[0]]
    ax.plot(border_x, border_y, color=GRID_COLOR, linestyle=GRID_LS, lw=0.8, zorder=1)

    # axes lines (extend beyond border to arrow tips)
    ax.plot([X_RANGE[0], X_RANGE[1] + XPAD - 0.05], [0, 0],
            color=AXIS_COLOR, lw=AXIS_LW, zorder=2)
    ax.plot([0, 0], [Y_RANGE[0], Y_RANGE[1] + YPAD - 0.05],
            color=AXIS_COLOR, lw=AXIS_LW, zorder=2)

    # axis arrow tips
    arrowprops = dict(arrowstyle="-|>", color=AXIS_COLOR,
                      lw=AXIS_LW, mutation_scale=10)
    ax.annotate("", xy=(X_RANGE[1] + XPAD, 0),
                xytext=(X_RANGE[1] + XPAD - 0.12, 0),
                arrowprops=arrowprops, zorder=4)
    ax.annotate("", xy=(0, Y_RANGE[1] + YPAD),
                xytext=(0, Y_RANGE[1] + YPAD - 0.12),
                arrowprops=arrowprops, zorder=4)

    # axis labels – both kept inside the axes limits to avoid overlap with title
    ax.text(X_RANGE[1] + XPAD + 0.04, -0.12, "x",
            fontsize=10, ha="left", va="center")
    ax.text(0.15, Y_RANGE[1] + YPAD - 0.15, "y",
            fontsize=10, ha="left", va="center")

    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    # title
    ax.set_title(f"$\\vec{{F}}(x, y) = {title_latex}$",
                 fontsize=TITLE_FS, fontname=TITLE_FONT, pad=8)


def save_fig(filename, title_latex, U_func, V_func):
    X, Y = make_grid()
    U = U_func(X, Y)
    V = V_func(X, Y)

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    # leave room above axes for y-axis arrow + label
    fig.subplots_adjust(top=0.82, bottom=0.04, left=0.04, right=0.96)

    plot_vector_field(ax, X, Y, U, V, title_latex)

    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=107, bbox_inches="tight", pad_inches=0.05,
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"Saved: {out_path}")


# ── 例2: F(x,y) = x î ────────────────────────────────────────────────────────
save_fig(
    "fig2-4-3.png",
    r"x\hat{i}",
    lambda x, y: x.copy(),
    lambda x, y: np.zeros_like(x),
)

# ── 例4: F(x,y) = y î + x ĵ ─────────────────────────────────────────────────
save_fig(
    "fig2-4-4.png",
    r"y\hat{i} + x\hat{j}",
    lambda x, y: y.copy(),
    lambda x, y: x.copy(),
)
