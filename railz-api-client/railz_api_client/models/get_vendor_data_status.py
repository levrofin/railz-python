from typing import Literal, Set, cast

GetVendorDataStatus = Literal["active", "archived", "unknown"]

GET_VENDOR_DATA_STATUS_VALUES: Set[GetVendorDataStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_vendor_data_status(value: str) -> GetVendorDataStatus:
    if value in GET_VENDOR_DATA_STATUS_VALUES:
        return cast(GetVendorDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_VENDOR_DATA_STATUS_VALUES!r}")
