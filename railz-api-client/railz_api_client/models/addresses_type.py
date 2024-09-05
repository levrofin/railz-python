from typing import Literal, Set, cast

AddressesType = Literal["billing", "shipping"]

ADDRESSES_TYPE_VALUES: Set[AddressesType] = {
    "billing",
    "shipping",
}


def check_addresses_type(value: str) -> AddressesType:
    if value in ADDRESSES_TYPE_VALUES:
        return cast(AddressesType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADDRESSES_TYPE_VALUES!r}")
