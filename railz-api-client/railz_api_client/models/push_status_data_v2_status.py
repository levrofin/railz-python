from typing import Literal, Set, cast

PushStatusDataV2Status = Literal["failed", "pending", "success"]

PUSH_STATUS_DATA_V2_STATUS_VALUES: Set[PushStatusDataV2Status] = {
    "failed",
    "pending",
    "success",
}


def check_push_status_data_v2_status(value: str) -> PushStatusDataV2Status:
    if value in PUSH_STATUS_DATA_V2_STATUS_VALUES:
        return cast(PushStatusDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_STATUS_DATA_V2_STATUS_VALUES!r}")
