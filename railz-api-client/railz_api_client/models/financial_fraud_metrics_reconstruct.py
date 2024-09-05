from typing import Literal, Set, cast

FinancialFraudMetricsReconstruct = Literal["false", "true"]

FINANCIAL_FRAUD_METRICS_RECONSTRUCT_VALUES: Set[FinancialFraudMetricsReconstruct] = {
    "false",
    "true",
}


def check_financial_fraud_metrics_reconstruct(value: str) -> FinancialFraudMetricsReconstruct:
    if value in FINANCIAL_FRAUD_METRICS_RECONSTRUCT_VALUES:
        return cast(FinancialFraudMetricsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_FRAUD_METRICS_RECONSTRUCT_VALUES!r}")
