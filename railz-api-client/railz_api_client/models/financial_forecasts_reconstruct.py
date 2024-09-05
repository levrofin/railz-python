from typing import Literal, Set, cast

FinancialForecastsReconstruct = Literal["false", "true"]

FINANCIAL_FORECASTS_RECONSTRUCT_VALUES: Set[FinancialForecastsReconstruct] = {
    "false",
    "true",
}


def check_financial_forecasts_reconstruct(value: str) -> FinancialForecastsReconstruct:
    if value in FINANCIAL_FORECASTS_RECONSTRUCT_VALUES:
        return cast(FinancialForecastsReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_FORECASTS_RECONSTRUCT_VALUES!r}")
