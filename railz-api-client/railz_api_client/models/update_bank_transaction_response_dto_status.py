from typing import Literal, Set, cast

UpdateBankTransactionResponseDtoStatus = Literal["failed", "pending", "success"]

UPDATE_BANK_TRANSACTION_RESPONSE_DTO_STATUS_VALUES: Set[UpdateBankTransactionResponseDtoStatus] = {
    "failed",
    "pending",
    "success",
}


def check_update_bank_transaction_response_dto_status(value: str) -> UpdateBankTransactionResponseDtoStatus:
    if value in UPDATE_BANK_TRANSACTION_RESPONSE_DTO_STATUS_VALUES:
        return cast(UpdateBankTransactionResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BANK_TRANSACTION_RESPONSE_DTO_STATUS_VALUES!r}"
    )
