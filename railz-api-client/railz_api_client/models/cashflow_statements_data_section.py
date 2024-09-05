from typing import Literal, Set, cast

CashflowStatementsDataSection = Literal["Cash", "Financing Activities", "Investing Activities", "Operating Activities"]

CASHFLOW_STATEMENTS_DATA_SECTION_VALUES: Set[CashflowStatementsDataSection] = {
    "Cash",
    "Financing Activities",
    "Investing Activities",
    "Operating Activities",
}


def check_cashflow_statements_data_section(value: str) -> CashflowStatementsDataSection:
    if value in CASHFLOW_STATEMENTS_DATA_SECTION_VALUES:
        return cast(CashflowStatementsDataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_DATA_SECTION_VALUES!r}")
