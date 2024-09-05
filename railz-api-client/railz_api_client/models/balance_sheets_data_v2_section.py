from typing import Literal, Set, cast

BalanceSheetsDataV2Section = Literal["Assets", "Equity", "Liabilities"]

BALANCE_SHEETS_DATA_V2_SECTION_VALUES: Set[BalanceSheetsDataV2Section] = {
    "Assets",
    "Equity",
    "Liabilities",
}


def check_balance_sheets_data_v2_section(value: str) -> BalanceSheetsDataV2Section:
    if value in BALANCE_SHEETS_DATA_V2_SECTION_VALUES:
        return cast(BalanceSheetsDataV2Section, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_DATA_V2_SECTION_VALUES!r}")
