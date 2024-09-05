from typing import Literal, Set, cast

GetCustomerDataStatus = Literal["active", "archived", "unknown"]

GET_CUSTOMER_DATA_STATUS_VALUES: Set[GetCustomerDataStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_customer_data_status(value: str) -> GetCustomerDataStatus:
    if value in GET_CUSTOMER_DATA_STATUS_VALUES:
        return cast(GetCustomerDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CUSTOMER_DATA_STATUS_VALUES!r}")
