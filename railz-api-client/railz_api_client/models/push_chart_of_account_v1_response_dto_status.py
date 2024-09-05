from typing import Literal, Set, cast

PushChartOfAccountV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushChartOfAccountV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_chart_of_account_v1_response_dto_status(value: str) -> PushChartOfAccountV1ResponseDtoStatus:
    if value in PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushChartOfAccountV1ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_V1_RESPONSE_DTO_STATUS_VALUES!r}"
    )
