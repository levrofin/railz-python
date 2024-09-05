from typing import Literal, Set, cast

PushInvoiceResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushInvoiceResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_invoice_response_v2_dto_status(value: str) -> PushInvoiceResponseV2DtoStatus:
    if value in PUSH_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushInvoiceResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES!r}")
