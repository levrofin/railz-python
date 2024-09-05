from typing import Literal, Set, cast

GetChartOfAccountsDataV2SubType = Literal[
    "cash&Bank",
    "costOfGoodsSold",
    "currentAsset",
    "currentLiability",
    "equity",
    "income",
    "longTermAsset",
    "longTermLiability",
    "operatingExpense",
    "propertyPlantAndEquipment",
]

GET_CHART_OF_ACCOUNTS_DATA_V2_SUB_TYPE_VALUES: Set[GetChartOfAccountsDataV2SubType] = {
    "cash&Bank",
    "costOfGoodsSold",
    "currentAsset",
    "currentLiability",
    "equity",
    "income",
    "longTermAsset",
    "longTermLiability",
    "operatingExpense",
    "propertyPlantAndEquipment",
}


def check_get_chart_of_accounts_data_v2_sub_type(value: str) -> GetChartOfAccountsDataV2SubType:
    if value in GET_CHART_OF_ACCOUNTS_DATA_V2_SUB_TYPE_VALUES:
        return cast(GetChartOfAccountsDataV2SubType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CHART_OF_ACCOUNTS_DATA_V2_SUB_TYPE_VALUES!r}")
