from typing import Literal, Set, cast

GetInvoiceV1DataStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_INVOICE_V1_DATA_STATUS_VALUES: Set[GetInvoiceV1DataStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_invoice_v1_data_status(value: str) -> GetInvoiceV1DataStatus:
    if value in GET_INVOICE_V1_DATA_STATUS_VALUES:
        return cast(GetInvoiceV1DataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INVOICE_V1_DATA_STATUS_VALUES!r}")
