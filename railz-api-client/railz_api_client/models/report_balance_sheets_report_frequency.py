from typing import Literal, Set, cast

ReportBalanceSheetsReportFrequency = Literal["month", "quarter", "year"]

REPORT_BALANCE_SHEETS_REPORT_FREQUENCY_VALUES: Set[ReportBalanceSheetsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_balance_sheets_report_frequency(value: str) -> ReportBalanceSheetsReportFrequency:
    if value in REPORT_BALANCE_SHEETS_REPORT_FREQUENCY_VALUES:
        return cast(ReportBalanceSheetsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BALANCE_SHEETS_REPORT_FREQUENCY_VALUES!r}")
