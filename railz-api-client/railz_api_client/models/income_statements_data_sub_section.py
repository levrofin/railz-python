from typing import Literal, Set, cast

IncomeStatementsDataSubSection = Literal[
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
]

INCOME_STATEMENTS_DATA_SUB_SECTION_VALUES: Set[IncomeStatementsDataSubSection] = {
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
}


def check_income_statements_data_sub_section(value: str) -> IncomeStatementsDataSubSection:
    if value in INCOME_STATEMENTS_DATA_SUB_SECTION_VALUES:
        return cast(IncomeStatementsDataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_DATA_SUB_SECTION_VALUES!r}")
