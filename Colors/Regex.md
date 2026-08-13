# Hex Color Codes

A regex for matching CSS-style hex color codes, in both shorthand (3-digit) and full (6-digit) form.

## Important Note

This does not match the 4- and 8-digit forms that include an alpha channel (`#rgba`, `#rrggbbaa`), which are valid in CSS but less common. Add `{4}` and `{8}` alternatives if you need those too.

## Regex

`^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$`

**Matches:**
- `#fff`
- `#FFFFFF`
- `#a3c113`

**Does not match:**
- `#ffff` (4 digits — not covered)
- `fff` (missing `#`)
