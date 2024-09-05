from typing import Literal, Set, cast

ConnectionsServiceName = Literal[
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

CONNECTIONS_SERVICE_NAME_VALUES: Set[ConnectionsServiceName] = {
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


def check_connections_service_name(value: str) -> ConnectionsServiceName:
    if value in CONNECTIONS_SERVICE_NAME_VALUES:
        return cast(ConnectionsServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTIONS_SERVICE_NAME_VALUES!r}")
