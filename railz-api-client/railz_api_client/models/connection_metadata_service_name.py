from typing import Literal, Set, cast

ConnectionMetadataServiceName = Literal[
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

CONNECTION_METADATA_SERVICE_NAME_VALUES: Set[ConnectionMetadataServiceName] = {
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


def check_connection_metadata_service_name(value: str) -> ConnectionMetadataServiceName:
    if value in CONNECTION_METADATA_SERVICE_NAME_VALUES:
        return cast(ConnectionMetadataServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTION_METADATA_SERVICE_NAME_VALUES!r}")
