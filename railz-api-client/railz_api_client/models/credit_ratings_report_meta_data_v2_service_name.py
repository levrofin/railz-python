from typing import Literal, Set, cast

CreditRatingsReportMetaDataV2ServiceName = Literal[
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

CREDIT_RATINGS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES: Set[CreditRatingsReportMetaDataV2ServiceName] = {
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


def check_credit_ratings_report_meta_data_v2_service_name(value: str) -> CreditRatingsReportMetaDataV2ServiceName:
    if value in CREDIT_RATINGS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES:
        return cast(CreditRatingsReportMetaDataV2ServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_REPORT_META_DATA_V2_SERVICE_NAME_VALUES!r}"
    )
