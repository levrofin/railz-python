from typing import Literal, Set, cast

CreditsReconstruct = Literal["false", "true"]

CREDITS_RECONSTRUCT_VALUES: Set[CreditsReconstruct] = {
    "false",
    "true",
}


def check_credits_reconstruct(value: str) -> CreditsReconstruct:
    if value in CREDITS_RECONSTRUCT_VALUES:
        return cast(CreditsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDITS_RECONSTRUCT_VALUES!r}")
