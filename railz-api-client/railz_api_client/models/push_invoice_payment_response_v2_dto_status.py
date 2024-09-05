from typing import Literal, Set, cast

PushInvoicePaymentResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushInvoicePaymentResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_payment_response_v2_dto_status(value: str) -> PushInvoicePaymentResponseV2DtoStatus:
    if value in PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushInvoicePaymentResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_PAYMENT_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
