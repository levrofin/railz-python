from typing import Literal, Set, cast

FinancialFraudRiskReportMetaDataServiceName = Literal[
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

FINANCIAL_FRAUD_RISK_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[FinancialFraudRiskReportMetaDataServiceName] = {
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


def check_financial_fraud_risk_report_meta_data_service_name(value: str) -> FinancialFraudRiskReportMetaDataServiceName:
    if value in FINANCIAL_FRAUD_RISK_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(FinancialFraudRiskReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FRAUD_RISK_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
