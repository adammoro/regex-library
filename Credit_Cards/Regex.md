# Credit Card Numbers

Regexes for matching credit card numbers by issuer, based on IIN (issuer identification number) prefix and total digit length.

## Important Note

These only check the prefix and length conventions for each network — they don't verify the Luhn checksum, so a made-up but correctly-shaped number will still match. They also don't cover every issuer or every newer prefix range (e.g. Mastercard's 2221-2720 range added in 2016 is not included below; only the classic 51-55 range is). Never use regex alone to validate a real card number before charging it — use your payment processor's validation.

## Regex

- Visa: `^4[0-9]{12}(?:[0-9]{3})?$`
  **Matches:** `4111111111111111`, `4222222222222`
  **Does not match:** `5111111111111111`

- Mastercard: `^5[1-5][0-9]{14}$`
  **Matches:** `5555555555554444`
  **Does not match:** `4111111111111111`

- American Express: `^3[47][0-9]{13}$`
  **Matches:** `378282246310005`
  **Does not match:** `4111111111111111`

- Discover: `^6(?:011|5[0-9]{2})[0-9]{12}$`
  **Matches:** `6011111111111117`
  **Does not match:** `6111111111111117`
