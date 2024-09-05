from typing import Literal, Set, cast

UpdateVendorIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[UpdateVendorIndividualResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_vendor_individual_response_v2_dto_status(value: str) -> UpdateVendorIndividualResponseV2DtoStatus:
    if value in UPDATE_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateVendorIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
