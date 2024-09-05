from typing import Literal, Set, cast

UpdateJournalEntriesIndividualV2ResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES: Set[
    UpdateJournalEntriesIndividualV2ResponseDtoStatus
] = {
    "failed",
    "pending",
    "success",
}


def check_update_journal_entries_individual_v2_response_dto_status(
    value: str,
) -> UpdateJournalEntriesIndividualV2ResponseDtoStatus:
    if value in UPDATE_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateJournalEntriesIndividualV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_JOURNAL_ENTRIES_INDIVIDUAL_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
