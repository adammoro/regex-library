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


def consecutive_runs(sorted_ints):
    """Group a sorted list of ints into (start, end) runs of consecutive values."""
    runs = []
    start = prev = sorted_ints[0]
    for n in sorted_ints[1:]:
        if n == prev + 1:
            prev = n
        else:
            runs.append((start, prev))
            start = prev = n
    runs.append((start, prev))
    return runs


def run_to_alternatives(low, high):
    """Turn one run of consecutive 3-digit prefixes into regex alternatives
    that each match a full 5-digit zip code."""
    low_s, high_s = str(low).zfill(3), str(high).zfill(3)
    if low == high:
        return [f"{low_s}[0-9]{{2}}"]
    # Run stays within one leading pair (e.g. 350-352): vary the third digit
    if low_s[:2] == high_s[:2]:
        return [f"{low_s[:2]}[{low_s[2]}-{high_s[2]}][0-9]{{2}}"]

    alternatives = []
    low_ten, high_ten = low // 10, high // 10
    # Partial leading block (e.g. 716-719 out of 716-729)
    if low % 10 != 0:
        head_high = min(high, low_ten * 10 + 9)
        alternatives.append(f"{str(low_ten).zfill(2)}[{low_s[2]}-{str(head_high).zfill(3)[2]}][0-9]{{2}}")
        low_ten += 1
    # Partial trailing block, emitted after any complete middle blocks
    tail = None
    if high % 10 != 9:
        tail = f"{str(high_ten).zfill(2)}[0-{high_s[2]}][0-9]{{2}}"
        high_ten -= 1
    # Complete tens blocks (e.g. 720-729 -> "72[0-9]{3}")
    if low_ten <= high_ten:
        for lead_digit in range(int(str(low_ten).zfill(2)[0]), int(str(high_ten).zfill(2)[0]) + 1):
            sub_low = max(low_ten, lead_digit * 10)
            sub_high = min(high_ten, lead_digit * 10 + 9)
            if sub_low > sub_high:
                continue
            a, b = str(sub_low).zfill(2)[1], str(sub_high).zfill(2)[1]
            digit = a if a == b else f"[{a}-{b}]"
            alternatives.append(f"{lead_digit}{digit}[0-9]{{3}}")
    if tail:
        alternatives.append(tail)
    return alternatives


def tidy(pattern):
    """Collapse degenerate constructs like [4-4] and [0-9][0-9]{2}."""
    pattern = re.sub(r"\[(\d)-\1\]", r"\1", pattern)
    pattern = pattern.replace("[0-9][0-9]{2}", "[0-9]{3}")
    return pattern


def generate_regex_pattern(state_abbreviation):
    zip_codes = search.by_state(state_abbreviation, returns=None)
    # Keep zips as zero-padded strings: Northeast zips (MA, CT, NJ, ...) start
    # with "0" and casting to int would silently drop that leading digit.
    prefixes = sorted({int(zc.zipcode.zfill(5)[:3]) for zc in zip_codes})

    alternatives = []
    for low, high in consecutive_runs(prefixes):
        alternatives.extend(run_to_alternatives(low, high))
    alternatives = [tidy(a) for a in alternatives]

    if len(alternatives) == 1:
        return f"^{alternatives[0]}$"
    return "^(?:" + "|".join(alternatives) + ")$"


def self_check(pattern, state_abbreviation):
    """Every zip actually in the state must match the generated pattern."""
    compiled = re.compile(pattern)
    for zc in search.by_state(state_abbreviation, returns=None):
        if not compiled.fullmatch(zc.zipcode.zfill(5)):
            raise AssertionError(f"{state_abbreviation}: {zc.zipcode} does not match {pattern}")


output = []
for state, abbreviation in us_states.items():
    regex = generate_regex_pattern(abbreviation)
    self_check(regex, abbreviation)
    output.append(f'- {state} ({abbreviation}): `{regex}`')

with open("zip_code_regexes.txt", "w") as file:
    file.write('\n'.join(output))
