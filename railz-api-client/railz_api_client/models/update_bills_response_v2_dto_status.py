from typing import Literal, Set, cast

UpdateBillsResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_BILLS_RESPONSE_V2_DTO_STATUS_VALUES: Set[UpdateBillsResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_bills_response_v2_dto_status(value: str) -> UpdateBillsResponseV2DtoStatus:
    if value in UPDATE_BILLS_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateBillsResponseV2DtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILLS_RESPONSE_V2_DTO_STATUS_VALUES!r}")
