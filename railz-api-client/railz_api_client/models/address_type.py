from typing import Literal, Set, cast

AddressType = Literal["billing", "other", "shipping"]

ADDRESS_TYPE_VALUES: Set[AddressType] = {
    "billing",
    "other",
    "shipping",
}


def check_address_type(value: str) -> AddressType:
    if value in ADDRESS_TYPE_VALUES:
        return cast(AddressType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADDRESS_TYPE_VALUES!r}")
