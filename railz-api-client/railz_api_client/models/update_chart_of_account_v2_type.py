from typing import Literal, Set, cast

UpdateChartOfAccountV2Type = Literal[
    "accountPayable",
    "accountReceivable",
    "bank",
    "cogs",
    "creditCard",
    "currentAsset",
    "currentLiability",
    "deferredExpense",
    "deferredIncome",
    "equity",
    "expense",
    "fixedAsset",
    "income",
    "incomeGeneral",
    "inventory",
    "nonCurrentAsset",
    "nonCurrentLiability",
    "otherExpense",
    "otherIncome",
    "unbilledReceivable",
]

UPDATE_CHART_OF_ACCOUNT_V2_TYPE_VALUES: Set[UpdateChartOfAccountV2Type] = {
    "accountPayable",
    "accountReceivable",
    "bank",
    "cogs",
    "creditCard",
    "currentAsset",
    "currentLiability",
    "deferredExpense",
    "deferredIncome",
    "equity",
    "expense",
    "fixedAsset",
    "income",
    "incomeGeneral",
    "inventory",
    "nonCurrentAsset",
    "nonCurrentLiability",
    "otherExpense",
    "otherIncome",
    "unbilledReceivable",
}


def check_update_chart_of_account_v2_type(value: str) -> UpdateChartOfAccountV2Type:
    if value in UPDATE_CHART_OF_ACCOUNT_V2_TYPE_VALUES:
        return cast(UpdateChartOfAccountV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CHART_OF_ACCOUNT_V2_TYPE_VALUES!r}")
