from typing import Literal, Set, cast

PushExpenseeResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_EXPENSEE_RESPONSE_DTO_STATUS_VALUES: Set[PushExpenseeResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_expensee_response_dto_status(value: str) -> PushExpenseeResponseDtoStatus:
    if value in PUSH_EXPENSEE_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushExpenseeResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_EXPENSEE_RESPONSE_DTO_STATUS_VALUES!r}")
