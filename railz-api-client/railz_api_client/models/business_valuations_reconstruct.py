from typing import Literal, Set, cast

BusinessValuationsReconstruct = Literal["false", "true"]

BUSINESS_VALUATIONS_RECONSTRUCT_VALUES: Set[BusinessValuationsReconstruct] = {
    "false",
    "true",
}


def check_business_valuations_reconstruct(value: str) -> BusinessValuationsReconstruct:
    if value in BUSINESS_VALUATIONS_RECONSTRUCT_VALUES:
        return cast(BusinessValuationsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_VALUATIONS_RECONSTRUCT_VALUES!r}")
