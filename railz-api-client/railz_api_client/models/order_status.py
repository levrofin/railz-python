from typing import Literal, Set, cast

OrderStatus = Literal["cancelled", "closed", "draft", "open", "unknown"]

ORDER_STATUS_VALUES: Set[OrderStatus] = {
    "cancelled",
    "closed",
    "draft",
    "open",
    "unknown",
}


def check_order_status(value: str) -> OrderStatus:
    if value in ORDER_STATUS_VALUES:
        return cast(OrderStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORDER_STATUS_VALUES!r}")
