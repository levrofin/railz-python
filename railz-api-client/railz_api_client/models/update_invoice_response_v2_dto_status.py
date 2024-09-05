from typing import Literal, Set, cast

UpdateInvoiceResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES: Set[UpdateInvoiceResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_invoice_response_v2_dto_status(value: str) -> UpdateInvoiceResponseV2DtoStatus:
    if value in UPDATE_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateInvoiceResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INVOICE_RESPONSE_V2_DTO_STATUS_VALUES!r}")
