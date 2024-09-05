from typing import Literal, Set, cast

TrialBalancesDataV2Section = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

TRIAL_BALANCES_DATA_V2_SECTION_VALUES: Set[TrialBalancesDataV2Section] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_trial_balances_data_v2_section(value: str) -> TrialBalancesDataV2Section:
    if value in TRIAL_BALANCES_DATA_V2_SECTION_VALUES:
        return cast(TrialBalancesDataV2Section, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCES_DATA_V2_SECTION_VALUES!r}")
