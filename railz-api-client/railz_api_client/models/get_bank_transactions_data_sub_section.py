from typing import Literal, Set, cast

GetBankTransactionsDataSubSection = Literal[
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

GET_BANK_TRANSACTIONS_DATA_SUB_SECTION_VALUES: Set[GetBankTransactionsDataSubSection] = {
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


def check_get_bank_transactions_data_sub_section(value: str) -> GetBankTransactionsDataSubSection:
    if value in GET_BANK_TRANSACTIONS_DATA_SUB_SECTION_VALUES:
        return cast(GetBankTransactionsDataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_DATA_SUB_SECTION_VALUES!r}")
