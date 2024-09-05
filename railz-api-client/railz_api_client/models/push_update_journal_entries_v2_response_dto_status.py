from typing import Literal, Set, cast

PushUpdateJournalEntriesV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushUpdateJournalEntriesV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_update_journal_entries_v2_response_dto_status(value: str) -> PushUpdateJournalEntriesV2ResponseDtoStatus:
    if value in PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushUpdateJournalEntriesV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
