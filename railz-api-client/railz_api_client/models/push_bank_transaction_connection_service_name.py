from typing import Literal, Set, cast

PushBankTransactionConnectionServiceName = Literal["xero"]

PUSH_BANK_TRANSACTION_CONNECTION_SERVICE_NAME_VALUES: Set[PushBankTransactionConnectionServiceName] = {
    "xero",
}


def check_push_bank_transaction_connection_service_name(value: str) -> PushBankTransactionConnectionServiceName:
    if value in PUSH_BANK_TRANSACTION_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushBankTransactionConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSACTION_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
