from typing import Literal, Set, cast

GetInventoryDataV2Type = Literal["inventory", "nonInventory", "service"]

GET_INVENTORY_DATA_V2_TYPE_VALUES: Set[GetInventoryDataV2Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_get_inventory_data_v2_type(value: str) -> GetInventoryDataV2Type:
    if value in GET_INVENTORY_DATA_V2_TYPE_VALUES:
        return cast(GetInventoryDataV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVENTORY_DATA_V2_TYPE_VALUES!r}")
