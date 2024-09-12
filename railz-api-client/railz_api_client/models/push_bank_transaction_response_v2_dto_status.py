from typing import Literal, Set, cast

PushBankTransactionResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBankTransactionResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bank_transaction_response_v2_dto_status(value: str) -> PushBankTransactionResponseV2DtoStatus:
    if value in PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBankTransactionResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
