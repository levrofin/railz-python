from typing import Literal, Set, cast

CreditsDataRailzGrade = Literal["Excellent", "Fair", "Good", "Poor", "Very Good", "Very Poor"]

CREDITS_DATA_RAILZ_GRADE_VALUES: Set[CreditsDataRailzGrade] = {
    "Excellent",
    "Fair",
    "Good",
    "Poor",
    "Very Good",
    "Very Poor",
}


def check_credits_data_railz_grade(value: str) -> CreditsDataRailzGrade:
    if value in CREDITS_DATA_RAILZ_GRADE_VALUES:
        return cast(CreditsDataRailzGrade, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_RAILZ_GRADE_VALUES!r}")
