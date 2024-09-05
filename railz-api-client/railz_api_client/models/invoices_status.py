from typing import Literal, Set, cast

InvoicesStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

INVOICES_STATUS_VALUES: Set[InvoicesStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_invoices_status(value: str) -> InvoicesStatus:
    if value in INVOICES_STATUS_VALUES:
        return cast(InvoicesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICES_STATUS_VALUES!r}")
