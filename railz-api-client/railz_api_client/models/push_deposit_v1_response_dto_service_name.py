from typing import Literal, Set, cast

PushDepositV1ResponseDtoServiceName = Literal[
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

PUSH_DEPOSIT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushDepositV1ResponseDtoServiceName] = {
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


def check_push_deposit_v1_response_dto_service_name(value: str) -> PushDepositV1ResponseDtoServiceName:
    if value in PUSH_DEPOSIT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushDepositV1ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
