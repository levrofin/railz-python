from typing import Literal, Set, cast

UpdateInventoryV2Type = Literal["inventory", "nonInventory", "service"]

UPDATE_INVENTORY_V2_TYPE_VALUES: Set[UpdateInventoryV2Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_update_inventory_v2_type(value: str) -> UpdateInventoryV2Type:
    if value in UPDATE_INVENTORY_V2_TYPE_VALUES:
        return cast(UpdateInventoryV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVENTORY_V2_TYPE_VALUES!r}")
