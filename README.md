# Regex Library

A growing list of regular expressions and related resources. Each folder has a file named `Regex.md` which lists the regular expression(s) and any relevant informtion about using them.

Some of the regexes will not work forever so I've provided scripts for updating them when possible.

Every pattern and its documented examples can be checked with:

```
python3 test_regexes.py
```

It compiles each regex in every `Regex.md` and asserts the "Matches" / "Does not match" examples, so a bad edit fails loudly.

## Categories

- [Colors](Colors/Regex.md) — hex color codes
- [Credit Cards](Credit_Cards/Regex.md) — card numbers by issuer
- [Dates](Dates/Regex.md) — ISO 8601 dates
- [Email](Email/Regex.md) — email addresses
- [IP Addresses](IP_Addresses/Regex.md) — IPv4 and IPv6
- [Phone Numbers](Phone_Numbers/Regex.md) — US/Canada phone numbers
- [URLs](URLs/Regex.md) — http/https URLs
- [US States](US_States/Regex.md) — ZIP codes by state
- [UUIDs](UUIDs/Regex.md) — UUID v1-v5

