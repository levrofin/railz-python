from typing import Literal, Set, cast

PushBillPaymentResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_PAYMENT_RESPONSE_DTO_STATUS_VALUES: Set[PushBillPaymentResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_payment_response_dto_status(value: str) -> PushBillPaymentResponseDtoStatus:
    if value in PUSH_BILL_PAYMENT_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushBillPaymentResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_PAYMENT_RESPONSE_DTO_STATUS_VALUES!r}")
