from typing import Literal, Set, cast

CashflowStatementsSection = Literal["Cash", "Financing Activities", "Investing Activities", "Operating Activities"]

CASHFLOW_STATEMENTS_SECTION_VALUES: Set[CashflowStatementsSection] = {
    "Cash",
    "Financing Activities",
    "Investing Activities",
    "Operating Activities",
}


def check_cashflow_statements_section(value: str) -> CashflowStatementsSection:
    if value in CASHFLOW_STATEMENTS_SECTION_VALUES:
        return cast(CashflowStatementsSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_SECTION_VALUES!r}")
