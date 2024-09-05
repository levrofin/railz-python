from typing import Literal, Set, cast

PushStatusDataV2ServiceName = Literal[
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

PUSH_STATUS_DATA_V2_SERVICE_NAME_VALUES: Set[PushStatusDataV2ServiceName] = {
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


def check_push_status_data_v2_service_name(value: str) -> PushStatusDataV2ServiceName:
    if value in PUSH_STATUS_DATA_V2_SERVICE_NAME_VALUES:
        return cast(PushStatusDataV2ServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_STATUS_DATA_V2_SERVICE_NAME_VALUES!r}")
