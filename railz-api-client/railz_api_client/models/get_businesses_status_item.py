from typing import Literal, Set, cast

GetBusinessesStatusItem = Literal["active", "inactive", "new"]

GET_BUSINESSES_STATUS_ITEM_VALUES: Set[GetBusinessesStatusItem] = {
    "active",
    "inactive",
    "new",
}


def check_get_businesses_status_item(value: str) -> GetBusinessesStatusItem:
    if value in GET_BUSINESSES_STATUS_ITEM_VALUES:
        return cast(GetBusinessesStatusItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BUSINESSES_STATUS_ITEM_VALUES!r}")
