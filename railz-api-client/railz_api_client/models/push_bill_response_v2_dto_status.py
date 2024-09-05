from typing import Literal, Set, cast

PushBillResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBillResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_response_v2_dto_status(value: str) -> PushBillResponseV2DtoStatus:
    if value in PUSH_BILL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBillResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_RESPONSE_V2_DTO_STATUS_VALUES!r}")
