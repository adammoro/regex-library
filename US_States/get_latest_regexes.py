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

def range_to_regex(low, high):
    if low == high:
        return re.escape(low)
    if len(low) == 1:
        return f"[{low}-{high}]"

    low_head, low_tail = low[0], low[1:]
    high_head, high_tail = high[0], high[1:]
    tail_len = len(low_tail)

    if low_head == high_head:
        return f"{low_head}{range_to_regex(low_tail, high_tail)}"

    parts = []

    if low_tail == "0" * tail_len:
        parts.append(f"{low_head}[0-9]{{{tail_len}}}")
    else:
        parts.append(f"{low_head}{range_to_regex(low_tail, '9' * tail_len)}")

    mid_low, mid_high = int(low_head) + 1, int(high_head) - 1
    if mid_low <= mid_high:
        digit_class = str(mid_low) if mid_low == mid_high else f"[{mid_low}-{mid_high}]"
        parts.append(f"{digit_class}[0-9]{{{tail_len}}}")

    if high_tail == "9" * tail_len:
        parts.append(f"{high_head}[0-9]{{{tail_len}}}")
    else:
        parts.append(f"{high_head}{range_to_regex('0' * tail_len, high_tail)}")

    return "(?:" + "|".join(parts) + ")"


def generate_regex_pattern(state_abbreviation):
    zip_codes = search.by_state(state_abbreviation, returns=None)
    # Zero-pad first: zip codes in the Northeast (MA, CT, NJ, ...) start with
    # "0" and casting straight to int would silently drop that leading digit.
    sorted_zip_codes = sorted(zc.zipcode.zfill(5) for zc in zip_codes)
    min_zip = sorted_zip_codes[0]
    max_zip = sorted_zip_codes[-1]

    pattern = f"^{range_to_regex(min_zip, max_zip)}$"
    return pattern

output = []
for state, abbreviation in us_states.items():
    regex = generate_regex_pattern(abbreviation)
    output.append(f'{state} ({abbreviation}): `{regex}`')

with open("zip_code_regexes.txt", "w") as file:
    file.write('\n'.join(output))
