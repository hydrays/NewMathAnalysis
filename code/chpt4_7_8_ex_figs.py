"""
chpt4_7_8_ex_figs.py — figures for chpt4 (integrals), chpt7 (ODEs), chpt8 (numerics).
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


# ─── chpt4 ─────────────────────────────────────────────────────────────────────

# ex001: Riemann sum for ∫_0^1 x dx
def fig_chpt4_ex001():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 100)
    ax.plot(x, x, color="#2563eb", lw=2.2, label=r"$y=x$")
    n = 8
    xs = np.linspace(0, 1, n + 1)
    for i in range(n):
        ax.bar(xs[i], xs[i], width=1/n, align="edge",
               color="#dc2626", alpha=0.25, edgecolor="#dc2626", linewidth=0.8)
    ax.fill_between(x, 0, x, color="#16a34a", alpha=0.25,
                    label=r"精确值 $\int_0^1 x\,dx = 1/2$")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title(r"黎曼和: $\sum f(x_i)\Delta x \to \int_0^1 x\,dx$", fontsize=10)
    _save("chpt4_ex001")


# ex002: Riemann sum for ∫_0^1 x² dx
def fig_chpt4_ex002():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 100)
    ax.plot(x, x**2, color="#2563eb", lw=2.2, label=r"$y=x^2$")
    n = 10
    xs = np.linspace(0, 1, n + 1)
    for i in range(n):
        # use right endpoint
        ax.bar(xs[i], xs[i+1]**2, width=1/n, align="edge",
               color="#dc2626", alpha=0.25, edgecolor="#dc2626", linewidth=0.8)
    ax.fill_between(x, 0, x**2, color="#16a34a", alpha=0.25,
                    label=r"精确值 $\int_0^1 x^2\,dx = 1/3$")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title(r"黎曼和 (右端点) 收敛到 $\int_0^1 x^2\,dx$", fontsize=10)
    _save("chpt4_ex002")


# ─── chpt7 ─────────────────────────────────────────────────────────────────────

# ex001: direction field for y' = y²/x²
def fig_chpt7_ex001():
    fig, ax = plt.subplots(figsize=(5.6, 4.4), dpi=150)
    x = np.linspace(0.3, 3, 18); y = np.linspace(-2, 2, 14)
    X, Y = np.meshgrid(x, y)
    with np.errstate(divide="ignore", invalid="ignore"):
        slope = Y**2 / X**2
    # normalize for unit-length arrows
    L = np.sqrt(1 + slope**2)
    U = 1 / L; V = slope / L
    ax.quiver(X, Y, U, V, color="#2563eb", scale=25, width=0.0035, alpha=0.85)
    # Sample solution curves: y = -x / (C - log x)? Actually for y'= y²/x², dy/y² = dx/x², -1/y = -1/x + C → y = x/(1-Cx)
    for C in [-1, -0.3, 0.3, 1.0]:
        xs = np.linspace(0.3, 3, 200)
        with np.errstate(divide="ignore", invalid="ignore"):
            ys = xs / (1 - C * xs)
        mask = np.abs(ys) < 5
        ax.plot(xs[mask], ys[mask], color="#dc2626", lw=1.5, alpha=0.8)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(0.3, 3); ax.set_ylim(-2, 2); ax.grid(True, alpha=0.25)
    ax.set_title(r"方程 $y' = y^2/x^2$ 的方向场与几条解曲线", fontsize=10)
    _save("chpt7_ex001")


# ex002: Newton cooling curve T(t) = T_env + (T0-T_env) e^(-kt)
def fig_chpt7_ex002():
    fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=150)
    t = np.linspace(0, 30, 240)
    T_env = 20; T0 = 90; k = 0.15
    T = T_env + (T0 - T_env) * np.exp(-k*t)
    ax.plot(t, T, color="#2563eb", lw=2.4, label=r"$T(t)=T_\infty + (T_0-T_\infty)e^{-kt}$")
    ax.axhline(T_env, color="#dc2626", lw=1.4, ls="--",
               label=r"环境温度 $T_\infty = 20\,°\!C$")
    ax.scatter([0], [T0], color="black", s=50, zorder=5)
    ax.text(0.5, T0, r"$T_0=90$", fontsize=10)
    ax.set_xlabel("时间 $t$ (分钟)"); ax.set_ylabel("$T$ (°C)")
    ax.set_xlim(0, 30); ax.set_ylim(15, 100); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("牛顿冷却定律: 指数趋向环境温度", fontsize=10)
    _save("chpt7_ex002")


# ex003: loan repayment — balance over time
def fig_chpt7_ex003():
    fig, ax = plt.subplots(figsize=(5.6, 3.8), dpi=150)
    # B' = rB - P; B(0) = B0; if r=0.05/year, B0=100k, P=8k/year → equilibrium B*=P/r=160k > B0 won't decay; so try P=10k
    r = 0.05; B0 = 100; P = 10  # k yuan/month
    # B(t) = (B0 - P/r) e^(rt) + P/r
    t = np.linspace(0, 25, 240)
    B = (B0 - P/r) * np.exp(r*t) + P/r
    ax.plot(t, B, color="#2563eb", lw=2.4, label=r"$B(t) = (B_0 - P/r) e^{rt} + P/r$")
    # zero line and zero-crossing
    zero_t = np.log(P / (P - r*B0)) / r
    ax.axhline(0, color="#dc2626", lw=1.4, ls="--", label="还清")
    ax.scatter([zero_t], [0], color="#16a34a", s=70, zorder=5,
               label=fr"$t \approx {zero_t:.1f}$ 年")
    ax.set_xlabel("时间 $t$ (年)"); ax.set_ylabel("贷款余额 $B$ (万元)")
    ax.set_xlim(0, 25); ax.set_ylim(-10, 110); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=9.5)
    ax.set_title("贷款偿还: 利息累积与还款的此消彼长", fontsize=10)
    _save("chpt7_ex003")


# ─── chpt8 ─────────────────────────────────────────────────────────────────────

# ex002: forward vs center difference for sin x at 0 — error vs h
def fig_chpt8_ex002():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    hs = np.logspace(-6, 0, 30)
    fwd = (np.sin(0 + hs) - np.sin(0)) / hs
    cen = (np.sin(0 + hs) - np.sin(0 - hs)) / (2*hs)
    err_fwd = np.abs(fwd - 1); err_cen = np.abs(cen - 1)
    ax.loglog(hs, err_fwd, color="#dc2626", marker="o", ms=4, label="前向差商: 误差 $\\propto h$")
    ax.loglog(hs, err_cen, color="#2563eb", marker="s", ms=4, label="中心差商: 误差 $\\propto h^2$")
    ax.set_xlabel(r"步长 $h$"); ax.set_ylabel("绝对误差")
    ax.grid(True, alpha=0.25, which="both")
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title(r"$f'(0) = 1$ 的差商近似 — 中心差商收敛快得多", fontsize=10)
    _save("chpt8_ex002")


# ex004: left vs right rectangles for ∫_0^1 x²
def fig_chpt8_ex004():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), dpi=150)
    x = np.linspace(0, 1, 100)
    n = 4; xs = np.linspace(0, 1, n + 1)
    for ax, mode, c, lbl in zip(axes, ["left", "right"], ["#dc2626", "#16a34a"],
                                 ["左矩形 (低估)", "右矩形 (高估)"]):
        ax.plot(x, x**2, color="#2563eb", lw=2.0)
        for i in range(n):
            h = xs[i]**2 if mode == "left" else xs[i+1]**2
            ax.bar(xs[i], h, width=1/n, align="edge", color=c, alpha=0.30,
                   edgecolor=c, linewidth=1.0)
        ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.1)
        ax.grid(True, alpha=0.25); ax.set_title(lbl, fontsize=11)
    _save("chpt8_ex004")


# ex005: trapezoidal rule for ∫_0^1 x²
def fig_chpt8_ex005():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 100)
    n = 4; xs = np.linspace(0, 1, n + 1); fs = xs**2
    ax.plot(x, x**2, color="#2563eb", lw=2.0)
    for i in range(n):
        ax.fill_between([xs[i], xs[i+1]], 0, [fs[i], fs[i+1]],
                        color="#dc2626", alpha=0.28, edgecolor="#dc2626")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.25)
    ax.set_title(r"梯形法估计 $\int_0^1 x^2\,dx \approx 0.34375$ (精确值 $1/3$)", fontsize=10)
    _save("chpt8_ex005")


# ex006: Simpson's rule
def fig_chpt8_ex006():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 100)
    n = 4; xs = np.linspace(0, 1, n + 1); fs = xs**2
    ax.plot(x, x**2, color="#2563eb", lw=2.0)
    for i in range(0, n, 2):
        xpair = np.linspace(xs[i], xs[i+2], 40)
        cf = np.polyfit([xs[i], xs[i+1], xs[i+2]],
                        [fs[i], fs[i+1], fs[i+2]], 2)
        yp = np.polyval(cf, xpair)
        ax.fill_between(xpair, 0, yp, color="#16a34a", alpha=0.30, edgecolor="#16a34a")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.25)
    ax.set_title(r"辛普森法 (二次抛物拟合) — 对 $x^2$ 精确等于 $1/3$", fontsize=10)
    _save("chpt8_ex006")


# ex007: Euler step visualization for y'=y, y(0)=1
def fig_chpt8_ex007():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    x = np.linspace(0, 1, 100)
    ax.plot(x, np.exp(x), color="#2563eb", lw=2.4, label=r"精确解 $y=e^x$")
    h = 0.2; n = int(1/h)
    xs = [0]; ys = [1]
    for _ in range(n):
        xs.append(xs[-1] + h); ys.append(ys[-1] + h*ys[-1])
    ax.plot(xs, ys, color="#dc2626", marker="o", lw=2.0,
            label=fr"Euler 步长 $h={h}$")
    for i in range(n):
        ax.plot([xs[i], xs[i+1]], [ys[i], ys[i+1]], color="#dc2626", lw=1.5, alpha=0.5)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(0.9, 3); ax.grid(True, alpha=0.25)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title(r"Euler 法解 $y'=y$, $y(0)=1$ — 折线追赶指数曲线", fontsize=10)
    _save("chpt8_ex007")


# ex008: Euler error vs step size for y'=y
def fig_chpt8_ex008():
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=150)
    hs = [0.5, 0.2, 0.1, 0.05, 0.01]
    errs = []
    for h in hs:
        n = int(1/h); y = 1
        for _ in range(n):
            y += h*y
        errs.append(abs(y - np.e))
    ax.loglog(hs, errs, color="#dc2626", marker="o", ms=8,
              label="Euler 误差 (在 $x=1$ 处)")
    ax.loglog(hs, [h*1.4 for h in hs], color="#888", lw=1.0, ls="--", label=r"$\propto h$")
    ax.set_xlabel("$h$"); ax.set_ylabel(r"$|y_{\mathrm{Euler}}(1) - e|$")
    ax.grid(True, alpha=0.25, which="both")
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("Euler 法是一阶方法 — 误差线性正比于 $h$", fontsize=10)
    _save("chpt8_ex008")


if __name__ == "__main__":
    fig_chpt4_ex001(); fig_chpt4_ex002()
    fig_chpt7_ex001(); fig_chpt7_ex002(); fig_chpt7_ex003()
    fig_chpt8_ex002(); fig_chpt8_ex004(); fig_chpt8_ex005()
    fig_chpt8_ex006(); fig_chpt8_ex007(); fig_chpt8_ex008()
