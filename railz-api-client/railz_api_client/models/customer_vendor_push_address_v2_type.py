from typing import Literal, Set, cast

CustomerVendorPushAddressV2Type = Literal["billing", "other", "shipping"]

CUSTOMER_VENDOR_PUSH_ADDRESS_V2_TYPE_VALUES: Set[CustomerVendorPushAddressV2Type] = {
    "billing",
    "other",
    "shipping",
}


def check_customer_vendor_push_address_v2_type(value: str) -> CustomerVendorPushAddressV2Type:
    if value in CUSTOMER_VENDOR_PUSH_ADDRESS_V2_TYPE_VALUES:
        return cast(CustomerVendorPushAddressV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOMER_VENDOR_PUSH_ADDRESS_V2_TYPE_VALUES!r}")
