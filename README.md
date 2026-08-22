<span align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![tests](https://github.com/billwallis/bank-holiday-calculator/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/bank-holiday-calculator/actions/workflows/tests.yaml)
[![coverage](https://raw.githubusercontent.com/billwallis/bank-holiday-calculator/refs/heads/main/coverage.svg)](https://smarie.github.io/python-genbadge/)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/bank-holiday-calculator/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/bank-holiday-calculator/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/bank-holiday-calculator)](https://shields.io/badges/git-hub-last-commit)

</span>

---

# Bank Holiday Calculator

UK bank holiday calculator.

## Contributing

Install the dependencies:

```shell
python -m venv .venv/
source .venv/bin/activate

pip install --editable . --group dev --group test
pre-commit install --install-hooks
```
