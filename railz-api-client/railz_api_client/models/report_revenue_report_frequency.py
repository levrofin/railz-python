from typing import Literal, Set, cast

ReportRevenueReportFrequency = Literal["month", "quarter", "year"]

REPORT_REVENUE_REPORT_FREQUENCY_VALUES: Set[ReportRevenueReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_revenue_report_frequency(value: str) -> ReportRevenueReportFrequency:
    if value in REPORT_REVENUE_REPORT_FREQUENCY_VALUES:
        return cast(ReportRevenueReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_REVENUE_REPORT_FREQUENCY_VALUES!r}")
