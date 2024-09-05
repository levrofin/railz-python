from typing import Literal, Set, cast

UpdateInvoicePaymentResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES: Set[UpdateInvoicePaymentResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_invoice_payment_response_dto_status(value: str) -> UpdateInvoicePaymentResponseDtoStatus:
    if value in UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateInvoicePaymentResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INVOICE_PAYMENT_RESPONSE_DTO_STATUS_VALUES!r}"
    )
