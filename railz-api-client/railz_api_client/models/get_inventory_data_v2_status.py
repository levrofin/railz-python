from typing import Literal, Set, cast

GetInventoryDataV2Status = Literal["active", "archived", "unknown"]

GET_INVENTORY_DATA_V2_STATUS_VALUES: Set[GetInventoryDataV2Status] = {
    "active",
    "archived",
    "unknown",
}


def check_get_inventory_data_v2_status(value: str) -> GetInventoryDataV2Status:
    if value in GET_INVENTORY_DATA_V2_STATUS_VALUES:
        return cast(GetInventoryDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVENTORY_DATA_V2_STATUS_VALUES!r}")
