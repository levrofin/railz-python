from typing import Literal, Set, cast

CreditsDataFitchRating = Literal[
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

CREDITS_DATA_FITCH_RATING_VALUES: Set[CreditsDataFitchRating] = {
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


def check_credits_data_fitch_rating(value: str) -> CreditsDataFitchRating:
    if value in CREDITS_DATA_FITCH_RATING_VALUES:
        return cast(CreditsDataFitchRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_FITCH_RATING_VALUES!r}")
