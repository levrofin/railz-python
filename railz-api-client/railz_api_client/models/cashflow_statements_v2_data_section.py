from typing import Literal, Set, cast

CashflowStatementsV2DataSection = Literal[
    "Cash", "Financing Activities", "Investing Activities", "Operating Activities"
]

CASHFLOW_STATEMENTS_V2_DATA_SECTION_VALUES: Set[CashflowStatementsV2DataSection] = {
    "Cash",
    "Financing Activities",
    "Investing Activities",
    "Operating Activities",
}


def check_cashflow_statements_v2_data_section(value: str) -> CashflowStatementsV2DataSection:
    if value in CASHFLOW_STATEMENTS_V2_DATA_SECTION_VALUES:
        return cast(CashflowStatementsV2DataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_V2_DATA_SECTION_VALUES!r}")
