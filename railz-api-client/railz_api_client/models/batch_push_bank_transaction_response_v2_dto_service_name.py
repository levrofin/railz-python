from typing import Literal, Set, cast

BatchPushBankTransactionResponseV2DtoServiceName = Literal[
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

BATCH_PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[
    BatchPushBankTransactionResponseV2DtoServiceName
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


def check_batch_push_bank_transaction_response_v2_dto_service_name(
    value: str,
) -> BatchPushBankTransactionResponseV2DtoServiceName:
    if value in BATCH_PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(BatchPushBankTransactionResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
