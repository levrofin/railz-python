from typing import Literal, Set, cast

PushChartOfAccountV1Classification = Literal["asset", "equity", "expense", "liability", "nonPosting", "revenue"]

PUSH_CHART_OF_ACCOUNT_V1_CLASSIFICATION_VALUES: Set[PushChartOfAccountV1Classification] = {
    "asset",
    "equity",
    "expense",
    "liability",
    "nonPosting",
    "revenue",
}


def check_push_chart_of_account_v1_classification(value: str) -> PushChartOfAccountV1Classification:
    if value in PUSH_CHART_OF_ACCOUNT_V1_CLASSIFICATION_VALUES:
        return cast(PushChartOfAccountV1Classification, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V1_CLASSIFICATION_VALUES!r}")
