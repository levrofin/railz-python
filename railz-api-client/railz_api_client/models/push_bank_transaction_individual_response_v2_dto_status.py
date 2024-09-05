from typing import Literal, Set, cast

PushBankTransactionIndividualResponseV2DtoStatus = Literal["failed", "pending", "success"]

PUSH_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES: Set[
    PushBankTransactionIndividualResponseV2DtoStatus
] = {
    "failed",
    "pending",
    "success",
}


def check_push_bank_transaction_individual_response_v2_dto_status(
    value: str,
) -> PushBankTransactionIndividualResponseV2DtoStatus:
    if value in PUSH_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES:
        return cast(PushBankTransactionIndividualResponseV2DtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_INDIVIDUAL_RESPONSE_V2_DTO_STATUS_VALUES!r}"
    )
