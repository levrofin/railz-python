from typing import Literal, Set, cast

BalanceSheetsSubSection = Literal[
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
]

BALANCE_SHEETS_SUB_SECTION_VALUES: Set[BalanceSheetsSubSection] = {
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
}


def check_balance_sheets_sub_section(value: str) -> BalanceSheetsSubSection:
    if value in BALANCE_SHEETS_SUB_SECTION_VALUES:
        return cast(BalanceSheetsSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_SUB_SECTION_VALUES!r}")
