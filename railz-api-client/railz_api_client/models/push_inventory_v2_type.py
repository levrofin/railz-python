from typing import Literal, Set, cast

PushInventoryV2Type = Literal["inventory", "nonInventory", "service"]

PUSH_INVENTORY_V2_TYPE_VALUES: Set[PushInventoryV2Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_push_inventory_v2_type(value: str) -> PushInventoryV2Type:
    if value in PUSH_INVENTORY_V2_TYPE_VALUES:
        return cast(PushInventoryV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V2_TYPE_VALUES!r}")
