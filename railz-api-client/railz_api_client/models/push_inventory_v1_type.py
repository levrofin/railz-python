from typing import Literal, Set, cast

PushInventoryV1Type = Literal["inventory", "nonInventory", "service"]

PUSH_INVENTORY_V1_TYPE_VALUES: Set[PushInventoryV1Type] = {
    "inventory",
    "nonInventory",
    "service",
}


def check_push_inventory_v1_type(value: str) -> PushInventoryV1Type:
    if value in PUSH_INVENTORY_V1_TYPE_VALUES:
        return cast(PushInventoryV1Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVENTORY_V1_TYPE_VALUES!r}")
