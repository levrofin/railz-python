from typing import Literal, Set, cast

PushCustomerBankAccountResponseDtoStatus = Literal["failed", "pending", "success"]

PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES: Set[PushCustomerBankAccountResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_push_customer_bank_account_response_dto_status(value: str) -> PushCustomerBankAccountResponseDtoStatus:
    if value in PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES:
        return cast(PushCustomerBankAccountResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_CUSTOMER_BANK_ACCOUNT_RESPONSE_DTO_STATUS_VALUES!r}"
    )
