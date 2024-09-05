from typing import Literal, Set, cast

IncomeStatementsV2DataSubSection = Literal[
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
]

INCOME_STATEMENTS_V2_DATA_SUB_SECTION_VALUES: Set[IncomeStatementsV2DataSubSection] = {
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
}


def check_income_statements_v2_data_sub_section(value: str) -> IncomeStatementsV2DataSubSection:
    if value in INCOME_STATEMENTS_V2_DATA_SUB_SECTION_VALUES:
        return cast(IncomeStatementsV2DataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_V2_DATA_SUB_SECTION_VALUES!r}")
