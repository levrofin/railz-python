from typing import Literal, Set, cast

GetContactDataStatus = Literal["active", "archived", "unknown"]

GET_CONTACT_DATA_STATUS_VALUES: Set[GetContactDataStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_get_contact_data_status(value: str) -> GetContactDataStatus:
    if value in GET_CONTACT_DATA_STATUS_VALUES:
        return cast(GetContactDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_DATA_STATUS_VALUES!r}")
