from typing import Literal, Set, cast

PushChartOfAccountV2SubType = Literal[
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

PUSH_CHART_OF_ACCOUNT_V2_SUB_TYPE_VALUES: Set[PushChartOfAccountV2SubType] = {
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


def check_push_chart_of_account_v2_sub_type(value: str) -> PushChartOfAccountV2SubType:
    if value in PUSH_CHART_OF_ACCOUNT_V2_SUB_TYPE_VALUES:
        return cast(PushChartOfAccountV2SubType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V2_SUB_TYPE_VALUES!r}")
