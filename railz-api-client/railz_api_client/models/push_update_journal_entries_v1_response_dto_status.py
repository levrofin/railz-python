from typing import Literal, Set, cast

PushUpdateJournalEntriesV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushUpdateJournalEntriesV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_update_journal_entries_v1_response_dto_status(value: str) -> PushUpdateJournalEntriesV1ResponseDtoStatus:
    if value in PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushUpdateJournalEntriesV1ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES!r}"
    )
