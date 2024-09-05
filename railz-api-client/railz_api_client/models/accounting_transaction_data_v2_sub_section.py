from typing import Literal, Set, cast

AccountingTransactionDataV2SubSection = Literal[
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

ACCOUNTING_TRANSACTION_DATA_V2_SUB_SECTION_VALUES: Set[AccountingTransactionDataV2SubSection] = {
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


def check_accounting_transaction_data_v2_sub_section(value: str) -> AccountingTransactionDataV2SubSection:
    if value in ACCOUNTING_TRANSACTION_DATA_V2_SUB_SECTION_VALUES:
        return cast(AccountingTransactionDataV2SubSection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_DATA_V2_SUB_SECTION_VALUES!r}"
    )
