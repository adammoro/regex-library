# URLs

A regex for matching `http` and `https` URLs, with an optional port and path/query/fragment.

## Important Note

This only matches `http(s)://` URLs — it won't match other schemes (`ftp://`, `mailto:`, `git@...`), protocol-relative URLs (`//example.com`), or bare domains without a scheme. It also doesn't validate that the host is a real, resolvable domain (or IP address) — it just checks the shape.

## Regex

`^https?://[A-Za-z0-9.-]+(:[0-9]+)?(/[^\s]*)?$`

**Matches:**
- `https://example.com`
- `http://sub.example.co.uk:8080/path?q=1`

**Does not match:**
- `ftp://example.com`
- `//example.com` (no scheme)
