from typing import Literal, Set, cast

PushCustomerIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_CUSTOMER_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushCustomerIndividualResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_customer_individual_response_v2_dto_status(value: str) -> PushCustomerIndividualResponseV2DtoStatus:
    if value in PUSH_CUSTOMER_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushCustomerIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
