# Tessellate Labs - research site

Static research site published from this repository. Pages live in `_pages/`;
shared facts live in `_data/`.

## Field report entry format

`_pages/field-reports.md` is hand-maintained. Every field report is one fixed
block:

```
**TITLE**\\
CONTRIBUTOR LINE\\
VENUE YEAR. [[link]](RECORD_URL) [[brief]](BRIEF_URL)
* bullet one
* bullet two
* bullet three


```

Rules (must be followed exactly):

- The title line is `**` + the record's exact title + `**`, followed by two
  literal backslash characters.
- The contributor line lists **the record's contributors in the order given by
  the authoritative archive record**. Names are joined with `, `. After every
  contributor whose `equal_contribution` flag is true in the record, append
  ` \*` (space, backslash, asterisk). The profile owner's name is wrapped as
  `*<ins>NAME</ins>*`. The line ends with two literal backslash characters.
- The metadata line starts with the record's venue and year, then the record's
  canonical `[[link]]` and `[[brief]]` URLs.
- Every entry has three `* ` bullet lines summarising the work.
- Leave two blank lines between blocks.
- Entries are ordered newest first (reverse chronological by publication date).

## Shared publication archive

The authoritative records live in the companion repository
`https://github.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5`. Its `README.md` explains the layout.
