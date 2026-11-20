# ADEV book

Sources, build pipeline, and editorial assets for the book that explains [A-Dev](https://github.com/scanalesespinoza/adev), the practice of AI Agentic Development.

The book explains the practice; it is not a normative source. Doctrine, policies, profiles, and agent skills live in the A-Dev repository.

## Contents

| Path | Purpose |
| --- | --- |
| [`adevelopment-book/book-es/`](adevelopment-book/book-es/README.md) | Spanish first edition, the editorial source of record |
| [`adevelopment-book/book-en/`](adevelopment-book/book-en/README.md) | English adaptation of the Spanish v2 manuscript |
| [`adevelopment-book/book/`](adevelopment-book/book/INDEX.md) | Historical English manuscript, retained for reference |
| [`adevelopment-book/collateral/`](adevelopment-book/collateral/) | Talks, posts, one-pager, and video material |
| [`manuscript/`](manuscript/README.md) | Earlier manuscript snapshot, preserved for provenance |
| [`publishing-kit/`](publishing-kit/00-inventory.md) | Proposal, readiness, rights, and launch planning |
| [`blog/`](blog/) | Published articles |

## Build

The [Spanish](.github/workflows/build-book-pdf.yml) and [English](.github/workflows/build-book-en.yml) workflows produce PDF and EPUB artifacts and publish them to a GitHub release on version tags. Validate the layout locally with:

```bash
python3 scripts/check_layout.py
```

## Provenance

This repository was extracted from A-Dev with its history. Links from the book into A-Dev doctrine are pinned to the A-Dev revision at extraction time (`340f705`) so they remain valid while the framework evolves. Releases published before the extraction remain available in the A-Dev repository.
