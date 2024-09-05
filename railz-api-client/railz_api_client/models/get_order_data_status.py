from typing import Literal, Set, cast

GetOrderDataStatus = Literal["cancelled", "closed", "draft", "open", "unknown"]

GET_ORDER_DATA_STATUS_VALUES: Set[GetOrderDataStatus] = {
    "cancelled",
    "closed",
    "draft",
    "open",
    "unknown",
}


def check_get_order_data_status(value: str) -> GetOrderDataStatus:
    if value in GET_ORDER_DATA_STATUS_VALUES:
        return cast(GetOrderDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ORDER_DATA_STATUS_VALUES!r}")
