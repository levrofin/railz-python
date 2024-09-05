from typing import Literal, Set, cast

PushRefundResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_REFUND_RESPONSE_DTO_STATUS_VALUES: Set[PushRefundResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_refund_response_dto_status(value: str) -> PushRefundResponseDtoStatus:
    if value in PUSH_REFUND_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushRefundResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_REFUND_RESPONSE_DTO_STATUS_VALUES!r}")
