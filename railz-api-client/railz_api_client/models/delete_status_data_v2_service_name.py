from typing import Literal, Set, cast

DeleteStatusDataV2ServiceName = Literal[
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

DELETE_STATUS_DATA_V2_SERVICE_NAME_VALUES: Set[DeleteStatusDataV2ServiceName] = {
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


def check_delete_status_data_v2_service_name(value: str) -> DeleteStatusDataV2ServiceName:
    if value in DELETE_STATUS_DATA_V2_SERVICE_NAME_VALUES:
        return cast(DeleteStatusDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_STATUS_DATA_V2_SERVICE_NAME_VALUES!r}")
