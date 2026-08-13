# Regex: US Zip Codes by State

Need a list of all the different zip code regexes by state? Here's one solution. 

You can find the most recently updated list of regexes here: [`Regex.md`](https://github.com/adammoro/regex-library/blob/main/US_States/Regex.md)

You can find a script for updating the list of regexes here: [`get_latest_regexes.py`](https://github.com/adammoro/regex-library/blob/main/US_States/get_latest_regexes.py)

I've provided this script because the list of US zip codes grows and changes over time. So if the last updated date is from a while ago, you'll probably want to update the regexes.

To run the script you'll need [`uszipcode`](https://pypi.org/project/uszipcode/), which as of its 1.0.1 release is incompatible with SQLAlchemy 2.x, so pin the older versions:

```
pip install uszipcode "SQLAlchemy<2" "sqlalchemy_mate==1.4.28.4"
```


