from typing import Literal, Set, cast

CashflowStatementsDataSubSection = Literal[
    "Adjustments", "Cash", "Changes", "Intangibles", "Payments", "Proceeds", "Property Plant And Equipment", "Stock"
]

CASHFLOW_STATEMENTS_DATA_SUB_SECTION_VALUES: Set[CashflowStatementsDataSubSection] = {
    "Adjustments",
    "Cash",
    "Changes",
    "Intangibles",
    "Payments",
    "Proceeds",
    "Property Plant And Equipment",
    "Stock",
}


def check_cashflow_statements_data_sub_section(value: str) -> CashflowStatementsDataSubSection:
    if value in CASHFLOW_STATEMENTS_DATA_SUB_SECTION_VALUES:
        return cast(CashflowStatementsDataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_DATA_SUB_SECTION_VALUES!r}")
