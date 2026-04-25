# Per-Callout Video Buttons Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let authors opt a specific callout (any type) into a `▶ 观看视频` button that lives on the right end of the banner and opens a video panel inside the callout body.

**Architecture:** Extend the existing `[!type: title]` markdown syntax with `| video: URL`. The Pandoc Lua filter parses that suffix and emits a `<button class="callout-video-btn" data-video-url="…">` inside the existing `.callout-header`. Front-end JS replaces its current auto-inject-on-every-tip logic with a delegated click handler on those buttons.

**Tech Stack:** Pandoc + Lua filter, vanilla JS, vanilla CSS, Python builder.

**Spec:** `specs/2026-04-24-callout-video-button-design.md`.

**Repo context:**
- Source of truth lives in `NewMathAnalysis/build/assets/` and gets rsynced to `NewMathAnalysis/docs/assets/` on build.
- `NewMathAnalysis/` is a git repo. The sibling `hydrays.github.io/` is a separate repo that gets the built `docs/` rsynced into it on publish.
- Commits in this plan refer to the `NewMathAnalysis/` repo unless stated otherwise. **Do not run `bash build/publish.sh` until Task 5** — that commits to a public-facing repo.

---

### Task 1: Parse `| video: URL` in the callout filter

**Files:**
- Modify: `NewMathAnalysis/build/filters.lua:14-72`
- Create fixture: `NewMathAnalysis/build/test_fixtures/callout_video.md`

**Context:** Today the filter handles two forms:

```lua
-- Pattern 1: [!type: custom title]
local ctype, custom_title = first_text:match("^%[!(%a+):%s*(.-)%s*%]%s*$")

-- Pattern 2: [!type] alone or [!type] inline-text
if not ctype then
  local marker = first.content[1]
  if marker.t ~= "Str" then return nil end
  ctype = marker.text:match("^%[!(%a+)%]$")
  if not ctype then return nil end
end
```

We extend **only Pattern 1**. Pattern 2 (inline-text form) does not accept video — explicitly out of scope per spec.

- [ ] **Step 1: Create a fixture that exercises the new syntax**

Write this file so later tasks and you have something to rebuild-and-grep against. Include: with-video, without-video, titleless-with-video, and a legacy no-video callout of each type.

Create `NewMathAnalysis/build/test_fixtures/callout_video.md`:

```markdown
---
title: Callout video fixture
---

# Fixture

> [!tip: Fourier 收敛性 | video: https://example.com/a.html?x=1]
> with video, tip.

> [!note: 仅标题]
> no video, note.

> [!important: | video: https://example.com/b.html]
> titleless with video, important.

> [!warning: 注意事项]
> no video, warning.

> [!caution: 小心 | video: https://example.com/c.html]
> with video, caution.

> [!extension: 拓展 | video: https://example.com/d.html]
> with video, extension.

> [!tip]
> legacy inline form, must still render.
```

- [ ] **Step 2: Modify filters.lua to extract the video URL**

Edit `NewMathAnalysis/build/filters.lua`. Replace the current lines 20-33 (the block that sets `ctype`, `custom_title`, and `label`) with:

```lua
  -- Pattern 1: [!type: custom title] — type sets color/icon, only title shown
  local ctype, custom_title = first_text:match("^%[!(%a+):%s*(.-)%s*%]%s*$")

  -- Pattern 2: [!type] alone or [!type] inline-text (legacy, no video)
  if not ctype then
    local marker = first.content[1]
    if marker.t ~= "Str" then return nil end
    ctype = marker.text:match("^%[!(%a+)%]$")
    if not ctype then return nil end
  end

  ctype = ctype:lower()
  local label = CALLOUT_LABELS[ctype] or (ctype:sub(1,1):upper() .. ctype:sub(2))

  -- Optional " | video: URL" suffix on the title of Pattern 1 callouts.
  local video_url = nil
  if custom_title then
    local title_part, url_part = custom_title:match("^(.-)%s*|%s*video:%s*(.-)%s*$")
    if url_part and url_part ~= "" then
      custom_title = title_part  -- may be empty string
      video_url = url_part
    end
  end
```

