from typing import Literal, Set, cast

UpdateBankTransactionResponseDtoServiceName = Literal[
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

UPDATE_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[UpdateBankTransactionResponseDtoServiceName] = {
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


def check_update_bank_transaction_response_dto_service_name(value: str) -> UpdateBankTransactionResponseDtoServiceName:
    if value in UPDATE_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(UpdateBankTransactionResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BANK_TRANSACTION_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
