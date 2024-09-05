from typing import Literal, Set, cast

ReportRevenueAccountingMethod = Literal["accrual", "cash"]

REPORT_REVENUE_ACCOUNTING_METHOD_VALUES: Set[ReportRevenueAccountingMethod] = {
    "accrual",
    "cash",
}


def check_report_revenue_accounting_method(value: str) -> ReportRevenueAccountingMethod:
    if value in REPORT_REVENUE_ACCOUNTING_METHOD_VALUES:
        return cast(ReportRevenueAccountingMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_REVENUE_ACCOUNTING_METHOD_VALUES!r}")
