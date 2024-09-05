from typing import Literal, Set, cast

UpdateInventoryV1Type = Literal["inventory", "nonInventory", "service"]

UPDATE_INVENTORY_V1_TYPE_VALUES: Set[UpdateInventoryV1Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_update_inventory_v1_type(value: str) -> UpdateInventoryV1Type:
    if value in UPDATE_INVENTORY_V1_TYPE_VALUES:
        return cast(UpdateInventoryV1Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V1_TYPE_VALUES!r}")
