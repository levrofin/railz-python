from typing import Literal, Set, cast

GetOrderDataFulfillmentStatus = Literal["cancelled", "fulfilled", "partial", "unfulfilled", "unknown"]

GET_ORDER_DATA_FULFILLMENT_STATUS_VALUES: Set[GetOrderDataFulfillmentStatus] = {
    "cancelled",
    "fulfilled",
    "partial",
    "unfulfilled",
    "unknown",
}


def check_get_order_data_fulfillment_status(value: str) -> GetOrderDataFulfillmentStatus:
    if value in GET_ORDER_DATA_FULFILLMENT_STATUS_VALUES:
        return cast(GetOrderDataFulfillmentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ORDER_DATA_FULFILLMENT_STATUS_VALUES!r}")
