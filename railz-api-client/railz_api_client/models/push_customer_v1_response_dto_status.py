from typing import Literal, Set, cast

PushCustomerV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushCustomerV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_customer_v1_response_dto_status(value: str) -> PushCustomerV1ResponseDtoStatus:
    if value in PUSH_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushCustomerV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES!r}")
