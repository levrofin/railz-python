from typing import Literal, Set, cast

CreditRatingsDataFitchRating = Literal[
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
    "CCC",
    "D",
    "DD",
    "DDD",
]

CREDIT_RATINGS_DATA_FITCH_RATING_VALUES: Set[CreditRatingsDataFitchRating] = {
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
    "CCC",
    "D",
    "DD",
    "DDD",
}


def check_credit_ratings_data_fitch_rating(value: str) -> CreditRatingsDataFitchRating:
    if value in CREDIT_RATINGS_DATA_FITCH_RATING_VALUES:
        return cast(CreditRatingsDataFitchRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_FITCH_RATING_VALUES!r}")
