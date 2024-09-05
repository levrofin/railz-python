from typing import Literal, Set, cast

PushChartOfAccountIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushChartOfAccountIndividualResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_chart_of_account_individual_response_v2_dto_status(
    value: str,
) -> PushChartOfAccountIndividualResponseV2DtoStatus:
    if value in PUSH_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushChartOfAccountIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CHART_OF_ACCOUNT_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
