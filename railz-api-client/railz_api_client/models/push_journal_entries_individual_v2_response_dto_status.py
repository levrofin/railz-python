from typing import Literal, Set, cast

PushJournalEntriesIndividualV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushJournalEntriesIndividualV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_journal_entries_individual_v2_response_dto_status(
    value: str,
) -> PushJournalEntriesIndividualV2ResponseDtoStatus:
    if value in PUSH_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushJournalEntriesIndividualV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
