from typing import Literal, Set, cast

PushUpdateCustomerConnectionServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
]

PUSH_UPDATE_CUSTOMER_CONNECTION_SERVICE_NAME_VALUES: Set[PushUpdateCustomerConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
}


def check_push_update_customer_connection_service_name(value: str) -> PushUpdateCustomerConnectionServiceName:
    if value in PUSH_UPDATE_CUSTOMER_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushUpdateCustomerConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_CUSTOMER_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
