from typing import Literal, Set, cast

PushTrackingCategoriesResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushTrackingCategoriesResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_tracking_categories_response_v2_dto_status(value: str) -> PushTrackingCategoriesResponseV2DtoStatus:
    if value in PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushTrackingCategoriesResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_TRACKING_CATEGORIES_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
