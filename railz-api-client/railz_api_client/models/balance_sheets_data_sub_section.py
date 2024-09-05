from typing import Literal, Set, cast

BalanceSheetsDataSubSection = Literal[
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
]

BALANCE_SHEETS_DATA_SUB_SECTION_VALUES: Set[BalanceSheetsDataSubSection] = {
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
}


def check_balance_sheets_data_sub_section(value: str) -> BalanceSheetsDataSubSection:
    if value in BALANCE_SHEETS_DATA_SUB_SECTION_VALUES:
        return cast(BalanceSheetsDataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_DATA_SUB_SECTION_VALUES!r}")
