from typing import Literal, Set, cast

GetInventoryDataV1ItemStatus = Literal["active", "archived", "unknown"]

GET_INVENTORY_DATA_V1_ITEM_STATUS_VALUES: Set[GetInventoryDataV1ItemStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_inventory_data_v1_item_status(value: str) -> GetInventoryDataV1ItemStatus:
    if value in GET_INVENTORY_DATA_V1_ITEM_STATUS_VALUES:
        return cast(GetInventoryDataV1ItemStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVENTORY_DATA_V1_ITEM_STATUS_VALUES!r}")
