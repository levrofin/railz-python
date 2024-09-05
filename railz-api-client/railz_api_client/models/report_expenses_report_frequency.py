from typing import Literal, Set, cast

ReportExpensesReportFrequency = Literal["month", "quarter", "year"]

REPORT_EXPENSES_REPORT_FREQUENCY_VALUES: Set[ReportExpensesReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_expenses_report_frequency(value: str) -> ReportExpensesReportFrequency:
    if value in REPORT_EXPENSES_REPORT_FREQUENCY_VALUES:
        return cast(ReportExpensesReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_EXPENSES_REPORT_FREQUENCY_VALUES!r}")
