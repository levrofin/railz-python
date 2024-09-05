from typing import Literal, Set, cast

UpdateInventoryV1ResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES: Set[UpdateInventoryV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_inventory_v1_response_dto_status(value: str) -> UpdateInventoryV1ResponseDtoStatus:
    if value in UPDATE_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateInventoryV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V1_RESPONSE_DTO_STATUS_VALUES!r}")