Now change the header-emitting block (the `string.format` call at current lines 63-67) so it appends the button when `video_url` is set. Replace lines 63-67 with:

```lua
  local button_html = ""
  if video_url then
    local escaped = video_url:gsub("&", "&amp;"):gsub('"', "&quot;")
    button_html =
      '<button class="callout-video-btn" type="button" data-video-url="'
      .. escaped .. '">&#9654; 观看视频</button>'
  end

  local header_html = string.format(
    '<div class="callout-header callout-header-%s">'
    .. '<span class="callout-icon"></span>'
    .. '<span class="callout-label">%s</span>%s</div>',
    ctype, label_text, button_html)
```

Handle the empty-title case — with `[!tip: | video: URL]` we now have `custom_title = ""`. The existing code below (current lines 38-61, handling `label_text`) treats `custom_title` as truthy on empty string only because Lua does; but we want an empty title to fall back to the default label (e.g. `提示`). Replace the existing `if custom_title then … elseif … else … end` block with:

```lua
  local label_text
  if custom_title and custom_title ~= "" then
    label_text = custom_title
  elseif (not custom_title) and #first.content > 1 then
    -- Legacy [!type] + inline-text form
    local i = 2
    if first.content[i] and
       (first.content[i].t == "SoftBreak" or first.content[i].t == "Space") then
      i = i + 1
    end
    local title_inlines = {}
    while i <= #first.content do
      table.insert(title_inlines, first.content[i])
      i = i + 1
    end
    if #title_inlines > 0 then
      label_text = label .. ": " .. pandoc.utils.stringify(pandoc.Span(title_inlines))
    else
      label_text = label
    end
  else
    label_text = label
  end
```

- [ ] **Step 3: Build the fixture and grep the output**

Run from `NewMathAnalysis/`:

```bash
pandoc build/test_fixtures/callout_video.md \
  --lua-filter build/filters.lua \
  --from markdown-mark+raw_html+smart+tex_math_dollars \
  --to html \
  -o /tmp/callout_video.html
```

Then verify:

```bash
grep -c 'class="callout-video-btn"' /tmp/callout_video.html
# Expected: 4  (tip, important, caution, extension)

grep -c 'data-video-url="https://example.com/a.html?x=1"' /tmp/callout_video.html
# Expected: 1

grep -c 'class="callout-label">提示</span><button' /tmp/callout_video.html
# Expected: 1 — titleless important? No — the titleless entry in fixture is "important",
# so check:

grep -c 'class="callout-label">重要</span><button class="callout-video-btn"' /tmp/callout_video.html
# Expected: 1

# Legacy [!tip] form must still produce a callout without a button:
grep -c 'class="callout callout-tip"' /tmp/callout_video.html
# Expected: 2  (Pattern 1 with-video + legacy inline)

grep 'callout-tip".*legacy inline form' /tmp/callout_video.html
# Expected: a line showing the legacy callout rendered (no button in its header)
```

If any expectation fails: re-read the replaced blocks and reconcile. Do **not** move on with a failing parser.

- [ ] **Step 4: Commit**

```bash
cd NewMathAnalysis
git add build/filters.lua build/test_fixtures/callout_video.md
git commit -m "feat(filter): parse '| video: URL' suffix on callouts"
```

---

### Task 2: Style the in-banner video button

**Files:**
- Modify: `NewMathAnalysis/build/assets/app.css:453-470` (remove `.video-inline-btn`)
- Modify: `NewMathAnalysis/build/assets/app.css:289-298` (confirm `.callout-header` is flex — it already is; no edit needed)
- Add new rule near the callout CSS (after line ~340)

- [ ] **Step 1: Remove obsolete .video-inline-btn rule**

Delete these lines from `NewMathAnalysis/build/assets/app.css` (currently lines 453-470, the two blocks `.video-inline-btn { … }` and `.video-inline-btn:hover { … }`). Leave everything else in that region intact.

