from typing import Literal, Set, cast

FinancialStatementReportMetaDataServiceName = Literal[
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

FINANCIAL_STATEMENT_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[FinancialStatementReportMetaDataServiceName] = {
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


def check_financial_statement_report_meta_data_service_name(value: str) -> FinancialStatementReportMetaDataServiceName:
    if value in FINANCIAL_STATEMENT_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(FinancialStatementReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_STATEMENT_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
