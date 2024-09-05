from typing import Literal, Set, cast

GetJournalDataStatus = Literal["active", "inactive", "unknown"]

GET_JOURNAL_DATA_STATUS_VALUES: Set[GetJournalDataStatus] = {
    "active",
    "inactive",
    "unknown",
}


def check_get_journal_data_status(value: str) -> GetJournalDataStatus:
    if value in GET_JOURNAL_DATA_STATUS_VALUES:
        return cast(GetJournalDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_JOURNAL_DATA_STATUS_VALUES!r}")
