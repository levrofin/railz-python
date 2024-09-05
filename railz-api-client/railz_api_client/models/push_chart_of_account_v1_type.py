from typing import Literal, Set, cast

PushChartOfAccountV1Type = Literal[
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

PUSH_CHART_OF_ACCOUNT_V1_TYPE_VALUES: Set[PushChartOfAccountV1Type] = {
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


def check_push_chart_of_account_v1_type(value: str) -> PushChartOfAccountV1Type:
    if value in PUSH_CHART_OF_ACCOUNT_V1_TYPE_VALUES:
        return cast(PushChartOfAccountV1Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V1_TYPE_VALUES!r}")
