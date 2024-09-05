from typing import Literal, Set, cast

GetBillPaymentRequestDataV2State = Literal["approved", "draft", "open", "partiallyPaid", "posted", "unknown", "void"]

GET_BILL_PAYMENT_REQUEST_DATA_V2_STATE_VALUES: Set[GetBillPaymentRequestDataV2State] = {
    "approved",
    "draft",
    "open",
    "partiallyPaid",
    "posted",
    "unknown",
    "void",
}


def check_get_bill_payment_request_data_v2_state(value: str) -> GetBillPaymentRequestDataV2State:
    if value in GET_BILL_PAYMENT_REQUEST_DATA_V2_STATE_VALUES:
        return cast(GetBillPaymentRequestDataV2State, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BILL_PAYMENT_REQUEST_DATA_V2_STATE_VALUES!r}")
