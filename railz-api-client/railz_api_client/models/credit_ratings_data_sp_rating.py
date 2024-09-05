from typing import Literal, Set, cast

CreditRatingsDataSpRating = Literal[
    "A",
    "A+",
    "A-",
    "AA",
    "AA+",
    "AA-",
    "AAA",
    "B",
    "B+",
    "B-",
    "BB",
    "BB+",
    "BB-",
    "BBB",
    "BBB+",
    "BBB-",
    "C",
    "CC",
    "CCC",
    "CCC+",
    "CCC-",
    "D",
]

CREDIT_RATINGS_DATA_SP_RATING_VALUES: Set[CreditRatingsDataSpRating] = {
    "A",
    "A+",
    "A-",
    "AA",
    "AA+",
    "AA-",
    "AAA",
    "B",
    "B+",
    "B-",
    "BB",
    "BB+",
    "BB-",
    "BBB",
    "BBB+",
    "BBB-",
    "C",
    "CC",
    "CCC",
    "CCC+",
    "CCC-",
    "D",
}


def check_credit_ratings_data_sp_rating(value: str) -> CreditRatingsDataSpRating:
    if value in CREDIT_RATINGS_DATA_SP_RATING_VALUES:
        return cast(CreditRatingsDataSpRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_SP_RATING_VALUES!r}")
