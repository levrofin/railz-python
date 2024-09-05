from typing import Literal, Set, cast

PushChartOfAccountV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushChartOfAccountV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_chart_of_account_v2_response_dto_status(value: str) -> PushChartOfAccountV2ResponseDtoStatus:
    if value in PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushChartOfAccountV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
