from typing import Literal, Set, cast

UpdateBillsResponseV1DtoStatus = Literal["failed", "pending", "success"]

UPDATE_BILLS_RESPONSE_V1_DTO_STATUS_VALUES: Set[UpdateBillsResponseV1DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_bills_response_v1_dto_status(value: str) -> UpdateBillsResponseV1DtoStatus:
    if value in UPDATE_BILLS_RESPONSE_V1_DTO_STATUS_VALUES:
        return cast(UpdateBillsResponseV1DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILLS_RESPONSE_V1_DTO_STATUS_VALUES!r}")
