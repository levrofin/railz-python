from typing import Literal, Set, cast

UpdateBillPaymentResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES: Set[UpdateBillPaymentResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_bill_payment_response_v2_dto_status(value: str) -> UpdateBillPaymentResponseV2DtoStatus:
    if value in UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateBillPaymentResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
