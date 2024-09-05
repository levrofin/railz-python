from typing import Literal, Set, cast

PushRefundResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_REFUND_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushRefundResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_refund_response_v2_dto_status(value: str) -> PushRefundResponseV2DtoStatus:
    if value in PUSH_REFUND_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushRefundResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_REFUND_RESPONSE_V2_DTO_STATUS_VALUES!r}")
