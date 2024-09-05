from typing import Literal, Set, cast

PushBankTransfersResponseDtoServiceName = Literal[
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

PUSH_BANK_TRANSFERS_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushBankTransfersResponseDtoServiceName] = {
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


def check_push_bank_transfers_response_dto_service_name(value: str) -> PushBankTransfersResponseDtoServiceName:
    if value in PUSH_BANK_TRANSFERS_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushBankTransfersResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSFERS_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
