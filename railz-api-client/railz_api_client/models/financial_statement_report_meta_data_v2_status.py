from typing import Literal, Set, cast

FinancialStatementReportMetaDataV2Status = Literal["empty", "failed", "pending", "success"]

FINANCIAL_STATEMENT_REPORT_META_DATA_V2_STATUS_VALUES: Set[FinancialStatementReportMetaDataV2Status] = {
    "empty",
    "failed",
    "pending",
    "success",
}


def check_financial_statement_report_meta_data_v2_status(value: str) -> FinancialStatementReportMetaDataV2Status:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_V2_STATUS_VALUES:
        return cast(FinancialStatementReportMetaDataV2Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_V2_STATUS_VALUES!r}"
    )
