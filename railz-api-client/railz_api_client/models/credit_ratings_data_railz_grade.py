from typing import Literal, Set, cast

CreditRatingsDataRailzGrade = Literal["Excellent", "Fair", "Good", "Poor", "Very Good", "Very Poor"]

CREDIT_RATINGS_DATA_RAILZ_GRADE_VALUES: Set[CreditRatingsDataRailzGrade] = {
    "Excellent",
    "Fair",
    "Good",
    "Poor",
    "Very Good",
    "Very Poor",
}


def check_credit_ratings_data_railz_grade(value: str) -> CreditRatingsDataRailzGrade:
    if value in CREDIT_RATINGS_DATA_RAILZ_GRADE_VALUES:
        return cast(CreditRatingsDataRailzGrade, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_RAILZ_GRADE_VALUES!r}")
