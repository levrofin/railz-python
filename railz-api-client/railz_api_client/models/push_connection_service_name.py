from typing import Literal, Set, cast

PushConnectionServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_CONNECTION_SERVICE_NAME_VALUES: Set[PushConnectionServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "plaid",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "shopify",
    "square",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_connection_service_name(value: str) -> PushConnectionServiceName:
    if value in PUSH_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CONNECTION_SERVICE_NAME_VALUES!r}")
