from typing import Literal, Set, cast

PushVendorBankAccountResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES: Set[PushVendorBankAccountResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_vendor_bank_account_response_dto_status(value: str) -> PushVendorBankAccountResponseDtoStatus:
    if value in PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushVendorBankAccountResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_VENDOR_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES!r}"
    )
