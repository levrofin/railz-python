from typing import Literal, Set, cast

GetBillV2DataStatus = Literal["draft", "open", "paid", "partiallyPaid", "unknown", "void"]

GET_BILL_V2_DATA_STATUS_VALUES: Set[GetBillV2DataStatus] = {
    "draft",
    "open",
    "paid",
    "partiallyPaid",
    "unknown",
    "void",
}


def check_get_bill_v2_data_status(value: str) -> GetBillV2DataStatus:
    if value in GET_BILL_V2_DATA_STATUS_VALUES:
        return cast(GetBillV2DataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_V2_DATA_STATUS_VALUES!r}")
