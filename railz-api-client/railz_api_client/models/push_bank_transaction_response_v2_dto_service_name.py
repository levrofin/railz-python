from typing import Literal, Set, cast

PushBankTransactionResponseV2DtoServiceName = Literal[
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

PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBankTransactionResponseV2DtoServiceName] = {
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


def check_push_bank_transaction_response_v2_dto_service_name(value: str) -> PushBankTransactionResponseV2DtoServiceName:
    if value in PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBankTransactionResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
