# Email Addresses

A regex for validating the general shape of an email address (`local-part@domain.tld`).

## Important Note

The full email spec (RFC 5322) is far more permissive than most people expect (quoted local parts, comments, IP-literal domains, etc.), and a fully compliant regex is famously huge and hard to read. This pattern instead covers the common case — it will reject some technically-valid addresses and accept some that a mail server would bounce. If you need to know an address actually receives mail, send a confirmation email; don't rely on regex alone.

## Regex

`^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`

**Matches:**
- `user@example.com`
- `first.last+tag@sub.domain.co`

**Does not match:**
- `user@.com`
- `user@domain` (no top-level domain)
