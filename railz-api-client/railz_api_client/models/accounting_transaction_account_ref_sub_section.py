from typing import Literal, Set, cast

AccountingTransactionAccountRefSubSection = Literal[
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

ACCOUNTING_TRANSACTION_ACCOUNT_REF_SUB_SECTION_VALUES: Set[AccountingTransactionAccountRefSubSection] = {
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


def check_accounting_transaction_account_ref_sub_section(value: str) -> AccountingTransactionAccountRefSubSection:
    if value in ACCOUNTING_TRANSACTION_ACCOUNT_REF_SUB_SECTION_VALUES:
        return cast(AccountingTransactionAccountRefSubSection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_ACCOUNT_REF_SUB_SECTION_VALUES!r}"
    )
