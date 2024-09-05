from typing import Literal, Set, cast

IncomeStatementsReportFrequency = Literal["month", "quarter", "year"]

INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES: Set[IncomeStatementsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_income_statements_report_frequency(value: str) -> IncomeStatementsReportFrequency:
    if value in INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES:
        return cast(IncomeStatementsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES!r}")
