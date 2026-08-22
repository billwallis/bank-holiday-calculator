import datetime

MONDAY = 0
SATURDAY = 5
SUNDAY = 6


def _calculate_new_years_day(year: int) -> datetime.date:
    """
    New Year's Day

    On 2nd or 3rd if New Year's Day is on a Sunday or Saturday,
    respectively.
    """

    january_1st = datetime.date(year=year, month=1, day=1)
    if january_1st.weekday() == SUNDAY:
        return datetime.date(year=year, month=1, day=2)
    elif january_1st.weekday() == SATURDAY:
        return datetime.date(year=year, month=1, day=3)
    else:
        return january_1st


def _calculate_easter_sunday(year: int) -> datetime.date:
    """
    Source - https://stackoverflow.com/a/78259311
    Posted by dan04
    Retrieved 2026-08-22, License - CC BY-SA 4.0
    """

    century = year // 100
    lunar_adj = (8 * century + 13) // 25
    solar_adj = -century + century // 4
    total_adj = solar_adj + lunar_adj
    leap_months = (210 * year - year % 19 + 19 * total_adj + 266) // 570
    full_moon = (6725 * year + 18) // 19 + 30 * leap_months - lunar_adj + year // 4 + 3
    if 286 <= (total_adj + year % 19 * 11) % 30 * 19 - year % 19 <= 312:
        full_moon -= 1
    week = full_moon // 7 - 38

    return datetime.date.fromordinal(week * 7)


def _calculate_good_friday(year: int) -> datetime.date:
    """
    Good Friday

    Based on moon cycle.
    """

    return _calculate_easter_sunday(year=year) - datetime.timedelta(days=2)


def _calculate_easter_monday(year: int) -> datetime.date:
    """
    Easter Monday

    Based on moon cycle.
    """

    return _calculate_easter_sunday(year=year) + datetime.timedelta(days=1)


def _calculate_early_may_bank_holiday(year: int) -> datetime.date:
    """
    Early May bank holiday

    First Monday in May.
    """

    may_1st = datetime.date(year=year, month=5, day=1)
    delta = (7 - may_1st.weekday()) % 7

    return may_1st + datetime.timedelta(days=delta)


def _calculate_spring_bank_holiday(year: int) -> datetime.date:
    """
    Spring bank holiday

    Last Monday in May.
    """

    may_31st = datetime.date(year=year, month=5, day=31)
    delta = may_31st.weekday()

    return may_31st - datetime.timedelta(days=delta)


def _calculate_summer_bank_holiday(year: int) -> datetime.date:
    """
    Summary bank holiday

    Last Monday in August.
    """

    august_31st = datetime.date(year=year, month=8, day=31)
    delta = august_31st.weekday()

    return august_31st - datetime.timedelta(days=delta)


def _calculate_christmas_day(year: int) -> datetime.date:
    """
    Christmas Day

    On 26th or 27th if Christmas Day is on a Sunday or Saturday respectively.
    """

    december_25th = datetime.date(year=year, month=12, day=25)
    if december_25th.weekday() == SUNDAY:
        return datetime.date(year=year, month=12, day=26)
    elif december_25th.weekday() == SATURDAY:
        return datetime.date(year=year, month=12, day=27)
    else:
        return december_25th


def _calculate_boxing_day(year: int) -> datetime.date:
    """
    Boxing Day

    Adjust for weekend accounting for the Christmas adjustment.
    """

    december_26th = datetime.date(year=year, month=12, day=26)
    if december_26th.weekday() == SATURDAY:
        return datetime.date(year=year, month=12, day=28)
    elif december_26th.weekday() == SUNDAY:
        return datetime.date(year=year, month=12, day=28)
    elif december_26th.weekday() == MONDAY:
        return datetime.date(year=year, month=12, day=27)
    else:
        return december_26th


def calculate_bank_holidays(year: int) -> dict[str, datetime.date]:
    return {
        "New Year's Day": _calculate_new_years_day(year=year),
        "Good Friday": _calculate_good_friday(year=year),
        "Easter Monday": _calculate_easter_monday(year=year),
        "Early May bank holiday":  _calculate_early_may_bank_holiday(year=year),
        "Spring bank holiday":  _calculate_spring_bank_holiday(year=year),
        "Summer bank holiday":  _calculate_summer_bank_holiday(year=year),
        "Christmas Day":  _calculate_christmas_day(year=year),
        "Boxing Day":  _calculate_boxing_day(year=year),
    }
