<span align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![tests](https://github.com/billwallis/bank-holiday-calculator/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/bank-holiday-calculator/actions/workflows/tests.yaml)
[![coverage](https://raw.githubusercontent.com/billwallis/bank-holiday-calculator/refs/heads/main/coverage.svg)](https://smarie.github.io/python-genbadge/)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/bank-holiday-calculator/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/bank-holiday-calculator/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/bank-holiday-calculator)](https://shields.io/badges/git-hub-last-commit)

</span>

---

# Bank Holiday Calculator

UK bank holiday calculator.

## Usage

Exposes a single function, `calculate_bank_holidays`, which returns a dictionary of the bank holidays for the specified year.

```python
from bank_holiday_calculator import calculate_bank_holidays

for name, date in calculate_bank_holidays(year=2026).items():
    print(f"{name:>24}: {date.isoformat()}")
```
```text
          New Year's Day: 2026-01-01
             Good Friday: 2026-04-03
           Easter Monday: 2026-04-06
  Early May bank holiday: 2026-05-04
     Spring bank holiday: 2026-05-25
     Summer bank holiday: 2026-08-31
           Christmas Day: 2026-12-25
              Boxing Day: 2026-12-28
```

### Note: this isn't always accurate

Sometimes the UK government will choose to change (or add!) the bank holidays. For example, in 2022 the **Spring bank holiday** was moved from `2022-05-30` to `2022-06-02` and a one-off additional day, the **Platinum Jubilee bank holiday**, was added on `2022-06-03`.

A better data source for real dates is either of the following:

- https://www.gov.uk/bank-holidays
- https://www.gov.uk/bank-holidays.json

## Contributing

Install the dependencies:

```shell
python -m venv .venv/
source .venv/bin/activate

pip install --editable . --group dev --group test
pre-commit install --install-hooks
```
