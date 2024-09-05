from typing import Literal, Set, cast

GetBankTransactionsDataSection = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

GET_BANK_TRANSACTIONS_DATA_SECTION_VALUES: Set[GetBankTransactionsDataSection] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_get_bank_transactions_data_section(value: str) -> GetBankTransactionsDataSection:
    if value in GET_BANK_TRANSACTIONS_DATA_SECTION_VALUES:
        return cast(GetBankTransactionsDataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_DATA_SECTION_VALUES!r}")
