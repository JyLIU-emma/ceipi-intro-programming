-- Wrap textual notebook outputs in a dedicated LaTeX environment.
-- Rich display outputs such as images remain unchanged.
local function has_class(element, wanted)
  for _, class_name in ipairs(element.classes) do
    if class_name == wanted then
      return true
    end
  end
  return false
end

function Div(element)
  if has_class(element, "output") and not has_class(element, "display_data") then
    -- Terminal progress bars may contain ANSI cursor/color controls that are
    -- meaningful on screen but invalid in LaTeX. Remove those controls and
    -- use portable glyphs for the remaining progress indicators.
    for _, block in ipairs(element.content) do
      if block.t == "CodeBlock" then
        block.text = block.text:gsub("\27%[[0-9;?]*[A-Za-z]", "")
        block.text = block.text:gsub("━", "=")
        block.text = block.text:gsub("✔", "[ok]")
      end
    end

    local blocks = pandoc.List({
      pandoc.RawBlock("latex", "\\begin{NotebookOutput}")
    })
    blocks:extend(element.content)
    blocks:insert(pandoc.RawBlock("latex", "\\end{NotebookOutput}"))
    return blocks
  end
end
