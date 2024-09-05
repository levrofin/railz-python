from typing import Literal, Set, cast

TrialBalanceSubSection = Literal[
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Operating Expenses",
    "Other Assets",
    "Other Expenses",
    "Other Income",
    "Other Liabilities",
    "Uncategorized Expenses",
    "Uncategorized Income",
]

TRIAL_BALANCE_SUB_SECTION_VALUES: Set[TrialBalanceSubSection] = {
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Operating Expenses",
    "Other Assets",
    "Other Expenses",
    "Other Income",
    "Other Liabilities",
    "Uncategorized Expenses",
    "Uncategorized Income",
}


def check_trial_balance_sub_section(value: str) -> TrialBalanceSubSection:
    if value in TRIAL_BALANCE_SUB_SECTION_VALUES:
        return cast(TrialBalanceSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCE_SUB_SECTION_VALUES!r}")
