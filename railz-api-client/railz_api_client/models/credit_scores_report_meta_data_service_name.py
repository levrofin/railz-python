from typing import Literal, Set, cast

CreditScoresReportMetaDataServiceName = Literal[
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

CREDIT_SCORES_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[CreditScoresReportMetaDataServiceName] = {
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


def check_credit_scores_report_meta_data_service_name(value: str) -> CreditScoresReportMetaDataServiceName:
    if value in CREDIT_SCORES_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(CreditScoresReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_SCORES_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
