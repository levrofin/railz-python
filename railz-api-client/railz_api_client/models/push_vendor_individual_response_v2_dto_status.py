from typing import Literal, Set, cast

PushVendorIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[PushVendorIndividualResponseV2DtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_vendor_individual_response_v2_dto_status(value: str) -> PushVendorIndividualResponseV2DtoStatus:
    if value in PUSH_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushVendorIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
