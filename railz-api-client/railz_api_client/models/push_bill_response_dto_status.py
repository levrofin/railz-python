from typing import Literal, Set, cast

PushBillResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_RESPONSE_DTO_STATUS_VALUES: Set[PushBillResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_response_dto_status(value: str) -> PushBillResponseDtoStatus:
    if value in PUSH_BILL_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushBillResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_RESPONSE_DTO_STATUS_VALUES!r}")
