from typing import Literal, Set, cast

PushInvoiceResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_RESPONSE_DTO_STATUS_VALUES: Set[PushInvoiceResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_response_dto_status(value: str) -> PushInvoiceResponseDtoStatus:
    if value in PUSH_INVOICE_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushInvoiceResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_RESPONSE_DTO_STATUS_VALUES!r}")
