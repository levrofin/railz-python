from typing import Literal, Set, cast

CashflowStatementsReportFrequency = Literal["month", "quarter", "year"]

CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES: Set[CashflowStatementsReportFrequency] = {
    "month",
    "quarter",
    "year",
}


def check_cashflow_statements_report_frequency(value: str) -> CashflowStatementsReportFrequency:
    if value in CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES:
        return cast(CashflowStatementsReportFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CASHFLOW_STATEMENTS_REPORT_FREQUENCY_VALUES!r}")
