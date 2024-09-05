from typing import Literal, Set, cast

PushJournalEntriesV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushJournalEntriesV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_journal_entries_v2_response_dto_status(value: str) -> PushJournalEntriesV2ResponseDtoStatus:
    if value in PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushJournalEntriesV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
