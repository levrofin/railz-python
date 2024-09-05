from typing import Literal, Set, cast

CreditsDataMoodysRating = Literal[
    "A1",
    "A2",
    "A3",
    "Aa1",
    "Aa2",
    "Aa3",
    "Aaa",
    "B1",
    "B2",
    "B3",
    "Ba1",
    "Ba2",
    "Ba3",
    "Baa1",
    "Baa2",
    "Baa3",
    "C",
    "Ca",
    "Caa1",
    "Caa2",
]

CREDITS_DATA_MOODYS_RATING_VALUES: Set[CreditsDataMoodysRating] = {
    "A1",
    "A2",
    "A3",
    "Aa1",
    "Aa2",
    "Aa3",
    "Aaa",
    "B1",
    "B2",
    "B3",
    "Ba1",
    "Ba2",
    "Ba3",
    "Baa1",
    "Baa2",
    "Baa3",
    "C",
    "Ca",
    "Caa1",
    "Caa2",
}


def check_credits_data_moodys_rating(value: str) -> CreditsDataMoodysRating:
    if value in CREDITS_DATA_MOODYS_RATING_VALUES:
        return cast(CreditsDataMoodysRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_DATA_MOODYS_RATING_VALUES!r}")
