from typing import Literal, Set, cast

GetBillDataStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_BILL_DATA_STATUS_VALUES: Set[GetBillDataStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_bill_data_status(value: str) -> GetBillDataStatus:
    if value in GET_BILL_DATA_STATUS_VALUES:
        return cast(GetBillDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_DATA_STATUS_VALUES!r}")
