from typing import Literal, Set, cast

PushTrackingCategoriesResponseV1DtoStatus = Literal["failed", "pending", "success"]

PUSH_TRACKING_CATEGORIES_RESPONSE_V1_DTO_STATUS_VALUES: Set[PushTrackingCategoriesResponseV1DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_tracking_categories_response_v1_dto_status(value: str) -> PushTrackingCategoriesResponseV1DtoStatus:
    if value in PUSH_TRACKING_CATEGORIES_RESPONSE_V1_DTO_STATUS_VALUES:
        return cast(PushTrackingCategoriesResponseV1DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_RESPONSE_V1_DTO_STATUS_VALUES!r}"
    )