- [ ] **Step 2: Add the new .callout-video-btn rule**

Insert this block in `NewMathAnalysis/build/assets/app.css` immediately after the last `.callout-extension` rule (currently line 339):

```css
/* Video button on the right end of the callout banner. The button
   inherits the header's text color per type; transparent background
   keeps the banner tint visible. */
.callout-video-btn {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  padding: 2px 10px;
  background: transparent;
  border: 1px solid currentColor;
  border-radius: 4px;
  color: inherit;
  font: inherit;
  font-size: 0.82em;
  letter-spacing: 0;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.callout-video-btn:hover,
.callout-video-btn:focus-visible {
  background: currentColor;
  color: #fff;
  outline: none;
}
/* When the button is the one that currently owns the open panel,
   show it filled so the state is obvious. */
.callout-video-btn.is-active {
  background: currentColor;
  color: #fff;
}
```

Note: `.callout-header` already has `display: flex; align-items: center; gap: 8px` (see current lines 289-298), so `margin-left: auto` pushes the button to the right end. No header edit needed.

- [ ] **Step 3: Rebuild and visual-sanity-check the asset copy**

Run from `NewMathAnalysis/`:

```bash
python3 build/build.py
grep -c 'callout-video-btn' docs/assets/app.css
# Expected: >= 3  (main rule + :hover + .is-active)

grep -c 'video-inline-btn' docs/assets/app.css
# Expected: 0
```

- [ ] **Step 4: Commit**

```bash
cd NewMathAnalysis
git add build/assets/app.css docs/assets/app.css
git commit -m "style(callout): move video button into banner, drop inline style"
```

