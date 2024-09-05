from typing import Literal, Set, cast

IncomeStatementsAccountingMethod = Literal["accrual", "cash"]

INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES: Set[IncomeStatementsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_income_statements_accounting_method(value: str) -> IncomeStatementsAccountingMethod:
    if value in INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES:
        return cast(IncomeStatementsAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES!r}")
