from typing import Literal, Set, cast

CreditRatingsDataDbrsRating = Literal[
    "A",
    "A (high)",
    "A (low)",
    "AA",
    "AA (high)",
    "AA (low)",
    "AAA",
    "BB",
    "BB (high)",
    "BB (low)",
    "BBB",
    "BBB (high)",
    "BBB (low)",
    "C",
    "CC",
    "CCC",
    "CCC (high)",
    "CCC (low)",
    "D",
]

CREDIT_RATINGS_DATA_DBRS_RATING_VALUES: Set[CreditRatingsDataDbrsRating] = {
    "A",
    "A (high)",
    "A (low)",
    "AA",
    "AA (high)",
    "AA (low)",
    "AAA",
    "BB",
    "BB (high)",
    "BB (low)",
    "BBB",
    "BBB (high)",
    "BBB (low)",
    "C",
    "CC",
    "CCC",
    "CCC (high)",
    "CCC (low)",
    "D",
}


def check_credit_ratings_data_dbrs_rating(value: str) -> CreditRatingsDataDbrsRating:
    if value in CREDIT_RATINGS_DATA_DBRS_RATING_VALUES:
        return cast(CreditRatingsDataDbrsRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_DBRS_RATING_VALUES!r}")
