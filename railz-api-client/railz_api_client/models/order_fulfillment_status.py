from typing import Literal, Set, cast

OrderFulfillmentStatus = Literal["cancelled", "fulfilled", "partial", "unfulfilled", "unknown"]

ORDER_FULFILLMENT_STATUS_VALUES: Set[OrderFulfillmentStatus] = {
    "cancelled",
    "fulfilled",
    "partial",
    "unfulfilled",
    "unknown",
}


def check_order_fulfillment_status(value: str) -> OrderFulfillmentStatus:
    if value in ORDER_FULFILLMENT_STATUS_VALUES:
        return cast(OrderFulfillmentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORDER_FULFILLMENT_STATUS_VALUES!r}")
