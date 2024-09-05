from typing import Literal, Set, cast

UpdateChartOfAccountV2ResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES: Set[UpdateChartOfAccountV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_chart_of_account_v2_response_dto_status(value: str) -> UpdateChartOfAccountV2ResponseDtoStatus:
    if value in UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateChartOfAccountV2ResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CHART_OF_ACCOUNT_V2_RESPONSE_DTO_STATUS_VALUES!r}"
    )
