# US Phone Numbers

A regex for matching 10-digit North American Numbering Plan (US/Canada) phone numbers, with or without an optional `+1` country code, in dashes, dots, spaces, or parenthesized-area-code format.

## Important Note

This checks formatting, not that the number is actually dialable — it doesn't validate area codes or exchange codes against the real NANP assignment list, and it only covers North American formatting. It won't match international numbers from other countries.

## Regex

`^(\+1[-. ]?)?\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$`

**Matches:**
- `(555) 123-4567`
- `555-123-4567`
- `+1 555.123.4567`
- `5551234567`

**Does not match:**
- `555-123-456` (too short)
- `+44 20 7946 0958` (non-NANP international format)
