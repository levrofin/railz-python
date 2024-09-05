from typing import Literal, Set, cast

JournalEntryLineItemsType = Literal["credit", "debit"]

JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES: Set[JournalEntryLineItemsType] = {
    "credit",
    "debit",
}


def check_journal_entry_line_items_type(value: str) -> JournalEntryLineItemsType:
    if value in JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES:
        return cast(JournalEntryLineItemsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOURNAL_ENTRY_LINE_ITEMS_TYPE_VALUES!r}")
