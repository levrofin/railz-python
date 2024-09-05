from typing import Literal, Set, cast

GetInvoiceV2DataStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_INVOICE_V2_DATA_STATUS_VALUES: Set[GetInvoiceV2DataStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_invoice_v2_data_status(value: str) -> GetInvoiceV2DataStatus:
    if value in GET_INVOICE_V2_DATA_STATUS_VALUES:
        return cast(GetInvoiceV2DataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVOICE_V2_DATA_STATUS_VALUES!r}")
