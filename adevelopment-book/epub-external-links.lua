-- EPUB packages cannot retain links to files that live outside the package.
-- Keep repository-relative links in the Markdown sources, but publish them as
-- links to the same asset in this repository at the commit being built, so a
-- versioned artifact never points at a moving branch.

local ref = os.getenv("GITHUB_SHA") or "main"

function Link(link)
  local target = link.target

  if not target:match("^%.%./") then
    return link
  end

  while target:match("^%.%./") do
    target = target:gsub("^%.%./", "", 1)
  end

  local view = target:match("/$") and "tree" or "blob"
  link.target = "https://github.com/scanalesespinoza/adev-book/"
    .. view .. "/" .. ref .. "/" .. target

  return link
end
