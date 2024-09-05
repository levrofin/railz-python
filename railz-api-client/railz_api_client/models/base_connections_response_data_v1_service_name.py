from typing import Literal, Set, cast

BaseConnectionsResponseDataV1ServiceName = Literal[
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

BASE_CONNECTIONS_RESPONSE_DATA_V1_SERVICE_NAME_VALUES: Set[BaseConnectionsResponseDataV1ServiceName] = {
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


def check_base_connections_response_data_v1_service_name(value: str) -> BaseConnectionsResponseDataV1ServiceName:
    if value in BASE_CONNECTIONS_RESPONSE_DATA_V1_SERVICE_NAME_VALUES:
        return cast(BaseConnectionsResponseDataV1ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASE_CONNECTIONS_RESPONSE_DATA_V1_SERVICE_NAME_VALUES!r}"
    )
