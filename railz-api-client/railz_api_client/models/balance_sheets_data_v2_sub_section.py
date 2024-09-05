from typing import Literal, Set, cast

BalanceSheetsDataV2SubSection = Literal[
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
]

BALANCE_SHEETS_DATA_V2_SUB_SECTION_VALUES: Set[BalanceSheetsDataV2SubSection] = {
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Other Assets",
    "Other Liabilities",
}


def check_balance_sheets_data_v2_sub_section(value: str) -> BalanceSheetsDataV2SubSection:
    if value in BALANCE_SHEETS_DATA_V2_SUB_SECTION_VALUES:
        return cast(BalanceSheetsDataV2SubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_DATA_V2_SUB_SECTION_VALUES!r}")
