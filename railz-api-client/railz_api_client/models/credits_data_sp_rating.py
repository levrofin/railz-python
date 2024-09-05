from typing import Literal, Set, cast

CreditsDataSpRating = Literal[
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

CREDITS_DATA_SP_RATING_VALUES: Set[CreditsDataSpRating] = {
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


def check_credits_data_sp_rating(value: str) -> CreditsDataSpRating:
    if value in CREDITS_DATA_SP_RATING_VALUES:
        return cast(CreditsDataSpRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_SP_RATING_VALUES!r}")
