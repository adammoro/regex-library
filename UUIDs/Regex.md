# UUIDs

A regex for matching standard 8-4-4-4-12 hex UUIDs, versions 1 through 5.

## Important Note

This enforces the version nibble (`1`-`5`) and the variant nibble (`8`, `9`, `a`, or `b`) per RFC 4122, so it will reject malformed or non-standard UUIDs (like the all-zero nil UUID, or version 0/6+ UUIDs). It's case-insensitive on the hex digits, matching common practice.

## Regex

`^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$`

**Matches:**
- `550e8400-e29b-41d4-a716-446655440000` (v4)
- `6fa459ea-ee8a-3ca4-894e-db77e160355e` (v3)

**Does not match:**
- `not-a-uuid`
- `123e4567-e89b-62d3-a456-426614174000` (invalid version digit `6`)
