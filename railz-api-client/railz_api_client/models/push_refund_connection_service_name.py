from typing import Literal, Set, cast

PushRefundConnectionServiceName = Literal["quickbooks", "xero"]

PUSH_REFUND_CONNECTION_SERVICE_NAME_VALUES: Set[PushRefundConnectionServiceName] = {
    "quickbooks",
    "xero",
}


def check_push_refund_connection_service_name(value: str) -> PushRefundConnectionServiceName:
    if value in PUSH_REFUND_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushRefundConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_REFUND_CONNECTION_SERVICE_NAME_VALUES!r}")
