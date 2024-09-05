from typing import Literal, Set, cast

TrialBalancesDataV1Section = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

TRIAL_BALANCES_DATA_V1_SECTION_VALUES: Set[TrialBalancesDataV1Section] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_trial_balances_data_v1_section(value: str) -> TrialBalancesDataV1Section:
    if value in TRIAL_BALANCES_DATA_V1_SECTION_VALUES:
        return cast(TrialBalancesDataV1Section, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCES_DATA_V1_SECTION_VALUES!r}")
