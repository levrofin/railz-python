from typing import Literal, Set, cast

PushChartOfAccountV2Type = Literal[
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

PUSH_CHART_OF_ACCOUNT_V2_TYPE_VALUES: Set[PushChartOfAccountV2Type] = {
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


def check_push_chart_of_account_v2_type(value: str) -> PushChartOfAccountV2Type:
    if value in PUSH_CHART_OF_ACCOUNT_V2_TYPE_VALUES:
        return cast(PushChartOfAccountV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V2_TYPE_VALUES!r}")
