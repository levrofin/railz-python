from typing import Literal, Set, cast

BalanceSheetsAccountingMethod = Literal["accrual", "cash"]

BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES: Set[BalanceSheetsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_balance_sheets_accounting_method(value: str) -> BalanceSheetsAccountingMethod:
    if value in BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES:
        return cast(BalanceSheetsAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES!r}")
