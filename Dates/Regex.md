# ISO 8601 Dates

A regex for matching calendar dates in `YYYY-MM-DD` format.

## Important Note

This bounds the month to 01-12 and the day to 01-31, but it doesn't know which months have 30/31 days or account for leap years — `2023-02-31` will incorrectly match. If you need real calendar validity, parse the date with your language's date library instead of just matching it.

## Regex

`^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

**Matches:**
- `2026-08-13`
- `1999-12-31`

**Does not match:**
- `2026-13-01` (invalid month)
- `2026/08/13` (wrong separator)
