from typing import Literal, Set, cast

UpdateChartOfAccountIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[
    UpdateChartOfAccountIndividualResponseV2DtoStatus
] = {
    "failed",
    "pending",
    "success",
}


def check_update_chart_of_account_individual_response_v2_dto_status(
    value: str,
) -> UpdateChartOfAccountIndividualResponseV2DtoStatus:
    if value in UPDATE_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateChartOfAccountIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
