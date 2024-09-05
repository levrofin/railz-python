from typing import Literal, Set, cast

PushBankTransfersConnectionServiceName = Literal["xero"]

PUSH_BANK_TRANSFERS_CONNECTION_SERVICE_NAME_VALUES: Set[PushBankTransfersConnectionServiceName] = {
    "xero",
}


def check_push_bank_transfers_connection_service_name(value: str) -> PushBankTransfersConnectionServiceName:
    if value in PUSH_BANK_TRANSFERS_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushBankTransfersConnectionServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUSH_BANK_TRANSFERS_CONNECTION_SERVICE_NAME_VALUES!r}"
    )
