from typing import Literal, Set, cast

ReportIncomeStatementsAccountingMethod = Literal["accrual", "cash"]

REPORT_INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES: Set[ReportIncomeStatementsAccountingMethod] = {
    "accrual",
    "cash",
}


def check_report_income_statements_accounting_method(value: str) -> ReportIncomeStatementsAccountingMethod:
    if value in REPORT_INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES:
        return cast(ReportIncomeStatementsAccountingMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_INCOME_STATEMENTS_ACCOUNTING_METHOD_VALUES!r}"
    )
