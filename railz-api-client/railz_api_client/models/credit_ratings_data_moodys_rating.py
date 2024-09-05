from typing import Literal, Set, cast

CreditRatingsDataMoodysRating = Literal[
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

CREDIT_RATINGS_DATA_MOODYS_RATING_VALUES: Set[CreditRatingsDataMoodysRating] = {
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


def check_credit_ratings_data_moodys_rating(value: str) -> CreditRatingsDataMoodysRating:
    if value in CREDIT_RATINGS_DATA_MOODYS_RATING_VALUES:
        return cast(CreditRatingsDataMoodysRating, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_DATA_MOODYS_RATING_VALUES!r}")
