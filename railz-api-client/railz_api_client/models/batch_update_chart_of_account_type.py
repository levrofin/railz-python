from typing import Literal, Set, cast

BatchUpdateChartOfAccountType = Literal[
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

BATCH_UPDATE_CHART_OF_ACCOUNT_TYPE_VALUES: Set[BatchUpdateChartOfAccountType] = {
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


def check_batch_update_chart_of_account_type(value: str) -> BatchUpdateChartOfAccountType:
    if value in BATCH_UPDATE_CHART_OF_ACCOUNT_TYPE_VALUES:
        return cast(BatchUpdateChartOfAccountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_CHART_OF_ACCOUNT_TYPE_VALUES!r}")
