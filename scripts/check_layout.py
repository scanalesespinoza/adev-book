"""Check relocation-sensitive publishing paths from any working directory."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "adevelopment-book"


def check():
    for edition in ("book", "book-en", "book-es"):
        for entry in (BOOK / edition / "Book.txt").read_text().splitlines():
            if entry.strip():
                assert (BOOK / edition / (entry.strip() + ".md")).is_file(), entry
    for template in ("pdf-cover.tex", "pdf-cover-en.tex"):
        content = (BOOK / template).read_text()
        targets = re.findall(r"\\includegraphics\[[^]]*\]\{([^}]+)\}", content)
        assert targets and all(p.startswith("adevelopment-book/dist/") for p in targets), template
    lua = (BOOK / "epub-external-links.lua").read_text()
    assert "scanalesespinoza/adev-book/" in lua, "EPUB links must resolve inside this repository"
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in re.findall(r"\]\((\.{1,2}/[^)#\s]*)", md.read_text()):
            assert (md.parent / target).resolve().exists(), f"{md.relative_to(ROOT)}: {target}"
    print("Book manifests, covers, EPUB links, and relative Markdown links: PASS")


if __name__ == "__main__":
    check()
