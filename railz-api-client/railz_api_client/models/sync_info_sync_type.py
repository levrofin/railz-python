from typing import Literal, Set, cast

SyncInfoSyncType = Literal["full", "manual", "partial"]

SYNC_INFO_SYNC_TYPE_VALUES: Set[SyncInfoSyncType] = {
    "full",
    "manual",
    "partial",
}


def check_sync_info_sync_type(value: str) -> SyncInfoSyncType:
    if value in SYNC_INFO_SYNC_TYPE_VALUES:
        return cast(SyncInfoSyncType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYNC_INFO_SYNC_TYPE_VALUES!r}")
