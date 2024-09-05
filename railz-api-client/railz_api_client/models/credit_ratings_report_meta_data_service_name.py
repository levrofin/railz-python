from typing import Literal, Set, cast

CreditRatingsReportMetaDataServiceName = Literal[
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

CREDIT_RATINGS_REPORT_META_DATA_SERVICE_NAME_VALUES: Set[CreditRatingsReportMetaDataServiceName] = {
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


def check_credit_ratings_report_meta_data_service_name(value: str) -> CreditRatingsReportMetaDataServiceName:
    if value in CREDIT_RATINGS_REPORT_META_DATA_SERVICE_NAME_VALUES:
        return cast(CreditRatingsReportMetaDataServiceName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_RATINGS_REPORT_META_DATA_SERVICE_NAME_VALUES!r}"
    )
