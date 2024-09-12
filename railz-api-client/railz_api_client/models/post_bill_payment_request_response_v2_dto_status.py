from typing import Literal, Set, cast

PostBillPaymentRequestResponseV2DtoStatus = Literal["failed", "pending", "success"]

POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_STATUS_VALUES: Set[PostBillPaymentRequestResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_post_bill_payment_request_response_v2_dto_status(value: str) -> PostBillPaymentRequestResponseV2DtoStatus:
    if value in POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PostBillPaymentRequestResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_BILL_PAYMENT_REQUEST_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
