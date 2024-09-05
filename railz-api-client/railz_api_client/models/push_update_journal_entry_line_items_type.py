from typing import Literal, Set, cast

PushUpdateJournalEntryLineItemsType = Literal["credit", "debit"]

PUSH_UPDATE_JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES: Set[PushUpdateJournalEntryLineItemsType] = {
    "credit",
    "debit",
}


def check_push_update_journal_entry_line_items_type(value: str) -> PushUpdateJournalEntryLineItemsType:
    if value in PUSH_UPDATE_JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES:
        return cast(PushUpdateJournalEntryLineItemsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_UPDATE_JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES!r}")
