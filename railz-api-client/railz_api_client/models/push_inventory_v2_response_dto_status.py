from typing import Literal, Set, cast

PushInventoryV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushInventoryV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_inventory_v2_response_dto_status(value: str) -> PushInventoryV2ResponseDtoStatus:
    if value in PUSH_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInventoryV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES!r}")
