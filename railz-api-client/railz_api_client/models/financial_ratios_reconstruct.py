from typing import Literal, Set, cast

FinancialRatiosReconstruct = Literal["false", "true"]

FINANCIAL_RATIOS_RECONSTRUCT_VALUES: Set[FinancialRatiosReconstruct] = {
    "false",
    "true",
}


def check_financial_ratios_reconstruct(value: str) -> FinancialRatiosReconstruct:
    if value in FINANCIAL_RATIOS_RECONSTRUCT_VALUES:
        return cast(FinancialRatiosReconstruct, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FINANCIAL_RATIOS_RECONSTRUCT_VALUES!r}")
