from typing import Literal, Set, cast

PushUpdateVendorConnectionServiceName = Literal[
    "dynamicsBusinessCentral", "freshbooks", "oracleNetsuite", "quickbooks", "sageBusinessCloud", "sageIntacct", "xero"
]

PUSH_UPDATE_VENDOR_CONNECTION_SERVICE_NAME_VALUES: Set[PushUpdateVendorConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "xero",
}


def check_push_update_vendor_connection_service_name(value: str) -> PushUpdateVendorConnectionServiceName:
    if value in PUSH_UPDATE_VENDOR_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushUpdateVendorConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_VENDOR_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
