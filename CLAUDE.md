# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A curated library of regular expressions, organized into one folder per topic/category. There is no build system, package manifest, or test suite — this is a documentation-style repo where the primary content is Markdown files listing regexes, occasionally paired with a small Python script that regenerates them from a live data source.

## Repository structure

- `README.md` — top-level index. States the convention: each category gets its own folder containing a `Regex.md` file listing the regex(es) and any relevant usage notes.
- `<Category>/Regex.md` — the actual regex list for that category, in Markdown.
- `<Category>/README.md` — short description of the category, links to its `Regex.md` and (if present) its generator script.
- `<Category>/get_latest_regexes.py` (optional, per category) — a script to regenerate that category's regexes from an external data source, since some regexes (e.g. ZIP codes) drift over time as underlying data changes.

Currently the only category is `US_States/`, covering US ZIP code regexes by state.

## Conventions to follow when adding or editing content

- **Adding a new category**: create `<Category>/`, add a `Regex.md` there, and follow the existing pattern of a short `README.md` linking to `Regex.md` (and to a generator script, if one exists). No central index needs to be regenerated beyond linking from the root `README.md` if appropriate.
- **`Regex.md` format** (see `US_States/Regex.md`): an `## Important Note` section on caveats/accuracy, a `## Regex` section with a `This list was last updated on: `<date>`` line, followed by one bullet per entry: `- <Label> (<abbrev>): `<regex>` `. Update the "last updated" date whenever the list changes.
- Regexes are anchored (`^...$`) and use POSIX-style character classes (e.g. `^35[0-9]{3}$`), not literal numeric ranges.

## Running the generator scripts

`US_States/get_latest_regexes.py` uses the `uszipcode` package (not vendored — install with `pip install uszipcode`) to pull current ZIP code data and build a `^min-max$`-style pattern per state, writing output to `zip_code_regexes.txt` in the current working directory. Run it from inside `US_States/` so the output lands next to the other files:

```
cd US_States
pip install uszipcode
python get_latest_regexes.py
```

**Known gap**: the script's output format (`^<min_zip>-<max_zip>$`) is a literal numeric range, not a regex character class, and does not match the character-class style already committed in `Regex.md` (e.g. `^35[0-9]{3}$`). If you regenerate the list, reconcile/reformat the script's output to match `Regex.md`'s existing convention before committing, rather than pasting it in as-is.

There is no test suite, linter, or CI configured in this repository.
