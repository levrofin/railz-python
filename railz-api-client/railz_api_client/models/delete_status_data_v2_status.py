from typing import Literal, Set, cast

DeleteStatusDataV2Status = Literal["failed", "pending", "success"]

DELETE_STATUS_DATA_V2_STATUS_VALUES: Set[DeleteStatusDataV2Status] = {
    "failed",
    "pending",
    "success",
}


def check_delete_status_data_v2_status(value: str) -> DeleteStatusDataV2Status:
    if value in DELETE_STATUS_DATA_V2_STATUS_VALUES:
        return cast(DeleteStatusDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_STATUS_DATA_V2_STATUS_VALUES!r}")
