from typing import Literal, Set, cast

ReportIncomeStatementsReportFrequency = Literal["month", "quarter", "year"]

REPORT_INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES: Set[ReportIncomeStatementsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_income_statements_report_frequency(value: str) -> ReportIncomeStatementsReportFrequency:
    if value in REPORT_INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES:
        return cast(ReportIncomeStatementsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_INCOME_STATEMENTS_REPORT_FREQUENCY_VALUES!r}")
