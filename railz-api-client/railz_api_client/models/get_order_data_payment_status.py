from typing import Literal, Set, cast

GetOrderDataPaymentStatus = Literal["approved", "cancelled", "failed", "paid", "pending", "refunded", "unknown"]

GET_ORDER_DATA_PAYMENT_STATUS_VALUES: Set[GetOrderDataPaymentStatus] = {
    "approved",
    "cancelled",
    "failed",
    "paid",
    "pending",
    "refunded",
    "unknown",
}


def check_get_order_data_payment_status(value: str) -> GetOrderDataPaymentStatus:
    if value in GET_ORDER_DATA_PAYMENT_STATUS_VALUES:
        return cast(GetOrderDataPaymentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ORDER_DATA_PAYMENT_STATUS_VALUES!r}")
