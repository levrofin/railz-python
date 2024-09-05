from typing import Literal, Set, cast

PushVendorV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES: Set[PushVendorV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_vendor_v1_response_dto_status(value: str) -> PushVendorV1ResponseDtoStatus:
    if value in PUSH_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushVendorV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES!r}")
