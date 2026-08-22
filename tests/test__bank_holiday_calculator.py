import datetime

import pytest

from bank_holiday_calculator import calculate_bank_holidays


@pytest.fixture
def bank_holidays__2018() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2018, month=1, day=1),
        "Good Friday": datetime.date(year=2018, month=3, day=30),
        "Easter Monday": datetime.date(year=2018, month=4, day=2),
        "Early May bank holiday": datetime.date(year=2018, month=5, day=7),
        "Spring bank holiday": datetime.date(year=2018, month=5, day=28),
        "Summer bank holiday": datetime.date(year=2018, month=8, day=27),
        "Christmas Day": datetime.date(year=2018, month=12, day=25),
        "Boxing Day": datetime.date(year=2018, month=12, day=26),
    }

@pytest.fixture
def bank_holidays__2019() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2019, month=1, day=1),
        "Good Friday": datetime.date(year=2019, month=4, day=19),
        "Easter Monday": datetime.date(year=2019, month=4, day=22),
        "Early May bank holiday": datetime.date(year=2019, month=5, day=6),
        "Spring bank holiday": datetime.date(year=2019, month=5, day=27),
        "Summer bank holiday": datetime.date(year=2019, month=8, day=26),
        "Christmas Day": datetime.date(year=2019, month=12, day=25),
        "Boxing Day": datetime.date(year=2019, month=12, day=26),
    }

@pytest.fixture
def bank_holidays__2020() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2020, month=1, day=1),
        "Good Friday": datetime.date(year=2020, month=4, day=10),
        "Easter Monday": datetime.date(year=2020, month=4, day=13),
        "Early May bank holiday": datetime.date(year=2020, month=5, day=4),
        "Spring bank holiday": datetime.date(year=2020, month=5, day=25),
        "Summer bank holiday": datetime.date(year=2020, month=8, day=31),
        "Christmas Day": datetime.date(year=2020, month=12, day=25),
        "Boxing Day": datetime.date(year=2020, month=12, day=28),
    }

@pytest.fixture
def bank_holidays__2021() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2021, month=1, day=1),
        "Good Friday": datetime.date(year=2021, month=4, day=2),
        "Easter Monday": datetime.date(year=2021, month=4, day=5),
        "Early May bank holiday": datetime.date(year=2021, month=5, day=3),
        "Spring bank holiday": datetime.date(year=2021, month=5, day=31),
        "Summer bank holiday": datetime.date(year=2021, month=8, day=30),
        "Christmas Day": datetime.date(year=2021, month=12, day=27),
        "Boxing Day": datetime.date(year=2021, month=12, day=28),
    }

@pytest.fixture
def bank_holidays__2022() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2022, month=1, day=3),
        "Good Friday": datetime.date(year=2022, month=4, day=15),
        "Easter Monday": datetime.date(year=2022, month=4, day=18),
        "Early May bank holiday": datetime.date(year=2022, month=5, day=2),
        "Spring bank holiday": datetime.date(year=2022, month=5, day=30),
        # This year was a special case
        # "Spring bank holiday": datetime.date(year=2022, month=6, day=2),
        # "Platinum Jubilee bank holiday": datetime.date(year=2022, month=6, day=3),
        "Summer bank holiday": datetime.date(year=2022, month=8, day=29),
        "Christmas Day": datetime.date(year=2022, month=12, day=26),
        "Boxing Day": datetime.date(year=2022, month=12, day=27),
    }

@pytest.fixture
def bank_holidays__2023() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2023, month=1, day=2),
        "Good Friday": datetime.date(year=2023, month=4, day=7),
        "Easter Monday": datetime.date(year=2023, month=4, day=10),
        "Early May bank holiday": datetime.date(year=2023, month=5, day=1),
        "Spring bank holiday": datetime.date(year=2023, month=5, day=29),
        "Summer bank holiday": datetime.date(year=2023, month=8, day=28),
        "Christmas Day": datetime.date(year=2023, month=12, day=25),
        "Boxing Day": datetime.date(year=2023, month=12, day=26),
    }

@pytest.fixture
def bank_holidays__2024() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2024, month=1, day=1),
        "Good Friday": datetime.date(year=2024, month=3, day=29),
        "Easter Monday": datetime.date(year=2024, month=4, day=1),
        "Early May bank holiday": datetime.date(year=2024, month=5, day=6),
        "Spring bank holiday": datetime.date(year=2024, month=5, day=27),
        "Summer bank holiday": datetime.date(year=2024, month=8, day=26),
        "Christmas Day": datetime.date(year=2024, month=12, day=25),
        "Boxing Day": datetime.date(year=2024, month=12, day=26),
    }

@pytest.fixture
def bank_holidays__2025() -> dict[str, datetime.date]:
    return {
        "New Year's Day": datetime.date(year=2025, month=1, day=1),
        "Good Friday": datetime.date(year=2025, month=4, day=18),
        "Easter Monday": datetime.date(year=2025, month=4, day=21),
        "Early May bank holiday": datetime.date(year=2025, month=5, day=5),
        "Spring bank holiday": datetime.date(year=2025, month=5, day=26),
        "Summer bank holiday": datetime.date(year=2025, month=8, day=25),
        "Christmas Day": datetime.date(year=2025, month=12, day=25),
        "Boxing Day": datetime.date(year=2025, month=12, day=26),
    }


@pytest.mark.parametrize(
    "year",
    [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
)
def test__calculate_bank_holidays__happy_path(
    year: int,
    request: pytest.FixtureRequest,
):
    expected = request.getfixturevalue(f"bank_holidays__{year}")
    assert calculate_bank_holidays(year=year) == expected
