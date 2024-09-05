from typing import Literal, Set, cast

PushChartOfAccountV2Classification = Literal["asset", "equity", "expense", "liability", "nonPosting", "revenue"]

PUSH_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES: Set[PushChartOfAccountV2Classification] = {
    "asset",
    "equity",
    "expense",
    "liability",
    "nonPosting",
    "revenue",
}


def check_push_chart_of_account_v2_classification(value: str) -> PushChartOfAccountV2Classification:
    if value in PUSH_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES:
        return cast(PushChartOfAccountV2Classification, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V2_CLASSIFICATION_VALUES!r}")
