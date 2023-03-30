import re
from uszipcode import SearchEngine

search = SearchEngine()

us_states = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

def generate_regex_pattern(state_abbreviation):
    zip_codes = search.by_state(state_abbreviation, returns=None)
    sorted_zip_codes = sorted([int(zc.zipcode) for zc in zip_codes])
    min_zip = sorted_zip_codes[0]
    max_zip = sorted_zip_codes[-1]

    pattern = f"^{min_zip}-{max_zip}$"
    return pattern

output = []
for state, abbreviation in us_states.items():
    regex = generate_regex_pattern(abbreviation)
    output.append(f'{state} ({abbreviation}): `{regex}`')

with open("zip_code_regexes.txt", "w") as file:
    file.write('\n'.join(output))
