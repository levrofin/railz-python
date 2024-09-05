from typing import Literal, Set, cast

ReportExpensesAccountingMethod = Literal["accrual", "cash"]

REPORT_EXPENSES_ACCOUNTING_METHOD_VALUES: Set[ReportExpensesAccountingMethod] = {
    "accrual",
    "cash",
}


def check_report_expenses_accounting_method(value: str) -> ReportExpensesAccountingMethod:
    if value in REPORT_EXPENSES_ACCOUNTING_METHOD_VALUES:
        return cast(ReportExpensesAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_EXPENSES_ACCOUNTING_METHOD_VALUES!r}")
