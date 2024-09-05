from typing import Literal, Set, cast

SaveDeleteCommunicationResponseV2ServiceName = Literal[
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

SAVE_DELETE_COMMUNICATION_RESPONSE_V2_SERVICE_NAME_VALUES: Set[SaveDeleteCommunicationResponseV2ServiceName] = {
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


def check_save_delete_communication_response_v2_service_name(
    value: str,
) -> SaveDeleteCommunicationResponseV2ServiceName:
    if value in SAVE_DELETE_COMMUNICATION_RESPONSE_V2_SERVICE_NAME_VALUES:
        return cast(SaveDeleteCommunicationResponseV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SAVE_DELETE_COMMUNICATION_RESPONSE_V2_SERVICE_NAME_VALUES!r}"
    )
