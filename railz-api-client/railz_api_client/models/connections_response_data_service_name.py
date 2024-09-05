from typing import Literal, Set, cast

ConnectionsResponseDataServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

CONNECTIONS_RESPONSE_DATA_SERVICE_NAME_VALUES: Set[ConnectionsResponseDataServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_connections_response_data_service_name(value: str) -> ConnectionsResponseDataServiceName:
    if value in CONNECTIONS_RESPONSE_DATA_SERVICE_NAME_VALUES:
        return cast(ConnectionsResponseDataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTIONS_RESPONSE_DATA_SERVICE_NAME_VALUES!r}")
