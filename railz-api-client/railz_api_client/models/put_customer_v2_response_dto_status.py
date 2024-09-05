from typing import Literal, Set, cast

PutCustomerV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUT_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES: Set[PutCustomerV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_put_customer_v2_response_dto_status(value: str) -> PutCustomerV2ResponseDtoStatus:
    if value in PUT_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PutCustomerV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_CUSTOMER_V2_RESPONSE_DTO_STATUS_VALUES!r}")
