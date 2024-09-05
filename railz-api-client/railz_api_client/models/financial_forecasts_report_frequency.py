from typing import Literal, Set, cast

FinancialForecastsReportFrequency = Literal["month", "quarter", "year"]

FINANCIAL_FORECASTS_REPORT_FREQUENCY_VALUES: Set[FinancialForecastsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_financial_forecasts_report_frequency(value: str) -> FinancialForecastsReportFrequency:
    if value in FINANCIAL_FORECASTS_REPORT_FREQUENCY_VALUES:
        return cast(FinancialForecastsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECASTS_REPORT_FREQUENCY_VALUES!r}")
