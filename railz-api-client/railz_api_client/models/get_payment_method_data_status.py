from typing import Literal, Set, cast

GetPaymentMethodDataStatus = Literal["active", "archived", "unknown"]

GET_PAYMENT_METHOD_DATA_STATUS_VALUES: Set[GetPaymentMethodDataStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_payment_method_data_status(value: str) -> GetPaymentMethodDataStatus:
    if value in GET_PAYMENT_METHOD_DATA_STATUS_VALUES:
        return cast(GetPaymentMethodDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PAYMENT_METHOD_DATA_STATUS_VALUES!r}")
