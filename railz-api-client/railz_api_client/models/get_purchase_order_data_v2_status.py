from typing import Literal, Set, cast

GetPurchaseOrderDataV2Status = Literal["closed", "draft", "open", "unknown", "void"]

GET_PURCHASE_ORDER_DATA_V2_STATUS_VALUES: Set[GetPurchaseOrderDataV2Status] = {
    "closed",
    "draft",
    "open",
    "unknown",
    "void",
}


def check_get_purchase_order_data_v2_status(value: str) -> GetPurchaseOrderDataV2Status:
    if value in GET_PURCHASE_ORDER_DATA_V2_STATUS_VALUES:
        return cast(GetPurchaseOrderDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PURCHASE_ORDER_DATA_V2_STATUS_VALUES!r}")
