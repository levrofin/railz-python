from typing import Literal, Set, cast

ReportCashflowStatementsAccountingMethod = Literal["accrual", "cash"]

REPORT_CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES: Set[ReportCashflowStatementsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_report_cashflow_statements_accounting_method(value: str) -> ReportCashflowStatementsAccountingMethod:
    if value in REPORT_CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES:
        return cast(ReportCashflowStatementsAccountingMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_CASHFLOW_STATEMENTS_ACCOUNTING_METHOD_VALUES!r}"
    )
