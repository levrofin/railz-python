from typing import Literal, Set, cast

GetPurchaseOrderDataV1Status = Literal["closed", "draft", "open", "unknown", "void"]

GET_PURCHASE_ORDER_DATA_V1_STATUS_VALUES: Set[GetPurchaseOrderDataV1Status] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_get_purchase_order_data_v1_status(value: str) -> GetPurchaseOrderDataV1Status:
    if value in GET_PURCHASE_ORDER_DATA_V1_STATUS_VALUES:
        return cast(GetPurchaseOrderDataV1Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PURCHASE_ORDER_DATA_V1_STATUS_VALUES!r}")
