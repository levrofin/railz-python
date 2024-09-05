from typing import Literal, Set, cast

PushUpdateBillsConnectionServiceName = Literal["quickbooks", "sageBusinessCloud", "sageIntacct", "xero"]

PUSH_UPDATE_BILLS_CONNECTION_SERVICE_NAME_VALUES: Set[PushUpdateBillsConnectionServiceName] = {
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "xero",
}


def check_push_update_bills_connection_service_name(value: str) -> PushUpdateBillsConnectionServiceName:
    if value in PUSH_UPDATE_BILLS_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushUpdateBillsConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_BILLS_CONNECTION_SERVICE_NAME_VALUES!r}")
