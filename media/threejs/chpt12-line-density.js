/**
 * chpt12-line-density.js
 * §12.2 motivation: mass of a non-uniform thin wire as a Riemann sum
 * over arc length.
 *
 * Curve L (one wave of a sinusoid):
 *   r(t) = (t, 0.7 sin t),  t ∈ [0, 2π]
 * Linear density along L:
 *   ρ(x, y) = 0.25 + 0.95 · exp(-0.6 ((x - π)² + (y - 0.5)²))
 * — Gaussian peak near the wave crest at (π, 0); low elsewhere.
 *
 * Top-down orthographic view. The curve is rendered as a thick coloured
 * ribbon (TubeGeometry, flattened); colour samples ρ at each axial vertex.
 * An N-segment partition overlays the curve as black dots at midpoints
 * (one per segment). A slider drives N (4 → 64). The HTML readout shows
 * the running Riemann sum ∑ ρ Δs and the precomputed reference mass.
 *
 * Math (x, y) → Three.js (x, 0, -y), matching chpt11 conventions.
 */

import * as THREE from 'three';

// ── Curve & density ────────────────────────────────────────────────────────

const T0 = 0, T1 = 2 * Math.PI;

function curve(t) {
  return { x: t, y: 0.7 * Math.sin(t) };
}
// dr/dt
function curveD(t) {
  return { x: 1, y: 0.7 * Math.cos(t) };
}
function rho(x, y) {
  const dx = x - Math.PI, dy = y - 0.5;
  return 0.25 + 0.95 * Math.exp(-0.6 * (dx * dx + dy * dy));
}

// Reference mass M = ∫ ρ(r(t)) |r'(t)| dt, Simpson at high res.
const TRUE_MASS = (() => {
  const M = 4000;
  const dt = (T1 - T0) / M;
  let s = 0;
  for (let i = 0; i <= M; i++) {
    const t = T0 + i * dt;
    const p = curve(t);
    const d = curveD(t);
    const ds = Math.sqrt(d.x * d.x + d.y * d.y);
    const w = (i === 0 || i === M) ? 1 : (i % 2 === 1 ? 4 : 2);
    s += w * rho(p.x, p.y) * ds;
  }
  return s * dt / 3;
})();

// ── Container ──────────────────────────────────────────────────────────────

const container = document.getElementById('chpt12-line-density');
container.style.position = 'relative';

// ── Renderer + camera ──────────────────────────────────────────────────────

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setClearColor(0xfafafa, 1);
renderer.domElement.style.cssText =
  'position:absolute;top:0;left:0;display:block;';
container.appendChild(renderer.domElement);

const X0 = -0.4, X1 = 2 * Math.PI + 0.4, Y0 = -1.0, Y1 = 1.0;
const W = X1 - X0, H = Y1 - Y0;
const PAD = 0.05;

const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.01, 100);
camera.position.set((X0 + X1) / 2, 10, -(Y0 + Y1) / 2);
camera.lookAt(new THREE.Vector3((X0 + X1) / 2, 0, -(Y0 + Y1) / 2));
camera.up.set(0, 0, -1);

function fitCamera() {
  const rect = container.getBoundingClientRect();
  const overlayH = (typeof overlay !== "undefined" && overlay) ? overlay.offsetHeight : 0;
  const canvasH = Math.max(1, rect.height - overlayH);
  const aspect = rect.width / canvasH;
  const dataAspect = W / H;
  let halfW, halfH;
  if (aspect >= dataAspect) {
    halfH = (H / 2) + PAD;
    halfW = halfH * aspect;
  } else {
    halfW = (W / 2) + PAD;
    halfH = halfW / aspect;
  }
  camera.left   = -halfW + (X0 + X1) / 2;
  camera.right  =  halfW + (X0 + X1) / 2;
  camera.top    =  halfH;
  camera.bottom = -halfH;
  camera.updateProjectionMatrix();
  // updateStyle=true shrinks the canvas DOM itself so the overlay sits
  // below the canvas rather than on top of it.
  renderer.setSize(rect.width, canvasH, true);
}

const scene = new THREE.Scene();

// ── Colormap (must be declared before the ribbon block uses it) ────────────
// Viridis-inspired four-stop ramp: perceptually uniform and clean.
const RAMP_STOPS = [
  { r: 0.267, g: 0.005, b: 0.329 },   // 0.00  deep purple
  { r: 0.231, g: 0.318, b: 0.545 },   // 0.33  blue
  { r: 0.129, g: 0.565, b: 0.553 },   // 0.66  teal
  { r: 0.992, g: 0.906, b: 0.144 },   // 1.00  yellow
];
function ramp(t) {
  t = Math.max(0, Math.min(1, t));
  // Mild gamma so the high-density region pops against the low-ρ bulk.
  t = Math.pow(t, 0.85);
  const n = RAMP_STOPS.length - 1;
  const idx = Math.min(n - 1, Math.floor(t * n));
  const u = t * n - idx;
  const a = RAMP_STOPS[idx], b = RAMP_STOPS[idx + 1];
  return { r: a.r + (b.r - a.r) * u, g: a.g + (b.g - a.g) * u, b: a.b + (b.b - a.b) * u };
}

