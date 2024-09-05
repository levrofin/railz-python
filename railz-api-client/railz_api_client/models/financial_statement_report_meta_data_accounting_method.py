from typing import Literal, Set, cast

FinancialStatementReportMetaDataAccountingMethod = Literal["accrual", "cash"]

FINANCIAL_STATEMENT_REPORT_META_DATA_ACCOUNTING_METHOD_VALUES: Set[FinancialStatementReportMetaDataAccountingMethod] = {
    "accrual",
    "cash",
}


def check_financial_statement_report_meta_data_accounting_method(
    value: str,
) -> FinancialStatementReportMetaDataAccountingMethod:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_ACCOUNTING_METHOD_VALUES:
        return cast(FinancialStatementReportMetaDataAccountingMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_ACCOUNTING_METHOD_VALUES!r}"
    )
