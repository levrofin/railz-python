from typing import Literal, Set, cast

PushDepositConnectionServiceName = Literal["quickbooks", "xero"]

PUSH_DEPOSIT_CONNECTION_SERVICE_NAME_VALUES: Set[PushDepositConnectionServiceName] = {
    "quickbooks",
    "xero",
}


def check_push_deposit_connection_service_name(value: str) -> PushDepositConnectionServiceName:
    if value in PUSH_DEPOSIT_CONNECTION_SERVICE_NAME_VALUES:
        return cast(PushDepositConnectionServiceName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUSH_DEPOSIT_CONNECTION_SERVICE_NAME_VALUES!r}")
