from typing import Literal, Set, cast

BaseConnectionsResponseDataV2ServiceName = Literal[
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

BASE_CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES: Set[BaseConnectionsResponseDataV2ServiceName] = {
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


def check_base_connections_response_data_v2_service_name(value: str) -> BaseConnectionsResponseDataV2ServiceName:
    if value in BASE_CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES:
        return cast(BaseConnectionsResponseDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASE_CONNECTIONS_RESPONSE_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
