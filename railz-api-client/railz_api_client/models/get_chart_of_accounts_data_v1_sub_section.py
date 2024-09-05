from typing import Literal, Set, cast

GetChartOfAccountsDataV1SubSection = Literal[
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Non-Posting",
    "Operating Expenses",
    "Other Assets",
    "Other Expenses",
    "Other Income",
    "Other Liabilities",
    "Uncategorized Expenses",
    "Uncategorized Income",
]

GET_CHART_OF_ACCOUNTS_DATA_V1_SUB_SECTION_VALUES: Set[GetChartOfAccountsDataV1SubSection] = {
    "Cost of Goods Sold",
    "Current Assets",
    "Current Liabilities",
    "Equity",
    "Expenses",
    "Income",
    "Non-Current Assets",
    "Non-Current Liabilities",
    "Non-Posting",
    "Operating Expenses",
    "Other Assets",
    "Other Expenses",
    "Other Income",
    "Other Liabilities",
    "Uncategorized Expenses",
    "Uncategorized Income",
}


def check_get_chart_of_accounts_data_v1_sub_section(value: str) -> GetChartOfAccountsDataV1SubSection:
    if value in GET_CHART_OF_ACCOUNTS_DATA_V1_SUB_SECTION_VALUES:
        return cast(GetChartOfAccountsDataV1SubSection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CHART_OF_ACCOUNTS_DATA_V1_SUB_SECTION_VALUES!r}")
