from typing import Literal, Set, cast

TrialBalanceSection = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

TRIAL_BALANCE_SECTION_VALUES: Set[TrialBalanceSection] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_trial_balance_section(value: str) -> TrialBalanceSection:
    if value in TRIAL_BALANCE_SECTION_VALUES:
        return cast(TrialBalanceSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCE_SECTION_VALUES!r}")
