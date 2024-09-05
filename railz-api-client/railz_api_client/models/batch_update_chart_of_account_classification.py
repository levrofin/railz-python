from typing import Literal, Set, cast

BatchUpdateChartOfAccountClassification = Literal["asset", "equity", "expense", "liability", "nonPosting", "revenue"]

BATCH_UPDATE_CHART_OF_ACCOUNT_CLASSIFICATION_VALUES: Set[BatchUpdateChartOfAccountClassification] = {
    "asset",
    "equity",
    "expense",
    "liability",
    "nonPosting",
    "revenue",
}


def check_batch_update_chart_of_account_classification(value: str) -> BatchUpdateChartOfAccountClassification:
    if value in BATCH_UPDATE_CHART_OF_ACCOUNT_CLASSIFICATION_VALUES:
        return cast(BatchUpdateChartOfAccountClassification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BATCH_UPDATE_CHART_OF_ACCOUNT_CLASSIFICATION_VALUES!r}"
    )
