from typing import Literal, Set, cast

IncomeStatementsDataSection = Literal["Expenses", "Income"]

INCOME_STATEMENTS_DATA_SECTION_VALUES: Set[IncomeStatementsDataSection] = {
    "Expenses",
    "Income",
}


def check_income_statements_data_section(value: str) -> IncomeStatementsDataSection:
    if value in INCOME_STATEMENTS_DATA_SECTION_VALUES:
        return cast(IncomeStatementsDataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_DATA_SECTION_VALUES!r}")
