from typing import Literal, Set, cast

CreditsDataRailzRating = Literal["A", "A+", "A-", "B", "B+", "B-", "C", "C+", "C-", "D"]

CREDITS_DATA_RAILZ_RATING_VALUES: Set[CreditsDataRailzRating] = {
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


def check_credits_data_railz_rating(value: str) -> CreditsDataRailzRating:
    if value in CREDITS_DATA_RAILZ_RATING_VALUES:
        return cast(CreditsDataRailzRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_RAILZ_RATING_VALUES!r}")
