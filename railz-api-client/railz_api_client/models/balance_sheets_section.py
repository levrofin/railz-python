from typing import Literal, Set, cast

BalanceSheetsSection = Literal["Assets", "Equity", "Liabilities"]

BALANCE_SHEETS_SECTION_VALUES: Set[BalanceSheetsSection] = {
    "Assets",
    "Equity",
    "Liabilities",
}


def check_balance_sheets_section(value: str) -> BalanceSheetsSection:
    if value in BALANCE_SHEETS_SECTION_VALUES:
        return cast(BalanceSheetsSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_SECTION_VALUES!r}")
