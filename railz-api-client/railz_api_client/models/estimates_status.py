from typing import Literal, Set, cast

EstimatesStatus = Literal["closed", "draft", "open", "unknown", "void"]

ESTIMATES_STATUS_VALUES: Set[EstimatesStatus] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_estimates_status(value: str) -> EstimatesStatus:
    if value in ESTIMATES_STATUS_VALUES:
        return cast(EstimatesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESTIMATES_STATUS_VALUES!r}")
