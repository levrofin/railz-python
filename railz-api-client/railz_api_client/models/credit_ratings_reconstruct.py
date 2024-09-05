from typing import Literal, Set, cast

CreditRatingsReconstruct = Literal["false", "true"]

CREDIT_RATINGS_RECONSTRUCT_VALUES: Set[CreditRatingsReconstruct] = {
    "false",
    "true",
}


def check_credit_ratings_reconstruct(value: str) -> CreditRatingsReconstruct:
    if value in CREDIT_RATINGS_RECONSTRUCT_VALUES:
        return cast(CreditRatingsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_RECONSTRUCT_VALUES!r}")
