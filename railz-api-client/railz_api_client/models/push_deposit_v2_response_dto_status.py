from typing import Literal, Set, cast

PushDepositV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_DEPOSIT_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushDepositV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_deposit_v2_response_dto_status(value: str) -> PushDepositV2ResponseDtoStatus:
    if value in PUSH_DEPOSIT_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushDepositV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_V2_RESPONSE_DTO_STATUS_VALUES!r}")
