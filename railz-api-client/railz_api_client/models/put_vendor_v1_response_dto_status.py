from typing import Literal, Set, cast

PutVendorV1ResponseDtoStatus = Literal["failed", "pending", "success"]

PUT_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES: Set[PutVendorV1ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_put_vendor_v1_response_dto_status(value: str) -> PutVendorV1ResponseDtoStatus:
    if value in PUT_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES:
        return cast(PutVendorV1ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_V1_RESPONSE_DTO_STATUS_VALUES!r}")
