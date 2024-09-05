from typing import Literal, Set, cast

ReportBalanceSheetsAccountingMethod = Literal["accrual", "cash"]

REPORT_BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES: Set[ReportBalanceSheetsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_report_balance_sheets_accounting_method(value: str) -> ReportBalanceSheetsAccountingMethod:
    if value in REPORT_BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES:
        return cast(ReportBalanceSheetsAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BALANCE_SHEETS_ACCOUNTING_METHOD_VALUES!r}")
