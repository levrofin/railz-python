from typing import Literal, Set, cast

PushUpdateJournalEntriesV2ResponseDtoServiceName = Literal[
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

PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[
    PushUpdateJournalEntriesV2ResponseDtoServiceName
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


def check_push_update_journal_entries_v2_response_dto_service_name(
    value: str,
) -> PushUpdateJournalEntriesV2ResponseDtoServiceName:
    if value in PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(PushUpdateJournalEntriesV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
