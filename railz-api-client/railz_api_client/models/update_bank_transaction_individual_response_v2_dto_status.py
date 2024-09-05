from typing import Literal, Set, cast

UpdateBankTransactionIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

UPDATE_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[
    UpdateBankTransactionIndividualResponseV2DtoStatus
] = {
    "failed",
    "pending",
    "success",
}


def check_update_bank_transaction_individual_response_v2_dto_status(
    value: str,
) -> UpdateBankTransactionIndividualResponseV2DtoStatus:
    if value in UPDATE_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(UpdateBankTransactionIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
