from typing import Literal, Set, cast

GetInventoryDataV1Type = Literal["inventory", "nonInventory", "service"]

GET_INVENTORY_DATA_V1_TYPE_VALUES: Set[GetInventoryDataV1Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_get_inventory_data_v1_type(value: str) -> GetInventoryDataV1Type:
    if value in GET_INVENTORY_DATA_V1_TYPE_VALUES:
        return cast(GetInventoryDataV1Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVENTORY_DATA_V1_TYPE_VALUES!r}")
