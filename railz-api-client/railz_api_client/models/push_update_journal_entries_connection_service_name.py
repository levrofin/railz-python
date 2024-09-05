from typing import Literal, Set, cast

PushUpdateJournalEntriesConnectionServiceName = Literal["oracleNetsuite", "quickbooks", "sageIntacct", "xero"]

PUSH_UPDATE_JOURNAL_ENTRIES_CONNECTION_SERVICE_NAME_VALUES: Set[PushUpdateJournalEntriesConnectionServiceName] = {
    "oracleNetsuite",
    "quickbooks",
    "sageIntacct",
    "xero",
}


def check_push_update_journal_entries_connection_service_name(
    value: str,
) -> PushUpdateJournalEntriesConnectionServiceName:
    if value in PUSH_UPDATE_JOURNAL_ENTRIES_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushUpdateJournalEntriesConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRIES_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
