from typing import Literal, Set, cast

ReportCashflowStatementsReportFrequency = Literal["month", "quarter", "year"]

REPORT_CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES: Set[ReportCashflowStatementsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_cashflow_statements_report_frequency(value: str) -> ReportCashflowStatementsReportFrequency:
    if value in REPORT_CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES:
        return cast(ReportCashflowStatementsReportFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES!r}"
    )
