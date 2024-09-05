from typing import Literal, Set, cast

PutVendorV2ResponseDtoStatus = Literal["failed", "pending", "success"]

PUT_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES: Set[PutVendorV2ResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_put_vendor_v2_response_dto_status(value: str) -> PutVendorV2ResponseDtoStatus:
    if value in PUT_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES:
        return cast(PutVendorV2ResponseDtoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_V2_RESPONSE_DTO_STATUS_VALUES!r}")
