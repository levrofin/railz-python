from typing import Literal, Set, cast

PushJournalEntriesV2ResponseDtoServiceName = Literal[
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

PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[PushJournalEntriesV2ResponseDtoServiceName] = {
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


def check_push_journal_entries_v2_response_dto_service_name(value: str) -> PushJournalEntriesV2ResponseDtoServiceName:
    if value in PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushJournalEntriesV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
