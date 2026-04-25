# Per-Callout Video Buttons — Design

Date: 2026-04-24
Scope: `NewMathAnalysis/build/` and `NewMathAnalysis/src/`

## Problem

`initVideo()` currently auto-appends a `▶ 观看视频` trigger after every
`.callout.callout-tip`, pointing at the chapter-level `video_url` in
`src/chptN.yaml`. Two issues:

1. The author can't choose which callouts get a video button — every tip gets one.
2. Only tips are eligible. Notes, warnings, etc. cannot carry videos.
3. There is only one URL per chapter. Different callouts cannot point at different videos.

## Goal

Let the author opt in per callout, on any callout type, and give each
annotated callout its own video URL. The button lives at the right end
of the callout header (banner). The video panel opens *inside* the
callout body.

## Markdown syntax

Extend the existing `[!type: title]` header line with an optional
`| video: URL` segment:

```markdown
> [!tip: Fourier 收敛性 | video: https://player.bilibili.com/player.html?bvid=BV1jE...]
> 如果 $f$ 是...
```

- Works for all callout types: `note`, `tip`, `important`, `warning`, `caution`, `extension`.
- Title is optional but a colon is required when adding video. Titleless form: `> [!tip: | video: URL]` (empty title between `:` and `|`).
- Omitting ` | video:` → no button (opt-in).
- Title text may not contain the literal ` | video:` substring (documented limitation).
- The legacy inline-text form (`> [!tip] 文字`) is unchanged and does **not** accept videos. Authors who want a video on such a callout convert it to the `[!type: ...]` form.

## Parser change — `build/filters.lua`

In the `BlockQuote` handler, after extracting `ctype` and `custom_title`:

1. If `custom_title` contains ` | video: `, split on the first occurrence.
   - Left side becomes the new `custom_title` (trimmed; may be empty).
   - Right side is the video URL (trimmed).
2. If the resulting title is empty, emit the callout with the default type label (e.g. 提示 for `tip`) and the video button.
3. Thread the URL into the emitted header HTML as a trailing `<button>`.

Emitted HTML when a video is present:

```html
<div class="callout-header callout-header-tip">
  <span class="callout-icon"></span>
  <span class="callout-label">Fourier 收敛性</span>
  <button class="callout-video-btn" type="button"
          data-video-url="https://player.bilibili.com/player.html?bvid=...">
    ▶ 观看视频
  </button>
</div>
```

When no video: header is unchanged from today (no button element emitted).

## CSS change — `build/assets/app.css`

Add `.callout-video-btn` styles:

- `margin-left: auto` to push to the right end of the header flex row.
- Small padding, rounded corners, transparent background, inherits header text color.
- Hover/focus states; `cursor: pointer`.
- Font size ~0.9em, kept compact so the header height doesn't change.

Confirm `.callout-header` is already `display: flex; align-items: center`. If not, set it. Header color tinting per type continues to come from the existing `callout-header-<type>` class.

## JS change — `build/assets/app.js`

Rewrite `initVideo()`:

- **Remove**: the `document.querySelectorAll(".callout.callout-tip")` loop that appends a trigger after each tip.
- **Add**: a delegated click listener on `document` that matches `.callout-video-btn`.
- On click:
  1. Find the enclosing `.callout` of the clicked button.
  2. Find its `.callout-body` child.
  3. Let `url = button.dataset.videoUrl`.
  4. If `activeOwner === button`, hide `#video-panel`, clear `activeOwner`, return (toggle close).
  5. Otherwise: move `#video-panel` to be the last child of `.callout-body`, set the iframe `src` to `url`, show the panel, set `activeOwner = button`.
- Keep: `× close` and `▲ 收起视频` behaviour (both hide the panel and clear `activeOwner`).
- Keep: `frame.style.height = panel.offsetWidth * 9/16 + "px"` — this still works; the panel is now narrower (inside the body's padding), so `offsetWidth` will be smaller and height scales with it.
- Call `initVideo()` once on initial load and once after each SPA content swap (as today).

## Cleanup

- `src/chpt1.yaml` currently holds `video_url: "..."`. After the UI change, delete that key. If the file becomes empty, delete the file.
- Remove any code in `build/build.py` and `build/template.html` that reads `video_url` / injects a default video URL into the page. (Only if it exists — verify during implementation.)
- The `#video-panel` element itself stays in the template; it is still the single moved panel.

## Migration

One chapter (`chpt1`) currently has a chapter-level URL. After this change it has **zero** video buttons until the author adds `| video: URL` to specific callouts. That is intentional.

## Out of scope

- Multiple videos per callout.
- Per-callout thumbnails or playback state.
- Analytics.
- Title text containing ` | video:`.

## Test plan

Manual, after rebuild + serve:

- [ ] Callout with `| video: URL` renders a button on the right end of the banner.
- [ ] Callout without it renders no button.
- [ ] Works on `note`, `tip`, `important`, `warning`, `caution`, `extension`.
- [ ] Clicking the button opens `#video-panel` inside the callout body with the right URL.
- [ ] Clicking the same button again closes the panel.
- [ ] Clicking a *different* button moves the panel to that callout.
- [ ] × and ▲ 收起视频 both close the panel.
- [ ] SPA nav between chapters: buttons on the new page still work.
- [ ] Iframe height is ~9/16 of the panel width; no overflow.
- [ ] Titleless form `> [!tip: | video: URL]` works and shows the default label (提示 etc.).
- [ ] Title with `|` characters but not ` | video:` still parses correctly.
