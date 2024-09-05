from typing import Literal, Set, cast

PushJournalEntriesV1ResponseDtoServiceName = Literal[
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

PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushJournalEntriesV1ResponseDtoServiceName] = {
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


def check_push_journal_entries_v1_response_dto_service_name(value: str) -> PushJournalEntriesV1ResponseDtoServiceName:
    if value in PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushJournalEntriesV1ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_JOURNAL_ENTRIES_V1_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
