from typing import Literal, Set, cast

PushJournalsDataStatus = Literal["active", "inactive", "unknown"]

PUSH_JOURNALS_DATA_STATUS_VALUES: Set[PushJournalsDataStatus] = {
    "active",
    "inactive",
    "unknown",
}


def check_push_journals_data_status(value: str) -> PushJournalsDataStatus:
    if value in PUSH_JOURNALS_DATA_STATUS_VALUES:
        return cast(PushJournalsDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_JOURNALS_DATA_STATUS_VALUES!r}")
