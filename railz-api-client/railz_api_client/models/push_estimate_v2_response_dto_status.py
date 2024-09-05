from typing import Literal, Set, cast

PushEstimateV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_ESTIMATE_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushEstimateV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_estimate_v2_response_dto_status(value: str) -> PushEstimateV2ResponseDtoStatus:
    if value in PUSH_ESTIMATE_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushEstimateV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_ESTIMATE_V2_RESPONSE_DTO_STATUS_VALUES!r}")
