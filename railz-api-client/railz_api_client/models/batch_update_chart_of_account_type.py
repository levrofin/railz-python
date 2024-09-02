from typing import Literal

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
