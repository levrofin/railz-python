from typing import Literal, Set, cast

UpdateInventoryV2ResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES: Set[UpdateInventoryV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_inventory_v2_response_dto_status(value: str) -> UpdateInventoryV2ResponseDtoStatus:
    if value in UPDATE_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateInventoryV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V2_RESPONSE_DTO_STATUS_VALUES!r}")
