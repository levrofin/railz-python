from typing import Literal, Set, cast

CreditScoresReconstruct = Literal["false", "true"]

CREDIT_SCORES_RECONSTRUCT_VALUES: Set[CreditScoresReconstruct] = {
    "false",
    "true",
}


def check_credit_scores_reconstruct(value: str) -> CreditScoresReconstruct:
    if value in CREDIT_SCORES_RECONSTRUCT_VALUES:
        return cast(CreditScoresReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_SCORES_RECONSTRUCT_VALUES!r}")
