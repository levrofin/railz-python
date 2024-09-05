from typing import Literal, Set, cast

SyncInfoStatus = Literal["completed", "error", "inProgress"]

SYNC_INFO_STATUS_VALUES: Set[SyncInfoStatus] = {
    "completed",
    "error",
    "inProgress",
}


def check_sync_info_status(value: str) -> SyncInfoStatus:
    if value in SYNC_INFO_STATUS_VALUES:
        return cast(SyncInfoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYNC_INFO_STATUS_VALUES!r}")