// ── Density-coloured ribbon along L ────────────────────────────────────────
// Implemented as a flat strip: at each sample t_k, place two vertices at
// r(t_k) ± half-width · n̂(t_k) where n̂ is the unit normal in-plane.

const RIBBON_RES = 800;
const RIBBON_HALF = 0.028;  // half-width of the ribbon, in math units

{
  const positions = new Float32Array((RIBBON_RES + 1) * 2 * 3);
  const colors    = new Float32Array((RIBBON_RES + 1) * 2 * 3);
  const indices   = new Uint32Array(RIBBON_RES * 2 * 3);

  // Pass 1: find ρ range to normalise.
  let lo = +Infinity, hi = -Infinity;
  for (let i = 0; i <= RIBBON_RES; i++) {
    const t = T0 + (T1 - T0) * (i / RIBBON_RES);
    const p = curve(t);
    const r = rho(p.x, p.y);
    if (r < lo) lo = r;
    if (r > hi) hi = r;
  }

  // Pass 2: build geometry.
  for (let i = 0; i <= RIBBON_RES; i++) {
    const t = T0 + (T1 - T0) * (i / RIBBON_RES);
    const p = curve(t);
    const d = curveD(t);
    const len = Math.hypot(d.x, d.y) || 1e-9;
    const tx = d.x / len, ty = d.y / len;
    // 2D normal: rotate tangent 90°
    const nx = -ty, ny = tx;
    const ax = p.x + RIBBON_HALF * nx, ay = p.y + RIBBON_HALF * ny;
    const bx = p.x - RIBBON_HALF * nx, by = p.y - RIBBON_HALF * ny;

    // Math (x,y) → Three.js (x, 0.001, -y)
    const base = i * 2 * 3;
    positions[base + 0] = ax; positions[base + 1] = 0.001; positions[base + 2] = -ay;
    positions[base + 3] = bx; positions[base + 4] = 0.001; positions[base + 5] = -by;

    const tNorm = (rho(p.x, p.y) - lo) / Math.max(1e-9, hi - lo);
    const c = ramp(tNorm);
    colors[base + 0] = c.r; colors[base + 1] = c.g; colors[base + 2] = c.b;
    colors[base + 3] = c.r; colors[base + 4] = c.g; colors[base + 5] = c.b;
  }
  for (let i = 0; i < RIBBON_RES; i++) {
    const a = i * 2, b = i * 2 + 1, c = (i + 1) * 2, d = (i + 1) * 2 + 1;
    const base = i * 6;
    indices[base + 0] = a; indices[base + 1] = b; indices[base + 2] = c;
    indices[base + 3] = b; indices[base + 4] = d; indices[base + 5] = c;
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geo.setAttribute('color',    new THREE.BufferAttribute(colors,    3));
  geo.setIndex(new THREE.BufferAttribute(indices, 1));
  const mat = new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.DoubleSide });
  scene.add(new THREE.Mesh(geo, mat));
}

// ── Partition: midpoint dots + tick marks (rebuilt on N change) ────────────

let dotsMesh = null;
let ticksLines = null;

// Sample points densely along L so we can do arc-length-based partitioning.
const LUT_N = 4000;
const lutT = new Float32Array(LUT_N + 1);
const lutS = new Float32Array(LUT_N + 1);
{
  let s = 0;
  let prev = curve(T0);
  lutT[0] = T0; lutS[0] = 0;
  for (let i = 1; i <= LUT_N; i++) {
    const t = T0 + (T1 - T0) * (i / LUT_N);
    const p = curve(t);
    s += Math.hypot(p.x - prev.x, p.y - prev.y);
    lutT[i] = t;
    lutS[i] = s;
    prev = p;
  }
}
const TOTAL_S = lutS[LUT_N];

// Inverse: given s ∈ [0, TOTAL_S] return t.
function tFromS(s) {
  if (s <= 0) return T0;
  if (s >= TOTAL_S) return T1;
  let lo = 0, hi = LUT_N;
  while (hi - lo > 1) {
    const mid = (lo + hi) >> 1;
    if (lutS[mid] <= s) lo = mid; else hi = mid;
  }
  const a = (s - lutS[lo]) / (lutS[hi] - lutS[lo]);
  return lutT[lo] + a * (lutT[hi] - lutT[lo]);
}

