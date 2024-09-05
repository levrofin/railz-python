from typing import Literal, Set, cast

ReconcilationAccountRefSection = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

RECONCILATION_ACCOUNT_REF_SECTION_VALUES: Set[ReconcilationAccountRefSection] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_reconcilation_account_ref_section(value: str) -> ReconcilationAccountRefSection:
    if value in RECONCILATION_ACCOUNT_REF_SECTION_VALUES:
        return cast(ReconcilationAccountRefSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECONCILATION_ACCOUNT_REF_SECTION_VALUES!r}")
