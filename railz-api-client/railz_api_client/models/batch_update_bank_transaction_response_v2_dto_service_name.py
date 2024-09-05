from typing import Literal, Set, cast

BatchUpdateBankTransactionResponseV2DtoServiceName = Literal[
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

BATCH_UPDATE_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[
    BatchUpdateBankTransactionResponseV2DtoServiceName
] = {
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


def check_batch_update_bank_transaction_response_v2_dto_service_name(
    value: str,
) -> BatchUpdateBankTransactionResponseV2DtoServiceName:
    if value in BATCH_UPDATE_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(BatchUpdateBankTransactionResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
