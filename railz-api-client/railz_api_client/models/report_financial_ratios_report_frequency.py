from typing import Literal, Set, cast

ReportFinancialRatiosReportFrequency = Literal["month", "quarter", "year"]

REPORT_FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES: Set[ReportFinancialRatiosReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_report_financial_ratios_report_frequency(value: str) -> ReportFinancialRatiosReportFrequency:
    if value in REPORT_FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES:
        return cast(ReportFinancialRatiosReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES!r}")
