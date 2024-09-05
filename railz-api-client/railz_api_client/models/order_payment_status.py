from typing import Literal, Set, cast

OrderPaymentStatus = Literal["approved", "cancelled", "failed", "paid", "pending", "refunded", "unknown"]

ORDER_PAYMENT_STATUS_VALUES: Set[OrderPaymentStatus] = {
    "approved",
    "cancelled",
    "failed",
    "paid",
    "pending",
    "refunded",
    "unknown",
}


def check_order_payment_status(value: str) -> OrderPaymentStatus:
    if value in ORDER_PAYMENT_STATUS_VALUES:
        return cast(OrderPaymentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORDER_PAYMENT_STATUS_VALUES!r}")
