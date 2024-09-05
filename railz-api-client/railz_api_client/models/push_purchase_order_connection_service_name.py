from typing import Literal, Set, cast

PushPurchaseOrderConnectionServiceName = Literal["dynamicsBusinessCentral", "oracleNetsuite", "quickbooks", "xero"]

PUSH_PURCHASE_ORDER_CONNECTION_SERVICE_NAME_VALUES: Set[PushPurchaseOrderConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "oracleNetsuite",
    "quickbooks",
    "xero",
}


def check_push_purchase_order_connection_service_name(value: str) -> PushPurchaseOrderConnectionServiceName:
    if value in PUSH_PURCHASE_ORDER_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushPurchaseOrderConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_PURCHASE_ORDER_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
