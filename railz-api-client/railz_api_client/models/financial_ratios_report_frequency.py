from typing import Literal, Set, cast

FinancialRatiosReportFrequency = Literal["month", "quarter", "year"]

FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES: Set[FinancialRatiosReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_financial_ratios_report_frequency(value: str) -> FinancialRatiosReportFrequency:
    if value in FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES:
        return cast(FinancialRatiosReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_RATIOS_REPORT_FREQUENCY_VALUES!r}")
