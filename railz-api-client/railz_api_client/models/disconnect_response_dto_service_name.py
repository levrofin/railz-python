from typing import Literal, Set, cast

DisconnectResponseDtoServiceName = Literal[
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

DISCONNECT_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[DisconnectResponseDtoServiceName] = {
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


def check_disconnect_response_dto_service_name(value: str) -> DisconnectResponseDtoServiceName:
    if value in DISCONNECT_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(DisconnectResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DISCONNECT_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
