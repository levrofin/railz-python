from typing import Literal, Set, cast

FinancialFraudMetricsReportFrequency = Literal["month", "quarter", "year"]

FINANCIAL_FRAUD_METRICS_REPORT_FREQUENCY_VALUES: Set[FinancialFraudMetricsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_financial_fraud_metrics_report_frequency(value: str) -> FinancialFraudMetricsReportFrequency:
    if value in FINANCIAL_FRAUD_METRICS_REPORT_FREQUENCY_VALUES:
        return cast(FinancialFraudMetricsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_FRAUD_METRICS_REPORT_FREQUENCY_VALUES!r}")
