from typing import Literal, Set, cast

PushDepositV2ResponseDtoServiceName = Literal[
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

PUSH_DEPOSIT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushDepositV2ResponseDtoServiceName] = {
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


def check_push_deposit_v2_response_dto_service_name(value: str) -> PushDepositV2ResponseDtoServiceName:
    if value in PUSH_DEPOSIT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushDepositV2ResponseDtoServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}")
