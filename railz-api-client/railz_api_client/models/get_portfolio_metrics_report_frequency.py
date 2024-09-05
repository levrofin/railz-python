from typing import Literal, Set, cast

GetPortfolioMetricsReportFrequency = Literal["month", "quarter", "year"]

GET_PORTFOLIO_METRICS_REPORT_FREQUENCY_VALUES: Set[GetPortfolioMetricsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_get_portfolio_metrics_report_frequency(value: str) -> GetPortfolioMetricsReportFrequency:
    if value in GET_PORTFOLIO_METRICS_REPORT_FREQUENCY_VALUES:
        return cast(GetPortfolioMetricsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PORTFOLIO_METRICS_REPORT_FREQUENCY_VALUES!r}")
