from typing import Literal, Set, cast

GetBillsStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_BILLS_STATUS_VALUES: Set[GetBillsStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_bills_status(value: str) -> GetBillsStatus:
    if value in GET_BILLS_STATUS_VALUES:
        return cast(GetBillsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILLS_STATUS_VALUES!r}")
