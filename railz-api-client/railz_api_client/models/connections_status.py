from typing import Literal, Set, cast

ConnectionsStatus = Literal["active", "disconnected", "expired", "invalid", "pending"]

CONNECTIONS_STATUS_VALUES: Set[ConnectionsStatus] = {
    "active",
    "disconnected",
    "expired",
    "invalid",
    "pending",
}


def check_connections_status(value: str) -> ConnectionsStatus:
    if value in CONNECTIONS_STATUS_VALUES:
        return cast(ConnectionsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTIONS_STATUS_VALUES!r}")
