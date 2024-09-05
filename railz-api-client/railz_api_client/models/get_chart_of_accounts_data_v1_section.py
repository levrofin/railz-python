from typing import Literal, Set, cast

GetChartOfAccountsDataV1Section = Literal["Assets", "Equity", "Expenses", "Income", "Liabilities", "Non-Posting"]

GET_CHART_OF_ACCOUNTS_DATA_V1_SECTION_VALUES: Set[GetChartOfAccountsDataV1Section] = {
    "Assets",
    "Equity",
    "Expenses",
    "Income",
    "Liabilities",
    "Non-Posting",
}


def check_get_chart_of_accounts_data_v1_section(value: str) -> GetChartOfAccountsDataV1Section:
    if value in GET_CHART_OF_ACCOUNTS_DATA_V1_SECTION_VALUES:
        return cast(GetChartOfAccountsDataV1Section, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CHART_OF_ACCOUNTS_DATA_V1_SECTION_VALUES!r}")
