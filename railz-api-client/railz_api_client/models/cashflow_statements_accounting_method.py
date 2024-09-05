from typing import Literal, Set, cast

CashflowStatementsAccountingMethod = Literal["accrual", "cash"]

CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES: Set[CashflowStatementsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_cashflow_statements_accounting_method(value: str) -> CashflowStatementsAccountingMethod:
    if value in CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES:
        return cast(CashflowStatementsAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES!r}")
