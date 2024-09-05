from typing import Literal, Set, cast

CreditRatingsDataRailzRating = Literal["A", "A+", "A-", "B", "B+", "B-", "C", "C+", "C-", "D"]

CREDIT_RATINGS_DATA_RAILZ_RATING_VALUES: Set[CreditRatingsDataRailzRating] = {
    "A",
    "A+",
    "A-",
    "B",
    "B+",
    "B-",
    "C",
    "C+",
    "C-",
    "D",
}


def check_credit_ratings_data_railz_rating(value: str) -> CreditRatingsDataRailzRating:
    if value in CREDIT_RATINGS_DATA_RAILZ_RATING_VALUES:
        return cast(CreditRatingsDataRailzRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_RAILZ_RATING_VALUES!r}")
