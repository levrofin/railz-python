from typing import Literal, Set, cast

PushInventoryV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushInventoryV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_inventory_v1_response_dto_status(value: str) -> PushInventoryV1ResponseDtoStatus:
    if value in PUSH_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInventoryV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES!r}")
