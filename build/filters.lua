-- vlook.lua — Pandoc Lua filter (compatible with Pandoc 2.x and 3.x)
-- Handles: [!TYPE] callouts, image sizing (#200w / #400h / #200pt)

local CALLOUT_LABELS = {
  note      = "注",
  tip       = "提示",
  important = "重要",
  warning   = "警告",
  caution   = "注意",
  extension = "扩展",
}

-- [!TYPE] and [!TYPE: custom title] callout blocks ─────────────────────────
function BlockQuote(el)
  if #el.content == 0 then return nil end
  local first = el.content[1]
  if first.t ~= "Para" or #first.content == 0 then return nil end

  local first_text = pandoc.utils.stringify(first)

  -- Pattern 1: [!type: custom title] — type sets color/icon, only title shown
  local ctype, custom_title = first_text:match("^%[!(%a+):%s*(.-)%s*%]%s*$")

  -- Pattern 2: [!type] alone or [!type] inline-text (legacy)
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
      custom_title = title_part
      video_url = url_part
    end
  end

  local body_blocks = {}
  for j = 2, #el.content do table.insert(body_blocks, el.content[j]) end

  local label_text
  if custom_title and custom_title ~= "" then
    -- [!type: custom title] — show only the custom title
    label_text = custom_title
  elseif #first.content > 1 and not custom_title then
    -- [!type] inline text — show "Label: inline text"
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

  local body_div = pandoc.Div(body_blocks, pandoc.Attr("", {"callout-body"}, {}))
  local inner = { pandoc.RawBlock("html", header_html), body_div }
  return pandoc.Div(inner, pandoc.Attr("", {"callout", "callout-" .. ctype}, {}))
end

-- ::: {.fold label="..."} ⟨body⟩ ::: ───────────────────────────────────────
-- Wrap a fenced div with class "fold" into a toggle button + hidden body.
-- The author writes this inside a callout to defer "the work" (proof,
-- derivation, alternate solution) behind a click.
function Div(el)
  if not el.classes:includes("fold") then return nil end

  local raw = el.attributes["label"] or ""
  local label = raw ~= "" and raw or "展开"
  local safe = label
    :gsub("&", "&amp;")
    :gsub("<", "&lt;")
    :gsub(">", "&gt;")
    :gsub('"', "&quot;")

  local btn_html = string.format(
    '<button class="callout-fold-btn" type="button" '
    .. 'aria-expanded="false">&#9654; %s</button>',
    safe)

  local body_open  = '<div class="callout-fold-body" hidden>'

  local out = {
    pandoc.RawBlock("html",
      '<div class="callout-fold" data-label="' .. safe .. '">'),
    pandoc.RawBlock("html", btn_html),
    pandoc.RawBlock("html", body_open),
  }
  for _, child in ipairs(el.content) do
    table.insert(out, child)
  end
  table.insert(out, pandoc.RawBlock("html", '</div></div>'))

  return out
end

-- Image dimension attributes: #200w, #400h, #300pt ──────────────────────────
function Image(el)
  local src = el.src
  local val, unit = src:match("#(%d+)(w)$")
  if not val then val, unit = src:match("#(%d+)(h)$") end
  if not val then val, unit = src:match("#(%d+)(pt)$") end

  if val then
    el.src = src:gsub("#%d+%a+$", "")
    if unit == "w" then
      el.attributes["width"] = val
    elseif unit == "h" then
      el.attributes["height"] = val
    elseif unit == "pt" then
      el.attributes["style"] = ("width:%spt"):format(val)
    end
  end
  return el
end
