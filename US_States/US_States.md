# US Zip Codes by State

Here's a list of regular expressions (i.e. regex) to match ZIP codes for each state in the US. 

# Important Note

The complexity of the US postal system makes it difficult to create a perfect regex for every state. US zip codes change over time due to population growth and changing postal routes, so it's always a good idea to verify your regex with an updated database or API. So I've provided a script to update the list below.

To create a new list simply download and run this Python script to generate a file named "zip_code_regexes.txt" with the latest regexes by state: `get_latest_regexes.py`

## Regex

This list was last updated on: `3/30/2023`

Alabama (AL): `^35[0-9]{3}$`
Alaska (AK): `^995[0-9]{2}$|^996[0-9]{2}$|^997[0-9]{2}$|^998[0-9]{2}$|^999[0-9]{2}$`
Arizona (AZ): `^85[0-9]{3}$|^86[0-9]{3}$`
Arkansas (AR): `^716[0-9]{2}$|^717[0-9]{2}$|^718[0-9]{2}$|^719[0-9]{2}$|^72[0-9]{3}$`
California (CA): `^90[0-9]{3}$|^91[0-9]{3}$|^92[0-9]{3}$|^93[0-9]{3}$|^94[0-9]{3}$|^95[0-9]{3}$|^96[0-9]{3}$`
Colorado (CO): `^80[0-9]{3}$|^81[0-9]{3}$`
Connecticut (CT): `^06[0-9]{3}$`
Delaware (DE): `^19[789][0-9]{2}$`
Florida (FL): `^32[0-9]{3}$|^33[0-9]{3}$|^34[0-9]{3}$`
Georgia (GA): `^30[0-9]{3}$|^31[0-9]{3}$|^399[0-9]{2}$`
Hawaii (HI): `^967[0-9]{2}$|^968[0-9]{2}$`
Idaho (ID): `^83[0-9]{3}$`
Illinois (IL): `^60[0-9]{3}$|^61[0-9]{3}$|^62[0-9]{3}$`
Indiana (IN): `^46[0-9]{3}$|^47[0-9]{3}$`
Iowa (IA): `^50[0-9]{3}$|^51[0-9]{3}$|^52[0-9]{3}$`
Kansas (KS): `^66[0-9]{3}$|^67[0-9]{3}$`
Kentucky (KY): `^40[0-9]{3}$|^41[0-9]{3}$|^42[0-9]{3}$`
Louisiana (LA): `^70[0-9]{3}$|^71[0-9]{3}$`
Maine (ME): `^03[0-9]{3}$|^04[0-9]{3}$`
Maryland (MD): `^2[01][0-9]{3}$`
Massachusetts (MA): `^010[0-9]{2}$|^011[0-9]{2}$|^012[0-9]{2}$|^013[0-9]{2}$|^014[0-9]{2}$|^015[0-9]{2}$|^016[0-9]{2}$|^017[0-9]{2}$|^018[0-9]{2}$|^019[0-9]{2}$|^020[0-9]{2}$|^021[0-9]{2}$|^022[0-9]{2}$|^023[0-9]{2}$|^024[0-9]{2}$|^025[0-9]{2}$|^026[0-9]{2}$|^027[0-9]{2}$`
Michigan (MI): `^48[0-9]{3}$|^49[0-9]{3}$`
Minnesota (MN): `^55[0-9]{3}$|^56[0-9]{3}$`
Mississippi (MS): `^386[0-9]{2}$|^387[0-9]{2}$|^38[89][0-9]{2}$|^39[0-9]{3}$`
Missouri (MO): `^63[0-9]{3}$|^64[0-9]{3}$|^65[0-9]{3}$`
Montana (MT): `^59[0-9]{3}$`
Nebraska (NE): `^68[0-9]{3}$|^69[0-9]{3}$`
Nevada (NV): `^889[0-9]{2}$|^89[0-9]{3}$`
New Hampshire (NH): `^03[0-9]{3}$`
New Jersey (NJ): `^07[0-9]{3}$|^08[0-9]{3}$`
New Mexico (NM): `^87[0-9]{3}$|^88[0-9]{3}$`
New York (NY): `^1[0-4][0-9]{3}$|^50[0-9]{3}$`
North Carolina (NC): `^27[0-9]{3}$|^28[0-9]{3}$`
North Dakota (ND): `^58[0-9]{3}$`
Ohio (OH): `^43[0-9]{3}$|^44[0-9]{3}$|^45[0-9]{3}$`
Oklahoma (OK): `^73[0-9]{3}$|^74[0-9]{3}$`
Oregon (OR): `^97[0-9]{3}$`
Pennsylvania (PA): `^1[5678][0-9]{3}$|^19[0-9]{3}$`
Rhode Island (RI): `^028[0-9]{2}$|^029[0-9]{2}$`
South Carolina (SC): `^29[0-9]{3}$`
South Dakota (SD): `^57[0-9]{3}$`
Tennessee (TN): `^37[0-9]{3}$|^38[0-9]{3}$`
Texas (TX): `^75[0-9]{3}$|^76[0-9]{3}$|^77[0-9]{3}$|^78[0-9]{3}$|^79[0-9]{3}$`
Utah (UT): `^84[0-9]{3}$`
Vermont (VT): `^05[0-9]{3}$`
Virginia (VA): `^2[2-4][0-9]{3}$`
Washington (WA): `^98[0-9]{3}$|^99[0-9]{3}$`
West Virginia (WV): `^247[0-9]{2}$|^248[0-9]{2}$|^25[0-9]{3}$|^26[0-9]{3}$`
Wisconsin (WI): `^53[0-9]{3}$|^54[0-9]{3}$`
Wyoming (WY): `^82[0-9]{3}$|^83[0-9]{3}$`


