# US Zip Codes by State

Here's a list of regular expressions (i.e. regex) to match ZIP codes for each state in the US.

## Important Note

The complexity of the US postal system makes it difficult to create a perfect regex for every state. US zip codes change over time due to population growth and changing postal routes, so it's always a good idea to verify your regex with an updated database or API. So I've provided a script to update the list below.

These patterns are built from the actual 3-digit ZIP prefixes assigned to each state, so every real ZIP in a state matches its state's pattern. Because they work at prefix granularity, a pattern can still match some 5-digit codes that don't exist (not every code within an assigned prefix is in use). Also note that two prefixes genuinely straddle state lines — `726xx` (AR/MO) and `834xx` (ID/WY) — so those appear in both states' patterns.

To create a new list simply download and run this Python script to generate a file named "zip_code_regexes.txt" with the latest regexes by state: [`get_latest_regexes.py`](https://github.com/adammoro/regex-library/blob/main/US_States/get_latest_regexes.py)

## Regex

This list was last updated on: `8/13/2026`

- Alabama (AL): `^(?:35[0-2][0-9]{2}|35[4-9][0-9]{2}|36[0-9]{3})$`
- Alaska (AK): `^99[5-9][0-9]{2}$`
- Arizona (AZ): `^(?:85[0-3][0-9]{2}|85[5-7][0-9]{2}|859[0-9]{2}|860[0-9]{2}|86[3-5][0-9]{2})$`
- Arkansas (AR): `^(?:71[6-9][0-9]{2}|72[0-9]{3})$`
- California (CA): `^(?:90[0-8][0-9]{2}|91[0-9]{3}|92[0-8][0-9]{2}|93[0-7][0-9]{2}|939[0-9]{2}|94[0-1][0-9]{2}|94[3-9][0-9]{2}|95[0-9]{3}|96[0-1][0-9]{2})$`
- Colorado (CO): `^(?:80[0-9]{3}|81[0-6][0-9]{2})$`
- Connecticut (CT): `^06[0-9]{3}$`
- Delaware (DE): `^19[7-9][0-9]{2}$`
- Florida (FL): `^(?:32[0-9]{3}|33[0-1][0-9]{2}|33[3-9][0-9]{2}|34[1-2][0-9]{2}|344[0-9]{2}|34[6-7][0-9]{2}|349[0-9]{2})$`
- Georgia (GA): `^(?:3[0-1][0-9]{3}|398[0-9]{2})$`
- Hawaii (HI): `^96[7-8][0-9]{2}$`
- Idaho (ID): `^83[2-8][0-9]{2}$`
- Illinois (IL): `^(?:6[0-1][0-9]{3}|620[0-9]{2}|62[2-9][0-9]{2})$`
- Indiana (IN): `^4[6-7][0-9]{3}$`
- Iowa (IA): `^(?:50[0-9]{3}|51[0-6][0-9]{2}|52[0-8][0-9]{2})$`
- Kansas (KS): `^(?:66[0-2][0-9]{2}|66[4-9][0-9]{2}|67[0-9]{3})$`
- Kentucky (KY): `^(?:40[0-9]{3}|41[0-8][0-9]{2}|42[0-7][0-9]{2})$`
- Louisiana (LA): `^(?:70[0-1][0-9]{2}|70[3-8][0-9]{2}|71[0-4][0-9]{2})$`
- Maine (ME): `^(?:039[0-9]{2}|04[0-9]{3})$`
- Maryland (MD): `^(?:20[6-9][0-9]{2}|21[0-2][0-9]{2}|21[4-9][0-9]{2})$`
- Massachusetts (MA): `^(?:01[0-9]{3}|02[0-7][0-9]{2})$`
- Michigan (MI): `^4[8-9][0-9]{3}$`
- Minnesota (MN): `^(?:55[0-1][0-9]{2}|55[3-9][0-9]{2}|56[0-7][0-9]{2})$`
- Mississippi (MS): `^(?:38[6-9][0-9]{2}|39[0-7][0-9]{2})$`
- Missouri (MO): `^(?:63[0-1][0-9]{2}|63[3-9][0-9]{2}|64[0-1][0-9]{2}|64[4-8][0-9]{2}|65[0-8][0-9]{2}|726[0-9]{2})$`
- Montana (MT): `^59[0-9]{3}$`
- Nebraska (NE): `^(?:68[0-1][0-9]{2}|68[3-9][0-9]{2}|69[0-3][0-9]{2})$`
- Nevada (NV): `^(?:89[0-1][0-9]{2}|89[3-5][0-9]{2}|89[7-8][0-9]{2})$`
- New Hampshire (NH): `^03[0-8][0-9]{2}$`
- New Jersey (NJ): `^0[7-8][0-9]{3}$`
- New Mexico (NM): `^(?:87[0-1][0-9]{2}|87[3-5][0-9]{2}|87[7-9][0-9]{2}|88[0-4][0-9]{2})$`
- New York (NY): `^1[0-4][0-9]{3}$`
- North Carolina (NC): `^2[7-8][0-9]{3}$`
- North Dakota (ND): `^58[0-8][0-9]{2}$`
- Ohio (OH): `^(?:4[3-4][0-9]{3}|45[0-8][0-9]{2})$`
- Oklahoma (OK): `^(?:73[0-1][0-9]{2}|73[4-9][0-9]{2}|74[0-1][0-9]{2}|74[3-9][0-9]{2})$`
- Oregon (OR): `^97[0-9]{3}$`
- Pennsylvania (PA): `^(?:1[5-8][0-9]{3}|19[0-1][0-9]{2}|19[3-6][0-9]{2})$`
- Rhode Island (RI): `^02[8-9][0-9]{2}$`
- South Carolina (SC): `^29[0-9]{3}$`
- South Dakota (SD): `^57[0-7][0-9]{2}$`
- Tennessee (TN): `^(?:37[0-4][0-9]{2}|37[6-9][0-9]{2}|38[0-5][0-9]{2})$`
- Texas (TX): `^(?:7[5-6][0-9]{3}|770[0-9]{2}|77[2-9][0-9]{2}|7[8-9][0-9]{3})$`
- Utah (UT): `^(?:84[0-1][0-9]{2}|84[3-7][0-9]{2})$`
- Vermont (VT): `^(?:05[0-4][0-9]{2}|05[6-9][0-9]{2})$`
- Virginia (VA): `^(?:201[0-9]{2}|2[2-3][0-9]{3}|24[0-6][0-9]{2})$`
- Washington (WA): `^(?:98[0-6][0-9]{2}|98[8-9][0-9]{2}|99[0-4][0-9]{2})$`
- West Virginia (WV): `^(?:24[7-9][0-9]{2}|25[0-9]{3}|26[0-8][0-9]{2})$`
- Wisconsin (WI): `^(?:53[0-2][0-9]{2}|53[4-5][0-9]{2}|53[7-9][0-9]{2}|54[0-9]{3})$`
- Wyoming (WY): `^(?:82[0-9]{3}|83[0-1][0-9]{2}|834[0-9]{2})$`
