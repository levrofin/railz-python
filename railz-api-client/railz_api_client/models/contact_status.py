from typing import Literal, Set, cast

ContactStatus = Literal["active", "archived", "unknown"]

CONTACT_STATUS_VALUES: Set[ContactStatus] = {
    "active",
    "archived",
    "unknown",
}


def check_contact_status(value: str) -> ContactStatus:
    if value in CONTACT_STATUS_VALUES:
        return cast(ContactStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_STATUS_VALUES!r}")
