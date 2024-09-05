from typing import Literal, Set, cast

GetCustomerDataV2Status = Literal["active", "archived", "unknown"]

GET_CUSTOMER_DATA_V2_STATUS_VALUES: Set[GetCustomerDataV2Status] = {
    "active",
    "archived",
    "unknown",
}


def check_get_customer_data_v2_status(value: str) -> GetCustomerDataV2Status:
    if value in GET_CUSTOMER_DATA_V2_STATUS_VALUES:
        return cast(GetCustomerDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CUSTOMER_DATA_V2_STATUS_VALUES!r}")
