from typing import Literal, Set, cast

ReconcilationAccountRefSubSection = Literal[
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
]

RECONCILATION_ACCOUNT_REF_SUB_SECTION_VALUES: Set[ReconcilationAccountRefSubSection] = {
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Operating Expenses",
    "Other Expenses",
    "Other Income",
}


def check_reconcilation_account_ref_sub_section(value: str) -> ReconcilationAccountRefSubSection:
    if value in RECONCILATION_ACCOUNT_REF_SUB_SECTION_VALUES:
        return cast(ReconcilationAccountRefSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECONCILATION_ACCOUNT_REF_SUB_SECTION_VALUES!r}")
