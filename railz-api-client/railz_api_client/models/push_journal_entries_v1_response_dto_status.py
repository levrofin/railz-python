from typing import Literal, Set, cast

PushJournalEntriesV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushJournalEntriesV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_journal_entries_v1_response_dto_status(value: str) -> PushJournalEntriesV1ResponseDtoStatus:
    if value in PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushJournalEntriesV1ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_STATUS_VALUES!r}"
    )
