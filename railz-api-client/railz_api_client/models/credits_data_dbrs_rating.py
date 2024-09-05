from typing import Literal, Set, cast

CreditsDataDbrsRating = Literal[
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

CREDITS_DATA_DBRS_RATING_VALUES: Set[CreditsDataDbrsRating] = {
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


def check_credits_data_dbrs_rating(value: str) -> CreditsDataDbrsRating:
    if value in CREDITS_DATA_DBRS_RATING_VALUES:
        return cast(CreditsDataDbrsRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_DBRS_RATING_VALUES!r}")
