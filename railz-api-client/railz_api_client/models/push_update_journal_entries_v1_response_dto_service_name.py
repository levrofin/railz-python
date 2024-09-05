from typing import Literal, Set, cast

PushUpdateJournalEntriesV1ResponseDtoServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[
    PushUpdateJournalEntriesV1ResponseDtoServiceName
] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_push_update_journal_entries_v1_response_dto_service_name(
    value: str,
) -> PushUpdateJournalEntriesV1ResponseDtoServiceName:
    if value in PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushUpdateJournalEntriesV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
