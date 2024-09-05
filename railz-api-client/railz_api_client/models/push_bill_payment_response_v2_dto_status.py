from typing import Literal, Set, cast

PushBillPaymentResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushBillPaymentResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_bill_payment_response_v2_dto_status(value: str) -> PushBillPaymentResponseV2DtoStatus:
    if value in PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBillPaymentResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES!r}")
