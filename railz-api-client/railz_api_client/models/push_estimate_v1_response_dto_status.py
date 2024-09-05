from typing import Literal, Set, cast

PushEstimateV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_ESTIMATE_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushEstimateV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_estimate_v1_response_dto_status(value: str) -> PushEstimateV1ResponseDtoStatus:
    if value in PUSH_ESTIMATE_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushEstimateV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ESTIMATE_V1_RESPONSE_DTO_STATUS_VALUES!r}")
