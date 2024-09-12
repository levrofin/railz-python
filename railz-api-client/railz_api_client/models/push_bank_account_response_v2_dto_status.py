from typing import Literal, Set, cast

PushBankAccountResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBankAccountResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bank_account_response_v2_dto_status(value: str) -> PushBankAccountResponseV2DtoStatus:
    if value in PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBankAccountResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BANK_ACCOUNT_RESPONSE_V2_DTO_STATUS_VALUES!r}")
