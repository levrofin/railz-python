from typing import Literal, Set, cast

PushInvoicePaymentResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES: Set[PushInvoicePaymentResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_payment_response_dto_status(value: str) -> PushInvoicePaymentResponseDtoStatus:
    if value in PUSH_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInvoicePaymentResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES!r}")