function rebuildPartition(N) {
  if (dotsMesh)   { scene.remove(dotsMesh);   dotsMesh.geometry.dispose(); }
  if (ticksLines) { scene.remove(ticksLines); ticksLines.geometry.dispose(); }

  const ds = TOTAL_S / N;

  // Tick lines at segment endpoints — short normal strokes.
  const linePts = [];
  for (let k = 0; k <= N; k++) {
    const sBoundary = k * ds;
    const t = tFromS(sBoundary);
    const p = curve(t);
    const d = curveD(t);
    const len = Math.hypot(d.x, d.y) || 1e-9;
    const nx = -d.y / len, ny = d.x / len;
    const tickHalf = 0.075;
    linePts.push(new THREE.Vector3(p.x + tickHalf * nx, 0.003, -(p.y + tickHalf * ny)));
    linePts.push(new THREE.Vector3(p.x - tickHalf * nx, 0.003, -(p.y - tickHalf * ny)));
  }
  const lg = new THREE.BufferGeometry().setFromPoints(linePts);
  const lm = new THREE.LineBasicMaterial({ color: 0x111111, transparent: true, opacity: 0.6 });
  ticksLines = new THREE.LineSegments(lg, lm);
  scene.add(ticksLines);

  // Midpoint dots — evaluation points.
  const radius = 0.045 * (24 / Math.max(24, N));
  const dotGeo = new THREE.SphereGeometry(radius, 10, 10);
  const dotMat = new THREE.MeshBasicMaterial({ color: 0x111111 });
  dotsMesh = new THREE.InstancedMesh(dotGeo, dotMat, N);
  const m = new THREE.Matrix4();
  for (let k = 0; k < N; k++) {
    const sMid = (k + 0.5) * ds;
    const t = tFromS(sMid);
    const p = curve(t);
    m.makeTranslation(p.x, 0.005, -p.y);
    dotsMesh.setMatrixAt(k, m);
  }
  scene.add(dotsMesh);
}

function riemannSum(N) {
  const ds = TOTAL_S / N;
  let s = 0;
  for (let k = 0; k < N; k++) {
    const sMid = (k + 0.5) * ds;
    const t = tFromS(sMid);
    const p = curve(t);
    s += rho(p.x, p.y) * ds;
  }
  return s;
}

// ── HTML overlay ───────────────────────────────────────────────────────────

const overlay = document.createElement('div');
overlay.style.cssText =
  'position:absolute;left:0;right:0;bottom:0;padding:10px 14px;' +
  'background:rgba(255,255,255,0.92);border-top:1px solid #e5e7eb;' +
  'font:14px/1.4 -apple-system,BlinkMacSystemFont,"Microsoft YaHei",sans-serif;' +
  'display:flex;gap:14px;align-items:center;flex-wrap:wrap;';
container.appendChild(overlay);

const sliderLabel = document.createElement('label');
sliderLabel.style.cssText = 'display:flex;align-items:center;gap:8px;';
sliderLabel.innerHTML = '<span style="white-space:nowrap">分割数 N =</span>';
const slider = document.createElement('input');
slider.type = 'range';
slider.min = '4';
slider.max = '64';
slider.step = '1';
slider.value = '8';
slider.style.cssText = 'width:160px;';
const nReadout = document.createElement('span');
nReadout.style.cssText = 'font-variant-numeric:tabular-nums;min-width:2ch;';
nReadout.textContent = slider.value;
sliderLabel.appendChild(slider);
sliderLabel.appendChild(nReadout);
overlay.appendChild(sliderLabel);

const numStat = document.createElement('span');
numStat.style.cssText = 'font-variant-numeric:tabular-nums;color:#374151;';
overlay.appendChild(numStat);

const trueStat = document.createElement('span');
trueStat.style.cssText = 'font-variant-numeric:tabular-nums;color:#15803d;';
trueStat.textContent = '真实质量 ≈ ' + TRUE_MASS.toFixed(4);
overlay.appendChild(trueStat);

function updateAll() {
  const N = parseInt(slider.value, 10);
  nReadout.textContent = String(N);
  rebuildPartition(N);
  const sum = riemannSum(N);
  const err = Math.abs(sum - TRUE_MASS);
  numStat.innerHTML =
    'Riemann 和 ≈ <strong>' + sum.toFixed(4) + '</strong>' +
    ' &nbsp; (误差 ' + err.toFixed(4) + ')';
}

slider.addEventListener('input', () => { updateAll(); });

// ── Init + render loop ─────────────────────────────────────────────────────

fitCamera();
updateAll();

let needsResize = true;
const ro = new ResizeObserver(() => { needsResize = true; });
ro.observe(container);

function frame() {
  if (needsResize) {
    fitCamera();
    needsResize = false;
  }
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
frame();
