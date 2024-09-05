from typing import Literal, Set, cast

ConnectionsResponseDataV2ServiceName = Literal[
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

CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES: Set[ConnectionsResponseDataV2ServiceName] = {
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


def check_connections_response_data_v2_service_name(value: str) -> ConnectionsResponseDataV2ServiceName:
    if value in CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES:
        return cast(ConnectionsResponseDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES!r}")
