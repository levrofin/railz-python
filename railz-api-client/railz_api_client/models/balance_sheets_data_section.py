from typing import Literal, Set, cast

BalanceSheetsDataSection = Literal["Assets", "Equity", "Liabilities"]

BALANCE_SHEETS_DATA_SECTION_VALUES: Set[BalanceSheetsDataSection] = {
    "Assets",
    "Equity",
    "Liabilities",
}


def check_balance_sheets_data_section(value: str) -> BalanceSheetsDataSection:
    if value in BALANCE_SHEETS_DATA_SECTION_VALUES:
        return cast(BalanceSheetsDataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_DATA_SECTION_VALUES!r}")
