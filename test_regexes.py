"""Validate every Regex.md in the library.

For each category folder's Regex.md this script:
  1. compiles every regex it finds (inline code spans anchored with ^...$),
  2. asserts each documented "Matches:" example matches its pattern,
  3. asserts each documented "Does not match:" example does not.

Examples are associated with the nearest preceding pattern in the file, so
per-issuer lists (like Credit_Cards) and single-pattern files both work.

Run with: python3 test_regexes.py   (exits non-zero on any failure)
"""
import re
import sys
from pathlib import Path

CODE_SPAN = re.compile(r"`([^`]+)`")

failures = []
patterns_checked = 0
examples_checked = 0

for regex_md in sorted(Path(__file__).parent.glob("*/Regex.md")):
    category = regex_md.parent.name
    current = None  # most recently seen (pattern, compiled) in this file
    expect = None   # True inside a "Matches:" context, False inside "Does not match:"

    for line in regex_md.read_text().splitlines():
        spans = CODE_SPAN.findall(line)

        # A line introducing examples may also carry them inline.
        lowered = line.lower()
        if "does not match" in lowered:
            expect = False
        elif "matches" in lowered:
            expect = True
        elif not line.strip().startswith(("-", "*", "`")):
            # Prose paragraph (e.g. Important Note): leave example context.
            expect = None

        for span in spans:
            if span.startswith("^") and span.endswith("$"):
                try:
                    current = (span, re.compile(span))
                    patterns_checked += 1
                except re.error as exc:
                    failures.append(f"{category}: pattern does not compile: `{span}` ({exc})")
                    current = None
                expect = None  # examples for this pattern come after it
            elif expect is not None and current is not None:
                pattern, compiled = current
                examples_checked += 1
                if bool(compiled.search(span)) != expect:
                    kind = "should match" if expect else "should NOT match"
                    failures.append(f"{category}: `{span}` {kind} `{pattern}`")

for failure in failures:
    print(f"FAIL {failure}")
print(f"{patterns_checked} patterns compiled, {examples_checked} examples checked, "
      f"{len(failures)} failures")
sys.exit(1 if failures else 0)
