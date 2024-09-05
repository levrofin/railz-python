from typing import Literal, Set, cast

PurchaseOrderStatus = Literal["closed", "draft", "open", "unknown", "void"]

PURCHASE_ORDER_STATUS_VALUES: Set[PurchaseOrderStatus] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_purchase_order_status(value: str) -> PurchaseOrderStatus:
    if value in PURCHASE_ORDER_STATUS_VALUES:
        return cast(PurchaseOrderStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_STATUS_VALUES!r}")
