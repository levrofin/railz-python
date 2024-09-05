from typing import Literal, Set, cast

PutVendorBankAccountResponseDtoStatus = Literal["failed", "pending", "success"]

PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES: Set[PutVendorBankAccountResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_put_vendor_bank_account_response_dto_status(value: str) -> PutVendorBankAccountResponseDtoStatus:
    if value in PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES:
        return cast(PutVendorBankAccountResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUT_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES!r}"
    )
