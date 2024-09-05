from typing import Literal, Set, cast

PushStatusDataV1Status = Literal["failed", "pending", "success"]

PUSH_STATUS_DATA_V1_STATUS_VALUES: Set[PushStatusDataV1Status] = {
    "failed",
    "pending",
    "success",
}


def check_push_status_data_v1_status(value: str) -> PushStatusDataV1Status:
    if value in PUSH_STATUS_DATA_V1_STATUS_VALUES:
        return cast(PushStatusDataV1Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_STATUS_DATA_V1_STATUS_VALUES!r}")
