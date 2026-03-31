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

-- [!TYPE] callout blocks ─────────────────────────────────────────────────────
function BlockQuote(el)
  if #el.content == 0 then return nil end
  local first = el.content[1]
  if first.t ~= "Para" or #first.content == 0 then return nil end

  local marker = first.content[1]
  if marker.t ~= "Str" then return nil end

  local ctype = marker.text:match("^%[!(%a+)%]$")
  if not ctype then return nil end
  ctype = ctype:lower()

  local label = CALLOUT_LABELS[ctype] or (ctype:sub(1,1):upper() .. ctype:sub(2))

  -- Collect body blocks and optional inline title:
  --   Case A: [!type] alone in first Para → no title, body is el.content[2..]
  --   Case B: [!type] text...             → inline text becomes title, body is el.content[2..]
  local body_blocks = {}
  local title_inlines = nil

  if #first.content == 1 then
    -- Case A: no title
    for j = 2, #el.content do
      table.insert(body_blocks, el.content[j])
    end
  else
    -- Case B: collect inlines after marker (skip leading SoftBreak/Space) as title
    local i = 2
    if first.content[i] and
       (first.content[i].t == "SoftBreak" or first.content[i].t == "Space") then
      i = i + 1
    end
    if i <= #first.content then
      title_inlines = {}
      while i <= #first.content do
        table.insert(title_inlines, first.content[i])
        i = i + 1
      end
    end
    for j = 2, #el.content do
      table.insert(body_blocks, el.content[j])
    end
  end

  -- Build header: "重要" or "重要: 符合函数"
  local label_text = label
  if title_inlines then
    -- Render title inlines to plain text
    local title_str = pandoc.utils.stringify(pandoc.Span(title_inlines))
    label_text = label .. ": " .. title_str
  end

  -- Build: outer div.callout > div.callout-header + div.callout-body
  local header_html = string.format(
    '<div class="callout-header callout-header-%s">'
    .. '<span class="callout-icon"></span>'
    .. '<span class="callout-label">%s</span></div>',
    ctype, label_text)

  local inner = { pandoc.RawBlock("html", header_html) }
  for _, b in ipairs(body_blocks) do
    table.insert(inner, b)
  end

  return pandoc.Div(inner, pandoc.Attr("", {"callout", "callout-" .. ctype}, {}))
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
