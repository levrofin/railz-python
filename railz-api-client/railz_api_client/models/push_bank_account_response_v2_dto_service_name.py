from typing import Literal, Set, cast

PushBankAccountResponseV2DtoServiceName = Literal[
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

PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBankAccountResponseV2DtoServiceName] = {
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


def check_push_bank_account_response_v2_dto_service_name(value: str) -> PushBankAccountResponseV2DtoServiceName:
    if value in PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBankAccountResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
