from typing import Literal, Set, cast

PushBankTransfersResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_BANK_TRANSFERS_RESPONSE_DTO_STATUS_VALUES: Set[PushBankTransfersResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bank_transfers_response_dto_status(value: str) -> PushBankTransfersResponseDtoStatus:
    if value in PUSH_BANK_TRANSFERS_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushBankTransfersResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSFERS_RESPONSE_DTO_STATUS_VALUES!r}")
