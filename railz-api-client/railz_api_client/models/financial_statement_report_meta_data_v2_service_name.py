from typing import Literal, Set, cast

FinancialStatementReportMetaDataV2ServiceName = Literal[
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
]

FINANCIAL_STATEMENT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[FinancialStatementReportMetaDataV2ServiceName] = {
    "dynamicsBusinessCentral",
    "freshbooks",
    "oracleNetsuite",
    "quickbooks",
    "quickbooksDesktop",
    "sageBusinessCloud",
    "sageIntacct",
    "wave",
    "xero",
    "zohoBooks",
}


def check_financial_statement_report_meta_data_v2_service_name(
    value: str,
) -> FinancialStatementReportMetaDataV2ServiceName:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(FinancialStatementReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
