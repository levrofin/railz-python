from typing import Literal, Set, cast

TrialBalancesDataV1SubSection = Literal[
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

TRIAL_BALANCES_DATA_V1_SUB_SECTION_VALUES: Set[TrialBalancesDataV1SubSection] = {
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


def check_trial_balances_data_v1_sub_section(value: str) -> TrialBalancesDataV1SubSection:
    if value in TRIAL_BALANCES_DATA_V1_SUB_SECTION_VALUES:
        return cast(TrialBalancesDataV1SubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIAL_BALANCES_DATA_V1_SUB_SECTION_VALUES!r}")
