from typing import Literal, Set, cast

UpdateCustomerIndividualResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_CUSTOMER_INDIVIDUAL_RESPONSE_DTO_STATUS_VALUES: Set[UpdateCustomerIndividualResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_customer_individual_response_dto_status(value: str) -> UpdateCustomerIndividualResponseDtoStatus:
    if value in UPDATE_CUSTOMER_INDIVIDUAL_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateCustomerIndividualResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOMER_INDIVIDUAL_RESPONSE_DTO_STATUS_VALUES!r}"
    )
