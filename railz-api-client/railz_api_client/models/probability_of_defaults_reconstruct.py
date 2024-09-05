from typing import Literal, Set, cast

ProbabilityOfDefaultsReconstruct = Literal["false", "true"]

PROBABILITY_OF_DEFAULTS_RECONSTRUCT_VALUES: Set[ProbabilityOfDefaultsReconstruct] = {
    "false",
    "true",
}


def check_probability_of_defaults_reconstruct(value: str) -> ProbabilityOfDefaultsReconstruct:
    if value in PROBABILITY_OF_DEFAULTS_RECONSTRUCT_VALUES:
        return cast(ProbabilityOfDefaultsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBABILITY_OF_DEFAULTS_RECONSTRUCT_VALUES!r}")
