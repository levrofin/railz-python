from typing import Literal, Set, cast

PushBankTransfersResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBankTransfersResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bank_transfers_response_v2_dto_status(value: str) -> PushBankTransfersResponseV2DtoStatus:
    if value in PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBankTransfersResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSFERS_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
