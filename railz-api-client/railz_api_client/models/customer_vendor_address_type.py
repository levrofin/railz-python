from typing import Literal, Set, cast

CustomerVendorAddressType = Literal["billing", "other", "shipping"]

CUSTOMER_VENDOR_ADDRESS_TYPE_VALUES: Set[CustomerVendorAddressType] = {
    "billing",
    "other",
    "shipping",
}


def check_customer_vendor_address_type(value: str) -> CustomerVendorAddressType:
    if value in CUSTOMER_VENDOR_ADDRESS_TYPE_VALUES:
        return cast(CustomerVendorAddressType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOMER_VENDOR_ADDRESS_TYPE_VALUES!r}")
