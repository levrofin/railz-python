from typing import Literal, Set, cast

PushJournalsResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_JOURNALS_RESPONSE_DTO_STATUS_VALUES: Set[PushJournalsResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_journals_response_dto_status(value: str) -> PushJournalsResponseDtoStatus:
    if value in PUSH_JOURNALS_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushJournalsResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_JOURNALS_RESPONSE_DTO_STATUS_VALUES!r}")
