from typing import Literal, Set, cast

BatchUpdateJournalEntriesV2ResponseDtoServiceName = Literal[
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

BATCH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[
    BatchUpdateJournalEntriesV2ResponseDtoServiceName
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


def check_batch_update_journal_entries_v2_response_dto_service_name(
    value: str,
) -> BatchUpdateJournalEntriesV2ResponseDtoServiceName:
    if value in BATCH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(BatchUpdateJournalEntriesV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
