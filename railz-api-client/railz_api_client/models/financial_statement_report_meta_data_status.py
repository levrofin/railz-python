from typing import Literal, Set, cast

FinancialStatementReportMetaDataStatus = Literal["empty", "failed", "pending", "success"]

FINANCIAL_STATEMENT_REPORT_META_DATA_STATUS_VALUES: Set[FinancialStatementReportMetaDataStatus] = {
    "empty",
    "failed",
    "pending",
    "success",
}


def check_financial_statement_report_meta_data_status(value: str) -> FinancialStatementReportMetaDataStatus:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_STATUS_VALUES:
        return cast(FinancialStatementReportMetaDataStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_STATUS_VALUES!r}"
    )
