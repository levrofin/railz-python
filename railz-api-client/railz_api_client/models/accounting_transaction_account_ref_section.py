from typing import Literal, Set, cast

AccountingTransactionAccountRefSection = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

ACCOUNTING_TRANSACTION_ACCOUNT_REF_SECTION_VALUES: Set[AccountingTransactionAccountRefSection] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_accounting_transaction_account_ref_section(value: str) -> AccountingTransactionAccountRefSection:
    if value in ACCOUNTING_TRANSACTION_ACCOUNT_REF_SECTION_VALUES:
        return cast(AccountingTransactionAccountRefSection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_ACCOUNT_REF_SECTION_VALUES!r}"
    )
