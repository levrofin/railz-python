from typing import Literal, Set, cast

SyncStatusAccountingMethod = Literal["accrual", "cash"]

SYNC_STATUS_ACCOUNTING_METHOD_VALUES: Set[SyncStatusAccountingMethod] = {
    "accrual",
    "cash",
}


def check_sync_status_accounting_method(value: str) -> SyncStatusAccountingMethod:
    if value in SYNC_STATUS_ACCOUNTING_METHOD_VALUES:
        return cast(SyncStatusAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYNC_STATUS_ACCOUNTING_METHOD_VALUES!r}")
