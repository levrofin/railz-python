from typing import Literal, Set, cast

PushCustomerV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushCustomerV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_customer_v2_response_dto_status(value: str) -> PushCustomerV2ResponseDtoStatus:
    if value in PUSH_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushCustomerV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES!r}")
