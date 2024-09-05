from typing import Literal, Set, cast

PushBankTransfersResponseV2DtoServiceName = Literal[
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

PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES: Set[PushBankTransfersResponseV2DtoServiceName] = {
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


def check_push_bank_transfers_response_v2_dto_service_name(value: str) -> PushBankTransfersResponseV2DtoServiceName:
    if value in PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES:
        return cast(PushBankTransfersResponseV2DtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_SERVICE_NAME_VALUES!r}"
    )
