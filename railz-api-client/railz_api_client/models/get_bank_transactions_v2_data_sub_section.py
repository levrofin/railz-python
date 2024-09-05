from typing import Literal, Set, cast

GetBankTransactionsV2DataSubSection = Literal[
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

GET_BANK_TRANSACTIONS_V2_DATA_SUB_SECTION_VALUES: Set[GetBankTransactionsV2DataSubSection] = {
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


def check_get_bank_transactions_v2_data_sub_section(value: str) -> GetBankTransactionsV2DataSubSection:
    if value in GET_BANK_TRANSACTIONS_V2_DATA_SUB_SECTION_VALUES:
        return cast(GetBankTransactionsV2DataSubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BANK_TRANSACTIONS_V2_DATA_SUB_SECTION_VALUES!r}")
