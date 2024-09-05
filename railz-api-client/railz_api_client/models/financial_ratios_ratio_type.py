from typing import Literal, Set, cast

FinancialRatiosRatioType = Literal[
    "credit", "efficiency", "leverage", "liquidity", "market", "profitability", "reliability"
]

FINANCIAL_RATIOS_RATIO_TYPE_VALUES: Set[FinancialRatiosRatioType] = {
    "credit",
    "efficiency",
    "leverage",
    "liquidity",
    "market",
    "profitability",
    "reliability",
}


def check_financial_ratios_ratio_type(value: str) -> FinancialRatiosRatioType:
    if value in FINANCIAL_RATIOS_RATIO_TYPE_VALUES:
        return cast(FinancialRatiosRatioType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_RATIOS_RATIO_TYPE_VALUES!r}")
