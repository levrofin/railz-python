from typing import Literal, Set, cast

IncomeStatementsSection = Literal["Expenses", "Income"]

INCOME_STATEMENTS_SECTION_VALUES: Set[IncomeStatementsSection] = {
    "Expenses",
    "Income",
}


def check_income_statements_section(value: str) -> IncomeStatementsSection:
    if value in INCOME_STATEMENTS_SECTION_VALUES:
        return cast(IncomeStatementsSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_SECTION_VALUES!r}")
