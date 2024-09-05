from typing import Literal, Set, cast

JournalEntryEntityRefType = Literal["customer", "employee", "vendor"]

JOURNAL_ENTRY_ENTITY_REF_TYPE_VALUES: Set[JournalEntryEntityRefType] = {
    "customer",
    "employee",
    "vendor",
}


def check_journal_entry_entity_ref_type(value: str) -> JournalEntryEntityRefType:
    if value in JOURNAL_ENTRY_ENTITY_REF_TYPE_VALUES:
        return cast(JournalEntryEntityRefType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOURNAL_ENTRY_ENTITY_REF_TYPE_VALUES!r}")
