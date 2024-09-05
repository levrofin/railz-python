from typing import Literal, Set, cast

IncomeStatementsSubSection = Literal[
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
]

INCOME_STATEMENTS_SUB_SECTION_VALUES: Set[IncomeStatementsSubSection] = {
    "Cost of Goods Sold",
    "Expenses",
    "Income",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
    "Uncategorized Expenses",
    "Uncategorized Income",
}


def check_income_statements_sub_section(value: str) -> IncomeStatementsSubSection:
    if value in INCOME_STATEMENTS_SUB_SECTION_VALUES:
        return cast(IncomeStatementsSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_SUB_SECTION_VALUES!r}")
