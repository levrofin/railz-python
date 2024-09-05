from typing import Literal, Set, cast

GetContactDataContactType = Literal["customer", "unknown", "vendor"]

GET_CONTACT_DATA_CONTACT_TYPE_VALUES: Set[GetContactDataContactType] = {
    "customer",
    "unknown",
    "vendor",
}


def check_get_contact_data_contact_type(value: str) -> GetContactDataContactType:
    if value in GET_CONTACT_DATA_CONTACT_TYPE_VALUES:
        return cast(GetContactDataContactType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_DATA_CONTACT_TYPE_VALUES!r}")
