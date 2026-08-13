# IP Addresses

Regexes for matching IPv4 and IPv6 addresses.

## Important Note

The IPv4 pattern correctly bounds each octet to 0-255. The IPv6 pattern only covers the **full, uncompressed** 8-group form (`xxxx:xxxx:...:xxxx`) — it deliberately doesn't attempt to handle `::` zero-compression, embedded IPv4 (`::ffff:192.0.2.1`), or zone IDs (`%eth0`), since a regex covering all of that correctly is large and hard to verify by eye. If you need to validate arbitrary real-world IPv6 addresses, use your language's IP address library (e.g. Python's `ipaddress` module) instead.

## Regex

**IPv4:**

`^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

**Matches:** `192.168.1.1`, `255.255.255.255`, `0.0.0.0`
**Does not match:** `256.1.1.1`, `1.2.3`, `1.2.3.4.5`

**IPv6 (full form only):**

`^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`

**Matches:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
**Does not match:** `2001:db8::1` (compressed form — not covered), `not-an-ipv6`
