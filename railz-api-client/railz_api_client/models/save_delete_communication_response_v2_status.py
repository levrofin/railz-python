from typing import Literal, Set, cast

SaveDeleteCommunicationResponseV2Status = Literal["failed", "pending", "success"]

SAVE_DELETE_COMMUNICATION_RESPONSE_V2_STATUS_VALUES: Set[SaveDeleteCommunicationResponseV2Status] = {
    "failed",
    "pending",
    "success",
}


def check_save_delete_communication_response_v2_status(value: str) -> SaveDeleteCommunicationResponseV2Status:
    if value in SAVE_DELETE_COMMUNICATION_RESPONSE_V2_STATUS_VALUES:
        return cast(SaveDeleteCommunicationResponseV2Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SAVE_DELETE_COMMUNICATION_RESPONSE_V2_STATUS_VALUES!r}"
    )
