from typing import Literal, Set, cast

CashflowStatementsV2DataSubSection = Literal[
    "Adjustments", "Cash", "Changes", "Intangibles", "Payments", "Proceeds", "Property Plant And Equipment", "Stock"
]

CASHFLOW_STATEMENTS_V2_DATA_SUB_SECTION_VALUES: Set[CashflowStatementsV2DataSubSection] = {
    "Adjustments",
    "Cash",
    "Changes",
    "Intangibles",
    "Payments",
    "Proceeds",
    "Property Plant And Equipment",
    "Stock",
}


def check_cashflow_statements_v2_data_sub_section(value: str) -> CashflowStatementsV2DataSubSection:
    if value in CASHFLOW_STATEMENTS_V2_DATA_SUB_SECTION_VALUES:
        return cast(CashflowStatementsV2DataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_V2_DATA_SUB_SECTION_VALUES!r}")
