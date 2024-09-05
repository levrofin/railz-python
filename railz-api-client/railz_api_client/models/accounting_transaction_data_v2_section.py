from typing import Literal, Set, cast

AccountingTransactionDataV2Section = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

ACCOUNTING_TRANSACTION_DATA_V2_SECTION_VALUES: Set[AccountingTransactionDataV2Section] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_accounting_transaction_data_v2_section(value: str) -> AccountingTransactionDataV2Section:
    if value in ACCOUNTING_TRANSACTION_DATA_V2_SECTION_VALUES:
        return cast(AccountingTransactionDataV2Section, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNTING_TRANSACTION_DATA_V2_SECTION_VALUES!r}")
