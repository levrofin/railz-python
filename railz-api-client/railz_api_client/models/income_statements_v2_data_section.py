from typing import Literal, Set, cast

IncomeStatementsV2DataSection = Literal["Expenses", "Income"]

INCOME_STATEMENTS_V2_DATA_SECTION_VALUES: Set[IncomeStatementsV2DataSection] = {
    "Expenses",
    "Income",
}


def check_income_statements_v2_data_section(value: str) -> IncomeStatementsV2DataSection:
    if value in INCOME_STATEMENTS_V2_DATA_SECTION_VALUES:
        return cast(IncomeStatementsV2DataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_V2_DATA_SECTION_VALUES!r}")
