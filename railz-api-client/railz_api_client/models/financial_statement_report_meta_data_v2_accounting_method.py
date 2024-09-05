from typing import Literal, Set, cast

FinancialStatementReportMetaDataV2AccountingMethod = Literal["accrual", "cash"]

FINANCIAL_STATEMENT_REPORT_META_DATA_V2_ACCOUNTING_METHOD_VALUES: Set[
    FinancialStatementReportMetaDataV2AccountingMethod
] = {
    "accrual",
    "cash",
}


def check_financial_statement_report_meta_data_v2_accounting_method(
    value: str,
) -> FinancialStatementReportMetaDataV2AccountingMethod:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_V2_ACCOUNTING_METHOD_VALUES:
        return cast(FinancialStatementReportMetaDataV2AccountingMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_V2_ACCOUNTING_METHOD_VALUES!r}"
    )
