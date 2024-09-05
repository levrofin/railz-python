from typing import Literal, Set, cast

PushDepositV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_DEPOSIT_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushDepositV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_deposit_v1_response_dto_status(value: str) -> PushDepositV1ResponseDtoStatus:
    if value in PUSH_DEPOSIT_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushDepositV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_V1_RESPONSE_DTO_STATUS_VALUES!r}")
