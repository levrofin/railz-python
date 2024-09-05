from typing import Literal, Set, cast

PushStatusDataV1ServiceName = Literal[
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

PUSH_STATUS_DATA_V1_SERVICE_NAME_VALUES: Set[PushStatusDataV1ServiceName] = {
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


def check_push_status_data_v1_service_name(value: str) -> PushStatusDataV1ServiceName:
    if value in PUSH_STATUS_DATA_V1_SERVICE_NAME_VALUES:
        return cast(PushStatusDataV1ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_STATUS_DATA_V1_SERVICE_NAME_VALUES!r}")