(If `docs/assets/app.css` is gitignored in this repo, only the build/assets file will stage — that's fine. Check with `git status` first.)

---

### Task 3: Rewrite initVideo() to use the new buttons

**Files:**
- Modify: `NewMathAnalysis/build/assets/app.js:332-377` (the whole `// ── Video panel ──` section including `initVideo`)

**Context:** Current `initVideo()` (lines 334-377):
- Reads `window.videoUrl` and bails if empty.
- Pre-sets `frame.src` to that URL.
- Queries `.callout.callout-tip` and appends a `.video-inline-btn` trigger after each.

We're removing both the chapter-level URL usage *and* the auto-append. Buttons are now in the header, each carries its own URL, and the panel moves inside the callout body.

- [ ] **Step 1: Replace the whole video-panel section**

In `NewMathAnalysis/build/assets/app.js`, replace the block from the comment `// ── Video panel ──` through the end of `initVideo()` (currently lines 332-377) with:

```javascript
  // ── Video panel ──────────────────────────────────────────────

  // activeOwner persists across SPA navigations; we clear it on navigate.
  var activeVideoOwner = null;

  function closeVideoPanel() {
    var panel = document.getElementById("video-panel");
    if (panel) panel.style.display = "none";
    if (activeVideoOwner) activeVideoOwner.classList.remove("is-active");
    activeVideoOwner = null;
  }

  function openVideoPanelFor(btn) {
    var panel = document.getElementById("video-panel");
    var frame = document.getElementById("video-frame");
    var mainEl = document.getElementById("main");
    if (!panel || !frame) return;

    var url = btn.getAttribute("data-video-url") || "";
    if (!url) return;

    var callout = btn.closest(".callout");
    var body = callout ? callout.querySelector(".callout-body") : null;
    if (!body) return;

    // Move the singleton panel into this callout's body.
    body.appendChild(panel);
    frame.src = url;
    panel.style.display = "block";
    frame.style.height = Math.round(panel.offsetWidth * 9 / 16) + "px";

    if (activeVideoOwner && activeVideoOwner !== btn) {
      activeVideoOwner.classList.remove("is-active");
    }
    activeVideoOwner = btn;
    btn.classList.add("is-active");

    if (mainEl) {
      var top = panel.getBoundingClientRect().top + mainEl.scrollTop - 56;
      mainEl.scrollTo({ top: top, behavior: "smooth" });
    }
  }

  function initVideo() {
    // Hide the panel on page load / after SPA swap; owner from the previous
    // page is gone now.
    var panel = document.getElementById("video-panel");
    var frame = document.getElementById("video-frame");
    if (panel) panel.style.display = "none";
    if (frame) frame.src = "";
    activeVideoOwner = null;

    var closeBtn = document.getElementById("video-close-btn");
    if (closeBtn) closeBtn.onclick = closeVideoPanel;
    var closeBottom = document.getElementById("video-close-bottom");
    if (closeBottom) closeBottom.onclick = closeVideoPanel;
  }

  // Delegated handler — works for buttons present on initial load
  // AND buttons rendered into #content after SPA navigation.
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".callout-video-btn");
    if (!btn) return;
    e.preventDefault();
    if (activeVideoOwner === btn) {
      closeVideoPanel();
    } else {
      openVideoPanelFor(btn);
    }
  });
```

- [ ] **Step 2: Rebuild and sanity-check**

Run from `NewMathAnalysis/`:

```bash
python3 build/build.py
grep -c 'callout-video-btn' docs/assets/app.js
# Expected: >= 3 (class selector used a few times)

grep -c 'video-inline-btn' docs/assets/app.js
# Expected: 0

grep -c 'window.videoUrl' docs/assets/app.js
# Expected: 0 — we stopped consuming it
```

- [ ] **Step 3: Manual smoke test in the browser**

```bash
cd NewMathAnalysis/docs && python3 -m http.server 8080 --bind 100.74.177.128
```

Open `http://100.74.177.128:8080/` and navigate to chapter 1. For now there are no `| video:` annotations in any chapter yet, so:
- Open DevTools → Elements.
- Confirm: no `.video-inline-btn` on any callout.
- Confirm: no `.callout-video-btn` on any callout (expected — nobody has opted in).
- Confirm: no console errors from the new handler.

Leave the server running; Task 5 will add a real authoring sample.

- [ ] **Step 4: Commit**

```bash
cd NewMathAnalysis
git add build/assets/app.js docs/assets/app.js
git commit -m "refactor(video): delegate to .callout-video-btn, open inside body"
```

---

### Task 4: Remove the chapter-level video_url plumbing

**Files:**
- Modify: `NewMathAnalysis/src/chpt1.yaml` (delete the `video_url` key, or the whole file if it becomes empty)
- Modify: `NewMathAnalysis/build/build.py:278` and `NewMathAnalysis/build/build.py:311`
- Modify: `NewMathAnalysis/build/template.html:54`

**Context:** These three places made up the old "one URL per chapter, injected as `window.videoUrl`" path. All three go.

- [ ] **Step 1: Drop video_url from chpt1.yaml**

Inspect `NewMathAnalysis/src/chpt1.yaml`. Its current content is exactly:

```yaml
video_url: "https://player.bilibili.com/player.html?bvid=BV1jEDcBoE8F&autoplay=0"
```

Since this is the only key, delete the entire file:

```bash
rm NewMathAnalysis/src/chpt1.yaml
```

If you later find other `chptN.yaml` files that contain `video_url` plus other keys, remove only the `video_url` key from those files.

```bash
grep -l "^video_url" NewMathAnalysis/src/*.yaml
# Expected (after the rm above): empty
```

- [ ] **Step 2: Remove video_url read & pandoc variable in build.py**

Edit `NewMathAnalysis/build/build.py`.

Delete line 278:

```python
    video_url = str(meta.get("video_url", "")).strip()
```

Delete line 311 (the `--variable` entry):

```python
            "--variable", f"video_url={video_url}",
```

Be careful to preserve the surrounding list commas and indentation. After the edit, that block should read (keeping its neighbours intact):

```python
            "--variable", f"doc_lib_json={json.dumps(doc_lib)}",
            "--variable", f"chp_autonum={chp_autonum}",
            "--highlight-style", "pygments",
```

- [ ] **Step 3: Remove window.videoUrl from template.html**

Edit `NewMathAnalysis/build/template.html`. Delete line 54:

```html
    window.videoUrl = "$if(video_url)$$video_url$$endif$";
```

Leave the surrounding `<script>` block intact.

- [ ] **Step 4: Rebuild and sanity-check**

Run from `NewMathAnalysis/`:

```bash
python3 build/build.py
grep -c 'window.videoUrl' docs/chapter1.html
# Expected: 0
grep -rn 'video_url' build/ src/
# Expected: no matches
```

- [ ] **Step 5: Commit**

```bash
cd NewMathAnalysis
git add -A  # captures the rm of src/chpt1.yaml plus edits
git commit -m "chore: drop chapter-level video_url plumbing"
```

---

### Task 5: End-to-end verification with a real annotation

**Files:**
- Modify: `NewMathAnalysis/src/chpt1.md` (add `| video: URL` to one real callout for testing)

- [ ] **Step 1: Pick a callout to annotate**

Open `NewMathAnalysis/src/chpt1.md` and find the first `[!tip:` callout (or any callout type). Change its header line from:

```markdown
> [!tip: 某个标题]
```

to:

```markdown
> [!tip: 某个标题 | video: https://player.bilibili.com/player.html?bvid=BV1jEDcBoE8F&autoplay=0]
```

(Use the bilibili URL that was previously the chapter default. Pick whichever callout makes sense pedagogically — there is no "right answer" at the code level.)

- [ ] **Step 2: Rebuild and grep**

Run from `NewMathAnalysis/`:

```bash
python3 build/build.py
grep -c 'callout-video-btn' docs/chapter1.html
# Expected: 1

grep 'callout-video-btn' docs/chapter1.html
# Eyeball: button should appear inside a .callout-header div, not after the callout.
```

- [ ] **Step 3: Full spec test-plan run in a browser**

Serve and open chapter 1:

```bash
cd NewMathAnalysis/docs && python3 -m http.server 8080 --bind 100.74.177.128
```

Walk through the spec's test plan on `http://100.74.177.128:8080/chapter1.html`:

- [ ] Annotated callout shows a button at the right end of the banner.
- [ ] Other callouts show no button.
- [ ] Clicking the button opens the video panel **inside** the callout body.
- [ ] Clicking the same button again closes the panel.
- [ ] × and `▲ 收起视频` close the panel.
- [ ] No console errors.
- [ ] Navigate to another chapter via sidebar, then back: button still works.

To also prove it works for other types, temporarily annotate a `[!note:` or `[!warning:` callout somewhere in the same chapter, rebuild, reload. Revert before committing if you don't want that annotation to stay.

- [ ] **Step 4: Commit the sample annotation**

```bash
cd NewMathAnalysis
git add src/chpt1.md
git commit -m "docs(chpt1): attach bilibili video to one tip callout"
```

- [ ] **Step 5: Publish**

Only after the browser smoke test passes:

```bash
bash build/publish.sh "feat: per-callout video buttons"
```

This rsyncs `docs/` into `hydrays.github.io/` and pushes that repo to GitHub Pages. Verify after the push:

```bash
cd /home/hydra/Code/books/hydrays.github.io && git log --oneline -3
```

You should see the new commit at the top, and `https://hydrays.github.io/chapter1.html` should pick up the change after GitHub Pages rebuilds.

---

## Self-review notes

- Spec coverage: syntax (Task 1), button in header right (Tasks 1+2), works for all types (fixture in Task 1 covers all six), panel inside body (Task 3), toggle (Task 3), cleanup (Task 4), manual test plan (Task 5). All spec sections mapped.
- Naming: `callout-video-btn`, `data-video-url`, `activeVideoOwner` used consistently across tasks.
- One known disposable artifact: the previously committed `lu153174b0d1rg.tmp` in `hydrays.github.io`. Not in this plan's scope; leave a note for a follow-up cleanup if you want.
