from typing import Literal, Set, cast

CashflowStatementsSubSection = Literal[
    "Adjustments", "Cash", "Changes", "Intangibles", "Payments", "Proceeds", "Property Plant And Equipment", "Stock"
]

CASHFLOW_STATEMENTS_SUB_SECTION_VALUES: Set[CashflowStatementsSubSection] = {
    "Adjustments",
    "Cash",
    "Changes",
    "Intangibles",
    "Payments",
    "Proceeds",
    "Property Plant And Equipment",
    "Stock",
}


def check_cashflow_statements_sub_section(value: str) -> CashflowStatementsSubSection:
    if value in CASHFLOW_STATEMENTS_SUB_SECTION_VALUES:
        return cast(CashflowStatementsSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_SUB_SECTION_VALUES!r}")
