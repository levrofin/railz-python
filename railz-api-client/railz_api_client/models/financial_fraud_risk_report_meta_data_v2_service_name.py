from typing import Literal, Set, cast

FinancialFraudRiskReportMetaDataV2ServiceName = Literal[
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

FINANCIAL_FRAUD_RISK_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[FinancialFraudRiskReportMetaDataV2ServiceName] = {
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


def check_financial_fraud_risk_report_meta_data_v2_service_name(
    value: str,
) -> FinancialFraudRiskReportMetaDataV2ServiceName:
    if value in FINANCIAL_FRAUD_RISK_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(FinancialFraudRiskReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FINANCIAL_FRAUD_RISK_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
