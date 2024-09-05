from typing import Literal, Set, cast

GetVendorDataV2Status = Literal["active", "archived", "unknown"]

GET_VENDOR_DATA_V2_STATUS_VALUES: Set[GetVendorDataV2Status] = {
    "active",
    "archived",
    "unknown",
}


def check_get_vendor_data_v2_status(value: str) -> GetVendorDataV2Status:
    if value in GET_VENDOR_DATA_V2_STATUS_VALUES:
        return cast(GetVendorDataV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_VENDOR_DATA_V2_STATUS_VALUES!r}")
