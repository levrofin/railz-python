from typing import Literal, Set, cast

CustomerVendorContactV2Status = Literal["active", "archived", "unknown"]

CUSTOMER_VENDOR_CONTACT_V2_STATUS_VALUES: Set[CustomerVendorContactV2Status] = {
    "active",
    "archived",
    "unknown",
}


def check_customer_vendor_contact_v2_status(value: str) -> CustomerVendorContactV2Status:
    if value in CUSTOMER_VENDOR_CONTACT_V2_STATUS_VALUES:
        return cast(CustomerVendorContactV2Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOMER_VENDOR_CONTACT_V2_STATUS_VALUES!r}")
