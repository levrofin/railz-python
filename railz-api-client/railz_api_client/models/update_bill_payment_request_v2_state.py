from typing import Literal, Set, cast

UpdateBillPaymentRequestV2State = Literal["paid"]

UPDATE_BILL_PAYMENT_REQUEST_V2_STATE_VALUES: Set[UpdateBillPaymentRequestV2State] = {
    "paid",
}


def check_update_bill_payment_request_v2_state(value: str) -> UpdateBillPaymentRequestV2State:
    if value in UPDATE_BILL_PAYMENT_REQUEST_V2_STATE_VALUES:
        return cast(UpdateBillPaymentRequestV2State, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILL_PAYMENT_REQUEST_V2_STATE_VALUES!r}")
