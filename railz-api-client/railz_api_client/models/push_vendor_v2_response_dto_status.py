from typing import Literal, Set, cast

PushVendorV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES: Set[PushVendorV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_vendor_v2_response_dto_status(value: str) -> PushVendorV2ResponseDtoStatus:
    if value in PUSH_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushVendorV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES!r}")
