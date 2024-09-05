from typing import Literal, Set, cast

PushBankTransactionResponseDtoServiceName = Literal[
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

PUSH_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushBankTransactionResponseDtoServiceName] = {
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


def check_push_bank_transaction_response_dto_service_name(value: str) -> PushBankTransactionResponseDtoServiceName:
    if value in PUSH_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushBankTransactionResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
