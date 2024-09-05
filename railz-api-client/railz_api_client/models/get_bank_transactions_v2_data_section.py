from typing import Literal, Set, cast

GetBankTransactionsV2DataSection = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities"]

GET_BANK_TRANSACTIONS_V2_DATA_SECTION_VALUES: Set[GetBankTransactionsV2DataSection] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
}


def check_get_bank_transactions_v2_data_section(value: str) -> GetBankTransactionsV2DataSection:
    if value in GET_BANK_TRANSACTIONS_V2_DATA_SECTION_VALUES:
        return cast(GetBankTransactionsV2DataSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_V2_DATA_SECTION_VALUES!r}")
