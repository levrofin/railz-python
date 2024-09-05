from typing import Literal, Set, cast

BatchPushJournalEntriesV2ResponseDtoServiceName = Literal[
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

BATCH_PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES: Set[BatchPushJournalEntriesV2ResponseDtoServiceName] = {
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


def check_batch_push_journal_entries_v2_response_dto_service_name(
    value: str,
) -> BatchPushJournalEntriesV2ResponseDtoServiceName:
    if value in BATCH_PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES:
        return cast(BatchPushJournalEntriesV2ResponseDtoServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_PUSH_JOURNAL_ENTRIES_V2_RESPONSE_DTO_SERVICE_NAME_VALUES!r}"
    )
