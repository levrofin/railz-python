from typing import Literal, Set, cast

CreditScoresReportMetaDataV2ServiceName = Literal[
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

CREDIT_SCORES_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[CreditScoresReportMetaDataV2ServiceName] = {
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


def check_credit_scores_report_meta_data_v2_service_name(value: str) -> CreditScoresReportMetaDataV2ServiceName:
    if value in CREDIT_SCORES_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(CreditScoresReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_SCORES_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
