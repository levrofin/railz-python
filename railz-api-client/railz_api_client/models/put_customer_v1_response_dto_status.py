from typing import Literal, Set, cast

PutCustomerV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUT_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES: Set[PutCustomerV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_put_customer_v1_response_dto_status(value: str) -> PutCustomerV1ResponseDtoStatus:
    if value in PUT_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PutCustomerV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_CUSTOMER_V1_RESPONSE_DTO_STATUS_VALUES!r}")
