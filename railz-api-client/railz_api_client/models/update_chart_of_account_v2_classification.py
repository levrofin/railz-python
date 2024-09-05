from typing import Literal, Set, cast

UpdateChartOfAccountV2Classification = Literal["asset", "equity", "expense", "liability", "nonPosting", "revenue"]

UPDATE_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES: Set[UpdateChartOfAccountV2Classification] = {
    "asset",
    "equity",
    "expense",
    "liability",
    "nonPosting",
    "revenue",
}


def check_update_chart_of_account_v2_classification(value: str) -> UpdateChartOfAccountV2Classification:
    if value in UPDATE_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES:
        return cast(UpdateChartOfAccountV2Classification, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES!r}")
